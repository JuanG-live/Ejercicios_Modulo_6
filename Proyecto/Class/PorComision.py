from Empleado import Empleado
from Enum.TipoContrato import TipoContrato
class PorComision(Empleado):
    def __init__(self, DNI, nombre, apellido, anioIngreso, Tipo_Contrato, clientesCaptados, montoPorCliente):
        super().__init__(DNI, nombre, apellido, anioIngreso, Tipo_Contrato)
        self.clientesCaptados = clientesCaptados
        self.montoPorCliente = montoPorCliente

    def calcularSalario(self):
        salario = self.clientesCaptados * self.montoPorCliente
        return salario

    @staticmethod
    def empleadoConMasClientes(empleados):
        max_clientes = 0
        empleado_max_clientes = None

        for empleado in empleados:
            if empleado.clientesCaptados > max_clientes:
                max_clientes = empleado.clientesCaptados
                empleado_max_clientes = empleado

        return empleado_max_clientes
    
    def mostrarSalario(self):
        return "Clientes Captados: " + str(self.clientesCaptados) + " Monto por Cliente: " + str(self.montoPorCliente)