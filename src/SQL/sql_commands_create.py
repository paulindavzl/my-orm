from utils import doc_link

def integer():
    sql_commands = f"**int** INTEGER"
        
    return sql_commands.strip()
    

def t_float():
    sql_commands = f"**float** FLOAT"
        
    return sql_commands
    

def decimal(precision: int, scale: int):
    if not isinstance(precision, int):
        raise TypeError(f"(decimal()) precision expected a int value, but received a {type(precision).__name__} ({precision}). {doc_link()}")
    if not isinstance(scale, int):
        raise TypeError(f"(decimal()) scale expected a int value, but received a {type(scale).__name__} ({scale}). {doc_link()}")
    
    sql_commands = f"**dec** DECIMAL({precision}, {scale})"
    
    return sql_commands

    
def double():
    sql_commands = f"**doub** DOUBLE"
        
    return sql_commands
    
    
def char(length: int):
    if not isinstance(length, int):
        raise TypeError(f"(char()) length expected a int value, but received a {type(length).__name__} ({length}). {doc_link()}")
    
    sql_commands = f"**char** CHAR({length})"

    return sql_commands
    

def varchar(max_length: int):
    if not isinstance(max_length, int):
        raise TypeError(f"(varchar()) max_length expected a int value, but received a {type(max_length).__name__} ({max_length}). {doc_link()}")
    
    sql_commands = f"**vchar** VARCHAR({max_length})"
        
    return sql_commands


def text():
    sql_commands = f"**txt** TEXT"
    
    return sql_commands
    
    
def boolean():
    sql_commands = f"**bool** BOOLEAN"
    
    return sql_commands
    

def date():
    sql_commands = f"**date** DATE"

    return sql_commands
    

def datetime():
    sql_commands = f"**dtime** DATETIME"
        
    return sql_commands
    
    
def timestamp():
    sql_commands = f"**tstamp** TIMESTAMP"

    return sql_commands