# src/dominio/trabajo.py
from src.dominio.evaluacion import Evaluacion
from datetime import date

class Trabajo(Evaluacion):
    def __init__(self, nombre: str, fecha: date, puntaje: float, num_paginas: int, tema: str):
        # Pasar el tipo "Trabajo" al constructor de la clase base
        super().__init__(nombre, fecha, puntaje, "Trabajo")
        self.num_paginas = num_paginas
        self.tema = tema
        if not (1 <= self.num_paginas <= 100):
            raise ValueError("El número de páginas debe estar entre 1 y 100.")
        if not tema:
            raise ValueError("El tema del trabajo no puede ser vacío.")

    def calcular_nota(self) -> float:
        # Lógica específica para calcular la nota de un trabajo
        # return self.puntaje # Si simplemente es el puntaje
        return self.puntaje * (1 + (self.num_paginas / 100)) # Ejemplo: más páginas, mejor nota

    def __str__(self):
        return f"Trabajo: {self.nombre}, Fecha: {self.fecha}, Puntaje: {self.puntaje}, Páginas: {self.num_paginas}, Tema: {self.tema}"

    def to_dict(self):
        # Sobrescribir to_dict para incluir parámetros específicos del trabajo
        data = super().to_dict()
        data.update({
            "num_paginas": self.num_paginas,
            "tema": self.tema
        })
        return data