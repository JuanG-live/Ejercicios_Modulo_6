from .Class.PorComision import *
from .Class.SalarioFijo import *
from Enum.TipoContrato import TipoContrato
from Enum.Antiguedad import Antiguedad



empleadoUno = SalarioFijo(12345678, "Juan", "Perez", 2010, TipoContrato.FIJO, 10000, 0.1)
empleadoDos = PorComision(87654321, "Maria", "Gonzalez", 2015, Antiguedad.CAT1, 10, 1000)


print(empleadoUno.mostrarSalario())  
