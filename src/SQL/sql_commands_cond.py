from typing import Optional as Op
from exceptions.errors_cmd_cond import type_error
    

def whe_(condition: str, cond_in: Op[list]=None):
    """retorna a condição WHERE"""
    if not isinstance(condition, str):
        raise type_error("condition", condition, "str", "whe_")
    if cond_in != None and not isinstance(cond_in, list):
        raise type_error("cond_in", cond_in, "list", "whe_")
    
    if cond_in != None:
        cond = in_(cond_in, "whe_")
    sql_command = f"**whe** WHERE {condition}{' '+cond if cond_in != None else ''}"
    
    return sql_command


def betw_(par1, par2) -> str:
    sql_command = f"**betw** BETWEEN {par1} AND {par2}"
    
    return sql_command
    

def and_(condition: str, cond_in: Op[list]=None):
    """retorna a condição AND"""
    if not isinstance(condition, str):
        raise type_error("condition", condition, "str", "and_")
    if cond_in != None and not isinstance(cond_in, list):
        raise type_error("cond_in", cond_in, "list", "and_")
    
    sql_command = ""
    if cond_in != None:
        cond = in_(cond_in, "and_")
        sql_command = f"**and** AND ({condition} {cond})"
    else:
        sql_command = f"**and** AND {condition}"
    
    return sql_command


def or_(condition: str, cond_in: Op[list]=None):
    """retorna a condição OR"""
    if not isinstance(condition, str):
        raise type_error("condition", condition, "str", "or_")
    if cond_in != None and not isinstance(cond_in, list):
        raise type_error("cond_in", cond_in, "list", "or_")
    
    sql_command = ""
    if cond_in != None:
        cond = in_(cond_in, "or_")
        sql_command = f"**or** OR ({condition} {cond})"
    else:
        sql_command = f"**or** OR {condition}"
    
    return sql_command
    
    
def in_(values: list, funct: Op[str]="in_"):
    """retorna a condição IN"""
    if not isinstance(values, list):
        raise type_error("values", values, "list", funct)
    if len(values) < 1:
        raise ValueError(f"({funct}()) The list of values ​​cannot be empty. See the documentation at https://github.com/paulindavzl/my-orm.")
    
    values_list = ", ".join(values)
    sql_command = f"**in** IN ({values_list})"
    
    return sql_command

