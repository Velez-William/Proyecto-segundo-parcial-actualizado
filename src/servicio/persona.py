# src/servicio/persona.py

import json
import re # Necesario para validaciones si usas expresiones regulares
from datetime import date

from PySide6.QtWidgets import (QMainWindow, QMessageBox, QTableWidgetItem,
                               QFileDialog, QApplication, QHeaderView, QTableWidget)
from PySide6.QtCore import QDate

# Asegúrate de que esta importación sea correcta para tu UI de evaluación
from src.UI.vntEvaluacion import Ui_vntEvaluacion

from src.dominio.examen import Examen
from src.dominio.presentacion import Presentacion
from src.dominio.trabajo import Trabajo
from src.servicio.gestor_evaluaciones import GestorEvaluaciones


class PersonaServicio(QMainWindow): # Renombrada de MainWindow
    """
    Clase principal de la aplicación que maneja la interfaz de usuario vntEvaluacion
    y la lógica de gestión de evaluaciones, incluyendo sus validaciones.
    """

    def __init__(self):
        super(PersonaServicio, self).__init__()
        self.ui = Ui_vntEvaluacion() # Usa la UI de vntEvaluacion
        self.ui.setupUi(self)

        self.gestor = GestorEvaluaciones()

        self.current_editing_eval_name = None

        # Conectar señales de la UI a los slots (métodos)
        self.ui.btnCrear.clicked.connect(self.crear_evaluacion)
        self.ui.btnLimpiar.clicked.connect(self.limpiar_campos)
        self.ui.cbTipo.currentIndexChanged.connect(self.ui.stackedWidget_parametros.setCurrentIndex)
        self.ui.cbTipo.currentIndexChanged.connect(self.actualizar_parametros_ui)

        self.ui.btnActualizar.clicked.connect(self.cargar_evaluaciones_en_tabla)
        self.ui.btnEliminar.clicked.connect(self.eliminar_evaluacion)
        self.ui.cbFiltro.currentIndexChanged.connect(self.cargar_evaluaciones_en_tabla)
        self.ui.btnVerDetalle.clicked.connect(self.mostrar_detalle_evaluacion)
        self.ui.btnEditar.clicked.connect(self.seleccionar_evaluacion_para_edicion)

        # Conexiones para las acciones del menú
        self.ui.actionNuevo.triggered.connect(self.limpiar_campos)
        self.ui.actionAbrir.triggered.connect(self.abrir_archivo_evaluaciones)
        self.ui.actionGuardar.triggered.connect(self.guardar_archivo_evaluaciones)
        self.ui.actionSalir.triggered.connect(self.close)
        self.ui.actionAcerca_de.triggered.connect(self.mostrar_acerca_de)

        # Configuración inicial de la tabla
        self.ui.tableWidget_evaluaciones.setSelectionBehavior(QTableWidget.SelectRows)
        self.ui.tableWidget_evaluaciones.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.tableWidget_evaluaciones.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_evaluaciones.verticalHeader().setVisible(False)

        # Inicializar la UI
        self.cargar_evaluaciones_en_tabla()
        self.actualizar_resumen_estadisticas()
        self.limpiar_campos()
        self.ui.tabWidget.setCurrentIndex(0)

    # --- Métodos de Validación (privados para la clase) ---
    def _validar_nombre_evaluacion(self, nombre: str) -> bool:
        if not nombre:
            QMessageBox.warning(self, "Entrada Inválida", "El nombre de la evaluación no puede estar vacío.")
            return False
        if len(nombre) < 3:
            QMessageBox.warning(self, "Entrada Inválida",
                                "El nombre de la evaluación debe tener al menos 3 caracteres.")
            return False
        if len(nombre) > 100:
            QMessageBox.warning(self, "Entrada Inválida",
                                "El nombre de la evaluación no puede exceder los 100 caracteres.")
            return False
        return True

    def _validar_tema_trabajo(self, tema: str) -> bool:
        if not tema:
            QMessageBox.warning(self, "Entrada Inválida", "El tema del trabajo no puede estar vacío.")
            return False
        if len(tema) < 3:
            QMessageBox.warning(self, "Entrada Inválida",
                                "El tema del trabajo debe tener al menos 3 caracteres.")
            return False
        if len(tema) > 255:
            QMessageBox.warning(self, "Entrada Inválida",
                                "El tema del trabajo no puede exceder los 255 caracteres.")
            return False
        return True

    # --- Métodos de la Interfaz y Lógica de Negocio ---
    def limpiar_campos(self):
        self.ui.txtNombre.clear()
        self.ui.dateEdit_fecha.setDate(QDate.currentDate())
        self.ui.doubleSpinBox_puntaje.setValue(0.0)
        self.ui.cbTipo.setCurrentIndex(0)

        self.ui.spinBox_duracion.setValue(15)
        self.ui.spinBox_preguntas.setValue(1)
        self.ui.spinBox_paginas.setValue(1)
        self.ui.txtTema.clear()
        self.ui.spinBox_duracion_pres.setValue(5)
        self.ui.spinBox_audiencia.setValue(1)

        self.ui.stackedWidget_parametros.setCurrentIndex(0)
        self.ui.btnCrear.setText("Crear Evaluación")
        self.current_editing_eval_name = None

    def actualizar_parametros_ui(self):
        pass

    def crear_evaluacion(self):
        nombre = self.ui.txtNombre.text().strip()
        fecha = self.ui.dateEdit_fecha.date().toPython()
        puntaje = self.ui.doubleSpinBox_puntaje.value()
        tipo_evaluacion_str = self.ui.cbTipo.currentText()

        # --- USO DE LAS VALIDACIONES INTERNAS ---
        if not self._validar_nombre_evaluacion(nombre):
            return
        # ----------------------------------------

        try:
            evaluacion = None
            if tipo_evaluacion_str == "Examen":
                duracion = self.ui.spinBox_duracion.value()
                num_preguntas = self.ui.spinBox_preguntas.value()
                evaluacion = Examen(nombre, fecha, puntaje, duracion, num_preguntas)
            elif tipo_evaluacion_str == "Trabajo":
                num_paginas = self.ui.spinBox_paginas.value()
                tema = self.ui.txtTema.text().strip()

                # --- USO DE LAS VALIDACIONES INTERNAS PARA TEMA ---
                if not self._validar_tema_trabajo(tema):
                    return
                # ----------------------------------------------------

                evaluacion = Trabajo(nombre, fecha, puntaje, num_paginas, tema)
            elif tipo_evaluacion_str == "Presentación":
                duracion_pres = self.ui.spinBox_duracion_pres.value()
                tamano_audiencia = self.ui.spinBox_audiencia.value()
                evaluacion = Presentacion(nombre, fecha, puntaje, duracion_pres, tamano_audiencia)
            else:
                QMessageBox.critical(self, "Error de Tipo", "Tipo de evaluación no reconocido.")
                return

            if self.current_editing_eval_name:
                self.gestor.eliminar_evaluacion_por_nombre(self.current_editing_eval_name)
                self.gestor.agregar_evaluacion(evaluacion)
                QMessageBox.information(self, "Éxito", f"Evaluación '{nombre}' actualizada correctamente.")
            else:
                if self.gestor.obtener_evaluacion_por_nombre(nombre):
                    QMessageBox.warning(self, "Evaluación Existente",
                                        f"Ya existe una evaluación con el nombre '{nombre}'. Por favor, use un nombre diferente o edite la existente.")
                    return
                self.gestor.agregar_evaluacion(evaluacion)
                QMessageBox.information(self, "Éxito", f"Evaluación '{nombre}' creada correctamente.")

            self.limpiar_campos()
            self.cargar_evaluaciones_en_tabla()
            self.actualizar_resumen_estadisticas()

        except ValueError as ve:
            QMessageBox.warning(self, "Error de Datos", str(ve))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error inesperado: {e}")

    def cargar_evaluaciones_en_tabla(self):
        self.ui.tableWidget_evaluaciones.setRowCount(0)

        filtro_tipo = self.ui.cbFiltro.currentText()
        evaluaciones_filtradas = self.gestor.filtrar_evaluaciones_por_tipo(filtro_tipo)

        self.ui.tableWidget_evaluaciones.setRowCount(len(evaluaciones_filtradas))

        for row, eval_obj in enumerate(evaluaciones_filtradas):
            self.ui.tableWidget_evaluaciones.setItem(row, 0, QTableWidgetItem(eval_obj.nombre))
            self.ui.tableWidget_evaluaciones.setItem(row, 1, QTableWidgetItem(eval_obj.__class__.__name__))
            self.ui.tableWidget_evaluaciones.setItem(row, 2,
                                                     QTableWidgetItem(eval_obj.fecha.strftime("%Y-%m-%d")))
            self.ui.tableWidget_evaluaciones.setItem(row, 3,
                                                     QTableWidgetItem(f"{eval_obj.puntaje:.1f}"))
            self.ui.tableWidget_evaluaciones.setItem(row, 4, QTableWidgetItem(
                f"{eval_obj.calcular_nota():.1f}"))

        self.ui.tableWidget_evaluaciones.resizeColumnsToContents()
        self.actualizar_resumen_estadisticas()

    def eliminar_evaluacion(self):
        selected_rows = self.ui.tableWidget_evaluaciones.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Eliminar Evaluación", "Por favor, seleccione una evaluación para eliminar.")
            return

        reply = QMessageBox.question(self, "Confirmar Eliminación",
                                     "¿Está seguro de que desea eliminar la evaluación seleccionada?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            for index in sorted(selected_rows, reverse=True):
                nombre_eval = self.ui.tableWidget_evaluaciones.item(index.row(), 0).text()
                self.gestor.eliminar_evaluacion_por_nombre(nombre_eval)
            QMessageBox.information(self, "Éxito", "Evaluación(es) eliminada(s) correctamente.")
            self.cargar_evaluaciones_en_tabla()
            self.actualizar_resumen_estadisticas()

    def mostrar_detalle_evaluacion(self):
        selected_rows = self.ui.tableWidget_evaluaciones.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Ver Detalle", "Por favor, seleccione una evaluación para ver su detalle.")
            return

        row = selected_rows[0].row()
        nombre_eval = self.ui.tableWidget_evaluaciones.item(row, 0).text()
        eval_obj = self.gestor.obtener_evaluacion_por_nombre(nombre_eval)

        if eval_obj:
            detalle_msg = f"Nombre: {eval_obj.nombre}\n" \
                          f"Fecha: {eval_obj.fecha.strftime('%Y-%m-%d')}\n" \
                          f"Puntaje Base: {eval_obj.puntaje:.1f}\n" \
                          f"Tipo: {eval_obj.__class__.__name__}\n"

            if isinstance(eval_obj, Examen):
                detalle_msg += f"Duración: {eval_obj.duracion_min} minutos\n" \
                               f"Nº Preguntas: {eval_obj.num_preguntas}\n"
            elif isinstance(eval_obj, Trabajo):
                detalle_msg += f"Nº Páginas: {eval_obj.num_paginas}\n" \
                               f"Tema: {eval_obj.tema}\n"
            elif isinstance(eval_obj, Presentacion):
                detalle_msg += f"Duración: {eval_obj.duracion_min} minutos\n" \
                               f"Tamaño Audiencia: {eval_obj.tamano_audiencia}\n"

            detalle_msg += f"Nota Calculada: {eval_obj.calcular_nota():.1f}"

            QMessageBox.information(self, f"Detalle de '{eval_obj.nombre}'", detalle_msg)
        else:
            QMessageBox.warning(self, "Error", "No se pudo encontrar la evaluación seleccionada.")

    def seleccionar_evaluacion_para_edicion(self):
        selected_rows = self.ui.tableWidget_evaluaciones.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(self, "Editar Evaluación", "Por favor, seleccione una evaluación para editar.")
            return

        row = selected_rows[0].row()
        nombre_eval = self.ui.tableWidget_evaluaciones.item(row, 0).text()
        eval_obj = self.gestor.obtener_evaluacion_por_nombre(nombre_eval)

        if eval_obj:
            self.limpiar_campos()
            self.ui.txtNombre.setText(eval_obj.nombre)
            self.ui.dateEdit_fecha.setDate(QDate(eval_obj.fecha))
            self.ui.doubleSpinBox_puntaje.setValue(eval_obj.puntaje)

            if isinstance(eval_obj, Examen):
                self.ui.cbTipo.setCurrentIndex(0)
                self.ui.spinBox_duracion.setValue(eval_obj.duracion_min)
                self.ui.spinBox_preguntas.setValue(eval_obj.num_preguntas)
            elif isinstance(eval_obj, Trabajo):
                self.ui.cbTipo.setCurrentIndex(1)
                self.ui.spinBox_paginas.setValue(eval_obj.num_paginas)
                self.ui.txtTema.setText(eval_obj.tema)
            elif isinstance(eval_obj, Presentacion):
                self.ui.cbTipo.setCurrentIndex(2)
                self.ui.spinBox_duracion_pres.setValue(eval_obj.duracion_min)
                self.ui.spinBox_audiencia.setValue(eval_obj.tamano_audiencia)

            self.ui.btnCrear.setText("Actualizar Evaluación")
            self.current_editing_eval_name = eval_obj.nombre
            self.ui.tabWidget.setCurrentIndex(0)
        else:
            QMessageBox.warning(self, "Error", "No se pudo encontrar la evaluación seleccionada para edición.")

    def actualizar_resumen_estadisticas(self):
        total_evaluaciones = len(self.gestor.evaluaciones)
        self.ui.lblTotalNumero.setText(str(total_evaluaciones))

        promedio_general = self.gestor.calcular_promedio_general()
        self.ui.lblPromedioNumero.setText(f"{promedio_general:.1f}")

        mejor_evaluacion = self.gestor.obtener_mejor_evaluacion()
        if mejor_evaluacion:
            self.ui.lblMejorNombre.setText(f"{mejor_evaluacion.nombre} ({mejor_evaluacion.calcular_nota():.1f})")
        else:
            self.ui.lblMejorNombre.setText("N/A")

        stats_por_tipo = self.gestor.obtener_estadisticas_por_tipo()
        stats_text = "<h3>Estadísticas por Tipo de Evaluación:</h3>"
        for tipo, stats in stats_por_tipo.items():
            stats_text += f"<h4>{tipo}:</h4>"
            if stats['count'] > 0:
                stats_text += f"  - Cantidad: {stats['count']}<br>"
                stats_text += f"  - Promedio: {stats['promedio']:.1f}<br>"
                stats_text += f"  - Mejor: {stats['best_name']} ({stats['best_score']:.1f})<br>"
            else:
                stats_text += "  - No hay evaluaciones registradas para este tipo.<br>"
        self.ui.textEdit_estadisticas.setHtml(stats_text)

    def abrir_archivo_evaluaciones(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Abrir Archivo de Evaluaciones", "",
                                                   "Archivos JSON (*.json);;Todos los archivos (*)")
        if file_name:
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                self.gestor.limpiar_todas_las_evaluaciones()

                for eval_dict in data:
                    nombre = eval_dict['nombre']
                    fecha = date.fromisoformat(eval_dict['fecha'])
                    puntaje = eval_dict['puntaje']
                    tipo = eval_dict['tipo']

                    eval_obj = None
                    if tipo == "Examen":
                        eval_obj = Examen(nombre, fecha, puntaje,
                                          eval_dict.get('duracion_min', 0),
                                          eval_dict.get('num_preguntas', 0))
                    elif tipo == "Trabajo":
                        eval_obj = Trabajo(nombre, fecha, puntaje,
                                           eval_dict.get('num_paginas', 0),
                                           eval_dict.get('tema', ''))
                    elif tipo == "Presentacion":
                        eval_obj = Presentacion(nombre, fecha, puntaje,
                                                eval_dict.get('duracion_min', 0),
                                                eval_dict.get('tamano_audiencia', 0))

                    if eval_obj:
                        self.gestor.agregar_evaluacion(eval_obj)

                QMessageBox.information(self, "Abrir Archivo", f"Evaluaciones cargadas desde '{file_name}'.")
                self.cargar_evaluaciones_en_tabla()
                self.actualizar_resumen_estadisticas()
                self.limpiar_campos()
            except Exception as e:
                QMessageBox.critical(self, "Error al abrir", f"Ocurrió un error al abrir el archivo: {e}")

    def guardar_archivo_evaluaciones(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Guardar Archivo de Evaluaciones", "",
                                                   "Archivos JSON (*.json);;Todos los archivos (*)")
        if file_name:
            try:
                data_to_save = []
                for eval_obj in self.gestor.evaluaciones:
                    eval_dict = {
                        'nombre': eval_obj.nombre,
                        'fecha': eval_obj.fecha.isoformat(),
                        'puntaje': eval_obj.puntaje,
                        'tipo': eval_obj.__class__.__name__
                    }
                    if isinstance(eval_obj, Examen):
                        eval_dict['duracion_min'] = eval_obj.duracion_min
                        eval_dict['num_preguntas'] = eval_obj.num_preguntas
                    elif isinstance(eval_obj, Trabajo):
                        eval_dict['num_paginas'] = eval_obj.num_paginas
                        eval_dict['tema'] = eval_obj.tema
                    elif isinstance(eval_obj, Presentacion):
                        eval_dict['duracion_min'] = eval_obj.duracion_min
                        eval_dict['tamano_audiencia'] = eval_obj.tamano_audiencia
                    data_to_save.append(eval_dict)

                with open(file_name, 'w', encoding='utf-8') as f:
                    json.dump(data_to_save, f, indent=4)
                QMessageBox.information(self, "Guardar Archivo", f"Evaluaciones guardadas en '{file_name}'.")
            except Exception as e:
                QMessageBox.critical(self, "Error al guardar", f"Ocurrió un error al guardar el archivo: {e}")

    def mostrar_acerca_de(self):
        QMessageBox.about(self, "Acerca de Sistema de Gestión de Evaluaciones",
                          "Sistema de Gestión de Evaluaciones Académicas\n"
                          "Versión 1.0\n\n"
                          "Desarrollado por: [Tu Nombre 1], [Tu Nombre 2]\n\n"
                          "Aplicación de ejemplo para demostrar principios de POO con PySide6.")
