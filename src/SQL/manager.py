"""
Este módulo realiza e gerencia a conexão com o banco de dados

Note:
    Nem este módulo nem suas funções devem ser acessadas diretamente pelo usuário, são funções internas do sistema

Functions:
    - _import_lib_for(dbs_type: str): importa a biblioteca necessária para conectar-se com o banco de dados escolhido pelo usuário
    - _connect_in(dbs_type: str, dbs_lib: Type[ModuleType], data: dict): conecta-se ao banco de dados e retorna as informações
    - _connect_dbs(dbs_type: str, data: dict): gerencia as funções responsáveis por fazer a conexão com o banco de dados
    
Requirements:
    - from types import ModuleType: suporte para o tipo ModuleType
    - from typing import Type: suporte para outros tipos de dados
    - from exceptions.errors import type_error, value_error_dbms: importa exceções personalizadas
"""

from types import ModuleType
from typing import Type
from exceptions.errors_cmd_create import type_error, value_error_dbms

def _import_lib_for(dbs_type: str) -> Type[ModuleType]:
    """importa somente a biblioteca necessária
        Args:
            - dbs_type (str): informa qual será o banco de dados usado"""
    
    if dbs_type == "sqlite":
        import sqlite3
        return sqlite3


def _connect_in(data: dict, dbs_lib: Type[ModuleType]):
    """realiza de fato a conexão com o banco de dados
        Args:
            - dbs_type (str): informa qual será o banco de dados usado
            - dbs_lib (module): biblioteca usada para realiza a conexão com o banco de dados
            - data (dict): dicionário com os dados necessários para realizar a conexão com o banco de dados"""
    
    if data.get("dbs") == "sqlite":
        conn = dbs_lib.connect(data.get("url"), check_same_thread=False)
        
        return conn


def _connect_dbs(data: dict):
    """gerencia a conexão com o banco de dados
        Args:
            - dbs_type (str): informa qual será o banco de dados usado
            - data (dict): dicionário com os dados necessários para realizar a conexão com o banco de dados"""
    
    if not isinstance(data, dict):
        raise type_error("data", data, "dict", "_connect_dbs")
    
    dbs_lib = _import_lib_for(data.get("dbs")) # importa a biblioteca necessária
    conn = _connect_in(data, dbs_lib)
    
    return conn