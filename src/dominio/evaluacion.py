# src/dominio/evaluacion.py
from datetime import date

class Evaluacion:
    def __init__(self, nombre: str, fecha: date, puntaje: float, tipo: str): # Añadir 'tipo' aquí
        self.nombre = nombre
        self.fecha = fecha
        self.puntaje = puntaje
        self.tipo = tipo # Guardar el atributo tipo
        # Asegúrate de que el nombre sea único o maneja colisiones en el gestor
        # Validación básica si quieres que no sea vacio
        if not nombre:
            raise ValueError("El nombre de la evaluación no puede ser vacío.")
        if not isinstance(fecha, date):
            raise TypeError("La fecha debe ser un objeto date.")
        if not (0.0 <= puntaje <= 100.0):
            raise ValueError("El puntaje debe estar entre 0.0 y 100.0.")

    def calcular_nota(self) -> float:
        # Este método podría ser abstracto o tener una implementación por defecto
        # que las subclases sobrescribirán.
        # Por ahora, simplemente devolvemos el puntaje tal como está si no hay otra lógica.
        return self.puntaje

    def __str__(self):
        return f"Evaluación: {self.nombre}, Tipo: {self.tipo}, Fecha: {self.fecha}, Puntaje: {self.puntaje}"

    def to_dict(self):
        # Método para serializar a diccionario (útil para JSON o DB)
        return {
            "nombre": self.nombre,
            "fecha": self.fecha.isoformat(),
            "puntaje": self.puntaje,
            "tipo": self.tipo
        }