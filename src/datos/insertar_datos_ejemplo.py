# src/datos/insertar_datos_ejemplo.py

import sys
import os
from datetime import date
import pyodbc as bd

from src.datos.conexion import Conexion

# Ajusta el sys.path si es necesario para que encuentre src.dominio
# Si el script se ejecuta directamente desde src/datos, necesitas subir un nivel para llegar a src
# y luego acceder a dominio.
# La línea project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ''))
# si insertar_datos_ejemplo.py está en src/datos, dirname(__file__) es src/datos.
# Entonces, para encontrar 'src', necesitaríamos ir un nivel más arriba:
project_root_for_src = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root_for_src not in sys.path:
    sys.path.append(project_root_for_src)

# Importaciones corregidas para la nueva ubicación:
# Para Conexion, es una importación relativa dentro del mismo paquete 'datos'


# Para las clases de dominio, ahora necesitas subir un nivel (..) para llegar a 'src'
# y luego entrar a 'dominio'



def insertar_ejemplo_evaluacion(nombre, fecha, puntaje, tipo, **kwargs):
    """
    Inserta una evaluación de ejemplo en la base de datos usando la conexión existente,
    dividiendo los datos en las tablas base y de subclase.
    """
    conexion = None
    cursor = None
    try:
        conexion = Conexion.obtenerConexion()
        cursor = Conexion.obtenerCursor()

        # 1. Insertar en la tabla base 'Evaluaciones'
        sql_base = """
        INSERT INTO Evaluaciones (Nombre, Fecha, Puntaje, TipoEvaluacion)
        OUTPUT INSERTED.EvaluacionID
        VALUES (?, ?, ?, ?)
        """
        parametros_base = (
            nombre,
            fecha,
            puntaje,
            tipo
        )
        cursor.execute(sql_base, parametros_base)
        evaluacion_id = cursor.fetchone()[0] # Obtener el ID generado

        # 2. Insertar en la tabla específica del tipo de evaluación
        if tipo == "Examen":
            sql_tipo = """
            INSERT INTO Examenes (EvaluacionID, DuracionMinutos, NumeroPreguntas)
            VALUES (?, ?, ?)
            """
            parametros_tipo = (
                evaluacion_id,
                kwargs.get('duracion_min'),
                kwargs.get('num_preguntas')
            )
            cursor.execute(sql_tipo, parametros_tipo)
        elif tipo == "Trabajo":
            sql_tipo = """
            INSERT INTO Trabajos (EvaluacionID, NumeroPaginas, Tema)
            VALUES (?, ?, ?)
            """
            parametros_tipo = (
                evaluacion_id,
                kwargs.get('num_paginas'),
                kwargs.get('tema')
            )
            cursor.execute(sql_tipo, parametros_tipo)
        elif tipo == "Presentacion":
            sql_tipo = """
            INSERT INTO Presentaciones (EvaluacionID, DuracionMinutos, TamanoAudiencia)
            VALUES (?, ?, ?)
            """
            parametros_tipo = (
                evaluacion_id,
                kwargs.get('duracion_min'),
                kwargs.get('tamano_audiencia')
            )
            cursor.execute(sql_tipo, parametros_tipo)

        conexion.commit()
        print(f"'{nombre}' ({tipo}) insertada con éxito. ID: {evaluacion_id}")

    except bd.Error as ex:
        sqlstate = ex.args[0]
        if conexion:
            conexion.rollback()
        print(f"Error SQLSTATE al insertar evaluación '{nombre}': {sqlstate}. Mensaje: {ex.args[1]}")
    except Exception as e:
        if conexion:
            conexion.rollback()
        print(f"Error inesperado al insertar evaluación '{nombre}': {e}")
    finally:
        # Asegúrate de cerrar la conexión si se abrió
        if 'conexion' in locals() and conexion:
            Conexion.cerrarConexion()


def limpiar_tablas():
    """
    Limpia todas las tablas de evaluaciones en la base de datos.
    """
    conn_temp = None
    try:
        conn_temp = Conexion.obtenerConexion()
        cursor_temp = conn_temp.cursor()
        print("Limpiando tablas existentes...")
        # Orden de eliminación para respetar claves foráneas
        cursor_temp.execute("DELETE FROM Examenes")
        cursor_temp.execute("DELETE FROM Trabajos")
        cursor_temp.execute("DELETE FROM Presentaciones")
        cursor_temp.execute("DELETE FROM Evaluaciones")
        conn_temp.commit()
        print("Tablas limpiadas correctamente.")
    except bd.Error as ex:
        sqlstate = ex.args[0]
        if conn_temp:
            conn_temp.rollback()
        print(f"Error SQLSTATE al limpiar tablas: {sqlstate}. Mensaje: {ex.args[1]}")
    except Exception as e:
        print(f"Error inesperado al limpiar tablas: {e}")
    finally:
        # Asegúrate de cerrar la conexión si se abrió, incluso si hubo un error en DELETE
        if 'conn_temp' in locals() and conn_temp:
            Conexion.cerrarConexion()


if __name__ == '__main__':
    limpiar_tablas() # Limpiar las tablas antes de insertar nuevos datos de ejemplo

    insertar_ejemplo_evaluacion(
        nombre="Matematicas Basicas",
        fecha=date(2025, 6, 15),
        puntaje=85.5,
        tipo='Examen',
        duracion_min=60,
        num_preguntas=20
    )

    insertar_ejemplo_evaluacion(
        nombre="Ensayo Literatura",
        fecha=date(2025, 6, 20),
        puntaje=92.0,
        tipo='Trabajo',
        num_paginas=10,
        tema="La importancia del realismo mágico"
    )

    insertar_ejemplo_evaluacion(
        nombre="Proyecto Final",
        fecha=date(2025, 6, 25),
        puntaje=78.0,
        tipo='Presentacion',
        duracion_min=30,
        tamano_audiencia=50
    )

    insertar_ejemplo_evaluacion(
        nombre="Contabilidad Avanzada",
        fecha=date(2025, 7, 1),
        puntaje=95.0,
        tipo='Examen',
        duracion_min=90,
        num_preguntas=30
    )