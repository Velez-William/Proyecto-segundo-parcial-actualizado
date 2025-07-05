Project Title: Sistema de Gestión de Evaluaciones Académicas
Descripción
Explique brevemente la función de este sistema. (Por ejemplo, "Este proyecto implementa una aplicación de escritorio para gestionar evaluaciones académicas, incluyendo diferentes tipos como exámenes, tareas y presentaciones. Permite a los usuarios crear, ver, editar y eliminar evaluaciones, y proporciona estadísticas basadas en los tipos de evaluación").
#nombre participante [ADRIANA BETANCOURTH, LISSETTE DANIELA MERO, WILLIAM VELEZ BARRE]
Características
Basándome en los archivos persona.pyy vntEvaluacion.py, puedo identificar estas características:

Operaciones CRUD para evaluaciones: crear, leer (enumerar), actualizar, eliminar evaluaciones.

Tipos de evaluación: Admite diferentes tipos de evaluaciones:

Exámenes ( Examen)

Tareas ( Trabajo)

Presentaciones ( Presentacion)

Integración de bases de datos: Conserva los datos de evaluación en una base de datos de SQL Server. (Mencionado en conexion.py[ Nombre del servidor], evaluacion_dao.py[Nombre del servidor], [Nombre del servidor gestor_evaluaciones.py]).

Estadísticas: Muestra estadísticas agrupadas por tipo de evaluación (basadas en groupBox_por_tipoy textEdit_estadisticasen vntEvaluacion.py).

Validación de datos: incluye validación de campos de entrada (por ejemplo, rango de puntuación, duración, números de página, etc.).

Operaciones con archivos: Guardar y cargar evaluaciones desde archivos JSON. (Mencionado en persona.py)

Tecnologías utilizadas
Python: El lenguaje de programación principal.

PySide6: Para la interfaz gráfica de usuario (GUI).

pyodbc: para conectarse a SQL Server.

SQL Server: el sistema de base de datos utilizado para la persistencia.

JSON: para almacenamiento de datos basado en archivos (guardar/cargar).

Estructura del proyecto
Puedo ayudarte a explicar el propósito de cada directorio y archivo clave:

src/:Contiene el código fuente principal.

UI/:

vntEvaluacion.py: (Generado a partir de vntEvaluacion.ui) Define el diseño de la GUI y los widgets para la ventana de administración de evaluación.

datos/:Maneja la interacción con la base de datos.

conexion.py:Administra la conexión de la base de datos a SQL Server.

evaluacion_dao.py:Objeto de acceso a datos (DAO) para realizar operaciones CRUD en evaluaciones en la base de datos.

insertar_datos_ejemplo.py:Script para rellenar la base de datos con datos de evaluación de ejemplo.

dominio/:Contiene los modelos de dominio (lógica de negocio).

evaluacion.py:Clase base para todos los tipos de evaluación.

examen.py: Representa un examen, heredando de Evaluacion.

presentacion.py: Representa una presentación, heredando de Evaluacion.

trabajo.py: Representa una Asignación (Trabajo), heredando de Evaluacion.

servicio/:Contiene la lógica de la capa de servicio.

gestor_evaluaciones.py:Administra la recopilación de evaluaciones e interactúa con el EvaluacionDAO.

persona.py:(Renombrado MainWindowen los comentarios) La lógica principal de la aplicación, que conecta la interfaz de usuario con la interfaz de usuario GestorEvaluacionesy maneja las interacciones del usuario.

Configuración e instalación
Prerrequisitos:

Python 3.x

SQL Server (con la GestionEvaluacionesbase de datos y Evaluacionesel usuario, tal como se configuró en conexion.py).

Controlador ODBC 17 para SQL Server.

Pasos de instalación:

Clonar el repositorio:git clone <your-repo-url>

Navegue hasta el directorio del proyecto:cd <project-directory>

Crear un entorno virtual (recomendado):python -m venv venv

Activar el entorno virtual:

Ventanas:.\venv\Scripts\activate

macOS/Linux:source venv/bin/activate

Instalar dependencias:pip install PySide6 pyodbc

Configuración de la base de datos:

Asegúrese de que su servidor SQL esté ejecutándose.

Crea una base de datos llamada GestionEvaluaciones.

Cree un usuario Evaluacionescon contraseña 1234y otórguele los permisos necesarios en la GestionEvaluacionesbase de datos (o ajústelo conexion.pycon sus credenciales).

Ejecutar src/datos/insertar_datos_ejemplo.pypara llenar la base de datos con datos iniciales: python src/datos/insertar_datos_ejemplo.py(este script también limpia los datos existentes antes de insertarlos).

Cómo correr
Desde el directorio raíz del proyecto, ejecute la aplicación principal:python src/servicio/persona.py

Uso
(Describe cómo utilizar la aplicación, por ejemplo, "Una vez que se inicia la aplicación, puedes utilizar el botón 'Crear' para agregar nuevas evaluaciones, 'Modificar' para editar las existentes, etc. Selecciona un tipo de evaluación del menú desplegable para ver campos específicos.")

Contribuyendo
(Sección estándar para contribuciones, si corresponde)

Licencia
(por ejemplo, licencia MIT)

Por favor hágamelo saber:

¿Quieres que genere el README.mdcontenido completo con los detalles que he descrito?

¿Hay alguna sección específica que desea agregar, eliminar o desarrollar?

¿Tiene instrucciones para crear la interfaz de usuario a partir del .uiarchivo (si vntEvaluacion.pyde hecho se genera)? (por ejemplo, pyside6-uic vntEvaluacion.ui -o vntEvaluacion.py)

¿Tienes alguna captura de pantalla (además de la que proporcionaste, que parece ser un diseño de interfaz de usuario) de la aplicación en ejecución que te gustaría incluir?

¿Quiénes son los desarrolladores? (Lo vi [Tu Nombre 1], [Tu Nombre 2]en persona.py)

Una vez que tenga esta información, puedo generar una versión más completa y personalizada README.mdpara su proyecto de GitHub.







cosas explicativa de mi proyecto y si quiere algo de codigo para expliacr el funcionamiento del proyecto



Ver razonamiento
Aquí tienes una propuesta de README.md con explicaciones detalladas y ejemplos de código para tu "Sistema de Gestión de Evaluaciones Académicas", diseñado para guiar a cualquier persona que explore tu repositorio en GitHub.

Sistema de Gestión de Evaluaciones Académicas
Descripción del Proyecto
Este proyecto implementa un sistema de gestión de evaluaciones académicas como una aplicación de escritorio, desarrollado en Python con PySide6 para la interfaz gráfica de usuario. Su objetivo principal es facilitar la administración de diferentes tipos de evaluaciones (Exámenes, Trabajos, Presentaciones), permitiendo a los usuarios crear, ver, modificar y eliminar registros. Además, el sistema ofrece funcionalidades para el almacenamiento persistente de datos en una base de datos SQL Server y la generación de estadísticas por tipo de evaluación.

Características Principales
Gestión Completa de Evaluaciones (CRUD): Permite la creación, lectura (listado), actualización y eliminación de registros de evaluaciones.

Diversidad de Tipos de Evaluación: Soporta y diferencia entre los siguientes tipos de evaluaciones, cada uno con atributos específicos:

Exámenes: Con atributos como duración en minutos y número de preguntas.

Trabajos: Incluye número de páginas y tema.

Presentaciones: Define duración en minutos y tamaño de audiencia.

Persistencia de Datos: Utiliza SQL Server como sistema de gestión de bases de datos para asegurar el almacenamiento y recuperación de la información de las evaluaciones.

Estadísticas Detalladas: Muestra estadísticas relevantes agrupadas por el tipo de evaluación, proporcionando una visión general del rendimiento académico.

Validación de Datos: Incorpora validaciones en la entrada de datos para asegurar la integridad de la información (ej. rangos de puntaje, duraciones, números de páginas).

Operaciones con Archivos: Capacidad para guardar y cargar datos de evaluaciones desde archivos JSON, lo que permite la portabilidad de los datos.

Tecnologías Utilizadas
Python: Lenguaje de programación principal del proyecto.

PySide6: Framework para el desarrollo de la interfaz gráfica de usuario (GUI).

pyodbc: Conector de base de datos Python para interactuar con SQL Server.

SQL Server: Sistema de gestión de bases de datos relacionales utilizado para la persistencia de datos.

JSON: Formato de intercambio de datos para la funcionalidad de guardar y cargar archivos.

Estructura del Proyecto
El proyecto está organizado en una estructura modular para facilitar la comprensión y el mantenimiento:

├── src/
│   ├── UI/
│   │   └── vntEvaluacion.py           # Define la interfaz de usuario (generado desde .ui)
│   ├── datos/
│   │   ├── conexion.py                 # Gestiona la conexión a la base de datos SQL Server
│   │   ├── evaluacion_dao.py           # Objeto de Acceso a Datos (DAO) para operaciones CRUD en la BD
│   │   └── insertar_datos_ejemplo.py   # Script para poblar la base de datos con datos de ejemplo
│   ├── dominio/
│   │   ├── evaluacion.py               # Clase base abstracta para todas las evaluaciones
│   │   ├── examen.py                   # Implementación específica para Exámenes
│   │   ├── presentacion.py             # Implementación específica para Presentaciones
│   │   └── trabajo.py                  # Implementación específica para Trabajos
│   └── servicio/
│       ├── gestor_evaluaciones.py      # Lógica de negocio para gestionar colecciones de evaluaciones
│       └── persona.py                  # Clase principal de la aplicación, conecta la UI con la lógica de negocio
└── README.md
Explicación del Funcionamiento del Proyecto (con Código)
1. Modelo de dominio (src/domain/)
Las clases en el directorio src/dominio/ definen la estructura de los datos del sistema. Evaluacion es la clase base, y Examen, Trabajo, Presentacion heredan de ella, añadiendo atributos y lógicas específicas.

Ejemplo: src/dominio/evaluacion.py (Clase Base)

Pitón

# src/dominio/evaluacion.py
from datetime import date

class Evaluacion:
    def __init__(self, nombre: str, fecha: date, puntaje: float, tipo: str):
        self.nombre = nombre
        self.fecha = fecha
        self.puntaje = puntaje
        self.tipo = tipo
        if not nombre:
            raise ValueError("El nombre de la evaluación no puede ser vacío.")
        if not isinstance(fecha, date):
            raise TypeError("La fecha debe ser un objeto date.")
        if not (0.0 <= puntaje <= 100.0):
            raise ValueError("El puntaje debe estar entre 0.0 y 100.0.")

    def calcular_nota(self) -> float:
        """
        Calcula la nota de la evaluación. Puede ser sobrescrito por subclases.
        """
        return self.puntaje

    def to_dict(self):
        """
        Serializa el objeto a un diccionario (útil para JSON o DB).
        """
        return {
            "nombre": self.nombre,
            "fecha": self.fecha.isoformat(), # Formato ISO para fechas
            "puntaje": self.puntaje,
            "tipo": self.tipo
        }
Ejemplo: src/dominio/examen.py (Clase Heredada)

Pitón

# src/dominio/examen.py
from src.dominio.evaluacion import Evaluacion
from datetime import date

class Examen(Evaluacion):
    def __init__(self, nombre: str, fecha: date, puntaje: float, duracion_min: int, num_preguntas: int):
        super().__init__(nombre, fecha, puntaje, "Examen") # Pasa el tipo "Examen"
        self.duracion_min = duracion_min
        self.num_preguntas = num_preguntas
        if not (15 <= self.duracion_min <= 300):
            raise ValueError("La duración del examen debe estar entre 15 y 300 minutos.")
        if not (1 <= self.num_preguntas <= 100):
            raise ValueError("El número de preguntas debe estar entre 1 y 100.")

    def calcular_nota(self) -> float:
        # Lógica específica para calcular la nota de un examen
        # Este es un ejemplo, se puede ajustar la fórmula.
        return self.puntaje * (self.num_preguntas / 100)
2. Conexión a la Base de Datos (src/datos/conexion.py)
La clase Conexion maneja la conexión singleton a SQL Server, asegurando que solo haya una instancia de conexión a la vez.

Ejemplo:src/datos/conexion.py

Pitón

# src/datos/conexion.py
import pyodbc as bd

class Conexion:
    _SERVIDOR = 'WILLIAM-PC\\VELEZSQLSERVER' # Configura tu servidor SQL
    _BBDD = 'GestionEvaluaciones'             # Configura tu base de datos
    _USUARIO = 'Evaluaciones'                 # Configura tu usuario
    _PASSWORD = '1234'                        # Configura tu contraseña

    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(
                    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                    f'SERVER={cls._SERVIDOR};'
                    f'DATABASE={cls._BBDD};'
                    f'UID={cls._USUARIO};'
                    f'PWD={cls._PASSWORD};'
                    f'CONNECT TIMEOUT=5;'
                )
                print("Conexión a SQL Server establecida exitosamente.")
            except bd.Error as ex:
                sqlstate = ex.args[0]
                raise ConnectionError(f"No se pudo conectar a la base de datos (SQLSTATE: {sqlstate}): {ex.args[1]}")
            except Exception as e:
                raise ConnectionError(f"Error inesperado al conectar a la base de datos: {e}")
        return cls._conexion

    @classmethod
    def cerrarConexion(cls):
        if cls._cursor:
            cls._cursor.close()
            cls._cursor = None
        if cls._conexion:
            cls._conexion.close()
            cls._conexion = None
            print("Conexión a SQL Server cerrada.")
3. Objeto de Acceso a Datos (src/datos/evaluacion_dao.py)
EvaluacionDAO es responsable de las operaciones de base de datos para los objetos Evaluacion y sus subclases.

Ejemplo: src/datos/evaluacion_dao.py (Fragmento para Cargar Evaluaciones)

Pitón

# src/datos/evaluacion_dao.py
import pyodbc
from src.datos.conexion import Conexion
from src.dominio.evaluacion import Evaluacion
from src.dominio.examen import Examen
from src.dominio.trabajo import Trabajo
from src.dominio.presentacion import Presentacion
from datetime import date

class EvaluacionDAO:
    def __init__(self):
        self.conexion = Conexion()

    def cargar_todas_las_evaluaciones(self):
        """
        Carga todas las evaluaciones desde la base de datos.
        """
        lista_evaluaciones = []
        conn = None
        cursor = None
        try:
            conn = self.conexion.obtenerConexion()
            cursor = conn.cursor()

            # Consulta para obtener evaluaciones base
            query_base = "SELECT EvaluacionID, Nombre, Fecha, Puntaje, Tipo FROM Evaluaciones"
            cursor.execute(query_base)
            evaluaciones_db = cursor.fetchall()

            for eval_id, nombre, fecha, puntaje, tipo in evaluaciones_db:
                # Dependiendo del tipo, cargar datos adicionales de las tablas específicas
                if tipo == "Examen":
                    query_especifico = "SELECT Duracion, NumPreguntas FROM Examenes WHERE EvaluacionID = ?"
                    cursor.execute(query_especifico, eval_id)
                    res = cursor.fetchone()
                    if res:
                        duracion, num_preguntas = res
                        lista_evaluaciones.append(Examen(nombre, fecha, puntaje, duracion, num_preguntas))
                elif tipo == "Trabajo":
                    query_especifico = "SELECT NumPaginas, Tema FROM Trabajos WHERE EvaluacionID = ?"
                    cursor.execute(query_especifico, eval_id)
                    res = cursor.fetchone()
                    if res:
                        num_paginas, tema = res
                        lista_evaluaciones.append(Trabajo(nombre, fecha, puntaje, num_paginas, tema))
                elif tipo == "Presentación":
                    query_especifico = "SELECT Duracion, TamanoAudiencia FROM Presentaciones WHERE EvaluacionID = ?"
                    cursor.execute(query_especifico, eval_id)
                    res = cursor.fetchone()
                    if res:
                        duracion, tamano_audiencia = res
                        lista_evaluaciones.append(Presentacion(nombre, fecha, puntaje, duracion, tamano_audiencia))
            return lista_evaluaciones
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            print(f"Error SQLSTATE al cargar evaluaciones: {sqlstate}. Mensaje: {ex.args[1]}")
            raise Exception(f"No se pudieron cargar las evaluaciones: {ex.args[1]}")
        finally:
            if cursor:
                cursor.close()
4. Gestor de Evaluaciones (src/servicio/gestor_evaluaciones.py)
El GestorEvaluaciones actúa como la capa de servicio, coordinando entre la lógica de la aplicación y el DAO.

Ejemplo: src/servicio/gestor_evaluaciones.py (Fragmento para Agregar una Evaluación)

Pitón

# src/servicio/gestor_evaluaciones.py
from src.dominio.evaluacion import Evaluacion
from src.datos.conexion import Conexion
from src.datos.evaluacion_dao import EvaluacionDAO
import pyodbc as bd

class GestorEvaluaciones:
    def __init__(self):
        self.evaluaciones = []
        self.dao = EvaluacionDAO() # Instancia el DAO
        self.db_conectada = False
        try:
            self.cargar_evaluaciones_desde_db()
            self.db_conectada = True
        except ConnectionError as e:
            print(f"Advertencia: La aplicación se inició sin conexión a la base de datos. Detalles: {e}")
            self.evaluaciones = []
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
            print("No hay conexión a la base de datos. No se puede agregar la evaluación.")
            return False

        if any(e.nombre == evaluacion.nombre for e in self.evaluaciones):
            print(f"Ya existe una evaluación con el nombre '{evaluacion.nombre}'.")
            return False

        try:
            self.dao.insertar_evaluacion(evaluacion) # Usa el DAO para insertar
            self.evaluaciones.append(evaluacion)
            print(f"Evaluación '{evaluacion.nombre}' agregada exitosamente.")
            return True
        except Exception as e:
            print(f"Error al agregar evaluación: {e}")
            return False

    def cargar_evaluaciones_desde_db(self):
        self.evaluaciones = self.dao.cargar_todas_las_evaluaciones() # Carga desde el DAO
        print(f"Cargadas {len(self.evaluaciones)} evaluaciones desde la base de datos.")

    # ... otros métodos como eliminar_evaluacion, actualizar_evaluacion, etc.
5. Lógica Principal de la Aplicación (src/servicio/persona.py)
La clase PersonaServicio (anteriormente MainWindow en los comentarios de tu código) es la que orquesta la interacción entre la interfaz de usuario y la lógica de negocio.

Ejemplo: src/servicio/persona.py (Fragmento para Crear una Evaluación)

Pitón

# src/servicio/persona.py
from PySide6.QtWidgets import (QMainWindow, QMessageBox, QTableWidgetItem,
                               QFileDialog, QApplication, QHeaderView, QTableWidget)
from PySide6.QtCore import QDate
from src.UI.vntEvaluacion import Ui_vntEvaluacion
from src.dominio.examen import Examen
from src.dominio.presentacion import Presentacion
from src.dominio.trabajo import Trabajo
from src.servicio.gestor_evaluaciones import GestorEvaluaciones
from datetime import date

class PersonaServicio(QMainWindow):
    def __init__(self):
        super(PersonaServicio, self).__init__()
        self.ui = Ui_vntEvaluacion()
        self.ui.setupUi(self)
        self.gestor = GestorEvaluaciones()
        self.current_editing_eval_name = None

        # Conectar señales de la UI a los slots (métodos)
        self.ui.btnCrear.clicked.connect(self.crear_evaluacion)
        self.ui.btnLimpiar.clicked.connect(self.limpiar_campos)
        self.ui.btnModificar.clicked.connect(self.modificar_evaluacion)
        self.ui.btnEliminar.clicked.connect(self.eliminar_evaluacion)
        self.ui.cboxTipoEvaluacion.currentIndexChanged.connect(self.actualizar_campos_por_tipo)
        self.ui.tablaEvaluaciones.itemSelectionChanged.connect(self.cargar_evaluacion_seleccionada)
        self.ui.actionGuardar.triggered.connect(self.guardar_a_json)
        self.ui.actionCargar.triggered.connect(self.cargar_desde_json)
        self.ui.actionAcerca_de.triggered.connect(self.mostrar_acerca_de)

        self.cargar_evaluaciones_en_tabla()
        self.actualizar_estadisticas()
        self.actualizar_campos_por_tipo() # Asegura que los campos correctos se muestren al inicio

    def crear_evaluacion(self):
        nombre = self.ui.txtNombre.text().strip()
        fecha_qdate = self.ui.dateEditFecha.date()
        fecha = date(fecha_qdate.year(), fecha_qdate.month(), fecha_qdate.day())
        puntaje = self.ui.sboxPuntaje.value()
        tipo_seleccionado = self.ui.cboxTipoEvaluacion.currentText()

        try:
            nueva_evaluacion = None
            if tipo_seleccionado == "Examen":
                duracion_min = self.ui.sboxDuracion.value()
                num_preguntas = self.ui.sboxPreguntas.value()
                nueva_evaluacion = Examen(nombre, fecha, puntaje, duracion_min, num_preguntas)
            elif tipo_seleccionado == "Trabajo":
                num_paginas = self.ui.sboxPaginas.value()
                tema = self.ui.txtTema.text().strip()
                nueva_evaluacion = Trabajo(nombre, fecha, puntaje, num_paginas, tema)
            elif tipo_seleccionado == "Presentación":
                duracion_min = self.ui.sboxDuracionPres.value() # Asumiendo un spinbox diferente
                tamano_audiencia = self.ui.sboxAudiencia.value()
                nueva_evaluacion = Presentacion(nombre, fecha, puntaje, duracion_min, tamano_audiencia)

            if nueva_evaluacion and self.gestor.agregar_evaluacion(nueva_evaluacion):
                QMessageBox.information(self, "Éxito", f"'{nombre}' agregado exitosamente.")
                self.cargar_evaluaciones_en_tabla()
                self.actualizar_estadisticas()
                self.limpiar_campos()
            elif not nueva_evaluacion:
                QMessageBox.warning(self, "Error de Tipo", "Tipo de evaluación no reconocido.")

        except ValueError as e:
            QMessageBox.warning(self, "Error de Validación", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error inesperado: {e}")

    # ... otros métodos como cargar_evaluaciones_en_tabla, actualizar_estadisticas, etc.
Configuración e instalación
Para configurar y ejecutar este proyecto, sigue estos pasos:

Prerrequisitos
Python 3.x: Asegúrate de tener Python instalado en tu sistema.

SQL Server: Necesitarás una instancia de SQL Server en ejecución. El proyecto está configurado para conectarse a WILLIAM-PC\VELEZSQLSERVER con la base de datos GestionEvaluaciones y un usuario Evaluaciones con contraseña 1234. Deberás ajustar estos valores en src/datos/conexion.py si tu configuración es diferente.

ODBC Driver 17 for SQL Server: Este driver es necesario para que pyodbc pueda comunicarse con SQL Server. Puedes descargarlo e instalarlo desde el sitio oficial de Microsoft.

Pasos de Instalación
Clonar el Repositorio:

Intento

git clone <URL_DE_TU_REPOSITORIO>
cd <nombre_de_tu_repositorio>
Crear y Activar un Entorno Virtual (Recomendado):

Intento

python -m venv venv
# En Windows:
.\venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate
Instalar Dependencias de Python:

Intento

pip install PySide6 pyodbc
Configuración de la Base de Datos:

Asegúrate de que tu instancia de SQL Server esté en funcionamiento.

Crea una base de datos con el nombre GestionEvaluaciones.

Crea un usuario Evaluaciones con la contraseña 1234 y otórgale los permisos necesarios (CREATE, SELECT, INSERT, UPDATE, DELETE) sobre la base de datos GestionEvaluaciones. Alternativamente, modifica las credenciales en src/datos/conexion.py para que coincidan con tu configuración de SQL Server.

Ejecutar el script de inserción de datos de ejemplo: Este script creará las tablas necesarias (Evaluaciones, Examenes, Trabajos, Presentaciones) y las poblará con algunos datos de prueba.

Intento

python src/datos/insertar_datos_ejemplo.py
(Nota: Este script limpia las tablas existentes antes de insertar nuevos datos de ejemplo, lo que es útil para pruebas iniciales.)

Cómo Ejecutar la Aplicación
Una vez que hayas completado la configuración e instalación, puedes ejecutar la aplicación principal desde el directorio raíz del proyecto:

Intento

python src/servicio/persona.py
Uso del Sistema
Al iniciar la aplicación, se mostrará la ventana principal del sistema de gestión de evaluaciones.

Puedes utilizar los campos de entrada y el selector de tipo de evaluación para ingresar los detalles de una nueva evaluación.

Haz clic en el botón "Crear" para añadir una nueva evaluación a la lista y a la base de datos.

Selecciona una fila en la tabla de evaluaciones para cargar sus datos en los campos y luego usar "Modificar" o "Eliminar".

La sección de "Estadísticas por Tipo" mostrará un resumen de las evaluaciones existentes.

Las opciones de menú "Archivo" permiten "Guardar" y "Cargar" datos de evaluaciones en formato JSON.
