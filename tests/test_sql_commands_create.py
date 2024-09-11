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
    """testa a função que gera o comando INTEGER do SQL"""
    
    integer_return = "id INTEGER PRIMARY KEY NOT NULL"
    assert integer("id", prop("pri_key", "n_null")) == integer_return
    

def test_integer_invalid_col_name():
    """testa adicionar um valor diferente de str em col_name"""
    
    error_col_name = re.escape(get_errors("TypeError", "col_name", 0, "str", "integer"))
    with pytest.raises(TypeError, match = error_col_name):
        integer(0, prop("n_null"))


def test_integer_invalid_args():
    """testa adiciona um valor diferente de str em *args"""
    
    error_args = re.escape(get_errors("TypeError", "*args", 0, "str", "integer"))
    with pytest.raises(TypeError, match = error_args):
        integer("id", 0)
    

def test_t_float():
    """testa a função que gera o comando FLOAT do SQL"""
    
    t_float_return = "price FLOAT NOT NULL"
    assert t_float("price", prop("n_null")) == t_float_return
    
    
def test_t_float_invalid_col_name():
    """testa adicionar um valor diferente de str em col_name"""
    
    error_col_name = re.escape(get_errors("TypeError", "col_name", 0, "str", "t_float"))
    with pytest.raises(TypeError, match = error_col_name):
        t_float(0, prop("n_null"))
        
        
def test_t_float_invalid_args():
    """testa adiciona um valor diferente de str em *args"""
    
    error_args = re.escape(get_errors("TypeError", "*args", 0, "str", "t_float"))
    with pytest.raises(TypeError, match = error_args):
        t_float("price", 0)
        
        
def test_decimal():
    """testa a função que gera o comando DECIMAL do SQL"""
        
    decimal_return = "pi DECIMAL(10, 9) NOT NULL"
    assert decimal("pi", 10, 9, prop("n_null")) == decimal_return
    
    
def test_decimal_invalid_col_name():
    """testa adicionar um valor diferente de str em col_name"""
    
    error_col_name = re.escape(get_errors("TypeError", "col_name", 0, "str", "decimal"))
    with pytest.raises(TypeError, match = error_col_name):
        decimal(0, 10, 9, prop("n_null"))
        
        
def test_decimal_invalid_preciosion():
    """testa adicionar um valor diferente de int em precision"""
    
    error_precision = re.escape(get_errors("TypeError", "precision", "a", "int", "decimal"))
    with pytest.raises(TypeError, match = error_precision):
        decimal("pi", "a", 9, prop("n_null"))
        
        
def test_decimal_invalid_scale():
    """testa adicionar um valor diferente de int em scale"""
    
    error_precision = re.escape(get_errors("TypeError", "scale", "a", "int", "decimal"))
    with pytest.raises(TypeError, match = error_precision):
        decimal("pi", 10, "a", prop("n_null"))
        
        
def test_decimal_invalid_args():
    """testa adiciona um valor diferente de str em *args"""
    
    error_args = re.escape(get_errors("TypeError", "*args", 0, "str", "decimal"))
    with pytest.raises(TypeError, match = error_args):
        decimal("pi", 10, 9, 0)
        

def test_double():
    """testa a função que gera o comando DOUBLE do SQL"""
    
    double_return = "weight DOUBLE NOT NULL"
    assert double("weight", prop("n_null")) == double_return
    
    
def test_double_invalid_col_name():
    """testa adicionar um valor diferente de str em col_name"""
    
    error_col_name = re.escape(get_errors("TypeError", "col_name", 0, "str", "double"))
    with pytest.raises(TypeError, match = error_col_name):
        double(0, prop("n_null"))
        
        
def test_double_invalid_args():
    """testa adiciona um valor diferente de str em *args"""
    
    error_args = re.escape(get_errors("TypeError", "*args", 0, "str", "double"))
    with pytest.raises(TypeError, match = error_args):
        double("weight", 0)


def test_char():
    """testa a função que gera o comando CHAR do SQL"""
    
    char_return = "address CHAR(10) NOT NULL"
    assert char("address", 10, prop("n_null")) == char_return
    

def test_char_invalid_col_name():
    """testa adicionar um valor diferente de str em col_name"""
    
    error_col_name = re.escape(get_errors("TypeError", "col_name", 0, "str", "char"))
    with pytest.raises(TypeError, match = error_col_name):
        char(0, 10, prop("n_null"))
        
def test_char_invalid_length():
    """testa adicionar um valor diferente de int em length"""
    
    error_length = re.escape(get_errors("TypeError", "length", "a", "int", "char"))
    with pytest.raises(TypeError, match = error_length):
        char("address", "a", prop("n_null"))
        

def test_char_invalid_args():
    """testa adicionar um valor diferente de str em *args"""
    
    error_args = re.escape(get_errors("TypeError", "*args", 0, "str", "char"))
    with pytest.raises(TypeError, match = error_args):
        char("address", 10, 0)
        

def test_varchar():
    """testa a função que gera o comando VARCHAR do SQL"""
    
    varchar_return = "username VARCHAR(10) UNIQUE NOT NULL"
    assert varchar("username", 10, prop("uni", "n_null")) == varchar_return
    

def test_varchar_invalid_col_name():
    """testa adicionar um valor diferente de str em col_name"""
    
    error_col_name = re.escape(get_errors("TypeError", "col_name", 0, "str", "varchar"))
    with pytest.raises(TypeError, match = error_col_name):
        varchar(0, 10, prop("uni", "n_null"))
        
        
def test_varchar_invalid_max_length():
    """testa adicionar um valor diferente de int em max_length"""
    
    error_length = re.escape(get_errors("TypeError", "max_length", "a", "int", "varchar"))
    with pytest.raises(TypeError, match = error_length):
        varchar("username", "a", prop("uni", "n_null"))
        

def test_varchar_invalid_args():
    """testa adicionar um valor diferente de str em *args"""
    
    error_args = re.escape(get_errors("TypeError", "*args", 0, "str", "varchar"))
    with pytest.raises(TypeError, match = error_args):
        varchar("username", 10, 0)
        

def test_text():
    """testa a função que gera o comando TEXT do SQL"""
    
    text_return = "description TEXT NOT NULL"
    assert text("description", prop("n_null")) == text_return
    

def test_text_invalid_col_name():
    """testa adicionar um valor diferente de str em col_name"""
    
    error_col_name = re.escape(get_errors("TypeError", "col_name", 0, "str", "text"))
    with pytest.raises(TypeError, match = error_col_name):
        text(0, prop("n_null"))
        

def test_text_invalid_args():
    """testa adicionar um valor diferente de str em *args"""
    
    error_args = re.escape(get_errors("TypeError", "*args", 0, "str", "text"))
    with pytest.raises(TypeError, match = error_args):
        text("description", 0)
        
        
def test_boolean():
    """testa a função que gera o comando BOOLEAN do SQL"""
    
    boolean_return = "active BOOLEAN NOT NULL"
    assert boolean("active", prop("n_null")) == boolean_return
    

def test_boolean_invalid_col_name():
    """testa adicionar um valor diferente de str em col_name"""
    
    error_col_name = re.escape(get_errors("TypeError", "col_name", 0, "str", "boolean"))
    with pytest.raises(TypeError, match = error_col_name):
        boolean(0, prop("n_null"))
        

def test_boolean_invalid_args():
    """testa adicionar um valor diferente de str em *args"""
    
    error_args = re.escape(get_errors("TypeError", "*args", 0, "str", "boolean"))
    with pytest.raises(TypeError, match = error_args):
        boolean("active", 0)
        
        
def test_date():
    """testa a função que gera o comando DATE do SQL"""
    
    date_return = "creation DATE NOT NULL"
    assert date("creation", prop("n_null")) == date_return
    

def test_date_invalid_col_name():
    """testa adicionar um valor diferente de str em col_name"""
    
    error_col_name = re.escape(get_errors("TypeError", "col_name", 0, "str", "date"))
    with pytest.raises(TypeError, match = error_col_name):
        date(0, prop("n_null"))
        

def test_date_invalid_args():
    """testa adicionar um valor diferente de str em *args"""
    
    error_args = re.escape(get_errors("TypeError", "*args", 0, "str", "date"))
    with pytest.raises(TypeError, match = error_args):
        date("creation", 0)
        

def test_datetime():
    """testa função que gera o comando DATETIME do SQL"""
    
    datetime_return = "creation DATETIME NOT NULL"
    assert datetime("creation", prop("n_null")) == datetime_return
    

def test_datetime_invalid_col_name():
    """testa adicionar um valor diferente de str em col_name"""
    
    error_col_name = re.escape(get_errors("TypeError", "col_name", 0, "str", "datetime"))
    with pytest.raises(TypeError, match = error_col_name):
        datetime(0, prop("n_null"))
        

def test_datetime_invalid_args():
    """testa adicionar um valor diferente de str em *args"""
    
    error_args = re.escape(get_errors("TypeError", "*args", 0, "str", "datetime"))
    with pytest.raises(TypeError, match = error_args):
        datetime("creation", 0)
        
        
def test_timestamp():
    """testa função que gera o comando TIMESTAMP do SQL"""
    
    timestamp_return = "creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
    assert timestamp("creation", prop(default="current")) == timestamp_return
    

def test_timestamp_invalid_col_name():
    """testa adicionar um valor diferente de str em col_name"""
    
    error_col_name = re.escape(get_errors("TypeError", "col_name", 0, "str", "timestamp"))
    with pytest.raises(TypeError, match = error_col_name):
        timestamp(0, prop(default="current"))
        

def test_timestamp_invalid_args():
    """testa adicionar um valor diferente de str em *args"""
    
    error_args = re.escape(get_errors("TypeError", "*args", 0, "str", "timestamp"))
    with pytest.raises(TypeError, match = error_args):
        timestamp("creation", 0)
        

if __name__ == "__main__":
    pytest.main(["-vv", "test_sql_commands_create.py"])
    