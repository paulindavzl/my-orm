from utils import doc_link

def for_key(referrer: str, referenced: str, *args: str):
    if not isinstance(referrer, str):
        raise TypeError(f"(for_key()) referrer expected a str value, but received a {type(referrer).__name__} ({referrer}). {doc_link}")
    elif not isinstance(referenced, str):
        raise TypeError(f"(for_key()) referenced expected a str value, but received a {type(referenced).__name__} ({referenced}). {doc_link}")
    elif not "(" in referenced or not ")" in referenced:
        raise ValueError(f"(for_key()) The value that referenced ({referenced}) receives is not valid! A value in the 'table(column)' format is required. {doc_link}")
    else:
        for arg in args:
            if not isinstance(arg, str):
                raise TypeError(f"(for_key()) *args expected a str value, but received a {type(arg).__name__} ({arg}). {doc_link}")
    
    sql_commands = f"**fkey** FOREIGN KEY ({referrer}) REFERENCES {referenced} "
    if args:
        sql_commands += " ".join(args)
        
    return sql_commands.strip()
    

def on_up(command: str):
    if not isinstance(command, str):
        raise TypeError(f"(on_up()) command expected a str value, but received a {type(command).__name__} ({command}). {doc_link}")
    
    return f"ON UPDATE {command.upper()}"
    
    
def on_del(command: str):
    if not isinstance(command, str):
        raise TypeError(f"(on_del()) command expected a str value, but received a {type(command).__name__} ({command}). {doc_link}")
    
    return f"ON DELETE {command.upper()}"
    
    
def prop(*args: str, default=None):
    for arg in args:
        if not isinstance(arg, str):
            raise TypeError(f"(prop()) *args expected a str value, but received a {type(arg).__name__} ({arg}). {doc_link}")
    
    # comandos SQL abreviados
    abbreviations = {
        "auto": "AUTO_INCREMENT",
        "current": "CURRENT_TIMESTAMP",
        "pri_key": "PRIMARY KEY",
        "uni": "UNIQUE",
        "n_null": "NOT NULL"
    }
    
    sql_commands = "**prop** "
    
    # verifica se existe um valor padrão
    if default != None:
        if default in abbreviations:
            default = f"DEFAULT {abbreviations.get(default)}"
        else:
            default = f"DEFAULT {default}"
        sql_commands += default
    
    
    commands = []
    for arg in args:
        commands += [abbreviations.get(arg.lower(), arg.upper())]
        
    sql_commands += " ".join(filter(None, commands))
        
    return sql_commands
    
    