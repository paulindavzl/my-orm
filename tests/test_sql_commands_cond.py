import pytest
import re
from SQL.sql_commands_cond import *


def get_error(err_name: str, *args):
    """organiza e retorna a mensagem de uma exceção personalizada
        Args:
            err_name (str): nome do erro
            *args: informações para personalizar o erro"""
    
    errors = {
        "type_error": f"({args[3]}()) {args[0]} expected a value like {args[2]}, but received a {type(args[1]).__name__} ({args[1]})"
    }
    
    return errors.get(err_name)


def test_adj_():
    """testa a função que remove marcações dos comandos"""
    
    expected_return = "WHERE column1 BETWEEN par1 AND par2 AND (value1 = value2) OR column2 IN ('tag1', 'tag2', 'tag3')"
    
    assert adj_(whe_("column1", betw_("par1", "par2"), and_("value1", "= value2"), or_("column2", in_("tag1", "tag2", "tag3")))) == expected_return
    

def test_whe_():
    """testa a função que gera o comando WHERE do SQL"""
    
    expected_return = "**whe**WHERE column = value"
    
    assert whe_("column", "= value") == expected_return
    

def test_whe_invalid_col_name():
    """testa usar a função whe_() com um nome diferente de string"""
    
    expected_return = re.escape(get_error("type_error", "col_name", 0, "str", "whe_"))
    
    with pytest.raises(TypeError, match=expected_return):
        whe_(0, "= value")
        
        
def test_betw_():
    """testa a função que gera a condição BETWEEN do SQL"""
    
    expected_return = "**betw**BETWEEN value1 AND value2"
    
    assert betw_("value1", "value2") == expected_return


def test_and_():
    """testa a função que gera a condição AND do SQL"""
    
    expected_return = "**and**AND (column = value)"
    
    assert and_("column", "= value") == expected_return
    

def test_and_with_in_():
    """testa a função que gera as condição AND com IN do SQL"""
    
    expected_return = "**and**AND column **in**IN ('tag1', 'tag2')"
    
    assert and_("column", in_("tag1", "tag2")) == expected_return
    

def test_and_invalid_col_name():
    """testa usar a função whe_() com um nome diferente de string"""
    
    expected_return = re.escape(get_error("type_error", "col_name", 0, "str", "and_"))
    
    with pytest.raises(TypeError, match=expected_return):
        and_(0, "= value")
    

def test_or_():
    """testa a função que gera a condição OR do SQL"""
    
    expected_return = "**or**OR (column = value)"
    
    assert or_("column", "= value") == expected_return
    

def test_or_with_in_():
    """testa a função que gera as condição OR com IN do SQL"""
    
    expected_return = "**or**OR column **in**IN ('tag1', 'tag2')"
    
    assert or_("column", in_("tag1", "tag2")) == expected_return
    
    
def test_or_invalid_col_name():
    """testa usar a função whe_() com um nome diferente de string"""
    
    expected_return = re.escape(get_error("type_error", "col_name", 0, "str", "or_"))
    
    with pytest.raises(TypeError, match=expected_return):
        or_(0, "= value")
    

def test_in_():
    """testa a função que gera a condicão IN do SQL"""
    
    expected_return = "**in**IN ('tag1', 'tag2')"
    
    assert in_("tag1", "tag2") == expected_return
    

if __name__ == "__main__":
    pytest.main(["-vv", "test_sql_commands_cond.py"])