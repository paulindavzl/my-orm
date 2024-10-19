from types import ModuleType
from typing import Type
from exceptions.errors_cmd_create import type_error, value_error_dbms

def _import_lib_for(dbs_type: str) -> Type[ModuleType]:
    if dbs_type == "sqlite":
        import sqlite3
        return sqlite3


def _connect_in(data: dict, dbs_lib: Type[ModuleType]):
    if data.get("dbs") == "sqlite":
        conn = dbs_lib.connect(data.get("url"), check_same_thread=False)
        
        return conn


def _connect_dbs(data: dict):
    if not isinstance(data, dict):
        raise type_error("data", data, "dict", "_connect_dbs")
    
    dbs_lib = _import_lib_for(data.get("dbs")) # importa a biblioteca necessária
    conn = _connect_in(data, dbs_lib)
    
    return conn