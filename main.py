# Clase Asiento
class Asiento:
    def __init__(self, color, registro):
        self.color = color
        self.registro = registro

    def cambiarColor(self, nuevoColor):
        # Validación de colores permitidos
        if nuevoColor in ["rojo", "verde", "amarillo", "negro", "blanco"]:
            self.color = nuevoColor


# Clase Motor
class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo if tipo in ["electrico", "gasolina"] else None
        self.registro = registro

    def cambiarRegistro(self, nuevoRegistro):
        # Aseguramos que el nuevo registro sea un entero
        if isinstance(nuevoRegistro, int):
            self.registro = nuevoRegistro

    def asignarTipo(self, nuevoTipo):
        # Validación de tipos de motor permitidos
        if nuevoTipo in ["electrico", "gasolina"]:
            self.tipo = nuevoTipo


# Clase Auto
class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = []  # Lista de objetos Asiento
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1

    def cantidadAsientos(self):
        # Retorna la cantidad de objetos Asiento en la lista asientos
        return len([asiento for asiento in self.asientos if isinstance(asiento, Asiento)])

    def verificarIntegridad(self):
        # Verificación de la integridad de los registros
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"
        for asiento in self.asientos:
            if asiento.registro != self.registro:
                return "Las piezas no son originales"
        return "Auto original"
