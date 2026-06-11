# test_calculadora_ia.py
# Testes unitários gerados com apoio de IA (Claude) para a função calcular_media
# Ferramenta utilizada: Claude (https://claude.ai)

import unittest
from calculadora import calcular_media


class TestCalculadoraIA(unittest.TestCase):
    """Testes ampliados para calcular_media com cenários sugeridos por IA."""

    def test_media_lista_inteiros(self):
        """Caso normal: lista com múltiplos números inteiros."""
        self.assertEqual(calcular_media([10, 8, 6]), 8)

    def test_media_lista_decimais(self):
        """Caso normal: lista com números decimais."""
        self.assertEqual(calcular_media([2.5, 7.5]), 5.0)

    def test_media_lista_negativos(self):
        """Caso normal: lista com números negativos."""
        self.assertEqual(calcular_media([-2, -4, -6]), -4)

    def test_media_lista_positivos_e_negativos(self):
        """Caso normal: lista com positivos e negativos que se cancelam."""
        self.assertEqual(calcular_media([-5, 5]), 0)

    def test_media_lista_um_elemento(self):
        """Caso de borda: lista com um único elemento deve retornar o próprio valor."""
        self.assertEqual(calcular_media([7]), 7)

    def test_media_lista_todos_zeros(self):
        """Caso de borda: lista com apenas zeros deve retornar zero."""
        self.assertEqual(calcular_media([0, 0, 0]), 0)

    def test_media_lista_vazia_lanca_excecao(self):
        """Caso de erro: lista vazia deve lançar ValueError."""
        with self.assertRaises(ValueError):
            calcular_media([])


if __name__ == "__main__":
    unittest.main()