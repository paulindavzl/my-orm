import pytest
import re
from SQL.sql_commands_cond import *


def get_error(err_name: str, *args):
    errors = {
        "type_error": f"({args[3]}()) {args[0]} expected a value like {args[2]}, but received a {type(args[1]).__name__} ({args[1]})"
    }
    
    return errors.get(err_name)
    

def test_whe_():
    expected_return = "**whe** WHERE column = value"
    
    assert whe_("column = value") == expected_return
    
    
def test_whe_with_in():
    expected_return = "**whe** WHERE column **in** IN (tag1, tag2)"
    
    assert whe_("column", ["tag1", "tag2"]) == expected_return
    

def test_whe_invalid_condition():
    expected_return = re.escape(get_error("type_error", "condition", 0, "str", "whe_"))
    
    with pytest.raises(TypeError, match=expected_return):
        whe_(0)
        

def test_whe_invalid_in():
    expected_return = re.escape(get_error("type_error", "cond_in", 0, "list", "whe_"))
        
    with pytest.raises(TypeError, match=expected_return):
        whe_("condition", 0)
    
        
def test_betw_():
    expected_return = "**betw** BETWEEN value1 AND value2"
    
    assert betw_("value1", "value2") == expected_return


def test_and_():
    expected_return = "**and** AND column = value"
    
    assert and_("column = value") == expected_return
    

def test_and_with_in_():
    expected_return = "**and** AND (column **in** IN (tag1, tag2))"
    
    assert and_("column", ["tag1", "tag2"]) == expected_return
    

def test_and_invalid_condition():
    expected_return = re.escape(get_error("type_error", "condition", 0, "str", "and_"))
    
    with pytest.raises(TypeError, match=expected_return):
        and_(0)
        

def test_and_invalid_in():
    expected_return = re.escape(get_error("type_error", "cond_in", 0, "list", "and_"))
        
    with pytest.raises(TypeError, match=expected_return):
        and_("condition", 0)
    

def test_or_():
    expected_return = "**or** OR column = value"
    
    assert or_("column = value") == expected_return
    

def test_or_with_in_():
    expected_return = "**or** OR (column **in** IN (tag1, tag2))"
    
    assert or_("column", ["tag1", "tag2"]) == expected_return
    
    
def test_or_invalid_condition():
    expected_return = re.escape(get_error("type_error", "condition", 0, "str", "or_"))
    
    with pytest.raises(TypeError, match=expected_return):
        or_(0)
        
        
def test_or_invalid_in():
    expected_return = re.escape(get_error("type_error", "cond_in", 0, "list", "or_"))
        
    with pytest.raises(TypeError, match=expected_return):
        or_("condition", 0)
    

def test_in_():
    expected_return = "**in** IN (tag1, tag2)"
    
    assert in_(["tag1", "tag2"]) == expected_return
    

if __name__ == "__main__":
    pytest.main(["-vv", "test_sql_commands_cond.py"])