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
        "type_error": f"{args[0]} {args[1]} expected a {args[2]} value, but received a {type(args[3]).__name__} ({args[3]}). {doc_link()}",
        "value_error_add": f"{args[0]} The number of values ​​in columns ({args[1]}) and values ({args[2]}) ​​is different! {doc_link()}"
    }
    
    return errors.get(error)
    

def test_create_table_name_not_str(orm):
    expected_return = re.escape(get_errors("type_error", "(MyORM.make())", "table_name", "str", 0))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.make(0, id=(integer(), prop("n_null")))
        
        
def test_create_f_key_not_tuple(orm):
    expected_return = re.escape(get_errors("type_error", "(MyORM.make())","f_key", "str", 0))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.make("table", f_key=0)
        
        
def test_insert_table_name_not_str(orm):
    expected_return = re.escape(get_errors("type_error", "(MyORM.add())","table_name",  "str", 0))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.add(0, value1="column1")
        
        
def test_insert_values_not_list(orm):
    expected_return = re.escape(get_errors("type_error", "(MyORM.add())", "values", "list", "value1"))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.add("table", values="value1", columns=["column1"])
        
        
def test_insert_columns_not_list(orm):
    expected_return = re.escape(get_errors("type_error", "(MyORM.add())", "columns", "list", "column1"))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.add("table", values=["value1"], columns="column1")
        
        
def test_insert_values_different_column(orm):
    expected_return = re.escape(get_errors("value_error_add", "(MyORM.add())", 1, 2, 0, 0))
    
    with pytest.raises(ValueError, match=expected_return):
        orm.add("table", values=["value1", "value2"], columns=["column1"])
    
    
def test_select_invalid_table_name(orm):
    expected_return = re.escape(get_errors("type_error", "(MyORM.get())", "table_name" , "str", 0))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.get(0, "all")
        

def test_select_invalid_columns_value(orm):
    expected_return = re.escape(get_errors("type_error", "(MyORM.get())","columns", "list", 0))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.get("table", 0)
        

def test_select_invalid_args(orm):
    expected_return = re.escape(get_errors("type_error", "(MyORM.get())", "*args", "str", 0))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.get("table", "all", 0)
        

def test_update_invalid_table_name(orm):
    expected_return = re.escape(get_errors("type_error", "(MyORM.edit())", "table_name", "str", 0))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.edit(0, column="value")
        

def test_update_invalid_args(orm):
    expected_return = re.escape(get_errors("type_error", "(MyORM.edit())", "*args", "str", 0))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.edit("table", 0, column="value")
        
        
def test_update_invalid_all(orm):
    expected_return = re.escape(get_errors("type_error", "(MyORM.edit())", "all", "bool", 0))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.edit("table", all=0, column="value")
        
        
def test_update_all_register_error(orm):
    expected_return = "For security, the WHERE condition is mandatory. See the documentation at https://github.com/paulindavzl/my-orm"
    
    with pytest.raises(ValueError, match=expected_return):
        orm.edit("table", column="value")
        

def test_delete_invalid_table_name(orm):
    expected_return = re.escape(get_errors("type_error", "(MyORM.remove())", "table_name", "str", 0))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.remove(0)
        

def test_delete_invalid_args(orm):
    expected_return = re.escape(get_errors("type_error", "(MyORM.remove())", "*args", "str", 0))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.remove("table", 0)
        
        
def test_delete_invalid_all(orm):
    expected_return = re.escape(get_errors("type_error", "(MyORM.remove())", "all", "bool", 0))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.remove("table", all=0)
        
        
def test_delete_all_register_error(orm):
    expected_return = "For security, the WHERE condition is mandatory. See the documentation at https://github.com/paulindavzl/my-orm"
    
    with pytest.raises(ValueError, match=expected_return):
        orm.remove("table")
    
    
if __name__ == "__main__":
    pytest.main(["-vv", "test_my_orm_exceptions.py"])