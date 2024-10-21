import pytest
import re
from my_orm import *

def get_errors(error: str, *args):
    
    errors = {
        "TypeError": f"({args[0]}) {args[1]} expected a {args[2]} value, but received a {type(args[3]).__name__} ({args[3]}). {doc_link}",
        "ValueError": f"(for_key()) The value that referenced ({args[0]}) receives is not valid! A value in the 'table(column)' format is required. {doc_link}"
    }
            
    return errors.get(error)
    

def test_foreign_key():
    foreign_key_return = "**fkey** FOREIGN KEY (id) REFERENCES people(uid) ON UPDATE CASCADE ON DELETE SET NULL"
    assert for_key("id", "people(uid)", on_up("cascade"), on_del("set null")) == foreign_key_return
    

def test_foreign_key_invalid_referrer():
    error_referrer = re.escape(get_errors("TypeError", "for_key()", "referrer", "str", 0))
    with pytest.raises(TypeError, match = error_referrer):
        for_key(0, "people(uid)", on_up("cascade"), on_del("set null"))
        
        
def test_foreign_key_invalid_referenced_type():
    error_referenced = re.escape(get_errors("TypeError", "for_key()", "referenced", "str", 0))
    with pytest.raises(TypeError, match = error_referenced):
        for_key("id", 0, on_up("cascade"), on_del("set null"))
        

def test_foreign_key_invalid_referenced_value():
    error_referenced = re.escape(get_errors("ValueError", "uid", 0, 0, 0))
    with pytest.raises(ValueError, match = error_referenced):
        for_key("id", "uid", on_up("cascade"), on_del("set null"))
        

def test_on_up():
    on_up_return = "ON UPDATE CASCADE"
    assert on_up("cascade") == on_up_return
    

def test_on_up_invalid_command():
    error_command = re.escape(get_errors("TypeError", "on_up()", "command", "str", 0))
    with pytest.raises(TypeError, match = error_command):
        on_up(0)
        

def test_on_del():
    on_del_return = "ON DELETE SET NULL"
    assert on_del("set null") == on_del_return
    

def test_on_del_invalid_command():
    error_command = re.escape(get_errors("TypeError", "on_del()", "command", "str", 0))
    with pytest.raises(TypeError, match = error_command):
        on_del(0)
        

def test_prop_default():
    prop_return = "**prop** DEFAULT 0"
    assert prop(default=0) == prop_return


def test_prop_default_current():
    prop_return = "**prop** DEFAULT CURRENT_TIMESTAMP"
    assert prop(default="current") == prop_return
    

def test_prop_uni():
    prop_return = "**prop** UNIQUE"
    assert prop("uni") == prop_return
    

def test_prop_n_null():
    prop_return = "**prop** NOT NULL"
    assert prop("n_null") == prop_return
    

def test_prop_pri_key():
    prop_return = "**prop** PRIMARY KEY"
    assert prop("pri_key") == prop_return
    

def test_prop_auto():
    prop_return = "**prop** AUTO_INCREMENT"
    assert prop("auto") == prop_return


if __name__ == "__main__":
    pytest.main(["-vv", "test_sql_commands_prop.py"])