import pytest
import re
from my_orm import *

@pytest.fixture
def orm():
    """cria uma instância da classe MyORM e retorna-a"""
    
    orm_instance = MyORM(execute=False)
    return orm_instance

def get_errors(error: str, *args: str):
    
    errors = {
        "type_error_create": f"(MyORM.make()) {args[0]} expected an {args[2]}, but received a {type(args[1]).__name__} ({args[1]}). See the documentation at https://github.com/paulindavzl/my-orm.",
        "value_error_create": f"(MyORM.make()) The tuple {args[0]} expected {args[2]}. Currently it has {len(str(args[1]))} ({args[1]}).. See the documentation at https://github.com/paulindavzl/my-orm.",
        "type_error_insert": f"{args[0]} expected a {args[2]} value but received an {type(args[1]).__name__} ({args[1]}) value. See the documentation at https://github.com/paulindavzl/my-orm",
        "type_error_insert_args": f"All arg values ​​must be strings. {args[0]} is an {type(args[0]).__name__}. See the documentation at https://github.com/paulindavzl/my-orm",
        "value_error_insert": f"The number of values ​({args[0]}) does not mean the number of columns ({args[1]})!",
        "type_error_select": f"(MyORM.get()) {args[0]} expected a {args[2]} value but received an {type(args[1]).__name__} ({args[1]}) value. See the documentation at https://github.com/paulindavzl/my-orm",
        "type_error_update": f"(MyORM.edit()) {args[0]} expected a {args[2]} value but received an {type(args[1]).__name__} ({args[1]}) value. See the documentation at https://github.com/paulindavzl/my-orm",
        "type_error_delete": f"(MyORM.remove()) {args[0]} expected a {args[2]} value but received an {type(args[1]).__name__} ({args[1]}) value. See the documentation at https://github.com/paulindavzl/my-orm"
    }
    
    return errors.get(error)
    

def test_create_table_name_not_str(orm):
    expected_return = re.escape(get_errors("type_error_create", "table_name", 0, "str"))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.make(0, id=(integer(), prop("n_null")))
        
        
def test_create_f_key_not_tuple(orm):
    expected_return = re.escape(get_errors("type_error_create", "f_key", 0, "tuple"))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.make("table", f_key=0)
        
        
def test_insert_table_name_not_str(orm):
    expected_return = re.escape(get_errors("type_error_insert", "table_name", 0, "str"))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.add(0, value1="column1")
        
        
def test_insert_values_not_list(orm):
    expected_return = re.escape(get_errors("type_error_insert", "values", "value1", "list"))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.add("table", values="value1", columns=["column1"])
        
        
def test_insert_columns_not_list(orm):
    expected_return = re.escape(get_errors("type_error_insert", "columns", "column1", "list"))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.add("table", values=["value1"], columns="column1")
        
        
def test_insert_values_different_column(orm):
    expected_return = re.escape(get_errors("value_error_insert", 1, 2, 0))
    
    with pytest.raises(ValueError, match=expected_return):
        orm.add("table", values=["value1", "value2"], columns=["column1"])
    
    
def test_select_invalid_table_name(orm):
    expected_return = re.escape(get_errors("type_error_select","table_name" , 0, "str"))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.get(0, "all")
        

def test_select_invalid_columns_value(orm):
    expected_return = re.escape(get_errors("type_error_select","columns" , 0, "list"))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.get("table", 0)
        

def test_select_invalid_args(orm):
    expected_return = re.escape(get_errors("type_error_select", "*args", 0, "str"))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.get("table", "all", 0)
        

def test_update_invalid_table_name(orm):
    expected_return = re.escape(get_errors("type_error_update", "table_name", 0, "str"))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.edit(0, column="value")
        

def test_update_invalid_args(orm):
    expected_return = re.escape(get_errors("type_error_update", "*args", 0, "str"))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.edit("table", 0, column="value")
        
        
def test_update_invalid_all(orm):
    expected_return = re.escape(get_errors("type_error_update", "all", 0, "bool"))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.edit("table", all=0, column="value")
        
        
def test_update_all_register_error(orm):
    expected_return = "For security, the WHERE condition is mandatory. See the documentation at https://github.com/paulindavzl/my-orm"
    
    with pytest.raises(ValueError, match=expected_return):
        orm.edit("table", column="value")
        

def test_delete_invalid_table_name(orm):
    expected_return = re.escape(get_errors("type_error_delete", "table_name", 0, "str"))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.remove(0)
        

def test_delete_invalid_args(orm):
    expected_return = re.escape(get_errors("type_error_delete", "*args", 0, "str"))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.remove("table", 0)
        
        
def test_delete_invalid_all(orm):
    expected_return = re.escape(get_errors("type_error_delete", "all", 0, "bool"))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.remove("table", all=0)
        
        
def test_delete_all_register_error(orm):
    expected_return = "For security, the WHERE condition is mandatory. See the documentation at https://github.com/paulindavzl/my-orm"
    
    with pytest.raises(ValueError, match=expected_return):
        orm.remove("table")
    
    
if __name__ == "__main__":
    pytest.main(["-vv", "test_my_orm_exceptions.py"])