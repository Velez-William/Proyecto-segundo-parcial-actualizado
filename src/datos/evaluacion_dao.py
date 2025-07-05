# src/datos/evaluacion_dao.py
#nombre participante [ADRIANA BETANCOURTH, LISSETTE DANIELA MERO, WILLIAM VELEZ BARRE]
import pyodbc
from src.datos.conexion import Conexion # <--- Importación corregida
from src.dominio.evaluacion import Evaluacion
from src.dominio.examen import Examen
from src.dominio.trabajo import Trabajo
from src.dominio.presentacion import Presentacion
from datetime import date

class EvaluacionDAO:
    """
    Data Access Object (DAO) para la entidad Evaluacion.
    Maneja la persistencia de objetos Evaluacion en la base de datos SQL Server.
    """
    def __init__(self):
        self.conexion = Conexion()

    def _ejecutar_consulta(self, query, params=None, fetch=False, commit=False):
        """
        Método auxiliar para ejecutar consultas SQL.
        """
        conn = None
        cursor = None
        result = None
        try:
            conn = self.conexion.obtenerConexion()
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            if fetch:
                result = cursor.fetchall()
            if commit:
                conn.commit()
            return result
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            print(f"Error SQLSTATE: {sqlstate}. Mensaje: {ex.args[1]}")
            raise Exception(f"Error en la operación de base de datos: {ex.args[1]}")
        finally:
            if cursor:
                cursor.close()

    def guardar_evaluacion(self, evaluacion: Evaluacion):
        """
        Guarda una evaluación (y sus detalles específicos si aplica) en la base de datos.
        """
        conn = None
        cursor = None
        try:
            conn = self.conexion.obtenerConexion()
            cursor = conn.cursor()

            sql_base = """
            INSERT INTO Evaluaciones (Nombre, Fecha, Puntaje, TipoEvaluacion)
            OUTPUT INSERTED.EvaluacionID
            VALUES (?, ?, ?, ?)
            """
            eval_fecha = getattr(evaluacion, 'fecha', date.today()) # Asume que Evaluacion tiene 'fecha', si no, usa today()

            params_base = (
                evaluacion.nombre,
                eval_fecha,
                evaluacion.calcular_nota(),
                evaluacion.__class__.__name__
            )

            cursor.execute(sql_base, params_base)
            evaluacion_id = cursor.fetchone()[0] # Obtener el ID generado

            if isinstance(evaluacion, Examen):
                sql_subclase = """
                INSERT INTO Examenes (EvaluacionID, Duracion)
                VALUES (?, ?)
                """
                duracion = getattr(evaluacion, 'duracion_min', 0) # Asegúrate de que Examen tenga este atributo
                params_subclase = (evaluacion_id, duracion)
                cursor.execute(sql_subclase, params_subclase)
            elif isinstance(evaluacion, Trabajo):
                sql_subclase = """
                INSERT INTO Trabajos (EvaluacionID, FechaEntrega)
                VALUES (?, ?)
                """
                fecha_entrega = getattr(evaluacion, 'fecha_entrega', date.today()) # Asegúrate de que Trabajo tenga este atributo
                params_subclase = (evaluacion_id, fecha_entrega)
                cursor.execute(sql_subclase, params_subclase)
            elif isinstance(evaluacion, Presentacion):
                sql_subclase = """
                INSERT INTO Presentaciones (EvaluacionID, NumIntegrantes)
                VALUES (?, ?)
                """
                num_integrantes = getattr(evaluacion, 'tamano_audiencia', 0) # Asegúrate de que Presentacion tenga este atributo
                params_subclase = (evaluacion_id, num_integrantes)
                cursor.execute(sql_subclase, params_subclase)

            conn.commit()
            print(f"Evaluación '{evaluacion.nombre}' ({evaluacion.__class__.__name__}) guardada en la base de datos con ID: {evaluacion_id}.")

        except pyodbc.Error as ex:
            if conn:
                conn.rollback()
            sqlstate = ex.args[0]
            print(f"Error SQLSTATE al guardar evaluación: {sqlstate}. Mensaje: {ex.args[1]}")
            raise Exception(f"No se pudo guardar la evaluación: {ex.args[1]}")
        finally:
            if cursor:
                cursor.close()

    def cargar_evaluaciones(self):
        """
        Carga todas las evaluaciones desde la base de datos, incluyendo detalles de subclase,
        y las retorna como una lista de objetos Evaluacion.
        """
        evaluaciones_cargadas = []
        conn = None
        cursor = None
        try:
            conn = self.conexion.obtenerConexion()
            cursor = conn.cursor()

            query = """
            SELECT
                e.EvaluacionID, e.Nombre, e.Fecha, e.Puntaje, e.TipoEvaluacion,
                ex.Duracion AS Examen_Duracion,
                tr.FechaEntrega AS Trabajo_FechaEntrega,
                pr.NumIntegrantes AS Presentacion_NumIntegrantes
            FROM Evaluaciones e
            LEFT JOIN Examenes ex ON e.EvaluacionID = ex.EvaluacionID
            LEFT JOIN Trabajos tr ON e.EvaluacionID = tr.EvaluacionID
            LEFT JOIN Presentaciones pr ON e.EvaluacionID = pr.EvaluacionID
            ORDER BY e.EvaluacionID
            """
            cursor.execute(query)

            for row in cursor.fetchall():
                eval_id, nombre, fecha, puntaje, tipo_evaluacion = \
                    row.EvaluacionID, row.Nombre, row.Fecha, row.Puntaje, row.TipoEvaluacion

                eval_obj = None
                if tipo_evaluacion == "Examen":
                    duracion = row.Examen_Duracion
                    eval_obj = Examen(nombre, puntaje)
                    eval_obj.duracion_min = duracion if duracion is not None else 0
                elif tipo_evaluacion == "Trabajo":
                    fecha_entrega = row.Trabajo_FechaEntrega
                    eval_obj = Trabajo(nombre, puntaje)
                    eval_obj.fecha_entrega = fecha_entrega if fecha_entrega is not None else date.today()
                elif tipo_evaluacion == "Presentacion":
                    num_integrantes = row.Presentacion_NumIntegrantes
                    eval_obj = Presentacion(nombre, puntaje)
                    eval_obj.tamano_audiencia = num_integrantes if num_integrantes is not None else 0
                else:
                    print(f"Tipo de evaluación desconocido '{tipo_evaluacion}' para '{nombre}'. Saltando.")
                    continue

                if eval_obj:
                    eval_obj.nombre = nombre
                    eval_obj.puntaje = float(puntaje)
                    eval_obj.fecha = fecha
                    evaluaciones_cargadas.append(eval_obj)

            print(f"Cargadas {len(evaluaciones_cargadas)} evaluaciones desde la base de datos.")
            return evaluaciones_cargadas

        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            print(f"Error SQLSTATE al cargar evaluaciones: {sqlstate}. Mensaje: {ex.args[1]}")
            raise Exception(f"No se pudieron cargar las evaluaciones: {ex.args[1]}")
        finally:
            if cursor:
                cursor.close()

    def eliminar_evaluacion_bd(self, nombre: str):
        """
        Elimina una evaluación y sus detalles asociados de la base de datos por nombre.
        """
        conn = None
        cursor = None
        try:
            conn = self.conexion.obtenerConexion()
            cursor = conn.cursor()

            sql_get_id = "SELECT EvaluacionID FROM Evaluaciones WHERE Nombre = ?"
            cursor.execute(sql_get_id, (nombre,))
            result = cursor.fetchone()

            if result:
                evaluacion_id = result[0]
                sql_delete = "DELETE FROM Evaluaciones WHERE EvaluacionID = ?"
                cursor.execute(sql_delete, (evaluacion_id,))
                conn.commit()
                print(f"Evaluación '{nombre}' (ID: {evaluacion_id}) eliminada de la base de datos.")
                return True
            else:
                print(f"No se encontró la evaluación con el nombre '{nombre}' en la base de datos para eliminar.")
                return False

        except pyodbc.Error as ex:
            if conn:
                conn.rollback()
            sqlstate = ex.args[0]
            print(f"Error SQLSTATE al eliminar evaluación: {sqlstate}. Mensaje: {ex.args[1]}")
            raise Exception(f"No se pudo eliminar la evaluación: {ex.args[1]}")
        finally:
            if cursor:
                cursor.close()

    def limpiar_todas_las_evaluaciones_bd(self):
        """
        Elimina todas las evaluaciones de la base de datos.
        """
        conn = None
        cursor = None
        try:
            conn = self.conexion.obtenerConexion()
            cursor = conn.cursor()
            query = "DELETE FROM Evaluaciones"
            cursor.execute(query)
            conn.commit()
            print("Todas las evaluaciones han sido limpiadas de la base de datos.")
        except pyodbc.Error as ex:
            if conn:
                conn.rollback()
            sqlstate = ex.args[0]
            print(f"Error SQLSTATE al limpiar evaluaciones: {sqlstate}. Mensaje: {ex.args[1]}")
            raise Exception(f"No se pudieron limpiar las evaluaciones en la base de datos: {ex.args[1]}")
        finally:
            if cursor:
                cursor.close()