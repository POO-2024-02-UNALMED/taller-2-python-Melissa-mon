# Clase Asiento
class Asiento:
    def __init__(self, color, registro, precio):
        self.color = color
        self.registro = registro
        self.precio = precio

    def cambiarColor(self, nuevoColor):
        if nuevoColor in ["rojo", "verde", "amarillo", "negro", "blanco"]:
            self.color = nuevoColor

# Clase Motor
class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, nuevoRegistro):
        self.registro = nuevoRegistro

    def asignarTipo(self, nuevoTipo):
        if nuevoTipo in ["electrico", "gasolina"]:
            self.tipo = nuevoTipo

# Clase Auto
class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = []
        self.marca = marca
        self.motor