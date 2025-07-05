# src/servicio/gestor_evaluaciones.py

#nombre participante [ADRIANA BETANCOURTH, LISSETTE DANIELA MERO, WILLIAM VELEZ BARRE]
from src.dominio.evaluacion import Evaluacion
from src.dominio.examen import Examen
from src.dominio.trabajo import Trabajo
from src.dominio.presentacion import Presentacion
from src.datos.conexion import Conexion
from datetime import date
import pyodbc as bd


class GestorEvaluaciones:
    def __init__(self):
        self.evaluaciones = []
        # Bandera para saber si la conexión a la DB fue exitosa
        self.db_conectada = False
        # Cargar evaluaciones al iniciar el gestor
        try:
            self.cargar_evaluaciones_desde_db()
            self.db_conectada = True
        except ConnectionError as e:
            print(f"Advertencia: La aplicación se inició sin conexión a la base de datos. Las operaciones de DB no funcionarán. Detalles: {e}")
            self.evaluaciones = [] # Asegurarse de que la lista esté vacía si no se pudo cargar
            self.db_conectada = False
        except Exception as e:
            print(f"Error inesperado al intentar cargar evaluaciones al inicio: {e}")
            self.evaluaciones = []
            self.db_conectada = False


    def agregar_evaluacion(self, evaluacion: Evaluacion):
        """
        Agrega una nueva evaluación al gestor y la persiste en la base de datos.
        """
        if not self.db_conectada:
            print("Error: No hay conexión a la base de datos. No se puede agregar la evaluación.")
            return False
        try:
            # Llama al método privado para guardar en la DB
            self._guardar_evaluacion_en_db(evaluacion)
            self.evaluaciones.append(evaluacion)  # Añadir a la lista en memoria solo si la DB tuvo éxito
            print(f"Evaluación '{evaluacion.nombre}' agregada y guardada en DB.")
            return True
        except Exception as e:
            print(f"Error al agregar y guardar la evaluación en la DB: {e}")
            return False

    def _guardar_evaluacion_en_db(self, evaluacion: Evaluacion):
        """
        Método privado para persistir una única evaluación en la base de datos.
        Levanta una excepción si hay un error.
        """
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()

            # --- NUEVO: Verificar si el nombre de la evaluación ya existe ---
            sql_check_name = "SELECT COUNT(*) FROM Evaluaciones WHERE Nombre = ?"
            cursor.execute(sql_check_name, evaluacion.nombre)
            if cursor.fetchone()[0] > 0:
                raise Exception(f"Ya existe una evaluación con el nombre '{evaluacion.nombre}'.")

            # --- NUEVO: Si es un Trabajo, verificar si el tema ya existe ---
            if isinstance(evaluacion, Trabajo):
                sql_check_tema = "SELECT COUNT(*) FROM Trabajos WHERE Tema = ?"
                cursor.execute(sql_check_tema, evaluacion.tema)
                if cursor.fetchone()[0] > 0:
                    raise Exception(f"Ya existe un Trabajo con el tema '{evaluacion.tema}'.")

            # 1. Insertar en la tabla base 'Evaluaciones'
            sql_base = """
             INSERT INTO Evaluaciones (Nombre, Fecha, Puntaje, TipoEvaluacion)
             OUTPUT INSERTED.EvaluacionID
             VALUES (?, ?, ?, ?)
             """
            parametros_base = (
                evaluacion.nombre,
                evaluacion.fecha,
                evaluacion.puntaje,
                evaluacion.__class__.__name__  # Obtener el tipo de la clase (Examen, Trabajo, Presentacion)
            )
            cursor.execute(sql_base, parametros_base)
            evaluacion_id = cursor.fetchone()[0]  # Obtener el ID de la evaluación insertada

            # 2. Insertar en la tabla específica del tipo de evaluación
            if isinstance(evaluacion, Examen):
                sql_tipo = """
                 INSERT INTO Examenes (EvaluacionID, Duracion, NumPreguntas)
                 VALUES (?, ?, ?)
                 """
                parametros_tipo = (
                    evaluacion_id,
                    evaluacion.duracion_min,
                    evaluacion.num_preguntas
                )
                cursor.execute(sql_tipo, parametros_tipo)
            elif isinstance(evaluacion, Trabajo):
                sql_tipo = """
                 INSERT INTO Trabajos (EvaluacionID, NumPaginas, Tema)
                 VALUES (?, ?, ?)
                 """
                parametros_tipo = (
                    evaluacion_id,
                    evaluacion.num_paginas,
                    evaluacion.tema
                )
                cursor.execute(sql_tipo, parametros_tipo)
            elif isinstance(evaluacion, Presentacion):
                sql_tipo = """
                 INSERT INTO Presentaciones (EvaluacionID, Duracion, TamanoAudiencia)
                 VALUES (?, ?, ?)
                 """
                parametros_tipo = (
                    evaluacion_id,
                    evaluacion.duracion_min,
                    evaluacion.tamano_audiencia
                )
                cursor.execute(sql_tipo, parametros_tipo)

            conexion.commit()  # Confirmar la transacción
            # Nota: Aquí podríamos asignar evaluacion_id al objeto evaluacion si necesitamos su ID de DB en Python.
            # evaluacion._evaluacion_id_db = evaluacion_id

        except bd.Error as ex:
            sqlstate = ex.args[0]
            if conexion:
                conexion.rollback()  # Revertir la transacción en caso de error
            # Re-lanzar la excepción para que el llamador (agregar_evaluacion) la capture y muestre el error
            raise Exception(f"Error SQL al guardar en DB: {sqlstate}. Mensaje: {ex.args[1]}")
        except Exception as e:
            if conexion:
                conexion.rollback()
            raise Exception(f"Error inesperado al guardar en DB: {e}")
        finally:
            Conexion.cerrarConexion()

    def eliminar_evaluacion_por_nombre(self, nombre: str):
        """
        Elimina una evaluación por su nombre de la lista en memoria y de la base de datos.
        """
        if not self.db_conectada:
            print("Error: No hay conexión a la base de datos. No se puede eliminar la evaluación.")
            return False
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()

            # 1. Obtener el EvaluacionID de la evaluación a eliminar
            sql_get_id = "SELECT EvaluacionID FROM Evaluaciones WHERE Nombre = ?"
            cursor.execute(sql_get_id, nombre)
            result = cursor.fetchone()

            if result is None:
                print(f"Evaluación '{nombre}' no encontrada en la base de datos.")
                # Aunque no se encontró en la DB, si por alguna razón está en memoria, la quitamos
                self.evaluaciones = [e for e in self.evaluaciones if e.nombre != nombre]
                return False  # No se encontró la evaluación en la DB

            evaluacion_id = result[0]

            # 2. Eliminar de las tablas específicas primero (por foreign key)
            # No importa si no hay registros en alguna de estas, el DELETE afectará 0 filas.
            cursor.execute("DELETE FROM Examenes WHERE EvaluacionID = ?", evaluacion_id)
            cursor.execute("DELETE FROM Trabajos WHERE EvaluacionID = ?", evaluacion_id)
            cursor.execute("DELETE FROM Presentaciones WHERE EvaluacionID = ?", evaluacion_id)

            # 3. Eliminar de la tabla base 'Evaluaciones'
            cursor.execute("DELETE FROM Evaluaciones WHERE EvaluacionID = ?", evaluacion_id)

            conexion.commit()  # Confirmar la transacción
            print(f"Evaluación '{nombre}' (ID: {evaluacion_id}) eliminada exitosamente de la DB.")

            # 4. Eliminar de la lista en memoria
            self.evaluaciones = [e for e in self.evaluaciones if e.nombre != nombre]
            print(f"Evaluación '{nombre}' eliminada de la memoria.")
            return True

        except bd.Error as ex:
            sqlstate = ex.args[0]
            if conexion:
                conexion.rollback()  # Revertir la transacción en caso de error
            print(f"Error SQLSTATE al eliminar evaluación: {sqlstate}. Mensaje: {ex.args[1]}")
            return False
        except Exception as e:
            if conexion:
                conexion.rollback()
            print(f"Error inesperado al eliminar evaluación: {e}")
            return False
        finally:
            Conexion.cerrarConexion()

    def obtener_evaluacion_por_nombre(self, nombre: str):
        """Obtiene una evaluación por su nombre."""
        # Esta operación no requiere DB, opera sobre la lista en memoria
        for eval_obj in self.evaluaciones:
            if eval_obj.nombre == nombre:
                return eval_obj
        return None

    def filtrar_evaluaciones_por_tipo(self, tipo: str):
        """Filtra y devuelve evaluaciones por tipo."""
        # Esta operación no requiere DB, opera sobre la lista en memoria
        if tipo == "Todos":
            return self.evaluaciones
        else:
            return [e for e in self.evaluaciones if e.__class__.__name__ == tipo]

    def calcular_promedio_general(self):
        """Calcula el promedio de puntajes de todas las evaluaciones."""
        # Esta operación no requiere DB, opera sobre la lista en memoria
        if not self.evaluaciones:
            return 0.0
        return sum(e.calcular_nota() for e in self.evaluaciones) / len(self.evaluaciones)

    def obtener_mejor_evaluacion(self):
        """Obtiene la evaluación con el puntaje más alto."""
        # Esta operación no requiere DB, opera sobre la lista en memoria
        if not self.evaluaciones:
            return None
        return max(self.evaluaciones, key=lambda e: e.calcular_nota())

    def obtener_estadisticas_por_tipo(self):
        """Obtiene estadísticas (cantidad, promedio, mejor) por tipo de evaluación."""
        # Esta operación no requiere DB, opera sobre la lista en memoria
        stats = {}
        tipos_validos = ["Examen", "Trabajo", "Presentacion"]
        for tipo in tipos_validos:
            evals_tipo = self.filtrar_evaluaciones_por_tipo(tipo)
            count = len(evals_tipo)
            if count > 0:
                promedio = sum(e.calcular_nota() for e in evals_tipo) / count
                best_eval = max(evals_tipo, key=lambda e: e.calcular_nota())
                stats[tipo] = {
                    'count': count,
                    'promedio': promedio,
                    'best_name': best_eval.nombre,
                    'best_score': best_eval.calcular_nota()
                }
            else:
                stats[tipo] = {
                    'count': 0,
                    'promedio': 0.0,
                    'best_name': "N/A",
                    'best_score': 0.0
                }
        return stats

    def limpiar_todas_las_evaluaciones(self):
        """
        Limpia la lista de evaluaciones en memoria y elimina TODAS las evaluaciones de la base de datos.
        """
        if not self.db_conectada:
            print("Error: No hay conexión a la base de datos. No se pueden limpiar las evaluaciones.")
            return False
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()

            # Eliminar registros de las tablas de subtipos primero (por foreign key)
            cursor.execute("DELETE FROM Examenes;")
            cursor.execute("DELETE FROM Trabajos;")
            cursor.execute("DELETE FROM Presentaciones;")
            # Finalmente, eliminar de la tabla base
            cursor.execute("DELETE FROM Evaluaciones;")
            conexion.commit()
            print("Todas las evaluaciones eliminadas exitosamente de la base de datos.")
            self.evaluaciones = []  # Limpiar la lista en memoria después de la DB
            print("Lista de evaluaciones en memoria limpiada.")
            return True
        except bd.Error as ex:
            sqlstate = ex.args[0]
            if conexion:
                conexion.rollback()
            print(f"Error SQLSTATE al limpiar todas las evaluaciones de la DB: {sqlstate}. Mensaje: {ex.args[1]}")
            return False
        except Exception as e:
            if conexion:
                conexion.rollback()
            print(f"Error inesperado al limpiar todas las evaluaciones de la DB: {e}")
            return False
        finally:
            Conexion.cerrarConexion()

    def cargar_evaluaciones_desde_db(self):
        """
        Carga todas las evaluaciones desde la base de datos.
        Levanta ConnectionError si no se puede conectar.
        """
        self.evaluaciones = []  # Limpiar la lista actual antes de cargar

        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()

            sql_query = """
             SELECT
                 e.EvaluacionID,
                 e.Nombre,
                 e.Fecha,
                 e.Puntaje,
                 e.TipoEvaluacion,
                 ex.Duracion AS Examen_duracion_min,
                 ex.NumPreguntas AS Examen_num_preguntas,
                 t.NumPaginas AS Trabajo_num_paginas,
                 t.Tema AS Trabajo_tema,
                 p.Duracion AS Presentacion_duracion_min,
                 p.TamanoAudiencia AS Presentacion_tamano_audiencia
             FROM Evaluaciones AS e
             LEFT JOIN Examenes AS ex ON e.EvaluacionID = ex.EvaluacionID AND e.TipoEvaluacion = 'Examen'
             LEFT JOIN Trabajos AS t ON e.EvaluacionID = t.EvaluacionID AND e.TipoEvaluacion = 'Trabajo'
             LEFT JOIN Presentaciones AS p ON e.EvaluacionID = p.EvaluacionID AND e.TipoEvaluacion = 'Presentacion';
             """
            cursor.execute(sql_query)
            rows = cursor.fetchall()

            for row in rows:
                evaluacion_id, nombre, fecha, puntaje, tipo_evaluacion = \
                    row[0], row[1], row[2], float(row[3]), row[4]

                eval_obj = None
                if tipo_evaluacion == 'Examen':
                    duracion_min = row[5]
                    num_preguntas = row[6]
                    if duracion_min is not None and num_preguntas is not None:
                        eval_obj = Examen(nombre, fecha, puntaje, duracion_min, num_preguntas)
                elif tipo_evaluacion == 'Trabajo':
                    num_paginas = row[7]
                    tema = row[8]
                    if num_paginas is not None and tema is not None:
                        eval_obj = Trabajo(nombre, fecha, puntaje, num_paginas, tema)
                elif tipo_evaluacion == 'Presentacion':
                    duracion_min = row[9]
                    tamano_audiencia = row[10]
                    if duracion_min is not None and tamano_audiencia is not None:
                        eval_obj = Presentacion(nombre, fecha, puntaje, duracion_min, tamano_audiencia)

                if eval_obj:
                    self.evaluaciones.append(eval_obj)

            print("Evaluaciones cargadas exitosamente desde la base de datos.")

        except bd.Error as ex:
            sqlstate = ex.args[0]
            # No re-lanzar Exception genérica, re-lanzar el error de conexión
            raise ConnectionError(f"Error SQLSTATE al cargar evaluaciones: {sqlstate}. Mensaje: {ex.args[1]}")
        except Exception as e:
            # Capturar cualquier otra excepción y re-lanzarla como ConnectionError
            raise ConnectionError(f"Error inesperado al cargar evaluaciones desde la DB: {e}")
        finally:
            Conexion.cerrarConexion()

    def buscar_evaluacion_por_nombre(self, nombre: str):
        """Busca y retorna una evaluación por su nombre."""
        # Esta operación no requiere DB, opera sobre la lista en memoria
        for eval_obj in self.evaluaciones:
            if eval_obj.nombre == nombre:
                return eval_obj
        return None

    def actualizar_evaluacion(self, nombre_original: str, evaluacion_actualizada: Evaluacion):
        """
        Actualiza una evaluación existente en la base de datos y en la lista en memoria.
        """
        if not self.db_conectada:
            print("Error: No hay conexión a la base de datos. No se puede actualizar la evaluación.")
            return False
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()

            # 1. Obtener el EvaluacionID de la evaluación original
            sql_get_id = "SELECT EvaluacionID FROM Evaluaciones WHERE Nombre = ?"
            cursor.execute(sql_get_id, nombre_original)
            result = cursor.fetchone()

            if result is None:
                print(f"Evaluación original '{nombre_original}' no encontrada para actualizar.")
                return False

            evaluacion_id = result[0]

            # Verificar si el nuevo nombre ya existe para otra evaluación (si el nombre ha cambiado)
            if nombre_original != evaluacion_actualizada.nombre:
                sql_check_name = "SELECT EvaluacionID FROM Evaluaciones WHERE Nombre = ? AND EvaluacionID != ?"
                cursor.execute(sql_check_name, evaluacion_actualizada.nombre, evaluacion_id)
                if cursor.fetchone():
                    print(f"El nuevo nombre '{evaluacion_actualizada.nombre}' ya está en uso por otra evaluación.")
                    return False  # El nuevo nombre ya existe para otra evaluación

            # 2. Actualizar en la tabla base 'Evaluaciones'
            sql_update_base = """
             UPDATE Evaluaciones SET Nombre = ?, Fecha = ?, Puntaje = ?, TipoEvaluacion = ?
             WHERE EvaluacionID = ?
             """
            parametros_update_base = (
                evaluacion_actualizada.nombre,
                evaluacion_actualizada.fecha,
                evaluacion_actualizada.puntaje,
                evaluacion_actualizada.__class__.__name__,
                evaluacion_id
            )
            cursor.execute(sql_update_base, parametros_update_base)

            # 3. Actualizar o insertar en la tabla específica del tipo de evaluación
            # Primero, eliminar el registro antiguo si el tipo de evaluación cambió
            # (o simplemente si siempre quieres una operación de upsert para los subtipos)
            cursor.execute("DELETE FROM Examenes WHERE EvaluacionID = ?", evaluacion_id)
            cursor.execute("DELETE FROM Trabajos WHERE EvaluacionID = ?, Tema = ?", evaluacion_id, evaluacion_actualizada.tema) # Update: Added Tema to deletion for Trabajos
            cursor.execute("DELETE FROM Presentaciones WHERE EvaluacionID = ?", evaluacion_id)

            if isinstance(evaluacion_actualizada, Examen):
                sql_tipo = """
                 INSERT INTO Examenes (EvaluacionID, Duracion, NumPreguntas)
                 VALUES (?, ?, ?)
                 """
                parametros_tipo = (
                    evaluacion_id,
                    evaluacion_actualizada.duracion_min,
                    evaluacion_actualizada.num_preguntas
                )
                cursor.execute(sql_tipo, parametros_tipo)
            elif isinstance(evaluacion_actualizada, Trabajo):
                sql_tipo = """
                 INSERT INTO Trabajos (EvaluacionID, NumPaginas, Tema)
                 VALUES (?, ?, ?)
                 """
                parametros_tipo = (
                    evaluacion_id,
                    evaluacion_actualizada.num_paginas,
                    evaluacion_actualizada.tema
                )
                cursor.execute(sql_tipo, parametros_tipo)
            elif isinstance(evaluacion_actualizada, Presentacion):
                sql_tipo = """
                 INSERT INTO Presentaciones (EvaluacionID, Duracion, TamanoAudiencia)
                 VALUES (?, ?, ?)
                 """
                parametros_tipo = (
                    evaluacion_id,
                    evaluacion_actualizada.duracion_min,
                    evaluacion_actualizada.tamano_audiencia
                )
                cursor.execute(sql_tipo, parametros_tipo)

            conexion.commit()  # Confirmar la transacción
            print(f"Evaluación '{evaluacion_actualizada.nombre}' (ID: {evaluacion_id}) actualizada exitosamente en DB.")

            # 4. Actualizar la lista en memoria
            for i, eval_obj in enumerate(self.evaluaciones):
                if eval_obj.nombre == nombre_original:
                    self.evaluaciones[i] = evaluacion_actualizada
                    print(f"Evaluación '{nombre_original}' actualizada en memoria a '{evaluacion_actualizada.nombre}'.")
                    break
            return True

        except bd.Error as ex:
            sqlstate = ex.args[0]
            if conexion:
                conexion.rollback()  # Revertir la transacción en caso de error
            print(f"Error SQLSTATE al actualizar evaluación: {sqlstate}. Mensaje: {ex.args[1]}")
            return False
        except Exception as e:
            if conexion:
                conexion.rollback()
            print(f"Error inesperado al actualizar evaluación: {e}")
            return False
        finally:
            Conexion.cerrarConexion()