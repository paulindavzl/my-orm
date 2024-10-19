from exceptions.errors_cmd_create import type_error, value_error

def for_key(referrer: str, referenced: str, *args: str) -> str:
    if not isinstance(referrer, str):
        raise type_error("referrer", referrer, "str", "for_key")
    elif not isinstance(referenced, str):
        raise type_error("referenced", referenced, "str", "for_key")
    elif not "(" in referenced or not ")" in referenced:
        raise value_error("referenced", referenced, "table(column)", "for_key")
    else:
        for arg in args:
            if not isinstance(arg, str):
                raise type_error("*args", arg, "str", "for_key")
    
    sql_commands = f"**fkey** FOREIGN KEY ({referrer}) REFERENCES {referenced} "
    if args:
        sql_commands += " ".join(args)
        
    return sql_commands.strip()
    

def on_up(command: str):
    if not isinstance(command, str):
        raise type_error("command", command, "str", "on_up")
    
    return f"ON UPDATE {command.upper()}"
    
    
def on_del(command: str):
    if not isinstance(command, str):
        raise type_error("command", command, "str", "on_del")
    
    return f"ON DELETE {command.upper()}"
    
    
def prop(*args: str, default=None):
    for arg in args:
        if not isinstance(arg, str):
            raise type_error("*args", arg, "str", "prop")
    
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
        commands += [abbreviations.get(arg.lower())]
        
    sql_commands += " ".join(filter(None, commands))
        
    return sql_commands
    