import pytest
from my_orm import *


# dados de conexão
@pytest.fixture
def data():
    return {"url": "test.db"}


# instância da classe MyORM
@pytest.fixture
def orm(data):
    return MyORM("sqlite", data, True, False)

def test_method_create(orm):
    """testa o método para criar tabelas"""
    
    expected_return = """CREATE TABLE IF NOT EXISTS table(
column1 INTEGER NOT NULL PRIMARY KEY,
column2 VARCHAR(25) NOT NULL,
column3 VARCHAR(15) UNIQUE NOT NULL,
FOREIGN KEY (uid) REFERENCES table(id) ON UPDATE CASCADE ON DELETE SET NULL
);"""
    
    assert orm.make(
        "table",
        integer("column1", prop("n_null", "pri_key")),
        varchar("column2", 25, prop("n_null")),
        varchar("column3", 15, prop("uni", "n_null")),
        foreign_key("uid", "table(id)", on_up("cascade"), on_del("set null"))
    ).get("sql") == expected_return
    

def test_method_show(orm, data):
    """testa o método que retorna os atributos da classe"""
    
    expected_return = {
        "dbs_type": "sqlite",
        "dbs_connection_data": data,
        "sql_return": True,
        "execute": False,
        "placeholder": "?"
    }
    
    assert orm.show() == expected_return
    

def test_method_insert(orm):
    """testa o método para inserir registros na tabela"""
    
    expected_return = """INSERT INTO table (column1, column2) VALUES (?, ?)"""
    
    assert orm.add("table", ["value1", "value2"], "column1", "column2").get("sql") == expected_return
    

def test_method_select(orm):
    """testa o método para selecionar registros na tabela"""
    
    expected_return = "SELECT * FROM table;"
    
    assert orm.get("table", "all").get("sql") == expected_return


if __name__ == "__main__":
    pytest.main(["-vv", "test_my_orm.py"])