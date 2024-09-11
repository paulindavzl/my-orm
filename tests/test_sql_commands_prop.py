import pytest
import re
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
    

def test_foreign_key():
    """testa a função que gera o comando FOREIGN KEY do SQL"""
    
    foreign_key_return = "FOREIGN KEY (id) REFERENCES people(uid) ON UPDATE CASCADE ON DELETE SET NULL"
    assert foreign_key("id", "people(uid)", on_up("cascade"), on_del("set null")) == foreign_key_return
    

def test_foreign_key_invalid_referrer():
    """testa adicionar um valor diferente de str em referrer"""
    
    error_referrer = re.escape(get_errors("TypeError", "referrer", 0, "str", "foreign_key"))
    with pytest.raises(TypeError, match = error_referrer):
        foreign_key(0, "people(uid)", on_up("cascade"), on_del("set null"))
        
        
def test_foreign_key_invalid_referenced_type():
    """testa adicionar um valor diferente de str em referenced"""
    
    error_referenced = re.escape(get_errors("TypeError", "referenced", 0, "str", "foreign_key"))
    with pytest.raises(TypeError, match = error_referenced):
        foreign_key("id", 0, on_up("cascade"), on_del("set null"))
        

def test_foreign_key_invalid_referenced_value():
    """testa adicionar um valor diferente do esperado em referenced"""
    
    error_referenced = re.escape(get_errors("ValueError", "referenced", "uid", "table(column)", "foreign_key"))
    with pytest.raises(ValueError, match = error_referenced):
        foreign_key("id", "uid", on_up("cascade"), on_del("set null"))
        

def test_on_up():
    """testa a função que gera o comando ON UPDATE do SQL"""
    
    on_up_return = "ON UPDATE CASCADE"
    assert on_up("cascade") == on_up_return
    

def test_on_up_invalid_command():
    """testa adicionar um valor diferente de str em command"""
    
    error_command = re.escape(get_errors("TypeError", "command", 0, "str", "on_up"))
    with pytest.raises(TypeError, match = error_command):
        on_up(0)
        

def test_on_del():
    """testa a função que gera o comando ON DELETE do SQL"""
    
    on_del_return = "ON DELETE SET NULL"
    assert on_del("set null") == on_del_return
    

def test_on_del_invalid_command():
    """testa adicionar um valor diferente de str em command"""
    
    error_command = re.escape(get_errors("TypeError", "command", 0, "str", "on_del"))
    with pytest.raises(TypeError, match = error_command):
        on_del(0)
        

def test_prop_default():
    """testa a função que gera a propriedade DEFAULT do SQL"""
    
    prop_return = "DEFAULT 0"
    assert prop(default=0) == prop_return


def test_prop_default_current():
    """testa a função que gera a propriedade DEFAULT CURRENT_TIMESTAMP do SQL"""
    
    prop_return = "DEFAULT CURRENT_TIMESTAMP"
    assert prop(default="current") == prop_return
    

def test_prop_uni():
    """testa a função que gera a propriedade UNIQUE do SQL"""
    
    prop_return = "UNIQUE"
    assert prop("uni") == prop_return
    

def test_prop_n_null():
    """testa a função que gera a propriedade NOT NULL do SQL"""
    
    prop_return = "NOT NULL"
    assert prop("n_null") == prop_return
    

def test_prop_pri_key():
    """testa a função que gera a propriedade PRIMARY KEY do SQL"""
    
    prop_return = "PRIMARY KEY"
    assert prop("pri_key") == prop_return
    

def test_prop_auto():
    """testa a função que gera a propriedade AUTO_INCREMENT do SQL"""
    
    prop_return = "AUTO_INCREMENT"
    assert prop("auto") == prop_return


if __name__ == "__main__":
    pytest.main(["-vv", "test_sql_commands_prop.py"])