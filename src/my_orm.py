"""
Este módulo realiza a conexão com um banco de dados e facilita a manipulação de comandos SQL!

Classes:
    - MyORM: classe responsável por gerenciar a conexão com bancos de dados e fornecer métodos para manipulação de comandos SQL
    
Methods:
    - MyORM.create(): cria uma tabela no banco de dados caso ela não exista
    - MyORM.insert(): insere valores em uma tabela
    - MyORM.execute(): executa comandos SQL
    - MyORM.show(): retornar todos os atributos da classe
    
Requirements:
    - from typing import Optional: suporte para tipos opcionais
    - from SQL.sql_commands_create import *: funções para criar tabelas
    - from SQL.sql_commands_prop import *: funções para adicionar propriedades nas tabelas
    - from SQL.manager import _connect_dbs: função para conectar-se ao banco de dados 
    - from exceptions import errors_insert
"""

from typing import Optional as Op
from SQL.sql_commands_create import *
from SQL.sql_commands_prop import *
from SQL.manager import _connect_dbs
from exceptions import errors_method_insert as err_in, errors_method_create as err_cr

class MyORM:
    """classe geral da ORM, gerencia todos os métodos
        Attributes:
            - __dbs_type (Optional[str]): tipo de banco de dados (ex: SQLite, MySQL...)
            - __dbs_conn_data (Optional[dict]): dados necessários para conectar-se ao banco de dados
            - __dbs_return (Optional[bool]): caso True, retorna o comando SQL gerado
            - __exe (Optional[bool]): caso True, executa os comandos gerados
            
        Methods:
            - create(table_name: str, *args: str): cria uma tabela sempre que não existir
            - execute(sql_commands: str, values: Optional[list]=None): executa comandos SQL
            - show(): retorna os atributos da classe"""
    
    def __init__(self, dbs_type: Op[str]=None, dbs_connection_data: Op[dict]=None, sql_return: Op[bool]=False, execute: Op[bool]=True):
        self.__dbs_type = dbs_type # tipo de banco de dados (SQLite, MySQL...)
        self.__dbs_conn_data = dbs_connection_data # dados para conexão com banco de dados (servidor, user...)
        self.__sql_return = sql_return # verifica se há necessidade de retornar os comandos gerados
        self.__exe = execute # varifica se é para executar os comandos gerados
        
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
        
        
    def execute(self, sql_commands: str, values: Op[list]=None, type="unique"):
        """executa comandos SQL
            Args:
                - sql_commands (str): comandos SQL
                - values (list): valores que serão adicionados nos comandos SQL. Não são obrigatórios"""
        
        if self.__exe:
            with _connect_dbs(self.__dbs_type, self.__dbs_conn_data) as conn:
                cursor = conn.cursor()
                if values:
                    if type == "unique":
                        cursor.execute(sql_commands, values)
                    else:
                        cursor.executemany(sql_commands, values)
                    
                    conn.commit()
                else:
                    cursor.execute(sql_commands)
                cursor.close()
        
        
    def create(self, table_name: str, *args: str) -> str:
        """cria uma tabela sempre que não existir no banco de dado
            Args:
                - table_name (str): nome da tabela que será criada
                - *args: série de comandos SQL gerado por funções"""
        
        # garante que table_name seja uma string
        if not isinstance(table_name, str):
            err_cr.type_error("table_name", table_name, "str")
            
        # garante que os valores de *args sejam strings
        for arg in args:
            if not isinstance(arg, str):
                err_cr.type_error("*args", arg, "str")
        
        values = ",\n".join(args)
        sql_commands = f"CREATE TABLE IF NOT EXISTS {table_name}(\n{values}\n);"
        
        # tenta executar os comandos SQL
        self.execute(sql_commands)
        
        if self.__sql_return:
            return {"sql": sql_commands}
            
    
    def insert(self, table_name: str, values: list, *args: str) -> str:
        """insere valores em uma tabela
            Args:
                - table_name (str): nome da tabela onde será inserido
                - values (list): valores que serão inseridos
                - *args (str): colunas da tabela que serão usadas"""
        
        # garante que table_name seja uma string
        if not isinstance(table_name, str):
            err_in.type_error("table_name", table_name, "str")
            
        # garante que values seja uma lista de valores
        if not isinstance(values, list):
            err_in.type_error("values", values, "list")
            
        # garante que *args seja composto por strings
        for arg in args:
            if not isinstance(arg, str):
                err_in.type_error_args(arg)
        
        # verifica se serão mais de um registro
        type_exe = "unique"
        if isinstance(values[0], list):
            type_exe = "multiple"
            
            # impede um número diferente de colunas para valores
            for value in values:
                if len(args) != len(value):
                    err_in.value_erro(args, value)
                    
        else:
            # impede um número diferente de colunas para valores
            if len(args) != len(values):
                err_in.value_error(args, values)
        
        placeholders = ", ".join([self.__placeholder for _ in args])
        columns = ", ".join(args)
        sql_commands = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        
        self.execute(sql_commands, values, type_exe)
        
        if self.__sql_return:
            return sql_commands
    
            

# ignore
def main():
    print(__doc__)

