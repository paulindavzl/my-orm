import pytest
from utils.convert import _to_dict

def test_to_dict():
    """testa transformar uma lista de tuplas em um dicionário"""
    
    expected_return = [{"key1": "value1", "key2": "value2"}]
    
    assert _to_dict([("value1", "value2")], ["key1", "key2"]) == expected_return
    

if __name__ == "__main__":
    pytest.main(["-vv", "test_convert.py"])