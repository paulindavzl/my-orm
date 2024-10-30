from typing import Optional as Op
from utils import doc_link
    

def whe_(condition: str, cond_in: Op[str]=None):
    """retorna a condição WHERE"""
    if not isinstance(condition, str):
        raise TypeError(f"(whe_()) condition expected a str value, but received a {type(condition).__name__} ({condition}). {doc_link()}")
    if cond_in != None and not isinstance(cond_in, str):
        raise TypeError(f"(whe_()) cond_in expected a str value, but received a {type(cond_in).__name__} ({cond_in}). {doc_link()}")
    
    if cond_in != None:
        cond = in_(cond_in, "whe_")
    sql_command = f"**whe** WHERE {condition}{' '+cond if cond_in != None else ''}"
    
    return sql_command


def betw_(column: str, par1, par2) -> str:
    if not isinstance(column, str):
        raise TypeError(f"(betw_()) column expected a str value, but received a {type(column).__name__} ({column}). {doc_link()}")
    
    sql_command = f"**betw** {column} BETWEEN {par1} AND {par2}"
    
    return sql_command
    

def and_(condition: str, cond_in: Op[str]=None):
    """retorna a condição AND"""
    if not isinstance(condition, str):
        raise TypeError(f"(and_()) condition expected a str value, but received a {type(condition).__name__} ({condition}). {doc_link()}")
    if cond_in != None and not isinstance(cond_in, str):
        raise TypeError(f"(and_()) cond_in expected a str value, but received a {type(cond_in).__name__} ({cond_in}). {doc_link()}")
    
    sql_command = ""
    if cond_in != None:
        cond = in_(cond_in, "and_")
        sql_command = f"**and** AND ({condition} {cond})"
    else:
        sql_command = f"**and** AND {condition}"
    
    return sql_command


def or_(condition: str, cond_in: Op[str]=None):
    """retorna a condição OR"""
    if not isinstance(condition, str):
        raise TypeError(f"(or_()) condition expected a str value, but received a {type(condition).__name__} ({condition}). {doc_link()}")
    if cond_in != None and not isinstance(cond_in, str):
        raise TypeError(f"(or_()) cond_in expected a str value, but received a {type(cond_in).__name__} ({cond_in}). {doc_link()}")
    
    sql_command = ""
    if cond_in != None:
        cond = in_(cond_in, "or_")
        sql_command = f"**or** OR ({condition} {cond})"
    else:
        sql_command = f"**or** OR {condition}"
    
    return sql_command
    
    
def in_(values: str, funct: Op[str]="in_"):
    """retorna a condição IN"""
    if not isinstance(values, str):
        raise TypeError(f"({funct}()) values expected a str value, but received a {type(values).__name__} ({values}). {doc_link()}")
    if len(values) < 1:
        raise ValueError(f"({funct}()) The list of values ​​cannot be empty. See the documentation at https://github.com/paulindavzl/my-orm.")
    
    sql_command = f"**in** IN ({values})"
    
    return sql_command

