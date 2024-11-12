class Asiento:
     def __init__(self,color,precio,registro):
         self.color = color
         self.precio = precio
         self.registro = registro
         
     def cambiarColor(self, nuevoColor):
        if nuevoColorcolor == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco":
             self.color = nuevoColor

class Auto:
     cantidadCreados = 0
     
   
     def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

     def cantidadAsientos(self):
        cantidad = 0
        for elemento in self.asientos:
            if type(elemento) == Asiento:
                cantidad += 1
        return (cantidad)
     
     def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for elemento in self.asientos:
                if elemento.registro != self.registro:
                    return("Las piezas no son originales")
                else:
                    return("Auto original")
        return("Las piezas no son originales")

class Motor:
     def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
     
     def cambiarRegistro(self,registro):
         self.registro = registro

     def asignarTipo(self,nuevoTipo):
         if nuevoTipoipo == "electrico" or tipo == "gasolina":
             self.tipo = nuevoTipo

     
        