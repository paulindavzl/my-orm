"""
Este módulo realiza a conexão com um banco de dados e facilita a manipulação de comandos SQL!

Classes:
    - MyORM: classe responsável por gerenciar a conexão com bancos de dados e fornecer métodos para manipulação de comandos SQL
    
Methods:
    - MyORM.make(): cria uma tabela no banco de dados caso ela não exista
    - MyORM.add(): insere valores em uma tabela
    - MyORM.get(): retorna registros de uma tabela
    - MyORM.exe(): executa comandos SQL
    - MyORM.show(): retornar todos os atributos da classe
    
Requirements:
    - from typing import Optional: suporte para tipos opcionais
    - from SQL.sql_commands_create import *: funções para criar tabelas
    - from SQL.sql_commands_prop import *: funções para adicionar propriedades nas tabelas
    - from SQL.sql_commands_cond import *: funções para condicionar consultas
    - from SQL.manager import _connect_dbs: função para conectar-se ao banco de dados 
    - from utils.convert import _to_dict: função que converte dados em listas
    - from utils.verify_tags import _requirements_tags, _remove_tags: importa funções relacionadas às tags
    - from exceptions import errors_method_insert, errors_method_create, errors_method_select: importa os erros personalizados de cada função
"""

from typing import Optional as Op
from SQL.sql_commands_create import *
from SQL.sql_commands_prop import *
from SQL.sql_commands_cond import *
from SQL.manager import _connect_dbs
from utils.convert import _to_dict
from utils.verify_tags import _requirements_tags as _req_tags, _remove_tags
from exceptions import errors_method_insert as err_add, errors_method_create as err_make, errors_method_select as err_get, errors_method_update as err_edit

class MyORM:
    """classe geral da ORM, gerencia todos os métodos
        Attributes:
            - __dbs_type (Optional[str]): tipo de banco de dados (ex: SQLite, MySQL...)
            - __dbs_conn_data (Optional[dict]): dados necessários para conectar-se ao banco de dados
            - __ret_sql (Optional[bool]): caso True, retorna o comando SQL gerado
            - __exe (Optional[bool]): caso True, executa os comandos gerados
            - __req_tag (Optional[bool]): quando ativo, garante que os comandos foram gerados por funções internas
            
        Methods:
            - make(table_name: str, *args: str): cria uma tabela sempre que não existir
            - add(self, table_name: str, values: list, *args: str): insere registros em uma tabela
            - get(self, table_name: str, columns: list, ret_dict: Op[dict]=True, *args: Op[str]): retorna dados de uma tabela
            - exe(sql_commands: str, values: Optional[list]=None): executa comandos SQL
            - show(): retorna os atributos da classe
            - cols_name(table_name: str): retorna o nome das colunas de uma tabela"""
    
    def __init__(self, dbs_type: Op[str]=None, dbs_connection_data: Op[dict]=None, sql_return: Op[bool]=False, execute: Op[bool]=True, return_dict: Op[bool]=True, require_tags: Op[bool]=True):
        self.__dbs_type = dbs_type # tipo de banco de dados (SQLite, MySQL...)
        self.__dbs_conn_data = dbs_connection_data # dados para conexão com banco de dados (servidor, user...)
        self.__ret_sql = sql_return # verifica se há necessidade de retornar os comandos gerados
        self.__exe = execute # varifica se é para executar os comandos gerados
        self.__req_tags = require_tags # quando ativo, aceita somente comandos com tags
        
        # define qual será o placeholder usado para diferentes bancos de dados
        self.__placeholder = {
            "sqlite": "?",
            "postgresql": "%s",
            "mysql": "%s"
        }.get(self.__dbs_type)
        
    
    def show(self):
        """retorna os atributos da classe"""
        
        attributes = {
            "dbs_type": self.__dbs_type,
            "dbs_connection_data": self.__dbs_conn_data,
            "sql_return": self.__ret_sql,
            "execute": self.__exe,
            "placeholder": self.__placeholder,
            "require_tags": self.__req_tags
        }
        
        return attributes
        
        
    def exe(self, sql_commands: str, values: Op[list]=None, type_exe="unique", require_tags=False):
        """executa comandos SQL
            Args:
                - sql_commands (str): comandos SQL
                - values (list): valores que serão adicionados nos comandos SQL. Não são obrigatórios
                - require_tags (bool): ativa ou desativa a verificação de tags manualmente"""
        
        if self.__exe:
            
            # garante que tenha as tags necessárias caso ativa
            is_safe = self.__verify_tags(sql_commands, require_tags)
            if is_safe.get("result", False):
                sql_commands = is_safe.get("cmd")
            else:
                raise ValueError("This SQL command is not valid as it does not have security tags!")
            
            with _connect_dbs(self.__dbs_type, self.__dbs_conn_data) as conn:
                cursor = conn.cursor()
                try:
                    resp = None
                    if values:
                        if type_exe == "unique":
                            resp = cursor.execute(sql_commands, values)
                        else:
                            resp = cursor.executemany(sql_commands, values)
                        
                        conn.commit()
                        return resp
                        
                    resp = cursor.execute(sql_commands)
                    return resp
                    
                except Exception as err:
                    print(err)
                    print(type(err).__name__)
                cursor.close()
                
   
    def make(self, table_name: str, **kwargs):
        """cria uma tabela sempre que não existir no banco de dado
            Args:
                - table_name (str): nome da tabela que será criada
                - **kwargs: colunas da tabela"""
        
        # garante que table_name seja uma string
        if not isinstance(table_name, str):
            raise err_make.type_error("table_name", table_name, "str")
            
        cols = []
        for key in kwargs:
            col = key + " " + " ".join(kwargs[key])
            cols.append(col)
            
        values = ", ".join(cols)
        
        sql_commands = f"**make** CREATE TABLE IF NOT EXISTS {table_name}({values});"
        
        # tenta executar os comandos SQL
        self.exe(sql_commands, require_tags=self.__req_tags)
        
        if self.__ret_sql:
            return {"sql": _remove_tags(sql_commands)}
            
    
    def add(self, table_name: str, **kwargs) -> str:
        """insere valores em uma tabela
            Args:
                - table_name (str): nome da tabela onde será inserido
                - **kwargs: colunas e valores que serão adicionados"""
        
        # garante que table_name seja uma string
        if not isinstance(table_name, str):
            raise err_add.type_error("table_name", table_name, "str")
        
        # verifica se é necessário organizar os dados
        values, columns = [], []
        if "columns" in kwargs and "values" in kwargs:
            col = kwargs["columns"]
            val = kwargs["values"]
            # garante que col = list
            if not isinstance(col, list):
                raise err_add.type_error("columns", col, "list")
            # garante que val = list
            if not isinstance(val, list):
                raise err_add.type_error("values", val, "list")
            
            columns = col
            values = val
        else:
            for column in kwargs:
                columns.append(column)
                values.append(kwargs[column])
        
        # verifica se serão mais de um registro
        type_exe = "unique"
        if isinstance(values[0], list):
            type_exe = "multiple"
            
            # impede um número diferente de colunas para valores
            for value in values:
                if len(columns) != len(value):
                    raise err_add.value_error(columns, value)
                    
        else:
            # impede um número diferente de colunas para valores
            if len(columns) != len(values):
                raise err_add.value_error(columns, values)
        
        placeholders = ", ".join([self.__placeholder for _ in columns])
        columns = ", ".join(columns)
        sql_commands = f"**add** INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        
        self.exe(sql_commands, values, type_exe)
        
        if self.__ret_sql:
            return {"sql": sql_commands}
            
        
    def get(self, table_name: str, columns: list, *args: Op[str], in_dict=True):
        """retorna dados de um banco de dados
            Args:
                table_name (str): nome da tabela
                columns (list): colunas que serão retornadas
                *args (str): parâmetros extras usados na seleção"""
        
        # garante que table_name seja uma string
        if not isinstance(table_name, str):
            raise err_get.type_error("table_name", table_name, "str")
            
        # garante que columns seja uma lista
        if not isinstance(columns, list) and columns != "all":
            raise err_get.type_error("columns", columns, "list")
            
        # garante que os valores de *args sejam str
        for arg in args:
            if not isinstance(arg, str):
                raise err_get.type_error("*args", arg, "str")
        
        col = "*"
        if columns != "all":
            col = ", ".join(columns)
        
        cond = " "+" ".join(args)
        sql_commands = f"**get**SELECT {col} FROM {table_name}{cond}".strip() + ";"
        
        result = {}
        if self.__exe:
            resp = self.exe(sql_commands).fetchall()
            
            if in_dict:
                if col == "*":
                    columns = self.cols_name(table_name)["resp"]
                    
                res_dict = _to_dict(resp, columns)
                result["resp"] = res_dict
            else:
                result["resp"] = resp
            
        
        if self.__ret_sql:
            result["sql"] = sql_commands
        
        return result
        
    
    def cols_name(self, table_name: str):
        """retorna o nome de todas as colunas de uma tabela
            Args:
                table_name (str): nome da tabela"""
                
        if not isinstance(table_name, str):
            raise TypeError("(cols_name()) table_name requires a string")
            
        resp = self.exe(f"PRAGMA table_info({table_name});").fetchall()
        
        columns = []
        for column in resp:
            columns.append(column[1])
        
        return {"resp": columns}
        
    
    def edit(self, table_name: str, *args, **kwargs):
        """atualiza um dado no tabela usando o comando UPDATE
            Args:
                table_name (str): nome da tabela
                *args (str): condições para consulta e atualização
                **kwargs (str): colunas = valores"""
                
        #garante que table_name seja str
        if not isinstance(table_name, str):
            raise err_edit.type_error("table_name", table_name, "str")
            
        # garante que *args seja str
        for arg in args:
            if not isinstance(arg, str):
                raise err_edit.type_error("*args", arg, "str")
        
        # garante que kwargs seja dict
        if not isinstance(kwargs, dict):
            raise err_edit.value_error(kwargs)
        
        values = []
        for key in kwargs:
            values.append(f"{key} = '{kwargs[key]}'")
        setter = ", ".join(values)
        
        cond = " "+" ".join(args)
        
        sql_commands = f"**edit** UPDATE {table_name} SET {setter}{cond.strip()};"
        
        if self.__exe:
            self.exe(sql_commands)
        
        if self.__ret_sql:
            return {"sql": f"{sql_commands}"}
    
    
    def __verify_tags(self, cmd: str, require_tags):
        """verifica se o comando possui as tags exigidas para evitar Injeção de SQL (caso o atributo __req_tags=True)
            Args:
                cmd (str): comando que será executado"""
        
        types = ["SELECT", "CREATE", "DELETE", "UPDATE", "INSERT"]
        
        # caso o atributo require_tags=True
        if require_tags:
            cmd_type = None
            for type in types:
                if type in cmd[:15]:
                    cmd_type = type.lower()
            
            if cmd_type == None:
                return {"result": False}
            
            is_safe = _req_tags(cmd, cmd_type)
            
            if is_safe.get("result", False):
                return is_safe
            return {"result": False}
        else:
            return {"result": True, "cmd": _remove_tags(cmd)}
    

# ignore
def main():
    print(__doc__)

