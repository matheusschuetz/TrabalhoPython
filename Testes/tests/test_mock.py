from unittest import TestCase, mock
from unittest.mock import patch, call

from mock.mock import VendinhaDoZe


class TestMock(TestCase):
    @patch('mock.mock.calculo_valor_total_da_compra')
    @patch('mock.mock.calculo_valor_total_refrigerantes')
    @patch('mock.mock.calculo_valor_total_salgados')
    @patch('mock.mock.print')
    def test_imprime_pedido(self, mock_print, mock_total_salgados, mock_total_refrigerantes, mock_total_compra):
        # Arrange(organizar)
        nova_vendinha_do_ze = VendinhaDoZe()
        mock_print.side_effects = ['', '', '', '']
        mock_total_refrigerantes.return_value = 100
        mock_total_salgados.return_value = 200
        mock_total_compra.return_value = 300

        #Action (ação)
        retorno = nova_vendinha_do_ze.imprime_pedido()

        #assertion(Afirmações)
        self.assertIsNone(retorno)
        mock_print.assert_has_calls([
            call('Seu pedido é: '),
            call('0 unidades de  no valor de 0.0'),
            call('0 unidades de  no valor de 0.0'),
            call('O valor total da compra é de R$ 0.0')
        ])