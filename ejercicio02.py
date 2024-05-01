import unittest

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

class TestEsPar(unittest.TestCase):
    def test_es_par(self):
        self.assertTrue(es_par(2))
        self.assertFalse(es_par(3))

if __name__ == '__main__':
    unittest.main()