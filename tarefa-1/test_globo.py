import unittest
from should_dsl import should

class MinimumNumberTest(unittest.TestCase):
    def test_deve_calcular_o_menor_numero_divisivel_por_tds_os_numeros_de_1_a_10(self):
        numero_minimo(10) |should| equal_to(2520)
    def test_deve_calcular_o_menor_numero_divisivel_por_tds_os_numeros_de_1_a_20(self):
        numero_minimo(20) |should| equal_to(232792560)

def numero_minimo(maximo_divisor):
    flag = True
    numero_base = 0
    while flag:
        numero_base += 1
        for divisor in range(1, maximo_divisor+1):
            if numero_base % divisor != 0:
                break
            elif divisor == maximo_divisor:
                flag = False

    return numero_base    

if __name__=="__main__":
    unittest.main()
