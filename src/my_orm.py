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
    - from SQL.sql_commands_select import *: funções para condicionar SELECT
    - from SQL.manager import _connect_dbs: função para conectar-se ao banco de dados 
    - from utils.convert import _to_dict: função que converte dados em listas
    - from exceptions import errors_method_insert as err_ins, errors_method_create as err_cre, errors_method_select as err_sel
"""

from typing import Optional as Op
from SQL.sql_commands_create import *
from SQL.sql_commands_prop import *
from SQL.sql_commands_cond import *
from SQL.manager import _connect_dbs
from utils.convert import _to_dict
from exceptions import errors_method_insert as err_ins, errors_method_create as err_cre, errors_method_select as err_sel

class MyORM:
    """classe geral da ORM, gerencia todos os métodos
        Attributes:
            - __dbs_type (Optional[str]): tipo de banco de dados (ex: SQLite, MySQL...)
            - __dbs_conn_data (Optional[dict]): dados necessários para conectar-se ao banco de dados
            - __dbs_return (Optional[bool]): caso True, retorna o comando SQL gerado
            - __exe (Optional[bool]): caso True, executa os comandos gerados
            - __return_dict (Optional[bool]): quando True, retorna as consultas em dicionários
            
        Methods:
            - make(table_name: str, *args: str): cria uma tabela sempre que não existir
            - add(self, table_name: str, values: list, *args: str): insere registros em uma tabela
            - get(self, table_name: str, columns: list, ret_dict: Op[dict]=True, *args: Op[str]): retorna dados de uma tabela
            - exe(sql_commands: str, values: Optional[list]=None): executa comandos SQL
            - show(): retorna os atributos da classe
            - cols_name(table_name: str): retorna o nome das colunas de uma tabela"""
    
    def __init__(self, dbs_type: Op[str]=None, dbs_connection_data: Op[dict]=None, sql_return: Op[bool]=False, execute: Op[bool]=True, return_dict: Op[bool]=True):
        self.__dbs_type = dbs_type # tipo de banco de dados (SQLite, MySQL...)
        self.__dbs_conn_data = dbs_connection_data # dados para conexão com banco de dados (servidor, user...)
        self.__sql_return = sql_return # verifica se há necessidade de retornar os comandos gerados
        self.__exe = execute # varifica se é para executar os comandos gerados
        self.__return_dict = return_dict # quando true, o retorno das consultas serão em dicionário
        
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
            "sql_return": self.__sql_return,
            "execute": self.__exe,
            "placeholder": self.__placeholder
        }
        
        return attributes
        
        
    def exe(self, sql_commands: str, values: Op[list]=None, type_exe="unique"):
        """executa comandos SQL
            Args:
                - sql_commands (str): comandos SQL
                - values (list): valores que serão adicionados nos comandos SQL. Não são obrigatórios"""
        
        if self.__exe:
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
        
        
    def make(self, table_name: str, *args: str) -> str:
        """cria uma tabela sempre que não existir no banco de dado
            Args:
                - table_name (str): nome da tabela que será criada
                - *args: série de comandos SQL gerado por funções"""
        
        # garante que table_name seja uma string
        if not isinstance(table_name, str):
            raise err_cre.type_error("table_name", table_name, "str")
            
        # garante que os valores de *args sejam strings
        for arg in args:
            if not isinstance(arg, str):
                raise err_cre.type_error("*args", arg, "str")
        
        values = ",\n".join(args)
        sql_commands = f"CREATE TABLE IF NOT EXISTS {table_name}(\n{values}\n);"
        
        # tenta executar os comandos SQL
        self.exe(sql_commands)
        
        if self.__sql_return:
            return {"sql": sql_commands}
            
    
    def add(self, table_name: str, values: list, *args: str) -> str:
        """insere valores em uma tabela
            Args:
                - table_name (str): nome da tabela onde será inserido
                - values (list): valores que serão inseridos
                - *args (str): colunas da tabela que serão usadas"""
        
        # garante que table_name seja uma string
        if not isinstance(table_name, str):
            raise err_ins.type_error("table_name", table_name, "str")
            
        # garante que values seja uma lista de valores
        if not isinstance(values, list):
            raise err_ins.type_error("values", values, "list")
            
        # garante que *args seja composto por strings
        for arg in args:
            if not isinstance(arg, str):
                raise err_ins.type_error_args(arg)
        
        # verifica se serão mais de um registro
        type_exe = "unique"
        if isinstance(values[0], list):
            type_exe = "multiple"
            
            # impede um número diferente de colunas para valores
            for value in values:
                if len(args) != len(value):
                    raise err_ins.value_erro(args, value)
                    
        else:
            # impede um número diferente de colunas para valores
            if len(args) != len(values):
                raise err_ins.value_error(args, values)
        
        placeholders = ", ".join([self.__placeholder for _ in args])
        columns = ", ".join(args)
        sql_commands = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        
        self.exe(sql_commands, values, type_exe)
        
        if self.__sql_return:
            return {"sql": adj_(sql_commands)}
            
        
    def get(self, table_name: str, columns: list, *args: Op[str]):
        """retorna dados de um banco de dados
            Args:
                table_name (str): nome da tabela
                columns (list): colunas que serão retornadas
                *args (str): parâmetros extras usados na seleção"""
        
        # garante que table_name seja uma string
        if not isinstance(table_name, str):
            raise err_sel.type_error("table_name", table_name, "str")
            
        # garante que columns seja uma lista
        if not isinstance(columns, list) and columns != "all":
            raise err_sel.type_error("columns", columns, "list")
            
        # garante que os valores de *args sejam str
        for arg in args:
            if not isinstance(arg, str):
                raise err_sel.type_error("*args", arg, "str")
        
        col = "*"
        if columns != "all":
            col = ", ".join(columns)
        
        cond = " "+" ".join(args)
        sql_commands = adj_(f"SELECT {col} FROM {table_name}{cond}").strip() + ";"
        
        result = {}
        if self.__exe:
            resp = self.exe(sql_commands).fetchall()
            
            if self.__return_dict:
                if col == "*":
                    columns = self.cols_name(table_name)["resp"]
                    
                res_dict = _to_dict(resp, columns)
                result["resp"] = res_dict
            else:
                result["resp"] = resp
            
        
        if self.__sql_return:
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
    
            

# ignore
def main():
    print(__doc__)
