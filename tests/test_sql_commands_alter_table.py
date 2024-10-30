import pytest
import re
from my_orm import *

def get_error(err_name: str, *args):
    errors = {
        "type_error": f"({args[0]}()) {args[1]} expected a {args[2]} value, but received a {type(args[3]).__name__} ({args[3]}). {doc_link()}"
    }
    
    return errors.get(err_name)
    
    
def test_add():
    expected_return = "**alter_add** ADD column **int** INTEGER;"
    
    assert add("column", integer()) == expected_return
    

def test_add_invalid_column_name():
    expected_return = re.escape(get_error("type_error", "add", "column_name", "str", 0))
    
    with pytest.raises(TypeError, match=expected_return):
        add(0, integer())
        

def test_add_invalid_props():
    expected_return = re.escape(get_error("type_error", "add", "props", "str/tuple/list", 0))
    
    with pytest.raises(TypeError, match=expected_return):
        add("column", 0)
        
        
def test_drop():
    expected_return = "**drop** DROP COLUMN column;"
    
    assert drop("column") == expected_return
    

def test_drop_invalid_column_name():
    expected_return = re.escape(get_error("type_error", "drop", "column_name", "str", 0))
    
    with pytest.raises(TypeError, match=expected_return):
        drop(0)
        
        
def test_edit():
    expected_return = "**alt_col** ALTER COLUMN column **int** INTEGER;"
    
    assert edit("column", integer()) == expected_return
        
        
def test_edit_invalid_column_name():
    expected_return = re.escape(get_error("type_error", "edit", "column_name", "str", 0))
    
    with pytest.raises(TypeError, match=expected_return):
        edit(0, integer())
        
        
def test_edit_invalid_props():
    expected_return = re.escape(get_error("type_error", "edit", "props", "str/tuple/list", 0))
    
    with pytest.raises(TypeError, match=expected_return):
        edit("column", 0)
        

def test_ren_column():
    expected_return = "**ren_col** RENAME COLUMN old_column new_column;"
    
    assert ren_column("old_column", "new_column") == expected_return
    

def test_ren_column_invalid_old_name():
    expected_return = re.escape(get_error("type_error", "ren_column", "old_name", "str", 0))
    
    with pytest.raises(TypeError, match=expected_return):
        ren_column(0, "new_column")
        
        
def test_ren_column_invalid_new_name():
    expected_return = re.escape(get_error("type_error", "ren_column", "new_name", "str", 0))
    
    with pytest.raises(TypeError, match=expected_return):
        ren_column("old_column", 0)
        

def test_rename():
    expected_return = "**rename** RENAME TO table;"
    
    assert rename("table") == expected_return
    
    
def test_rename_invalid_new_name():
    expected_return = re.escape(get_error("type_error", "rename", "new_name", "str", 0))
    
    with pytest.raises(TypeError, match=expected_return):
        rename(0)
    

if __name__ == "__main__":
    pytest.main(["-vv", "test_sql_commands_alter_table.py"])