import Practica;
import pytest;
from unittest import mock

modulo = Practica

def test_division_1():  
    opcion = ''
    valor = ''
    with mock.patch('builtins.input', side_effect = [opcion, valor]:
        assert modulo.convertir() == -9.444444444444445
                    
