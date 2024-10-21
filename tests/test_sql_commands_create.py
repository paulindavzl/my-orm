import pytest
import re
from my_orm import *

def get_errors(error: str, *args):
    errors = {
        "TypeError": f"({args[0]}) {args[1]} expected a {args[2]} value, but received a {type(args[3]).__name__} ({args[3]}). {doc_link()}"
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
    error_precision = re.escape(get_errors("TypeError", "decimal()", "precision", "int", "a"))
    with pytest.raises(TypeError, match = error_precision):
        decimal("a", 9), prop("n_null")
        
        
def test_decimal_invalid_scale():
    error_precision = re.escape(get_errors("TypeError", "decimal()", "scale", "int", "a"))
    with pytest.raises(TypeError, match = error_precision):
        decimal(10, "a"), prop("n_null")
        
        
def test_double():
    double_return = "DOUBLE NOT NULL"
    assert double(), prop("n_null") == double_return
    

def test_char():
    char_return = "CHAR(10) NOT NULL"
    assert char(10), prop("n_null") == char_return
    
    
def test_char_invalid_length():
    error_length = re.escape(get_errors("TypeError", "char()", "length", "int", "a"))
    with pytest.raises(TypeError, match = error_length):
        char("a"), prop("n_null")
        

def test_varchar():
    varchar_return = "VARCHAR(10) UNIQUE NOT NULL"
    assert varchar(10), prop("uni", "n_null") == varchar_return
    

def test_varchar_invalid_max_length():
    error_length = re.escape(get_errors("TypeError", "varchar()", "max_length", "int", "a"))
    with pytest.raises(TypeError, match = error_length):
        varchar("a"), prop("uni", "n_null")
        

def test_text():
    text_return = "TEXT NOT NULL"
    assert text(), prop("n_null") == text_return
    

def test_boolean():
    boolean_return = "BOOLEAN NOT NULL"
    assert boolean(), prop("n_null") == boolean_return
    

def test_date():
    date_return = "DATE NOT NULL"
    assert date(), prop("n_null") == date_return
    

def test_datetime():
    datetime_return = "DATETIME NOT NULL"
    assert datetime(), prop("n_null") == datetime_return
    

def test_timestamp():
    timestamp_return = "TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
    assert timestamp(), prop(default="current") == timestamp_return
    

if __name__ == "__main__":
    pytest.main(["-vv", "test_sql_commands_create.py"])
    