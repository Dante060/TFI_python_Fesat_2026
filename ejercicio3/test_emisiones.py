import unittest
from utils import calcular_emisiones_carbono

class TestCalculoEmisiones(unittest.TestCase):

    def test_calculo_nominal_factor_defecto(self):
        resultado = calcular_emisiones_carbono(100)
        self.assertAlmostEqual(resultado, 40)

    def test_calculo_nominal_factor_personalizado(self):
        resultado = calcular_emisiones_carbono(200, factor_emision= 0.5)
        self.assertAlmostEqual(resultado, 100)

    def test_calculo_consumo_cero(self):
        self.assertAlmostEqual(calcular_emisiones_carbono(0), 0.0)
    
    def test_consumo_negativo_lanza_excepcion(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-10)

if __name__ == "__main__":
    unittest.main()