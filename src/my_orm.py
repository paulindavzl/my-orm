"""
Este módulo realiza a conexão com um banco de dados e facilita a manipulação de comandos SQL!

Classes:
    - MyORM: classe responsável por gerenciar a conexão com bancos de dados e fornecer métodos para manipulação de comandos SQL
    
Methods:
    - MyORM.create(): cria uma tabela no banco de dados caso ela não exista
    - MyORM.execute(): executa comandos SQL
    
Requirements:
    - from typing import Optional: suporte para tipos opcionais
    - from SQL.sql_commands_create import *: funções para criar tabelas
    - from SQL.sql_commands_prop import *: funções para adicionar propriedades nas tabelas
    - from SQL.manager import _connect_dbs: função para conectar-se ao banco de dados 
"""

from typing import Optional as Op
from SQL.sql_commands_create import *
from SQL.sql_commands_prop import *
from SQL.manager import _connect_dbs

class MyORM:
    """classe geral da ORM, gerencia todos os métodos
        Attributes:
            - __dbs_type (Optional[str]): tipo de banco de dados (ex: SQLite, MySQL...)
            - __dbs_conn_data (Optional[dict]): dados necessários para conectar-se ao banco de dados
            - __dbs_return (Optional[bool]): caso True, retorna o comando SQL gerado
            
        Methods:
            - create(table_name: str, *args: str): cria uma tabela sempre que não existir
            - execute(sql_commands: str, values: Optional[list]=None): executa comandos SQL"""
    
    def __init__(self, dbs_type: Op[str]=None, dbs_connection_data: Op[dict]=None, sql_return: Op[bool]=True):
        self.__dbs_type = dbs_type # tipo de banco de dados (SQLite, MySQL...)
        self.__dbs_conn_data = dbs_connection_data # dados para conexão com banco de dados (servidor, user...)
        self.__sql_return = sql_return # verifica se há necessidade de retornar os comandos gerados
        
        
    def execute(self, sql_commands: str, values: Op[list]=None):
        """executa comandos SQL
            Args:
                - sql_commands (str): comandos SQL
                - values (list): valores que serão adicionados nos comandos SQL. Não são obrigatórios"""
                
        with _connect_dbs(self.__dbs_type, self.__dbs_conn_data) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_commands)
            cursor.close()
        
        
    def create(self, table_name: str, *args: str) -> str:
        """cria uma tabela sempre que não existir no banco de dado
            Args:
                - table_name (str): nome da tabela que será criada
                - *args: série de comandos SQL gerado por funções"""
        
        values = ",\n".join(args)
        sql_commands = f"CREATE TABLE IF NOT EXISTS {table_name}(\n{values}\n);"
        
        # tenta executar os comandos SQL
        self.execute(sql_commands)
        
        if self.__sql_return:
            return {"sql": sql_commands}
            

# ignore
def main():
    print(__doc__)

if __name__ == "__main__":
    my_orm = MyORM("sqlite", {"url": "./sqlite.db"})
    my_orm.create(
        "people", 
        integer("id", prop("uni", "n_null", "pri_key")),
        varchar("name", 30, prop("n_null"))
    )
