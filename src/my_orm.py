from typing import Optional as Op
from SQL.sql_commands_create import *
from SQL.sql_commands_prop import *
from SQL.sql_commands_cond import *
from SQL.manager import _connect_dbs
from utils.convert import _to_dict
from utils.verify_tags import _requirements_tags as _req_tags, _remove_tags
from utils.validate import _is_valid_dbs_data
from exceptions import errors_method_insert as err_add, errors_method_create as err_make, errors_method_select as err_get, errors_method_update as err_edit, errors_method_delete as err_remove

class MyORM:
    
    def __init__(self, sql_return: Op[bool]=False, execute: Op[bool]=True, return_dict: Op[bool]=True, require_tags: Op[bool]=True, alter_all: Op[bool]=False, **dbs_data):
        self.__dbs_data = dbs_data # dados do banco de dados
        self.__ret_sql = sql_return # verifica se há necessidade de retornar os comandos gerados
        self.__exe = execute # varifica se é para executar os comandos gerados
        self.__req_tags = require_tags # quando ativo, aceita somente comandos com tags
        self.__alter_all = alter_all # quando False impeder alterar dados sem condições
        
        # define qual será o placeholder usado para diferentes bancos de dados
        self.__placeholder = {
            "sqlite": "?",
            "postgresql": "%s",
            "mysql": "%s"
        }.get(self.__dbs_data.get("dbs", "sqlite"))
        
    
    def show(self):   
        attributes = {
            "dbs_data": self.__dbs_data,
            "sql_return": self.__ret_sql,
            "execute": self.__exe,
            "placeholder": self.__placeholder,
            "require_tags": self.__req_tags,
            "alter_all": self.__alter_all
        }
        
        return attributes
        
        
    def exe(self, sql_commands: str, values: Op[list]=None, type_exe="unique", require_tags=None):
        if require_tags == None:
            require_tags = self.__req_tags
        
        if self.__exe:
            result = _is_valid_dbs_data(self.__dbs_data)
            if not result.get("result"):
                raise ValueError(f"Some information is missing to connect to the database ({result.get('missing')}). See the documentation at https://github.com/paulindavzl/my-orm")
            
            # garante que tenha as tags necessárias caso ativa
            is_safe = self.__verify_tags(sql_commands, require_tags)
            if is_safe.get("result", False):
                sql_commands = is_safe.get("cmd")
            else:
                raise ValueError("This SQL command is not valid as it does not have security tags!")
            
            with _connect_dbs(self.__dbs_data) as conn:
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
        if not isinstance(table_name, str):
            raise err_make.type_error("table_name", table_name, "str")
            
        fkey = kwargs.get("f_key")
        kwargs.pop("f_key")
        if fkey != None and not isinstance(fkey, tuple):
            raise err_make.type_error("f_key", fkey, "tuple")
        elif fkey != None and len(fkey) < 2:
            raise err_make.value_error("f_key", fkey, "2 or more")
            
        f_key = None
        if fkey != None:
            f_key = for_key(
                fkey[0], 
                fkey[1], 
                fkey[2] if len(fkey) >= 3 else "", 
                fkey[3] if len(fkey) >= 4 else ""
            )
        cols = []
        for key in kwargs:
            col = key + " " + " ".join(kwargs[key])
            cols.append(col)
            
        values = ", ".join(cols)
        sql_commands = f"**make** CREATE TABLE IF NOT EXISTS {table_name}({values}){' '+f_key if f_key != None else ''};"
        
        # tenta executar os comandos SQL
        if self.__exe:
            self.exe(sql_commands)
        
        if self.__ret_sql:
            return {"sql": _remove_tags(sql_commands)}
           
    
    def add(self, table_name: str, **kwargs) -> str:
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
            
        
    def get(self, table_name: str, columns: Op[list]="all", *args: Op[str], in_dict=True):
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
        sql_commands = f"**get** SELECT {col} FROM {table_name}{cond}".strip() + ";"
        
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
        if not isinstance(table_name, str):
            raise TypeError("(cols_name()) table_name requires a string")
            
        resp = self.exe(f"PRAGMA table_info({table_name});", require_tags=False).fetchall()
        
        columns = []
        for column in resp:
            columns.append(column[1])
        
        return {"resp": columns}
        
    
    def edit(self, table_name: str, *args, all: Op[bool]=None, **kwargs):
        # o atributo all impede que todos os dados sejam editados de uma vez, desde que all=True
        
        if all == None:
            all = self.__alter_all
            
        if not isinstance(table_name, str):
            raise err_edit.type_error("table_name", table_name, "str")
        for arg in args:
            if not isinstance(arg, str):
                raise err_edit.type_error("*args", arg, "str")
        if not isinstance(all, bool):
            raise err_edit.type_error("all", all, "bool")
        if not isinstance(kwargs, dict):
            raise err_edit.value_error(kwargs)
        
        values = []
        for key in kwargs:
            values.append(f"{key} = '{kwargs[key]}'")
        setter = ", ".join(values)
        
        cond = " "+" ".join(args)
        
        sql_commands = f"**edit** UPDATE {table_name} SET {setter} {cond.strip()};"
        
        if not "WHERE" in sql_commands and not all:
            raise ValueError("For security, the WHERE condition is mandatory. See the documentation at https://github.com/paulindavzl/my-orm")
        
        if self.__exe:
            self.exe(sql_commands)
        
        if self.__ret_sql:
            return {"sql": f"{sql_commands}"}
    
    
    def __verify_tags(self, cmd: str, require_tags):
        types = ["SELECT", "CREATE", "DELETE", "UPDATE", "INSERT"]
        
        # caso o atributo require_tags=True
        if require_tags:
            cmd_type = None
            for type in types:
                if type in cmd[:15] or type in cmd[10:17]:
                    cmd_type = type.lower()
            
            if cmd_type == None:
                return {"result": False}
            
            is_safe = _req_tags(cmd, cmd_type)
            
            if is_safe.get("result", False):
                return is_safe
            return {"result": False}
        else:
            return {"result": True, "cmd": _remove_tags(cmd)}
            
    
    def remove(self, table_name: str, *args: str, all: Op[bool]=None):
        # o atributo all impede que todos os dados sejam editados de uma vez, desde que all=True
        
        if all == None:
            all = self.__alter_all
        
        if not isinstance(table_name, str):
            raise err_remove.type_error("table_name", table_name, "str")
        elif not isinstance(all, bool):
            raise err_remove.type_error("all", all, "bool")
        else:
            for arg in args:
                if not isinstance(arg, str):
                    raise err_remove.type_error("*args", arg, "str")
            
        
        cond = " ".join(args)
        sql_command = f"**remove** DELETE FROM {table_name} {cond};"
        
        if not "WHERE" in sql_command and not all:
            raise ValueError("For security, the WHERE condition is mandatory. See the documentation at https://github.com/paulindavzl/my-orm")
        
        if self.__exe:
            self.exe(sql_command)
                
        if self.__ret_sql:
            return {"sql": sql_command}
    

# ignore
def main():
    print(__doc__)

