def type_error(var_name, var, expec):
    """função para organizar o erro TypeError no geral
        Args:
            va_name (str): nome da variável com erro
            var: variável com erro (valor)
            expec (str): tipo esperado"""
            
    return TypeError(f"(MyORM.get()) {var_name} expected a {expec} value but received an {type(var).__name__} ({var}) value. See the documentation at https://github.com/paulindavzl/my-orm")