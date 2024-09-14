import pytest
import re
from my_orm import *

@pytest.fixture
def orm():
    """cria uma instância da classe MyORM e retorna-a"""
    
    orm_instance = MyORM(execute=False)
    return orm_instance

def get_errors(error: str, *args: str):
    """gerencia os erros deste teste
        Args:
            error (str): nome do erro
            *args (str): parâmetros contidos no erro"""
    
    errors = {
        "type_error_create": f"{args[0]} expected an {args[2]}, but received a {type(args[1]).__name__} ({args[1]}). See the documentation at https://github.com/paulindavzl/my-orm.",
        "type_error_insert": f"{args[0]} expected a {args[2]} value but received an {type(args[1]).__name__} ({args[1]}) value. See the documentation at https://github.com/paulindavzl/my-orm",
        "type_error_insert_args": f"All arg values ​​must be strings. {args[0]} is an {type(args[0]).__name__}. See the documentation at https://github.com/paulindavzl/my-orm",
        "value_error_insert": f"The number of values ​({args[0]}) does not mean the number of columns ({args[1]})!"
    }
    
    return errors.get(error)
    

def test_create_table_name_not_str(orm):
    """testa criar uma tabela com um nome diferente de string"""
    
    expected_return = re.escape(get_errors("type_error_create", "table_name", 0, "str"))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.create(0, integer("id", prop("n_null")))
        
        
def test_create_args_not_str(orm):
    """testa criar uma tabela com valores diferente de string"""
    
    expected_return = re.escape(get_errors("type_error_create", "*args", 0, "str"))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.create("table", 0)
        
        
def test_insert_table_name_not_str(orm):
    """testa passar o nome de uma tabela diferente de string"""
    
    expected_return = re.escape(get_errors("type_error_insert", "table_name", 0, "str"))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.insert(0, ["value1"], "column1")
        
        
def test_insert_values_not_list(orm):
    """testa passar valores fora de uma lista"""
    
    expected_return = re.escape(get_errors("type_error_insert", "values", "value1", "list"))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.insert("table", "value1", "column1")
        
        
def test_insert_args_not_str(orm):
    """testa passar valores fora de uma lista"""
    
    expected_return = re.escape(get_errors("type_error_insert_args", 0, 0, 0))
    
    with pytest.raises(TypeError, match=expected_return):
        orm.insert("table", ["value1"], 0)
        
        
def test_insert_values_different_column(orm):
    """passa um número de valores diferente do de colunas"""
    
    expected_return = re.escape(get_errors("value_error_insert", 1, 2, 0))
    
    with pytest.raises(ValueError, match=expected_return):
        orm.insert("table", ["value1", "value2"], "column1")
    
    
if __name__ == "__main__":
    pytest.main(["-vv", "test_my_orm_exceptions.py"])