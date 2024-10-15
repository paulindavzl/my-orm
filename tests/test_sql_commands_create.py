import pytest
import re
from SQL.sql_commands_create import *
from SQL.sql_commands_prop import *

def get_errors(error: str, *args) -> str:
    """retorna as exceções
        Args:
            type (str): tipo de erro (ValueError, TypeError...)
            args (str): informações extras para o erro"""
    
    errors = {
        "TypeError": f"Unexpected '{type(args[1]).__name__}' ({args[1]}) in {args[3]}(). {args[0]} expects a value of type '{args[2]}'. See the documentation at https://github.com/paulindavzl/my-orm.",
        "ValueError": f"The value passed in '{args[0]}' ({args[1]}) is incorrect! {args[3]}() expects the value in '{args[2]}' format for the variable '{args[0]}'. See the documentation at https://github.com/paulindavzl/my-orm"
    }
            
    return errors.get(error)
            

def test_integer():
    integer_return = "INTEGER PRIMARY KEY NOT NULL"
    assert integer(), prop("pri_key", "n_null") == integer_return
    

def test_t_float():
    t_float_return = "FLOAT NOT NULL"
    assert t_float(), prop("n_null") == t_float_return
    
   
def test_decimal():
    decimal_return = "DECIMAL(10, 9) NOT NULL"
    assert decimal(10, 9), prop("n_null") == decimal_return
    
    
def test_decimal_invalid_preciosion():
    error_precision = re.escape(get_errors("TypeError", "precision", "a", "int", "decimal"))
    with pytest.raises(TypeError, match = error_precision):
        decimal("a", 9), prop("n_null")
        
        
def test_decimal_invalid_scale():
    error_precision = re.escape(get_errors("TypeError", "scale", "a", "int", "decimal"))
    with pytest.raises(TypeError, match = error_precision):
        decimal(10, "a"), prop("n_null")
        
        
def test_double():
    double_return = "DOUBLE NOT NULL"
    assert double(), prop("n_null") == double_return
    

def test_char():
    char_return = "CHAR(10) NOT NULL"
    assert char(10), prop("n_null") == char_return
    
    
def test_char_invalid_length():
    error_length = re.escape(get_errors("TypeError", "length", "a", "int", "char"))
    with pytest.raises(TypeError, match = error_length):
        char("a"), prop("n_null")
        

def test_varchar():
    varchar_return = "VARCHAR(10) UNIQUE NOT NULL"
    assert varchar(10), prop("uni", "n_null") == varchar_return
    

def test_varchar_invalid_max_length():
    error_length = re.escape(get_errors("TypeError", "max_length", "a", "int", "varchar"))
    with pytest.raises(TypeError, match = error_length):
        varchar("a"), prop("uni", "n_null")
        

def test_text():
    text_return = "TEXT NOT NULL"
    assert text(), prop("n_null") == text_return
    

def test_boolean():
    boolean_return = "BOOLEAN NOT NULL"
    assert boolean(), prop("n_null") == boolean_return
    

def test_date():
    """testa a função que gera o comando DATE do SQL"""
    
    date_return = "DATE NOT NULL"
    assert date(), prop("n_null") == date_return
    

def test_datetime():
    """testa função que gera o comando DATETIME do SQL"""
    
    datetime_return = "DATETIME NOT NULL"
    assert datetime(), prop("n_null") == datetime_return
    

def test_timestamp():
    """testa função que gera o comando TIMESTAMP do SQL"""
    
    timestamp_return = "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
    assert timestamp(), prop(default="current") == timestamp_return
    

if __name__ == "__main__":
    pytest.main(["-vv", "test_sql_commands_create.py"])
    