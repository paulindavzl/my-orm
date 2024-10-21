from utils import doc_link

def add(column_name: str, props):
    if not isinstance(column_name, str):
        raise TypeError(f"(add()) column_name expected a str value, but received a {type(column_name).__name__} ({column_name}). {doc_link()}")
    elif not isinstance(props, tuple) and not isinstance(props, list) and not isinstance(props, str):
        raise TypeError(f"(add()) props expected a str/tuple/list value, but received a {type(props).__name__} ({props}). {doc_link()}")
    
    types = props
    if not isinstance(props, str):
        types = " ".join(props)
    
    sql_command = f"**alter_add** ADD {column_name} {types};"
    return sql_command
 

def drop(column_name: str):
    if not isinstance(column_name, str):
        raise TypeError(f"(drop()) column_name expected a str value, but received a {type(column_name).__name__} ({column_name}). {doc_link()}")
        
    sql_command = f"**drop** DROP COLUMN {column_name};"
    return sql_command
    
    
def edit(column_name: str, props):
    if not isinstance(column_name, str):
        raise TypeError(f"(edit()) column_name expected a str value, but received a {type(column_name).__name__} ({column_name}). {doc_link()}")
    elif not isinstance(props, tuple) and not isinstance(props, list) and not isinstance(props, str):
        raise TypeError(f"(edit()) props expected a str/tuple/list value, but received a {type(props).__name__} ({props}). {doc_link()}")
    
    types = props
    if not isinstance(props, str):
        types = " ".join(props)
        
    sql_command = f"**alt_col** ALTER COLUMN {column_name} {types};"
    return sql_command
    

def ren_column(old_name: str, new_name: str):
    if not isinstance(old_name, str):
        raise TypeError(f"(ren_column()) old_name expected a str value, but received a {type(old_name).__name__} ({old_name}). {doc_link()}")
    elif not isinstance(new_name, str):
        raise TypeError(f"(ren_column()) new_name expected a str value, but received a {type(new_name).__name__} ({new_name}). {doc_link()}")
    
    sql_command = f"**ren_col** RENAME COLUMN {old_name} {new_name};"
    return sql_command
    
    
def rename(new_name: str):
    if not isinstance(new_name, str):
        raise TypeError(f"(rename()) new_name expected a str value, but received a {type(new_name).__name__} ({new_name}). {doc_link()}")
    
    sql_command = f"**rename** RENAME TO {new_name};"
    return sql_command
    
