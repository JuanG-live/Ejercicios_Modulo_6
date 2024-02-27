from ..Class import Empleado

class SalarioFijo(Empleado):
    def __init__(self, DNI, nombre, apellido, anioIngreso, Tipo_Contrato, sueldo_fijo, porcentaje_adicional):
        super().__init__(DNI, nombre, apellido, anioIngreso, Tipo_Contrato)
        self.sueldo_fijo = sueldo_fijo
        self.porcentaje_adicional = porcentaje_adicional

    def calcularAntiguedad(self):
        antiguedad = 2024 - self.anioIngreso
        if antiguedad < 2:
            return 0
        elif antiguedad >= 2 and antiguedad <= 5:
            return 0.05
        else:
            return 0.1
        
    def calcularSalar(self):
        salario = self.sueldo_fijo + (self.sueldo_fijo * self.calcularAntiguedad())
        return salario
    
    def mostrarSalario(self):
        return "Salario Fijo: " + str(self.sueldo_fijo) + " " + str(self.porcentaje_adicional)
    