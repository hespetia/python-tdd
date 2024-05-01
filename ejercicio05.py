import unittest

def calcular_media_ponderada(numeros, pesos):
    """
    Calcula la media ponderada de una lista de números.

    Args:
        numeros (list): La lista de números a ponderar.
        pesos (list): La lista de pesos correspondientes a cada número.

    Returns:
        float: La media ponderada de los números.
    """
    # Implementación de la función

class TestCalcularMediaPonderada(unittest.TestCase):

    def test_media_ponderada_caso_simple(self):
        """
        Prueba el caso simple con dos números y pesos iguales.
        """
        numeros = [1, 2]
        pesos = [1, 1]
        resultado_esperado = 1.5
        self.assertEqual(calcular_media_ponderada(numeros, pesos), resultado_esperado)

    def test_media_ponderada_caso_pesos_diferentes(self):
        """
        Prueba el caso con dos números y pesos diferentes.
        """
        numeros = [1, 2]
        pesos = [2, 1]
        resultado_esperado = 1.3333333333333333
        self.assertEqual(calcular_media_ponderada(numeros, pesos), resultado_esperado)

    def test_media_ponderada_varios_numeros(self):
        """
        Prueba el caso con varios números y pesos.
        """
        numeros = [1, 2, 3, 4]
        pesos = [1, 2, 3, 4]
        resultado_esperado = 2.5
        self.assertEqual(calcular_media_ponderada(numeros, pesos), resultado_esperado)

    def test_media_ponderada_peso_cero(self):
        """
        Prueba el caso con un peso cero.
        """
        with self.assertRaises(ZeroDivisionError):
            numeros = [1, 2, 3]
            pesos = [1, 0, 1]
            calcular_media_ponderada(numeros, pesos)

if __name__ == "__main__":
    unittest.main()