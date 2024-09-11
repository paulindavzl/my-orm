def type_error(var_name: str, var_error, expected: str, funct_name: str) -> TypeError:
    """retorna um erro personalizado tipo TypeError
        Args:
            var_name (str):  nome da variável com erro
            var_error: valor da variável com erro
            expected (str): tipo de valor esperado para a variável
            funct_name (str): nome da função onde ocorre o erro"""
    
    raise TypeError(f"Unexpected '{type(var_error).__name__}' ({var_error}) in {funct_name}(). {var_name} expects a value of type '{expected}'. See the documentation at https://github.com/paulindavzl/my-orm.")
    

def value_error(var_name: str, var_error, expected: str, funct_name: str) -> ValueError:
    """retorna um erro personalizado tipo ValueError
        Args:
            var_name (str): nome da variável
            var_error: valor variável com erro
            expected (str): valor esperado
            funct_name (str): nome da função onde ocorre o erro"""
        
    raise ValueError(f"The value passed in '{var_name}' ({var_error}) is incorrect! {funct_name}() expects the value in '{expected}' format for the variable '{var_name}'. See the documentation at https://github.com/paulindavzl/my-orm")


def value_error_dbms(dbms_error: str, supported: list) -> ValueError:
    """retorna um erro personalizado tipo ValueError para SGBD
        Args:
            sgbd_error (str): sgbd informado sem suporte
            supported (list): lista de sgbd suportados"""
    
    sup = ", ".join(supported)
    
    raise ValueError(f"MyORM does not support '{dbms_error}'! Currently supported DBMSs are: {sup}. See the documentation at https://github.com/paulindavzl/my-orm")
   