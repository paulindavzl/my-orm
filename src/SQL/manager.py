from types import ModuleType
from typing import Type

def _import_lib_for(dbs_type: str):
    if dbs_type == "sqlite":
        import sqlite3
        return sqlite3


def _connect_in(data: dict, dbs_lib):
    if data.get("dbs") == "sqlite":
        conn = dbs_lib.connect(data.get("url"), check_same_thread=False)
        
        return conn


def _connect_dbs(data: dict):
    dbs_lib = _import_lib_for(data.get("dbs")) # importa a biblioteca necessária
    conn = _connect_in(data, dbs_lib)
    
    return conn