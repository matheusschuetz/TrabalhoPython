from unittest import TestCase
from Testes.soma import soma


class TestAssert(TestCase):
    def test_soma(self):
        resultado = soma(2, 2)
        self.assertEqual(resultado, 4)