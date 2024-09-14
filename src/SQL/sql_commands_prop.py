"""
Neste módulo contém os comandos SQL utilizados para adicionar propriedades às colunas

Note:
    Este módulo não deve ser acessado diretamente pelo usuário. Não modifique suas funções!
    
Functions:
    - foreign_key(referrer: str, referenced: str, *args: str): adiciona uma chave estrangeira
    - on_up(command: str): ON UPDATE comando complementar para foreign_key, define uma ação quando a chave estrangeira for atualizada
    - on_del(command: str): ON DELETE comando complementar para foreign_key, define uma ação quando a chave estrangeira for deletada
    - prop(*args: str, default=None): outras propriedades abreviadas:
        - uni: UNIQUE não permite que exista maisnde uma coluna como mesmo valor
        - auto: AUTO_INCREMENT adiciona um valor sequencial automaticamente quando a um novo registro for adicionado
        - default: DEFAULT adiciona um valor padrão para uma coluna, pode receber valores de prop() ou de fora
        - pri_key: PRIMARY KEY adiciona um chave primária numa coluna
        - current: CURRENT_TIMESTAMP mantém as informações uma coluna de data e hora sempre atualizadas
        - n_null: NOT NULL não permite que uma coluna receba um valor vazio
        
Requirements:
    from exceptions.errors import type_error, value_error: importa exceções personalizadas
"""

from exceptions.errors_cmd_create import type_error, value_error

def foreign_key(referrer: str, referenced: str, *args: str) -> str:
    """retorna o comando SQL que define uma chave estrangeira
        Args:
            referrer (str): coluna que contém a chave estrangeira
            referenced (str): tabela que contém a chave primária
            *args (str): propriedades extras da chave estrangeira"""
            
    # trata possíveis erros
    if not isinstance(referrer, str):
        type_error("referrer", referrer, "str", "foreign_key")
    elif not isinstance(referenced, str):
        type_error("referenced", referenced, "str", "foreign_key")
    elif not "(" in referenced or not ")" in referenced:
        value_error("referenced", referenced, "table(column)", "foreign_key")
    else:
        for arg in args:
            if not isinstance(arg, str):
                type_error("*args", arg, "str", "foreign_key")
    
    sql_commands = f"FOREIGN KEY ({referrer}) REFERENCES {referenced} "
    if args:
        sql_commands += " ".join(args)
        
    return sql_commands.strip()
    

def on_up(command: str) -> str:
    """retorna o comando SQL para ON UPDATE"""
    
    # trata possíveis erros
    if not isinstance(command, str):
        type_error("command", command, "str", "on_up")
    
    return f"ON UPDATE {command.upper()}"
    
    
def on_del(command: str) -> str:
    """retorna o comando SQL para ON DELETE"""
    
    # trata possíveis erros
    if not isinstance(command, str):
        type_error("command", command, "str", "on_del")
    
    return f"ON DELETE {command.upper()}"
    
    
def prop(*args: str, default=None) -> str:
    """outras propriedades que podem ser abreviadas
        Args:
            *args (str): propriedades abreviadas
                Examples:
                    auto -> AUTO_INCREMENT
                    current -> CURRENT_TIMESTAMP
                    pri_key -> PRIMARY KEY
                    uni -> UNIQUE
                    n_null -> NOT NULL
            default: DEFAULT valor padrão de uma coluna"""
    
    # trata possíveis erros
    for arg in args:
        if not isinstance(arg, str):
            type_error("*args", arg, "str", "prop")
    
    # comandos SQL abreviados
    abbreviations = {
        "auto": "AUTO_INCREMENT",
        "current": "CURRENT_TIMESTAMP",
        "pri_key": "PRIMARY KEY",
        "uni": "UNIQUE",
        "n_null": "NOT NULL"
    }
    
    sql_commands = ""
    
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
    