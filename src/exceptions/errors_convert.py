def type_error(var_name: str, var, expec: str, funct: str):
    """retorna um erro personalizado tipo TypeError
        Args:
            var_name (str):  nome da variável com erro
            var: valor da variável com erro
            expec (str): tipo de valor esperado para a variável
            funct (str): nome da função onde ocorre o erro"""
            
    return TypeError(f"({funct}()) {var_name} expected a {expec}, but received a {type(var).__name__}")
    

def value_error(status: bool, data, keys):
    """retorna um erro personalizado caso as listas tenham tamanho diferente
        Args:
            status (bool): verifica se a primeira é maior que a segunda"""
            
    if status:
        err = f"(_to_dict()) data tem mais valores que keys ({len(data)} > {len(keys)})!"
    else:
        err = f"(_to_dict()) data tem menos valores que keys ({len(data)} < {len(keys)})!"
        
    return ValueError(err)