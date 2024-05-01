import unittest

def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    return a / b
    
class TestOperaciones(unittest.TestCase):
          
    def test_suma(self):        
        esperado = 3
        actual = suma(1, 2)
        # Pásalo en el orden: actual, esperado
        self.assertEqual(actual, esperado)

    def test_resta(self):
        esperado = 5
        actual = resta(10, 5)
        # Pásalo en el orden: actual, esperado
        self.assertEqual(actual, esperado)

    def test_multiplicacion(self):
        esperado = 50
        actual = multiplicacion(10, 5)
        # Pásalo en el orden: actual, esperado
        self.assertEqual(actual, esperado)

    def test_division(self):
        esperado = 6
        actual = division(12, 2)
        # Pásalo en el orden: actual, esperado
        self.assertEqual(actual, esperado)

    def tearDown(self):
        # Aquí lo contrario de setUp, cuando cada test ha terminado
        pass

if __name__ == '__main__':
    unittest.main()