import unittest

class CuentaBancaria:

    def __init__(self, nombre_titular):
        self.nombre_titular = nombre_titular
        self.saldo = 0
        self.historial_transacciones = []

    def depositar(self, monto):
        """
        Deposita un monto en la cuenta y actualiza el historial de transacciones.

        Args:
            monto (float): El monto a depositar.
        """
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser positivo")

        self.saldo += monto
        self.historial_transacciones.append(f"Deposito: ${monto}")

    def retirar(self, monto):
        """
        Retira un monto de la cuenta, actualiza el historial de transacciones y verifica que el saldo no quede negativo.

        Args:
            monto (float): El monto a retirar.
        """
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser positivo")

        if monto > self.saldo:
            raise ValueError("Saldo insuficiente para la retirada")

        self.saldo -= monto
        self.historial_transacciones.append(f"Retiro: ${monto}")

    def consultar_saldo(self):
        """
        Devuelve el saldo actual de la cuenta.

        Returns:
            float: El saldo actual de la cuenta.
        """
        return self.saldo

    def obtener_historial_transacciones(self):
        """
        Devuelve el historial de transacciones de la cuenta.

        Returns:
            list: El historial de transacciones de la cuenta.
        """
        return self.historial_transacciones

class TestCuentaBancaria(unittest.TestCase):

    def setUp(self):
        self.cuenta = CuentaBancaria("Juan Perez")

    def test_inicializacion_cuenta(self):
        self.assertEqual(self.cuenta.nombre_titular, "Juan Perez")
        self.assertEqual(self.cuenta.saldo, 0)
        self.assertEqual(self.cuenta.historial_transacciones, [])

    def test_depositar_monto_valido(self):
        self.cuenta.depositar(100)
        self.assertEqual(self.cuenta.saldo, 100)
        self.assertEqual(self.cuenta.historial_transacciones, ["Deposito: $100"])

    def test_depositar_monto_invalido(self):
        with self.assertRaises(ValueError):
            self.cuenta.depositar(-50)

    def test_retirar_monto_valido(self):
        self.cuenta.depositar(100)
        self.cuenta.retirar(10)

if __name__ == "__main__":
    unittest.main()
