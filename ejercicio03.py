import unittest

def calcular_area_triangulo(base, altura):
    # Implementación de la función
    return (base * altura) / 2

class TestCalcularAreaTriangulo(unittest.TestCase):

    def test_calcular_area_triangulo_base_cero(self):
        """
        Prueba el caso en que la base del triángulo es cero.
        """
        self.assertEqual(calcular_area_triangulo(0, 5), 0)

    def test_calcular_area_triangulo_altura_cero(self):
        """
        Prueba el caso en que la altura del triángulo es cero.
        """
        self.assertEqual(calcular_area_triangulo(5, 0), 0)

    def test_calcular_area_triangulo_caso_general(self):
        """
        Prueba el caso general con base y altura positivas.
        """
        self.assertEqual(calcular_area_triangulo(5, 4), 10)

if __name__ == "__main__":
    unittest.main()