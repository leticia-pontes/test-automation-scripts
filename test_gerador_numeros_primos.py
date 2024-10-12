import unittest
from gerador_numeros_primos import gerar_numeros_primos

class TestNumerosPrimos(unittest.TestCase):
    def test_gerar_numeros_primos(self):
        self.assertEqual(gerar_numeros_primos(17), [2, 3, 5, 7, 11, 13, 17])

if __name__ == '__main__':
    unittest.main()