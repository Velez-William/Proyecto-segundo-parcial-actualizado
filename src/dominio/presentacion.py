# src/dominio/presentacion.py
#nombre participante [ADRIANA BETANCOURTH, LISSETTE DANIELA MERO, WILLIAM VELEZ BARRE]
from src.dominio.evaluacion import Evaluacion
from datetime import date

class Presentacion(Evaluacion):
    def __init__(self, nombre: str, fecha: date, puntaje: float, duracion_min: int, tamano_audiencia: int):
        # Pasar el tipo "Presentación" al constructor de la clase base
        super().__init__(nombre, fecha, puntaje, "Presentación") # Usar "Presentación" para coincidir con la UI
        self.duracion_min = duracion_min
        self.tamano_audiencia = tamano_audiencia
        if not (5 <= self.duracion_min <= 60):
            raise ValueError("La duración de la presentación debe estar entre 5 y 60 minutos.")
        if not (1 <= self.tamano_audiencia <= 1000): # Ajusta el rango de audiencia si es necesario
            raise ValueError("El tamaño de la audiencia debe ser al menos 1.")

    def calcular_nota(self) -> float:
        # Lógica específica para calcular la nota de una presentación
        # return self.puntaje # Si simplemente es el puntaje
        return self.puntaje * (1 + (self.tamano_audiencia / 200)) # Ejemplo: más audiencia, mejor nota

    def __str__(self):
        return f"Presentación: {self.nombre}, Fecha: {self.fecha}, Puntaje: {self.puntaje}, Duración: {self.duracion_min} min, Audiencia: {self.tamano_audiencia}"

    def to_dict(self):
        # Sobrescribir to_dict para incluir parámetros específicos de la presentación
        data = super().to_dict()
        data.update({
            "duracion_min": self.duracion_min,
            "tamano_audiencia": self.tamano_audiencia
        })
        return data