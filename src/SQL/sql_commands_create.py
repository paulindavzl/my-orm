"""
Neste módulo contém os comandos SQL utilizados para criar uma tabela

Note:
    Este módulo não deve ser acessado diretamente pelo usuário. Não modifique suas funções!

Functions:
    - integer(): comando para criar colunas de números inteiros (int)
    - t_float(): comando para criar colunas números decimais (float)
    - decimal(precision: int, scale: int): comando para criar colunas de números decimais (semelhante ao t_float), porém com mais precisão e liberdade em relação às casas decimais (float)
    - double(): semelhante à t_float e decimal, porém com mais precisão e espaço que t_float (float)
    - char(length: int): comando para criar colunas de textos com número fixo de caractéres (str)
    - varchar(max_length: int): comando para criar colunas de textos com um limite máximo de caractére (str)
    - text(): comando para criar colunas de textos sem limite de caractéres (str)
    - boolean(): comando para criar colunas booleanas (lógicas: TRUE, FALSE, UNKNOWN) (bool)
    - date(): comando para criar colunas de datas (YYYY/MM/DD)
    - datetime (): comando para criar colunas de data e hora (YYYY/MM/DD HH:MM:SS)
    - timestamp (): comando para criar colunas de data e hora que podem estar sujeitas ao fuso horário do sistema (YYYY/MM/DD HH:MM:SS)
    
Requirements:
    from exceptions.errors import type_error: importa exceções personalizadas
"""


from exceptions.errors_cmd_create import type_error

def integer():
    """retorna um comando para adicionar uma coluna tipo int"""
    
    sql_commands = f"**int** INTEGER"
        
    return sql_commands.strip()
    

def t_float():
    """retorna um comando para adicionar uma coluna tipo float"""
    
    sql_commands = f"**float** FLOAT"
        
    return sql_commands
    

def decimal(precision: int, scale: int):
    """Retorna um comando para adicionar uma coluna do tipo DECIMAL, semelhante ao FLOAT, porém com mais liberdade da parte do usuário"""
    
    # trata possíveis erros
    if not isinstance(precision, int):
        raise type_error("precision", precision, "int", "decimal")
    if not isinstance(scale, int):
        raise type_error("scale", scale, "int", "decimal")
    
    sql_commands = f"**dec** DECIMAL({precision}, {scale})"
    
    return sql_commands

    

def double():
    """retorna um comando para adicionar uma coluna tipo double (semelhante ao tipo float, porém com mais precisão e espaço)"""
        
    sql_commands = f"**doub** DOUBLE"
        
    return sql_commands
    
    
def char(length: int):
    """retorna um comando para adicionar uma coluna tipo str mas com um tamanho fixo"""
    
    # trata possíveis erros
    if not isinstance(length, int):
        raise type_error("length", length, "int", "char")
    
    sql_commands = f"**char** CHAR({length})"

    return sql_commands
    

def varchar(max_length: int):
    """retorna um comando para adicionar uma coluna tipo str mas com um tamanho máximo"""
    
    if not isinstance(max_length, int):
        raise type_error("max_length", max_length, "int", "varchar")
    
    sql_commands = f"**vchar** VARCHAR({max_length})"
        
    return sql_commands


def text():
    """retorna um comando para adicionar uma coluna tipo str com tamanho variável"""
    
    sql_commands = f"**txt** TEXT"
    
    return sql_commands
    
    
def boolean():
    """retorna um comando para adicionar uma coluna tipo bool"""
    
    sql_commands = f"**bool** BOOLEAN"
    
    return sql_commands
    

def date():
    """retorna um comando para adicionar uma coluna para armazenar uma data (YYYY/MM/DD HH:MM:SS)"""
    
    sql_commands = f"**date** DATE"

    return sql_commands
    

def datetime():
    """retorna um comando para adicionar uma coluna para armazenar uma data e hora (YYYY/MM/DD HH:MM:SS)"""
    
    sql_commands = f"**dtime** DATETIME"
        
    return sql_commands
    
    
def timestamp():
    """retorna um comando para adicionar uma coluna para armazenar uma data e hora que podem ser afetadas pelo fuso horário do sistemal () YYYY/MM/DD HH:MM:SS)"""
    
    sql_commands = f"**tstamp** TIMESTAMP"

    return sql_commands