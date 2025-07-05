# src/datos/conexion.py
import sys
import pyodbc as bd

class Conexion:
    _SERVIDOR = 'WILLIAM-PC\\VELEZSQLSERVER'
    _BBDD = 'GestionEvaluaciones'
    _USUARIO = 'Evaluaciones'
    _PASSWORD = '1234'

    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                # Modificado para usar un tiempo de espera más corto para la conexión
                # connect_timeout=5 significa 5 segundos. Ajusta si es necesario.
                cls._conexion = bd.connect(
                    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                    f'SERVER={cls._SERVIDOR};'
                    f'DATABASE={cls._BBDD};'
                    f'UID={cls._USUARIO};'
                    f'PWD={cls._PASSWORD};'
                    f'CONNECT TIMEOUT=5;' # Añadir un timeout para no esperar indefinidamente
                )
                print("Conexión a SQL Server establecida exitosamente.")
            except bd.Error as ex:
                sqlstate = ex.args[0]
                print(f"Error de conexión a SQL Server (SQLSTATE: {sqlstate}): {ex.args[1]}")
                # En lugar de sys.exit(1), levantamos una excepción.
                # Puedes crear una excepción custom si quieres, o usar una genérica.
                raise ConnectionError(f"No se pudo conectar a la base de datos: {ex.args[1]}")
            except Exception as e:
                print(f"Error inesperado al intentar conectar: {e}")
                raise ConnectionError(f"Error inesperado al conectar a la base de datos: {e}")
        return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            # Asegurarse de que la conexión exista antes de obtener el cursor
            cls.obtenerConexion() # Esto intentará conectar si no lo está
            cls._cursor = cls._conexion.cursor()
        return cls._cursor

    @classmethod
    def cerrarConexion(cls):
        if cls._cursor:
            cls._cursor.close()
            cls._cursor = None
        if cls._conexion:
            cls._conexion.close()
            cls._conexion = None
            print("Conexión a SQL Server cerrada.")

# El bloque __main__ para pruebas puede seguir como está, pero ten en cuenta que ahora
# levantará una excepción en lugar de salir directamente si falla la conexión.
if __name__ == '__main__':
    print("Intentando probar la conexión a la base de datos...")
    try:
        conn = Conexion.obtenerConexion()
        cursor = Conexion.obtenerCursor()
        cursor.execute("SELECT GETDATE() AS CurrentDateTime;")
        result = cursor.fetchone()
        print(f"Consulta de prueba exitosa. Fecha/Hora del servidor: {result[0]}")
    except ConnectionError as ce:
        print(f"Falló la prueba de conexión (controlado): {ce}")
    except Exception as e:
        print(f"Falló la prueba de conexión (inesperado): {e}")
    finally:
        Conexion.cerrarConexion()