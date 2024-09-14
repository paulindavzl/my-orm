def type_error(var_name: str, var, expect: str):
    """função que organiza o erro TypeError
        Args:
            var_name (str): nome da variável com erro
            var: variável com erro
            expect (str): valor esperado para a variável"""
            
    raise TypeError(f"{var_name} expected an {expect}, but received a {type(var).__name__} ({var}). See the documentation at https://github.com/paulindavzl/my-orm.")
    