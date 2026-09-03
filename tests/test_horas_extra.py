import unittest

from horas_extra import calcular_pago_horas_extra


class TestCalcularPagoHorasExtra(unittest.TestCase):
    def test_calculo_basico(self):
        self.assertEqual(calcular_pago_horas_extra(5000, 3), 22500.0)

    def test_cero_horas(self):
        self.assertEqual(calcular_pago_horas_extra(5000, 0), 0.0)

    def test_valores_negativos_lanzan_error(self):
        with self.assertRaises(ValueError):
            calcular_pago_horas_extra(-1, 3)
        with self.assertRaises(ValueError):
            calcular_pago_horas_extra(5000, -1)


if __name__ == "__main__":
    unittest.main()
