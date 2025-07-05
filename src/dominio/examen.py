# src/dominio/examen.py
from src.dominio.evaluacion import Evaluacion
from datetime import date

class Examen(Evaluacion):
    def __init__(self, nombre: str, fecha: date, puntaje: float, duracion_min: int, num_preguntas: int):
        # Pasar el tipo "Examen" al constructor de la clase base
        super().__init__(nombre, fecha, puntaje, "Examen")
        self.duracion_min = duracion_min
        self.num_preguntas = num_preguntas
        if not (15 <= self.duracion_min <= 300):
            raise ValueError("La duración del examen debe estar entre 15 y 300 minutos.")
        if not (1 <= self.num_preguntas <= 100):
            raise ValueError("El número de preguntas debe estar entre 1 y 100.")

    def calcular_nota(self) -> float:
        # Lógica específica para calcular la nota de un examen
        # Por ejemplo, podrías dar más peso a las preguntas o la duración
        return (self.puntaje * self.num_preguntas / 100) / (self.duracion_min / 60) # Ejemplo: puedes ajustar esta fórmula
        # O simplemente el puntaje, si esa es la lógica actual
        # return self.puntaje

    def __str__(self):
        return f"Examen: {self.nombre}, Fecha: {self.fecha}, Puntaje: {self.puntaje}, Duración: {self.duracion_min} min, Preguntas: {self.num_preguntas}"

    def to_dict(self):
        # Sobrescribir to_dict para incluir parámetros específicos del examen
        data = super().to_dict()
        data.update({
            "duracion_min": self.duracion_min,
            "num_preguntas": self.num_preguntas
        })
        return data