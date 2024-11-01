from types import ModuleType
from typing import Type
from utils import doc_link

def _import_lib_for(dbs_type: str):
    sql = None
    
    if dbs_type == "sqlite":
        try:
            import sqlite3 as sql
        except ImportError:
            raise ImportError(f"It looks like you don't have the 'sqlite3' library installed! Use 'pip install sqlite3' and try again. {doc_link()}")
    elif dbs_type == "mysql":
        try:
            import mysql.connector as sql
        except ImportError:
            raise ImportError(f"It looks like you don't have the 'mysql-connector-python' library installed! Use 'pip install mysql-connector-python' and try again. {doc_link()}")
    elif dbs_type == "postgres":
        try:
            import pg8000 as sql
        except ImportError:
            raise ImportError(f"It looks like you don't have the 'pg8000' library installed! Use 'pip install pg8000' and try again. {doc_link()}")
    else:
        raise ValueError(f"This ORM does not support the SGDB provided ({dbs_type})! {doc_link()}")
        
    return sql


def _connect_in(data: dict, dbs_lib):
    dbs = data.get("dbs")
    conn = None
    
    if dbs == "sqlite":
        conn = dbs_lib.connect(data.get("path"), check_same_thread=False)
    elif dbs == "mysql":
        conn = dbs_lib.connect(
            user = data.get("user"),
            password = data.get("password"),
            host = data.get("host"),
            database = data.get("database"),
            port=data.get("port", 3306)
        )
    elif dbs == "postgres":
        conn = dbs_lib.connect(
            user = data.get("user"),
            password = data.get("password"),
            host = data.get("host"),
            database = data.get("database"),
            port=data.get("port", 5432)
        )
    else:
        raise ValueError(f"This ORM does not support the SGDB provided ({dbs})! {doc_link()}")
        
    return conn


def _connect_dbs(data: dict):
    dbs_lib = _import_lib_for(data.get("dbs")) # importa a biblioteca necessária
    conn = _connect_in(data, dbs_lib)
    
    return conn