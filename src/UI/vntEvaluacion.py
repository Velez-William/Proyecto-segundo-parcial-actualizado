# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vntEvaluacion.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDateEdit,
    QDoubleSpinBox, QFormLayout, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_vntEvaluacion(object):
    def setupUi(self, vntEvaluacion):
        if not vntEvaluacion.objectName():
            vntEvaluacion.setObjectName(u"vntEvaluacion")
        vntEvaluacion.resize(800, 579)
        self.actionNuevo = QAction(vntEvaluacion)
        self.actionNuevo.setObjectName(u"actionNuevo")
        self.actionAbrir = QAction(vntEvaluacion)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(vntEvaluacion)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionSalir = QAction(vntEvaluacion)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionAcerca_de = QAction(vntEvaluacion)
        self.actionAcerca_de.setObjectName(u"actionAcerca_de")
        self.centralwidget = QWidget(vntEvaluacion)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_main = QVBoxLayout(self.centralwidget)
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.lblTitulo = QLabel(self.centralwidget)
        self.lblTitulo.setObjectName(u"lblTitulo")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_main.addWidget(self.lblTitulo)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_crear = QWidget()
        self.tab_crear.setObjectName(u"tab_crear")
        self.verticalLayout_crear = QVBoxLayout(self.tab_crear)
        self.verticalLayout_crear.setObjectName(u"verticalLayout_crear")
        self.groupBox_datos = QGroupBox(self.tab_crear)
        self.groupBox_datos.setObjectName(u"groupBox_datos")
        self.formLayout = QFormLayout(self.groupBox_datos)
        self.formLayout.setObjectName(u"formLayout")
        self.lblNombre = QLabel(self.groupBox_datos)
        self.lblNombre.setObjectName(u"lblNombre")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblNombre)

        self.txtNombre = QLineEdit(self.groupBox_datos)
        self.txtNombre.setObjectName(u"txtNombre")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.txtNombre)

        self.lblFecha = QLabel(self.groupBox_datos)
        self.lblFecha.setObjectName(u"lblFecha")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblFecha)

        self.dateEdit_fecha = QDateEdit(self.groupBox_datos)
        self.dateEdit_fecha.setObjectName(u"dateEdit_fecha")
        self.dateEdit_fecha.setCalendarPopup(True)
        self.dateEdit_fecha.setDate(QDate(2024, 1, 1))

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.dateEdit_fecha)

        self.lblPuntaje = QLabel(self.groupBox_datos)
        self.lblPuntaje.setObjectName(u"lblPuntaje")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lblPuntaje)

        self.doubleSpinBox_puntaje = QDoubleSpinBox(self.groupBox_datos)
        self.doubleSpinBox_puntaje.setObjectName(u"doubleSpinBox_puntaje")
        self.doubleSpinBox_puntaje.setMaximum(100.000000000000000)
        self.doubleSpinBox_puntaje.setSingleStep(0.500000000000000)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox_puntaje)

        self.lblTipoEvaluacion = QLabel(self.groupBox_datos)
        self.lblTipoEvaluacion.setObjectName(u"lblTipoEvaluacion")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblTipoEvaluacion)

        self.cbTipo = QComboBox(self.groupBox_datos)
        self.cbTipo.addItem("")
        self.cbTipo.addItem("")
        self.cbTipo.addItem("")
        self.cbTipo.setObjectName(u"cbTipo")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cbTipo)


        self.verticalLayout_crear.addWidget(self.groupBox_datos)

        self.groupBox_parametros = QGroupBox(self.tab_crear)
        self.groupBox_parametros.setObjectName(u"groupBox_parametros")
        self.verticalLayout_parametros = QVBoxLayout(self.groupBox_parametros)
        self.verticalLayout_parametros.setObjectName(u"verticalLayout_parametros")
        self.stackedWidget_parametros = QStackedWidget(self.groupBox_parametros)
        self.stackedWidget_parametros.setObjectName(u"stackedWidget_parametros")
        self.page_examen = QWidget()
        self.page_examen.setObjectName(u"page_examen")
        self.formLayout_examen = QFormLayout(self.page_examen)
        self.formLayout_examen.setObjectName(u"formLayout_examen")
        self.lblDuracion = QLabel(self.page_examen)
        self.lblDuracion.setObjectName(u"lblDuracion")

        self.formLayout_examen.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblDuracion)

        self.spinBox_duracion = QSpinBox(self.page_examen)
        self.spinBox_duracion.setObjectName(u"spinBox_duracion")
        self.spinBox_duracion.setMinimum(15)
        self.spinBox_duracion.setMaximum(300)
        self.spinBox_duracion.setValue(120)

        self.formLayout_examen.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox_duracion)

        self.lblPreguntas = QLabel(self.page_examen)
        self.lblPreguntas.setObjectName(u"lblPreguntas")

        self.formLayout_examen.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblPreguntas)

        self.spinBox_preguntas = QSpinBox(self.page_examen)
        self.spinBox_preguntas.setObjectName(u"spinBox_preguntas")
        self.spinBox_preguntas.setMinimum(1)
        self.spinBox_preguntas.setMaximum(100)
        self.spinBox_preguntas.setValue(20)

        self.formLayout_examen.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinBox_preguntas)

        self.stackedWidget_parametros.addWidget(self.page_examen)
        self.page_trabajo = QWidget()
        self.page_trabajo.setObjectName(u"page_trabajo")
        self.formLayout_trabajo = QFormLayout(self.page_trabajo)
        self.formLayout_trabajo.setObjectName(u"formLayout_trabajo")
        self.lblPaginas = QLabel(self.page_trabajo)
        self.lblPaginas.setObjectName(u"lblPaginas")

        self.formLayout_trabajo.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblPaginas)

        self.spinBox_paginas = QSpinBox(self.page_trabajo)
        self.spinBox_paginas.setObjectName(u"spinBox_paginas")
        self.spinBox_paginas.setMinimum(1)
        self.spinBox_paginas.setMaximum(100)
        self.spinBox_paginas.setValue(10)

        self.formLayout_trabajo.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox_paginas)

        self.label_tema = QLabel(self.page_trabajo)
        self.label_tema.setObjectName(u"label_tema")

        self.formLayout_trabajo.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_tema)

        self.txtTema = QLineEdit(self.page_trabajo)
        self.txtTema.setObjectName(u"txtTema")

        self.formLayout_trabajo.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtTema)

        self.stackedWidget_parametros.addWidget(self.page_trabajo)
        self.page_presentacion = QWidget()
        self.page_presentacion.setObjectName(u"page_presentacion")
        self.formLayout_presentacion = QFormLayout(self.page_presentacion)
        self.formLayout_presentacion.setObjectName(u"formLayout_presentacion")
        self.lblDuracionPres = QLabel(self.page_presentacion)
        self.lblDuracionPres.setObjectName(u"lblDuracionPres")

        self.formLayout_presentacion.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lblDuracionPres)

        self.spinBox_duracion_pres = QSpinBox(self.page_presentacion)
        self.spinBox_duracion_pres.setObjectName(u"spinBox_duracion_pres")
        self.spinBox_duracion_pres.setMinimum(5)
        self.spinBox_duracion_pres.setMaximum(60)
        self.spinBox_duracion_pres.setValue(15)

        self.formLayout_presentacion.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox_duracion_pres)

        self.lblAudiencia = QLabel(self.page_presentacion)
        self.lblAudiencia.setObjectName(u"lblAudiencia")

        self.formLayout_presentacion.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblAudiencia)

        self.spinBox_audiencia = QSpinBox(self.page_presentacion)
        self.spinBox_audiencia.setObjectName(u"spinBox_audiencia")
        self.spinBox_audiencia.setMinimum(1)
        self.spinBox_audiencia.setMaximum(100)
        self.spinBox_audiencia.setValue(25)

        self.formLayout_presentacion.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinBox_audiencia)

        self.stackedWidget_parametros.addWidget(self.page_presentacion)

        self.verticalLayout_parametros.addWidget(self.stackedWidget_parametros)


        self.verticalLayout_crear.addWidget(self.groupBox_parametros)

        self.horizontalLayout_botones_crear = QHBoxLayout()
        self.horizontalLayout_botones_crear.setObjectName(u"horizontalLayout_botones_crear")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_botones_crear.addItem(self.horizontalSpacer)

        self.btnLimpiar = QPushButton(self.tab_crear)
        self.btnLimpiar.setObjectName(u"btnLimpiar")

        self.horizontalLayout_botones_crear.addWidget(self.btnLimpiar)

        self.btnCrear = QPushButton(self.tab_crear)
        self.btnCrear.setObjectName(u"btnCrear")

        self.horizontalLayout_botones_crear.addWidget(self.btnCrear)


        self.verticalLayout_crear.addLayout(self.horizontalLayout_botones_crear)

        self.tabWidget.addTab(self.tab_crear, "")
        self.tab_lista = QWidget()
        self.tab_lista.setObjectName(u"tab_lista")
        self.verticalLayout_lista = QVBoxLayout(self.tab_lista)
        self.verticalLayout_lista.setObjectName(u"verticalLayout_lista")
        self.horizontalLayout_filtros = QHBoxLayout()
        self.horizontalLayout_filtros.setObjectName(u"horizontalLayout_filtros")
        self.lblFiltro = QLabel(self.tab_lista)
        self.lblFiltro.setObjectName(u"lblFiltro")

        self.horizontalLayout_filtros.addWidget(self.lblFiltro)

        self.cbFiltro = QComboBox(self.tab_lista)
        self.cbFiltro.addItem("")
        self.cbFiltro.addItem("")
        self.cbFiltro.addItem("")
        self.cbFiltro.addItem("")
        self.cbFiltro.setObjectName(u"cbFiltro")

        self.horizontalLayout_filtros.addWidget(self.cbFiltro)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_filtros.addItem(self.horizontalSpacer_2)

        self.btnActualizar = QPushButton(self.tab_lista)
        self.btnActualizar.setObjectName(u"btnActualizar")

        self.horizontalLayout_filtros.addWidget(self.btnActualizar)


        self.verticalLayout_lista.addLayout(self.horizontalLayout_filtros)

        self.tableWidget_evaluaciones = QTableWidget(self.tab_lista)
        if (self.tableWidget_evaluaciones.columnCount() < 5):
            self.tableWidget_evaluaciones.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_evaluaciones.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_evaluaciones.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_evaluaciones.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_evaluaciones.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_evaluaciones.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget_evaluaciones.setObjectName(u"tableWidget_evaluaciones")
        self.tableWidget_evaluaciones.setAlternatingRowColors(True)
        self.tableWidget_evaluaciones.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_evaluaciones.setSortingEnabled(True)

        self.verticalLayout_lista.addWidget(self.tableWidget_evaluaciones)

        self.horizontalLayout_botones_lista = QHBoxLayout()
        self.horizontalLayout_botones_lista.setObjectName(u"horizontalLayout_botones_lista")
        self.btnVerDetalle = QPushButton(self.tab_lista)
        self.btnVerDetalle.setObjectName(u"btnVerDetalle")

        self.horizontalLayout_botones_lista.addWidget(self.btnVerDetalle)

        self.btnEditar = QPushButton(self.tab_lista)
        self.btnEditar.setObjectName(u"btnEditar")

        self.horizontalLayout_botones_lista.addWidget(self.btnEditar)

        self.btnEliminar = QPushButton(self.tab_lista)
        self.btnEliminar.setObjectName(u"btnEliminar")

        self.horizontalLayout_botones_lista.addWidget(self.btnEliminar)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_botones_lista.addItem(self.horizontalSpacer_3)


        self.verticalLayout_lista.addLayout(self.horizontalLayout_botones_lista)

        self.tabWidget.addTab(self.tab_lista, "")
        self.tab_estadisticas = QWidget()
        self.tab_estadisticas.setObjectName(u"tab_estadisticas")
        self.verticalLayout_estadisticas = QVBoxLayout(self.tab_estadisticas)
        self.verticalLayout_estadisticas.setObjectName(u"verticalLayout_estadisticas")
        self.groupBox_resumen = QGroupBox(self.tab_estadisticas)
        self.groupBox_resumen.setObjectName(u"groupBox_resumen")
        self.gridLayout_resumen = QGridLayout(self.groupBox_resumen)
        self.gridLayout_resumen.setObjectName(u"gridLayout_resumen")
        self.lblTotalEval = QLabel(self.groupBox_resumen)
        self.lblTotalEval.setObjectName(u"lblTotalEval")

        self.gridLayout_resumen.addWidget(self.lblTotalEval, 0, 0, 1, 1)

        self.lblTotalNumero = QLabel(self.groupBox_resumen)
        self.lblTotalNumero.setObjectName(u"lblTotalNumero")
        font1 = QFont()
        font1.setBold(True)
        self.lblTotalNumero.setFont(font1)

        self.gridLayout_resumen.addWidget(self.lblTotalNumero, 0, 1, 1, 1)

        self.lblPromedio = QLabel(self.groupBox_resumen)
        self.lblPromedio.setObjectName(u"lblPromedio")

        self.gridLayout_resumen.addWidget(self.lblPromedio, 1, 0, 1, 1)

        self.lblPromedioNumero = QLabel(self.groupBox_resumen)
        self.lblPromedioNumero.setObjectName(u"lblPromedioNumero")
        self.lblPromedioNumero.setFont(font1)

        self.gridLayout_resumen.addWidget(self.lblPromedioNumero, 1, 1, 1, 1)

        self.lblMejor = QLabel(self.groupBox_resumen)
        self.lblMejor.setObjectName(u"lblMejor")

        self.gridLayout_resumen.addWidget(self.lblMejor, 2, 0, 1, 1)

        self.lblMejorNombre = QLabel(self.groupBox_resumen)
        self.lblMejorNombre.setObjectName(u"lblMejorNombre")
        self.lblMejorNombre.setFont(font1)

        self.gridLayout_resumen.addWidget(self.lblMejorNombre, 2, 1, 1, 1)


        self.verticalLayout_estadisticas.addWidget(self.groupBox_resumen)

        self.groupBox_por_tipo = QGroupBox(self.tab_estadisticas)
        self.groupBox_por_tipo.setObjectName(u"groupBox_por_tipo")
        self.verticalLayout_tipos = QVBoxLayout(self.groupBox_por_tipo)
        self.verticalLayout_tipos.setObjectName(u"verticalLayout_tipos")
        self.textEdit_estadisticas = QTextEdit(self.groupBox_por_tipo)
        self.textEdit_estadisticas.setObjectName(u"textEdit_estadisticas")
        self.textEdit_estadisticas.setReadOnly(True)

        self.verticalLayout_tipos.addWidget(self.textEdit_estadisticas)


        self.verticalLayout_estadisticas.addWidget(self.groupBox_por_tipo)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_estadisticas.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_estadisticas, "")

        self.verticalLayout_main.addWidget(self.tabWidget)

        vntEvaluacion.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(vntEvaluacion)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        vntEvaluacion.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vntEvaluacion)
        self.statusbar.setObjectName(u"statusbar")
        vntEvaluacion.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuArchivo.addAction(self.actionNuevo)
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menuAyuda.addAction(self.actionAcerca_de)

        self.retranslateUi(vntEvaluacion)
        self.cbTipo.currentIndexChanged.connect(self.stackedWidget_parametros.setCurrentIndex)

        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget_parametros.setCurrentIndex(1)
        self.btnCrear.setDefault(True)


        QMetaObject.connectSlotsByName(vntEvaluacion)
    # setupUi

    def retranslateUi(self, vntEvaluacion):
        vntEvaluacion.setWindowTitle(QCoreApplication.translate("vntEvaluacion", u"Sistema de Gesti\u00f3n de Evaluaciones", None))
        self.actionNuevo.setText(QCoreApplication.translate("vntEvaluacion", u"Nuevo", None))
#if QT_CONFIG(shortcut)
        self.actionNuevo.setShortcut(QCoreApplication.translate("vntEvaluacion", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbrir.setText(QCoreApplication.translate("vntEvaluacion", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("vntEvaluacion", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("vntEvaluacion", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("vntEvaluacion", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSalir.setText(QCoreApplication.translate("vntEvaluacion", u"Salir", None))
#if QT_CONFIG(shortcut)
        self.actionSalir.setShortcut(QCoreApplication.translate("vntEvaluacion", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionAcerca_de.setText(QCoreApplication.translate("vntEvaluacion", u"Acerca de", None))
        self.lblTitulo.setText(QCoreApplication.translate("vntEvaluacion", u"Sistema de Gesti\u00f3n de Evaluaciones Acad\u00e9micas", None))
        self.groupBox_datos.setTitle(QCoreApplication.translate("vntEvaluacion", u"Datos de la Evaluaci\u00f3n", None))
        self.lblNombre.setText(QCoreApplication.translate("vntEvaluacion", u"Nombre:", None))
        self.txtNombre.setPlaceholderText(QCoreApplication.translate("vntEvaluacion", u"Ingrese el nombre de la evaluaci\u00f3n", None))
        self.lblFecha.setText(QCoreApplication.translate("vntEvaluacion", u"Fecha:", None))
        self.lblPuntaje.setText(QCoreApplication.translate("vntEvaluacion", u"Puntaje:", None))
        self.lblTipoEvaluacion.setText(QCoreApplication.translate("vntEvaluacion", u"Tipo de Evaluaci\u00f3n:", None))
        self.cbTipo.setItemText(0, QCoreApplication.translate("vntEvaluacion", u"Examen", None))
        self.cbTipo.setItemText(1, QCoreApplication.translate("vntEvaluacion", u"Trabajo", None))
        self.cbTipo.setItemText(2, QCoreApplication.translate("vntEvaluacion", u"Presentaci\u00f3n", None))

        self.groupBox_parametros.setTitle(QCoreApplication.translate("vntEvaluacion", u"Par\u00e1metros Espec\u00edficos", None))
        self.lblDuracion.setText(QCoreApplication.translate("vntEvaluacion", u"Duraci\u00f3n (minutos):", None))
        self.lblPreguntas.setText(QCoreApplication.translate("vntEvaluacion", u"N\u00famero de preguntas:", None))
        self.lblPaginas.setText(QCoreApplication.translate("vntEvaluacion", u"N\u00famero de p\u00e1ginas:", None))
        self.label_tema.setText(QCoreApplication.translate("vntEvaluacion", u"Tema:", None))
        self.txtTema.setPlaceholderText(QCoreApplication.translate("vntEvaluacion", u"Ingrese el tema del trabajo", None))
        self.lblDuracionPres.setText(QCoreApplication.translate("vntEvaluacion", u"Duraci\u00f3n (minutos):", None))
        self.lblAudiencia.setText(QCoreApplication.translate("vntEvaluacion", u"Tama\u00f1o de audiencia:", None))
        self.btnLimpiar.setText(QCoreApplication.translate("vntEvaluacion", u"Limpiar", None))
        self.btnCrear.setText(QCoreApplication.translate("vntEvaluacion", u"Crear Evaluaci\u00f3n", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_crear), QCoreApplication.translate("vntEvaluacion", u"Crear Evaluaci\u00f3n", None))
        self.lblFiltro.setText(QCoreApplication.translate("vntEvaluacion", u"Filtrar por tipo:", None))
        self.cbFiltro.setItemText(0, QCoreApplication.translate("vntEvaluacion", u"Todos", None))
        self.cbFiltro.setItemText(1, QCoreApplication.translate("vntEvaluacion", u"Examen", None))
        self.cbFiltro.setItemText(2, QCoreApplication.translate("vntEvaluacion", u"Trabajo", None))
        self.cbFiltro.setItemText(3, QCoreApplication.translate("vntEvaluacion", u"Presentaci\u00f3n", None))

        self.btnActualizar.setText(QCoreApplication.translate("vntEvaluacion", u"Actualizar", None))
        ___qtablewidgetitem = self.tableWidget_evaluaciones.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("vntEvaluacion", u"Nombre", None));
        ___qtablewidgetitem1 = self.tableWidget_evaluaciones.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("vntEvaluacion", u"Tipo", None));
        ___qtablewidgetitem2 = self.tableWidget_evaluaciones.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("vntEvaluacion", u"Fecha", None));
        ___qtablewidgetitem3 = self.tableWidget_evaluaciones.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("vntEvaluacion", u"Puntaje", None));
        ___qtablewidgetitem4 = self.tableWidget_evaluaciones.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("vntEvaluacion", u"Nota Calculada", None));
        self.btnVerDetalle.setText(QCoreApplication.translate("vntEvaluacion", u"Ver Detalle", None))
        self.btnEditar.setText(QCoreApplication.translate("vntEvaluacion", u"Editar", None))
        self.btnEliminar.setText(QCoreApplication.translate("vntEvaluacion", u"Eliminar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_lista), QCoreApplication.translate("vntEvaluacion", u"Lista de Evaluaciones", None))
        self.groupBox_resumen.setTitle(QCoreApplication.translate("vntEvaluacion", u"Resumen General", None))
        self.lblTotalEval.setText(QCoreApplication.translate("vntEvaluacion", u"Total de Evaluaciones:", None))
        self.lblTotalNumero.setText(QCoreApplication.translate("vntEvaluacion", u"0", None))
        self.lblPromedio.setText(QCoreApplication.translate("vntEvaluacion", u"Promedio General:", None))
        self.lblPromedioNumero.setText(QCoreApplication.translate("vntEvaluacion", u"0.0", None))
        self.lblMejor.setText(QCoreApplication.translate("vntEvaluacion", u"Mejor Evaluaci\u00f3n:", None))
        self.lblMejorNombre.setText(QCoreApplication.translate("vntEvaluacion", u"N/A", None))
        self.groupBox_por_tipo.setTitle(QCoreApplication.translate("vntEvaluacion", u"Estad\u00edsticas por Tipo", None))
        self.textEdit_estadisticas.setHtml(QCoreApplication.translate("vntEvaluacion", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">No hay evaluaciones registradas a\u00fan.</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_estadisticas), QCoreApplication.translate("vntEvaluacion", u"Estad\u00edsticas", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("vntEvaluacion", u"Archivo", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("vntEvaluacion", u"Ayuda", None))
    # retranslateUi

