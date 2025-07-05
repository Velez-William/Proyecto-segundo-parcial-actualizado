# main.py

import sys
from PySide6.QtWidgets import QApplication

# Importa la clase PersonaServicio desde el archivo persona.py
from src.servicio.persona import PersonaServicio

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Crea una instancia de PersonaServicio, que ahora maneja vntEvaluacion
    vnt_evaluacion = PersonaServicio()
    vnt_evaluacion.show()
    sys.exit(app.exec())
