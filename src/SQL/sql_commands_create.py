"""
Neste módulo contém os comandos SQL utilizados para criar uma tabela

Note:
    Este módulo não deve ser acessado diretamente pelo usuário. Não modifique suas funções!

Functions:
    - integer(col_name: str, *args: str): comando para criar colunas de números inteiros (int)
    - t_float(col_name: str, *args: str): comando para criar colunas números decimais (float)
    - decimal(col_name: str, precision: int, scale: int, *args: str): comando para criar colunas de números decimais (semelhante ao t_float), porém com mais precisão e liberdade em relação às casas decimais (float)
    - double(col_name: str, *args: str): semelhante à t_float e decimal, porém com mais precisão e espaço que t_float (float)
    - char(col_name: str, length: int, *args: str): comando para criar colunas de textos com número fixo de caractéres (str)
    - varchar(col_name: str, max_length: int, *args: str): comando para criar colunas de textos com um limite máximo de caractére (str)
    - text(col_name: str, *args: str): comando para criar colunas de textos sem limite de caractéres (str)
    - boolean(col_name: str, *args: str): comando para criar colunas booleanas (lógicas: TRUE, FALSE, UNKNOWN) (bool)
    - date(col_name: str, *args: str): comando para criar colunas de datas (YYYY/MM/DD)
    - datetime (col_name: str, *args: str): comando para criar colunas de data e hora (YYYY/MM/DD HH:MM:SS)
    - timestamp (col_name: str, *args: str): comando para criar colunas de data e hora que podem estar sujeitas ao fuso horário do sistema (YYYY/MM/DD HH:MM:SS)
    
Requirements:
    from exceptions.errors import type_error: importa exceções personalizadas
"""


from exceptions.errors_cmd_create import type_error

def integer(col_name: str, *args: str) -> str:
    """retorna um comando para adicionar uma coluna tipo int
        Args:
            col_name (str): nome da coluna
            *args: (str): propriedades da coluna"""
            
    # trata possíveis erros
    if not isinstance(col_name, str):
        raise type_error("col_name", col_name, "str", "integer")
    else:
        for arg in args:
            if not isinstance(arg, str):
                raise type_error("*args", arg, "str", "integer")
    
    sql_commands = f"{col_name} INTEGER "
    if args:
        sql_commands += " ".join(args)
        
    return sql_commands.strip()
    

def t_float(col_name: str, *args: str) -> str:
    """retorna um comando para adicionar uma coluna tipo float
        Args:
            col_name (str): nome da coluna
            *args: (str): propriedades da coluna"""
    
    # trata possíveis erros
    if not isinstance(col_name, str):
        raise type_error("col_name", col_name, "str", "t_float")
    else:
        for arg in args:
            if not isinstance(arg, str):
                raise type_error("*args", arg, "str", "t_float")
    
    sql_commands = f"{col_name} FLOAT "
    if args:
        sql_commands += " ".join(args)
        
    return sql_commands.strip()
    

def decimal(col_name: str, precision: int, scale: int, *args: str) -> str:
    """Retorna um comando para adicionar uma coluna do tipo DECIMAL, semelhante ao FLOAT, porém com mais liberdade da parte do usuário
        Args:
            col_name (str): Nome da coluna
            precision (int): Número total de dígitos
            scale (int): Número de dígitos após o ponto decimal
            *args (str): Propriedades adicionais da coluna"""
    
    # trata possíveis erros
    if not isinstance(col_name, str):
        raise type_error("col_name", col_name, "str", "decimal")
    elif not isinstance(precision, int):
        raise type_error("precision", precision, "int", "decimal")
    elif not isinstance(scale, int):
        raise type_error("scale", scale, "int", "decimal")
    else:
        for arg in args:
            if not isinstance(arg, str):
                raise type_error("*args", arg, "str", "decimal")
    
    sql_commands = f"{col_name} DECIMAL({precision}, {scale}) "
    if args:
        sql_commands += " ".join(args)
    
    return sql_commands.strip()

    

def double(col_name: str, *args: str) -> str:
    """retorna um comando para adicionar uma coluna tipo double (semelhante ao tipo float, porém com mais precisão e espaço)
        Args:
            col_name (str): nome da coluna
            *args: (str): propriedades da coluna"""
    
    # trata possíveis erros
    if not isinstance(col_name, str):
        raise type_error("col_name", col_name, "str", "double")
    else:
        for arg in args:
            if not isinstance(arg, str):
                raise type_error("*args", arg, "str", "double")
    
    sql_commands = f"{col_name} DOUBLE "
    if args:
        sql_commands += " ".join(args)
        
    return sql_commands.strip()
    
    
def char(col_name: str, length: int, *args: str) -> str:
    """retorna um comando para adicionar uma coluna tipo str mas com um tamanho fixo
        Args:
            col_name (str): nome da coluna
            length (int): defino o tamanho que a coluna terá
            *args: (str): propriedades da coluna"""
    
    # trata possíveis erros
    if not isinstance(col_name, str):
        raise type_error("col_name", col_name, "str", "char")
    if not isinstance(length, int):
        raise type_error("length", length, "int", "char")
    else:
        for arg in args:
            if not isinstance(arg, str):
                raise type_error("*args", arg, "str", "char")
    
    sql_commands = f"{col_name} CHAR({length}) "
    if args:
        sql_commands += " ".join(args)
        
    return sql_commands.strip()
    

def varchar(col_name: str, max_length: int, *args: str) -> str:
    """retorna um comando para adicionar uma coluna tipo str mas com um tamanho máximo
        Args:
            col_name (str): nome da coluna
            max_length (int): defino o tamanho que a coluna terá
            *args: (str): propriedades da coluna"""
    
    # trata possíveis erros
    if not isinstance(col_name, str):
        raise type_error("col_name", col_name, "str", "varchar")
    if not isinstance(max_length, int):
        raise type_error("max_length", max_length, "int", "varchar")
    else:
        for arg in args:
            if not isinstance(arg, str):
                raise type_error("*args", arg, "str", "varchar")
    
    sql_commands = f"{col_name} VARCHAR({max_length}) "
    if args:
        sql_commands += " ".join(args)
        
    return sql_commands.strip()


def text(col_name: str, *args: str) -> str:
    """retorna um comando para adicionar uma coluna tipo str com tamanho variável
        Args:
            col_name (str): nome da coluna
            *args: (str): propriedades da coluna"""
    
    # trata possíveis erros
    if not isinstance(col_name, str):
        raise type_error("col_name", col_name, "str", "text")
    else:
        for arg in args:
            if not isinstance(arg, str):
                raise type_error("*args", arg, "str", "text")
    
    sql_commands = f"{col_name} TEXT "
    if args:
        sql_commands += " ".join(args)
        
    return sql_commands.strip()
    
    
def boolean(col_name: str, *args: str) -> str:
    """retorna um comando para adicionar uma coluna tipo bool
        Args:
            col_name (str): nome da coluna
            *args: (str): propriedades da coluna"""
    
    # trata possíveis erros
    if not isinstance(col_name, str):
        raise type_error("col_name", col_name, "str", "boolean")
    else:
        for arg in args:
            if not isinstance(arg, str):
                raise type_error("*args", arg, "str", "boolean")
    
    sql_commands = f"{col_name} BOOLEAN "
    if args:
        sql_commands += " ".join(args)
        
    return sql_commands.strip()
    

def date(col_name: str, *args: str) -> str:
    """retorna um comando para adicionar uma coluna para armazenar uma data
        Args:
            col_name (str): nome da coluna
            *args: (str): propriedades da coluna
        FORMAT:
            YYYY/MM/DD"""
    
    # trata possíveis erros
    if not isinstance(col_name, str):
        raise type_error("col_name", col_name, "str", "date")
    else:
        for arg in args:
            if not isinstance(arg, str):
                raise type_error("*args", arg, "str", "date")
    
    sql_commands = f"{col_name} DATE "
    if args:
        sql_commands += " ".join(args)
        
    return sql_commands.strip()
    

def datetime(col_name: str, *args: str) -> str:
    """retorna um comando para adicionar uma coluna para armazenar uma data e hora
        Args:
            col_name (str): nome da coluna
            *args: (str): propriedades da coluna
        FORMAT:
            YYYY/MM/DD HH:MM:SS"""
    
    # trata possíveis erros
    if not isinstance(col_name, str):
        raise type_error("col_name", col_name, "str", "datetime")
    else:
        for arg in args:
            if not isinstance(arg, str):
                raise type_error("*args", arg, "str", "datetime")
    
    sql_commands = f"{col_name} DATETIME "
    if args:
        sql_commands += " ".join(args)
        
    return sql_commands.strip()
    
    
def timestamp(col_name: str, *args: str) -> str:
    """retorna um comando para adicionar uma coluna para armazenar uma data e hora que podem ser afetadas pelo fuso horário do sistema
        Args:
            col_name (str): nome da coluna
            *args: (str): propriedades da coluna
        FORMAT:
            YYYY/MM/DD HH:MM:SS"""
    
    # trata possíveis erros
    if not isinstance(col_name, str):
        raise type_error("col_name", col_name, "str", "timestamp")
    else:
        for arg in args:
            if not isinstance(arg, str):
                raise type_error("*args", arg, "str", "timestamp")
    
    sql_commands = f"{col_name} TIMESTAMP "
    if args:
        sql_commands += " ".join(args)
        
    return sql_commands.strip()