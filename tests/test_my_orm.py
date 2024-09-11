import pytest
from my_orm import *

def test_method_create():
    """testa o método para criar tabelas"""
    
    orm = MyORM(sql_return=True, execute=False)
    expected_return = """CREATE TABLE IF NOT EXISTS table(
column1 INTEGER NOT NULL PRIMARY KEY,
column2 VARCHAR(25) NOT NULL,
column3 VARCHAR(15) UNIQUE NOT NULL,
FOREIGN KEY (uid) REFERENCES table(id) ON UPDATE CASCADE ON DELETE SET NULL
);"""
    
    assert orm.create(
        "table",
        integer("column1", prop("n_null", "pri_key")),
        varchar("column2", 25, prop("n_null")),
        varchar("column3", 15, prop("uni", "n_null")),
        foreign_key("uid", "table(id)", on_up("cascade"), on_del("set null"))
    ).get("sql") == expected_return
    

def test_method_show():
    """testa o método que retorna os atributos da classe"""
    
    data = {"url": "./database/sqlite.db"}
    orm = MyORM("sqlite", data, True, False)
    expected_return = {
        "dbs_type": "sqlite",
        "dbs_connection_data": data,
        "sql_return": True,
        "execute": False
    }
    
    assert orm.show() == expected_return


if __name__ == "__main__":
    pytest.main(["-vv", "test_my_orm.py"])