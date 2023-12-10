import unittest
from conversor import (celsius_para_fahrenheit, fahrenheit_para_celsius, celsius_para_kelvin, kelvin_para_celsius,fahrenheit_para_kelvin, kelvin_para_fahrenheit, metros_para_quilometros, quilometros_para_metros, metros_para_centimetros, quilometros_para_centimetros)

class TestConversions(unittest.TestCase):

    # Testes de conversão de temperatura...
    
    # Testes de conversão de medidas de comprimento
    def test_metros_para_quilometros(self):
        self.assertAlmostEqual(metros_para_quilometros(1000), 1)
        self.assertAlmostEqual(metros_para_quilometros(5000), 5)
        self.assertAlmostEqual(metros_para_quilometros(0), 0)

    def test_quilometros_para_metros(self):
        self.assertAlmostEqual(quilometros_para_metros(1), 1000)
        self.assertAlmostEqual(quilometros_para_metros(5), 5000)
        self.assertAlmostEqual(quilometros_para_metros(0), 0)

    def test_metros_para_centimetros(self):
        self.assertAlmostEqual(metros_para_centimetros(1), 100)
        self.assertAlmostEqual(metros_para_centimetros(5), 500)
        self.assertAlmostEqual(metros_para_centimetros(0), 0)

    def test_quilometros_para_centimetros(self):
        self.assertAlmostEqual(quilometros_para_centimetros(1), 100000)
        self.assertAlmostEqual(quilometros_para_centimetros(5), 500000)
        self.assertAlmostEqual(quilometros_para_centimetros(0), 0)

 