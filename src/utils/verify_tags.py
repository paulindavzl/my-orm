"""
Este módulo verifica se um comando possui as tags exigidas

Note:
    As funções contidas neste módulo são de uso interno e não devem usadas pelo usuário
    
Functions:
    - _get_tags_to(funct: str): retorna as tags de acordo com a função
    - _remove_tags(cmd: str): retorna um comando sem as tags
    - _have_tag(cmd: str, tags: list): verifica se possui as tags passadas em uma lista
    - _get_other_types(cmd: str): obtém outros tipo de funções
    - _requirements_tags(cmd: str, type: str): agrupas todas a funcionalidades e verifica se possui as tags
"""

def _get_tags_to(funct: str) -> tuple:
    """retorna todas as tags de acordo com nome da função
        Args:
            funct (str): nome da função relacionada as tags"""
    
    conds = ["**whe**", "**betw**", "**and**", "**in**", "**or**"]
    data_types = ["**int**", "**float**", "**dec**", "**doub**", "**char**", "**vchar**", "**txt**", "**bool**", "**date**", "**dtime**", "**tstamp**", "**fkey**", "**prop**"]
    
    tags = {
        "create": [
            "**make**"
        ],
        "insert": [
            "**add**"
        ],
        "select": [
            "**get**"
        ],
        "conds": conds,
        "data_types": data_types
    }
    
    response = []
    if funct != "all":
        response = tags.get(funct, ["**err**"])
    else:
        for key in tags:
            response += tags[key]
    
    return response
    
    
def _remove_tags(cmd):
    """remove as tags do comando e retorna-o sem tag
        Args:
            cmd (str): comando com tags"""
    
    tags = _get_tags_to("all")
    for tag in tags:
        cmd = cmd.replace(tag+" ", "")
    
    return cmd
    
    
def _have_tag(cmd: str, tags: list):
    """Verifica se a tag existe no comando
        Args:
            cmd (str): comando
            tags (list): lista de tags"""
    
    for tag in tags:
        if tag in cmd:
            return True
    return False
    
    
def _get_other_types(cmd: str):
    """verifica, agrupa e retorna os outros tipos de dado do comando
        Args:
            -cmd (str): comando analizado"""
            
    types = {
        " INTEGER ": "**int**", " FLOAT ": "**float**", " DECIMAL(": "**dec**",
        " DOUBLE ": "**doub**", " CHAR(": "**char**", " VARCHAR(": "**vchar**",
        " TEXT ": "**txt**", " DATE ": "**date**", " DATETIME ": "**dtime**",
        " BOOLEAN ": "**bool**", " TIMESTAMP ": "**tstamp**", " WHERE ": "**whe**", 
        " BETWEEN": "**betw**", " AND ": "**and**", " OR ": "**or**", 
        " IN ": "**in**", " FOREIGN KEY ": "**fkey**", " AUTO_INCREMENT ": "**prop**",
        " CURRENT_TIMESTAMP ": "**prop**", " PRIMARY_KEY ": "**prop**",
        " UNIQUE ": "**prop**", " NOT NULL ": "**prop**", " DEFAULT ": "**prop**"
    }
    
    list_types = []
    for type in types:
        if type in cmd:
            list_types.append(types[type])
    return list_types


def _requirements_tags(cmd, type):
    """organiza a verificação das tags exigidas
        Args:
            cmd (str): comando analisado
            type (str): tipo de função que gerou o comando"""
            
    tags = _get_tags_to(type)
    methods = ["create", "insert", "select", "update", "delete"]
    
    if type in methods:
        if not cmd.startswith(tags[0]):
            return {"result": False}
        
        other_types = _get_other_types(cmd)
        for type in other_types:
            if type not in cmd:
                print(type)
                return {"result": False}
        
    else:
        if not _have_tag(cmd, tags):
            return {"result": False}
    return {"result": True, "cmd": _remove_tags(cmd)}
    

