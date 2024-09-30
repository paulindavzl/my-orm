"""
Este módulo faz a conversão de um tipo de dado para outro

Note:
    As funções contidas neste módulo não devem ser usadas diretamente pelo usuário

Methods:
    - _to_dict(data: list, keys: list): transforma uma lista em um dicionário
    
Requirements:
    - from exceptions.errors_convert import type_error, value_error: importa exceções
"""

from exceptions.errors_convert import type_error, value_error

def _to_dict(data: list, keys: list):
    """transforma uma lista em um dicionário de acordo com as chaves passadas
        Args:
            data (list): lista de dados
            keys (list): lista com as chaves do dicionário"""
    
    # garante que o valor de data seja uma lista
    if not isinstance(data, list):
        raise type_error("data", data, "list", "_to_dict")
        
    # garante que o valor de keys seja uma lista
    if not isinstance(keys, list):
        raise type_error("keys", keys, "list", "_to_dict")
        
    # garante que tenha chaves o suficiente para os valores de data
    if len(data[0]) != len(keys):
        raise value_error(len(data) > len(keys), data, keys)
    
    result = []
    for pos in range(len(data)):
        sub_pos = 0
        res_dict = {}
        for item in data[pos]:
            res_dict[str(keys[sub_pos])] = item
            sub_pos += 1
        
        result.append(res_dict)
        
    return result
    
