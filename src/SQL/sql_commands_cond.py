"""
Neste módulo contém os comandos SQL utilizados para condicionar consultas em uma tabela

Note:
    Este módulo não deve ser acessado diretamente pelo usuário. Não modifique suas funções!

Functions:
    whe_(col_name: str, *args: str): para criar comandos WHERE
    betw_(par1, par2): para adicionar o comando BETWEEN
    and_(col_name: str, *args: str): para adicionar o comando AND
    or_(col_name: str, *args: str): para adicionar o comando OR
    in_(*args): para adiconar o comando IN"""
    

from exceptions.errors_cmd_cond import type_error
    

def whe_(col_name: str, *args: str) -> str:
    """adiciona uma condição WHERE na consulta
        Args:
            col_name (str): nome da coluna
            *args (str): condições"""
            
    # garante que col_name seja uma string
    if not isinstance(col_name, str):
        raise type_error("col_name", col_name, "str", "whe_")
    
    cond = " ".join([str(arg) for arg in args])
    sql_command = f"**whe** WHERE {col_name} {cond}"
    
    return sql_command


def betw_(par1, par2) -> str:
    """seleciona itens de dentro de um intervalo
        Args:
            par1: primeiro parâmetro do intervalo
            par2: segundo parâmetro do intervalo"""
    
    sql_command = f"**betw** BETWEEN {par1} AND {par2}"
    
    return sql_command
    

def and_(col_name: str, *args: str) -> str:
    """adiciona uma condição AND na consulta
        Args:
            col_name (str): nome da coluna
            *args (str): condições"""
            
    # garante que col_name seja uma string
    if not isinstance(col_name, str):
        raise type_error("col_name", col_name, "str", "and_")
    
    cond = " ".join([str(arg) for arg in args])
    
    if "**in**" in cond:
        sql_command = f"**and** AND {col_name} {cond}"
    else:
        cond = cond.replace("**in**", "")
        sql_command = f"**and** AND ({col_name} {cond})"
    
    return sql_command


def or_(col_name: str, *args: str) -> str:
    """adiciona uma condição OR na consulta
        Args:
            col_name (str): nome da coluna
            *args (str): condições"""
            
    # garante que col_name seja uma string
    if not isinstance(col_name, str):
        raise type_error("col_name", col_name, "str", "or_")
    
    cond = " ".join([str(arg) for arg in args])
    
    if "**in**" in cond:
        sql_command = f"**or** OR {col_name} {cond}"
    else:
        cond = cond.replace("**in**", "")
        sql_command = f"**or** OR ({col_name} {cond})"
    
    return sql_command
    
    
def in_(*args) -> str:
    """seleciona valores que correspondem a uma lista de valores
        Args:
            *args (str): valores que devem conter na consulta"""
    
    values_list = ", ".join(f"'{arg}'" for arg in args)
    sql_command = f"**in** IN ({values_list})"
    
    return sql_command
