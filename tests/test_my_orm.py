import pytest
import re
from my_orm import *

# instância da classe MyORM
@pytest.fixture
def orm():
    orm = MyORM(sql="sqlite", url="./dbs.db", sql_return=True, execute=False)
    return orm

def test_method_create(orm):
    expected_return = """CREATE TABLE IF NOT EXISTS table(column1 INTEGER NOT NULL PRIMARY KEY, column2 VARCHAR(25) NOT NULL, column3 VARCHAR(15) UNIQUE NOT NULL) FOREIGN KEY (uid) REFERENCES table(id) ON UPDATE CASCADE ON DELETE SET NULL;"""
    
    resp = orm.make(
        "table",
        column1 = (integer(), prop("n_null", "pri_key")),
        column2 = (varchar(25), prop("n_null")),
        column3 = (varchar(15), prop("uni", "n_null")),
        f_key=("uid", "table(id)", on_up("cascade"), on_del("set null"))
    ).get("sql")
    
    assert expected_return == resp
    

def test_method_show(orm):
    expected_return = {
        "dbs_data": {"sql": "sqlite", "url": "./dbs.db"},
        "sql_return": True,
        "execute": False,
        "placeholder": "?",
        "require_tags": True,
        "alter_all": False
    }
    
    resp = orm.show()
    
    assert resp == expected_return
    

def test_method_add_multiple(orm):
    expected_return = """INSERT INTO table (column1, column2) VALUES (?, ?)"""
    
    resp = orm.add(
        "table",
        columns = ["column1", "column2"],
        values = [["value1", "value2"], ["value3", "value4"]]).get("sql")
        
    assert resp == expected_return
    

def test_method_add_simple(orm):
    expected_return = """INSERT INTO table (column1, column2) VALUES (?, ?)"""
    
    resp = orm.add(
        "table",
        column1 = "value1",
        column2 = "value2").get("sql")
        
    assert resp == expected_return
    

def test_method_select(orm):
    expected_return = "SELECT * FROM table;"
    
    resp = orm.get("table", "all").get("sql")
    
    assert resp == expected_return
    

def test_method_update(orm):
    expected_return = """UPDATE table SET column1 = 'value1' WHERE column2 IN ('tag1', 'tag2');"""
    
    resp = orm.edit("table", whe_("column2", "'tag1', 'tag2'"), column1="value1").get("sql")
    assert resp == expected_return
    

def test_method_delete(orm):
    expected_return = """DELETE FROM table WHERE column1 = 'value1';"""
    
    resp = orm.remove("table", whe_("column1 = 'value1'")).get("sql")
    assert resp == expected_return
    

def test_method_alter_table(orm):
    expected_return = "ALTER TABLE Users ADD cpf INTEGER UNIQUE;"
    
    resp = orm.edit_table("Users", add("cpf", (integer(), prop("uni")))).get("sql")
    assert resp == expected_return


if __name__ == "__main__":
    pytest.main(["-vv", "test_my_orm.py"])