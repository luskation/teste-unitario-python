# test_calculadora.py

import unittest
from calculadora import somar, subtrair, multiplicar, dividir, potencia, calcular_media

class TestCalculadora(unittest.TestCase):
    """Classe de testes para as funções do arquivo calculadora.py."""

    def test_somar(self):
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-1, 1), 0)
        self.assertEqual(somar(0, 0), 0)

    def test_subtrair(self):
        self.assertEqual(subtrair(10, 5), 5)
        self.assertEqual(subtrair(5, 10), -5)
        self.assertEqual(subtrair(0, 0), 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 4), 12)
        self.assertEqual(multiplicar(5, 0), 0)
        self.assertEqual(multiplicar(-2, 3), -6)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(9, 3), 3)
        self.assertEqual(dividir(5, 2), 2.5)

    def test_dividir_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)
        self.assertEqual(potencia(5, 0), 1)
        self.assertEqual(potencia(10, 2), 100)

    def test_calcular_media_lista_valida(self):
        self.assertEqual(calcular_media([10, 8, 6]), 8)
        self.assertEqual(calcular_media([5.5, 4.5]), 5.0)
        self.assertEqual(calcular_media([7]), 7)

    def test_calcular_media_lista_vazia(self):
        with self.assertRaises(ValueError):
            calcular_media([])

if __name__ == "__main__":
    unittest.main()