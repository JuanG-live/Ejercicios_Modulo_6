from ..Enum import TipoContrato

class Empleado:
    def __init__(self, DNI, nombre, apellido, anioIngreso, Tipo_Contrato):       
        self.DNI = DNI 
        self.nombre = nombre
        self.apellido = apellido
        self.anioIngreso = anioIngreso
        self.Tipo_Contrato = Tipo_Contrato

    def getDNI(self):
        return self.DNI
    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apellido
    def getAnioIngreso(self):
        return self.anioIngreso
    def setNombre(self, nombre):
        self.nombre = nombre
    def setApellido(self, apellido):
        self.apellido = apellido
    def setAnioIngreso(self, anioIngreso):
        self.anioIngreso = anioIngreso
    def __str__(self):
        return "Empleado: " + self.nombre + " " + self.apellido + " " + str(self.anioIngreso)
    
    def calcularSalario(self):
        pass

    def mostrarSalario(self):
        pass
