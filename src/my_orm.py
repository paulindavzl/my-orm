import webbrowser
from time import sleep
from os import system
from random import uniform
from typing import Optional as Op
from SQL.sql_commands_create import *
from SQL.sql_commands_prop import *
from SQL.sql_commands_cond import *
from SQL.sql_commands_alter_table import *
from SQL.manager import _connect_dbs
from utils import doc_link
from utils.convert import _to_dict
from utils.verify_tags import _requirements_tags as _req_tags, _remove_tags
from utils.validate import _is_valid_dbs_data

class MyORM:
    
    def __init__(self, sql_return: Op[bool]=False, execute: Op[bool]=True, return_dict: Op[bool]=True, require_tags: Op[bool]=True, alter_all: Op[bool]=False, **dbs_data):
        self.__dbs_data = dbs_data # dados do banco de dados
        self.__ret_sql = sql_return # verifica se há necessidade de retornar os comandos gerados
        self.__exe = execute # varifica se é para executar os comandos gerados
        self.__req_tags = require_tags # quando ativo, aceita somente comandos com tags
        self.__alter_all = alter_all # quando False impede alterar dados sem condições
        
        # define qual será o placeholder usado para diferentes bancos de dados
        self.__placeholder = {
            "sqlite": "?",
            "postgres": "%s",
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
                raise ValueError(f"Some information is missing to connect to the database ({result.get('missing')}). {doc_link()}")
            
            # garante que tenha as tags necessárias caso ativa
            is_safe = self.__verify_tags(sql_commands, require_tags)
            if is_safe.get("result", False):
                sql_commands = is_safe.get("cmd")
            else:
                raise ValueError(f"This SQL command is not valid as it does not have security tags! {doc_link()}")
            
            dbs = self.__dbs_data.get("dbs", "sqlite")
            
            with _connect_dbs(self.__dbs_data) as conn:
                
                if dbs == "postgres":
                    sql_commands = sql_commands.replace("AUTO_INCREMENT", "SERIAL")
                
                cursor = conn.cursor()
                resp = None
                
                if values:
                    if type_exe == "unique":
                        cursor.execute(sql_commands, values)
                    else:
                        cursor.executemany(sql_commands, values)
                        
                else:     
                    cursor.execute(sql_commands)
                
                if dbs == "postgres":
                    conn.commit()
                    try:
                        return cursor.fetchall()
                    except:
                        return cursor
                else:
                    try:
                        conn.commit()
                    except:
                        pass
                    return cursor.fetchall()
                
                
   
    def make(self, table_name: str, **kwargs): 
        if not isinstance(table_name, str):
            raise TypeError(f"(MyORM.make()) table_name expected a str value, but received a {type(table_name).__name__} ({table_name}). {doc_link()}")
            
        fkey = kwargs.get("f_key")
        if fkey != None and not isinstance(fkey, tuple):
            raise TypeError(f"(MyORM.make()) f_key expected a str value, but received a {type(fkey).__name__} ({fkey}). {doc_link()}")
        elif fkey != None and len(fkey) < 2:
            raise ValueError(f"(MyORM.make()) f_key must have at least 2 values ​​(foreign key + primary key). {doc_link()}")
            
        f_key = None
        if fkey != None:
            kwargs.pop("f_key")
            f_key = for_key(
                fkey[0], 
                fkey[1], 
                fkey[2] if len(fkey) >= 3 else "", 
                fkey[3] if len(fkey) >= 4 else ""
            )
        cols = []
        for key in kwargs:
            if isinstance(kwargs[key], str):
                kwargs[key] = [kwargs[key]]
            col = key + " " + " ".join(list(kwargs[key]))
            cols.append(col)
            
        values = ", ".join(cols)
        sql_commands = f"**make** CREATE TABLE IF NOT EXISTS {table_name}({values}){' '+f_key if f_key != None else ''};"
        
        # tenta executar os comandos SQL
        if self.__exe:
            self.exe(sql_commands)
        
        if self.__ret_sql:
            return {"sql": _remove_tags(sql_commands)}
           
    
    def add(self, table_name: str, **kwargs) -> str:
        if not isinstance(table_name, str):
            raise TypeError(f"(MyORM.add()) table_name expected a str value, but received a {type(table_name).__name__} ({table_name}). {doc_link()}")
        
        # verifica se é necessário organizar os dados
        values, columns = [], []
        if "columns" in kwargs and "values" in kwargs:
            col = kwargs["columns"]
            val = kwargs["values"]
            
            if not isinstance(col, list):
                raise TypeError(f"(MyORM.add()) columns expected a list value, but received a {type(col).__name__} ({col}). {doc_link()}")
            if not isinstance(val, list):
                raise TypeError(f"(MyORM.add()) values expected a list value, but received a {type(val).__name__} ({val}). {doc_link()}")
            
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
                    raise ValueError(f"(MyORM.add()) The number of values ​​in columns ({len(columns)}) and values ({len(values)}) ​​is different! {doc_link()}")
                    
        else:
            # impede um número diferente de colunas para valores
            if len(columns) != len(values):
                raise ValueError(f"(MyORM.add()) The number of values ​​in columns ({len(columns)}) and values ({len(values)}) ​​is different! {doc_link()}")
        
        placeholders = ", ".join([self.__placeholder for _ in columns])
        columns = ", ".join(columns)
        sql_commands = f"**add** INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        
        self.exe(sql_commands, values, type_exe)
        
        if self.__ret_sql:
            return {"sql": _remove_tags(sql_commands)}
            
        
    def get(self, table_name: str, columns: Op[list]="all", *args: Op[str], in_dict=True):
        if not isinstance(table_name, str):
            raise TypeError(f"(MyORM.get()) table_name expected a str value, but received a {type(table_name).__name__} ({table_name}). {doc_link()}")
        if not isinstance(columns, list) and columns != "all":
            raise TypeError(f"(MyORM.get()) columns expected a list value, but received a {type(columns).__name__} ({columns}). {doc_link()}")
        for arg in args:
            if not isinstance(arg, str):
                raise TypeError(f"(MyORM.get()) *args expected a str value, but received a {type(arg).__name__} ({arg}). {doc_link()}")
        
        col = "*"
        if columns != "all":
            col = ", ".join(columns)
        
        cond = " "+" ".join(args)
        sql_commands = f"**get** SELECT {col} FROM {table_name}{cond}".strip() + ";"
        
        result = {}
        if self.__exe:
            resp = self.exe(sql_commands)
            
            if in_dict:
                if col == "*":
                    columns = self.cols_name(table_name)["resp"]
                
                res_dict = _to_dict(resp, columns)
                result["resp"] = res_dict
            else:
                result["resp"] = resp
            
        
        if self.__ret_sql:
            result["sql"] = _remove_tags(sql_commands)
        
        return result
        
    
    def cols_name(self, table_name: str):
        if not isinstance(table_name, str):
            raise TypeError("(MyORM.cols_name()) table_name requires a string")
            
        dbs = self.__dbs_data.get("dbs", "sqlite")
        
        cmd = {
            "sqlite": f"PRAGMA table_info({table_name});",
            "mysql": f"SHOW COLUMNS FROM {table_name};",
            "postgres": f"""SELECT column_name FROM information_schema.columns WHERE table_name = {table_name};"""
        }
        
        index = {
            "sqlite": 1,
            "mysql": 0,
            "postgres": 0
        }
        
        resp = self.exe(cmd.get(dbs).replace('"', "'"), require_tags=False)
        
        columns = []
        for column in resp:
            columns.append(column[index.get(dbs)])
        
        return {"resp": columns}
        
    
    def edit(self, table_name: str, *args, all: Op[bool]=None, **kwargs):
        # o atributo all impede que todos os dados sejam editados de uma vez, desde que all=True
        
        if all == None:
            all = self.__alter_all
            
        if not isinstance(table_name, str):
            raise TypeError(f"(MyORM.edit()) table_name expected a str value, but received a {type(table_name).__name__} ({table_name}). {doc_link()}")
        for arg in args:
            if not isinstance(arg, str):
                raise TypeError(f"(MyORM.edit()) *args expected a str value, but received a {type(arg).__name__} ({arg}). {doc_link()}")
        if not isinstance(all, bool):
            raise TypeError(f"(MyORM.edit()) all expected a bool value, but received a {type(all).__name__} ({all}). {doc_link()}")
        
        values = []
        for key in kwargs:
            values.append(f"{key} = '{kwargs[key]}'")
        setter = ", ".join(values)
        
        cond = " "+" ".join(args)
        
        sql_commands = f"**edit** UPDATE {table_name} SET {setter} {cond.strip()};"
        
        if not "WHERE" in sql_commands and not all:
            raise ValueError(f"For security, the WHERE condition is mandatory. {doc_link()}")
        
        if self.__exe:
            self.exe(sql_commands)
        
        if self.__ret_sql:
            return {"sql": _remove_tags(sql_commands)}
    
    
    def __verify_tags(self, cmd: str, require_tags):
        types = ["SELECT", "CREATE", "DELETE", "UPDATE", "INSERT", "ALTER TABLE"]
        # caso o atributo require_tags=True
        if require_tags:
            cmd_type = None
            for type in types:
                if type in cmd[:15] or type in cmd[10:17] or type in cmd[10:21]:
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
            raise TypeError(f"(MyORM.remove()) table_name expected a str value, but received a {type(table_name).__name__} ({table_name}). {doc_link()}")
        elif not isinstance(all, bool):
            raise TypeError(f"(MyORM.remove()) all expected a bool value, but received a {type(all).__name__} ({all}). {doc_link()}")
        else:
            for arg in args:
                if not isinstance(arg, str):
                    raise TypeError(f"(MyORM.remove()) *args expected a str value, but received a {type(arg).__name__} ({arg}). {doc_link()}")
            
        
        cond = " ".join(args)
        sql_command = f"**remove** DELETE FROM {table_name} {cond};"
        
        if not "WHERE" in sql_command and not all:
            raise ValueError(f"For security, the WHERE condition is mandatory. {doc_link()}")
        
        if self.__exe:
            self.exe(sql_command)
                
        if self.__ret_sql:
            return {"sql": _remove_tags(sql_command)}
            
    
    def edit_table(self, table_name: str, *args: str):
        if not isinstance(table_name, str):
            raise TypeError(f"(MyORM.edit_table()) table_name expected a value str, but received a {type(table_name)} ({table_name}). {doc_link()}")
        for arg in args:
            if not isinstance(arg, str) and not isinstance(arg, list):
                raise TypeError(f"(MyORM.edit_table()) *args expected a str/list value, but received a {type(arg).__name__} ({arg}). {doc_link()}")
        
        base_cmd = f"**altab** ALTER TABLE {table_name} "
        for arg in args:
            if isinstance(arg, tuple) or isinstance(arg, list):
                for block in arg:
                    sql_command = " ".join((base_cmd, block))
                    if self.__exe:
                        self.exe(sql_command)
            else:
                alt = " ".join(args)
                sql_command = base_cmd + alt
                
                if self.__exe:
                    self.exe(sql_command)
                
                if self.__ret_sql:
                    return {"sql": _remove_tags(sql_command)}
                
                
                    
        
    

# ignore
def main():
    system("clear")
    print("Documentation for this project is available at: https://github.com/paulindavzl/my-orm.\n Opening...")
    sleep(uniform(0, 1.5))
    system("clear")
    webbrowser.open("https://github.com/paulindavzl/my-orm")
    sleep(0.5)
    print("Documentation for this project is available at: https://github.com/paulindavzl/my-orm.")
    