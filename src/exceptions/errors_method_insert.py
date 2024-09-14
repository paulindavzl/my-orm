def type_error(var_name, var, expec):
    """função para organizar o erro TypeError no geral
        Args:
            va_name (str): nome da variável com erro
            var: variável com erro (valor)
            expec (str): tipo esperado"""
            
    raise TypeError(f"{var_name} expected a {expec} value but received an {type(var).__name__} ({var}) value. See the documentation at https://github.com/paulindavzl/my-orm")
    

def type_error_args(arg):
    """função para organizar o error TypeError para *args
        Args:
            arg: variável que gerou o erro"""
    
    raise TypeError(f"All arg values ​​must be strings. {arg} is an {type(arg).__name__}. See the documentation at https://github.com/paulindavzl/my-orm")
    

def value_error(*args):
    """função que organiza a chamada do erro ValueError
        Args:
            *args: argumentos que serão comparados"""
    
    raise ValueError(f"The number of values ​({len(args[0])}) does not mean the number of columns ({len(args[1])})!")