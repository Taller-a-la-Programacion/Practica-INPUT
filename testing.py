import Practica;
import pytest;
from unittest import mock
# from unittest.mock import patch

modulo = Practica

def test_division_1():  
    opcion = '2'
    valor = '15'
    with mock.patch('builtins.input', side_effect = [opcion, valor]):
        assert modulo.convertir() == -9.444444444444445
                    
