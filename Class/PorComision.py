class PorComision:
    def __init__(self, clientesCaptados, montoPorCliente):
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