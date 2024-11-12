class Asiento:
    def __init__(self, color, registro, precio):
        self.color = color
        self.registro = registro
        self.precio = precio

    def cambiarColor(self, nuevoColor):
        if nuevoColor == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco":
            self.color = nuevoColor
            
# Clase Auto
class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, asiento, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asiento
        self.marca = marca
        self.motor = motor
        self.registro = registro
    
    def cantidadAsientos(self):
        cantidadCreados = 0 
        for elementro in self.asientos: 
            if type(elementro)== Asiento: 
                cantidad += 1
        return (cantidad)
    
    def verificarIntegridad(self):
         if self.registro == self.motor.registro:
             for elemento in self.asientos:
                    if elementro.registro != self.registro:
                      return("Las piezas no son originales")
                    else:
                        return("Auto original")
         return("Las piezas no son originales")
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