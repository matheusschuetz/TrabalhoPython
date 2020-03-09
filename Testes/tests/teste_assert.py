from unittest import TestCase
from soma import soma, Pessoa


class TestAssert(TestCase):
    def test_soma(self):
        resultado = soma(2, 2)
        self.assertEqual(resultado, 4)

    def test_class_pessoa(self):
        #Arrange(Organizar)

        #Action(Ação)
        nova_pessoa = Pessoa('Ronaldinho', 'Gaucho')

        #Assertion(Afirmações)
        self.assertIsInstance(nova_pessoa, Pessoa)
        self.assertEqual(nova_pessoa.nome, 'Ronaldinho')
        self.assertEqual(nova_pessoa.sobrenome, 'Gaucho')