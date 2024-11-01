def _get_tags_to(funct: str):
    conds = ["**whe**", "**betw**", "**and**", "**in**", "**or**"]
    data_types = ["**int**", "**float**", "**dec**", "**doub**", "**char**", "**vchar**", "**txt**", "**bool**", "**date**", "**dtime**", "**tstamp**", "**fkey**", "**prop**", "**alter_add**", "**drop**", "**ren_column**", "**rename**", "**alt_col**"]
    
    tags = {
        "create": ["**make**"],
        "insert": ["**add**"],
        "select": ["**get**"],
        "update": ["**edit**"],
        "delete": ["**remove**"],
        "conds": conds,
        "data_types": data_types,
        "alter table": ["**altab**"]
    }
    
    response = []
    if funct != "all":
        response = tags.get(funct, ["**err**"])
    else:
        for key in tags:
            response += tags[key]
    
    return response
    
    
def _remove_tags(cmd):
    tags = _get_tags_to("all")
    for tag in tags:
        cmd = cmd.replace(tag+" ", "")
    
    return cmd
    
    
def _have_tag(cmd: str, tags: list):
    for tag in tags:
        if tag in cmd:
            return True
    return False
    
    
def _get_other_types(cmd: str):
    types = {
        " INTEGER ": "**int**", " FLOAT ": "**float**", " DECIMAL(": "**dec**",
        " DOUBLE ": "**doub**", " CHAR(": "**char**", " VARCHAR(": "**vchar**",
        " TEXT ": "**txt**", " DATE ": "**date**", " DATETIME ": "**dtime**",
        " BOOLEAN ": "**bool**", " TIMESTAMP ": "**tstamp**", " WHERE ": "**whe**", 
        " BETWEEN": "**betw**", " AND ": "**and**", " OR ": "**or**", 
        " IN ": "**in**", " FOREIGN KEY ": "**fkey**", " AUTO_INCREMENT ": "**prop**",
        " CURRENT_TIMESTAMP ": "**prop**", " PRIMARY_KEY ": "**prop**",
        " UNIQUE ": "**prop**", " NOT NULL ": "**prop**", " DEFAULT ": "**prop**",
        "ADD": "**alter_add**", "DROP COLUMN": "**drop**", 
        "ALTER COLUMN": "**alt_col**", "RENAME COLUMN": "**ren_col**", 
        "RENAME TO": "**rename**"
    }
    
    list_types = []
    for type in types:
        if type in cmd:
            list_types.append(types[type])
    return list_types


def _requirements_tags(cmd, type):
    tags = _get_tags_to(type)
    methods = ["create", "insert", "select", "update", "delete", "alter table"]
    
    if type in methods:
        if not cmd.startswith(tags[0]):
            return {"result": False}
        
        other_types = _get_other_types(cmd)
        for type in other_types:
            if type not in cmd:
                return {"result": False}
        
    else:
        if not _have_tag(cmd, tags):
            return {"result": False}
    return {"result": True, "cmd": _remove_tags(cmd)}
   