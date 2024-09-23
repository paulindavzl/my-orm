def type_error(var_name: str, var, expec: str, funct: str):
    """retorna um erro personalizado tipo TypeError
        Args:
            var_name (str):  nome da variável com erro
            var: valor da variável com erro
            expec (str): tipo de valor esperado para a variável
            funct (str): nome da função onde ocorre o erro"""
            
    return TypeError(f"({funct}()) {var_name} expected a value like {expec}, but received a {type(var).__name__} ({var})")