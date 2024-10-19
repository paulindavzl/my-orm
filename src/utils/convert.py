from exceptions.errors_convert import type_error, value_error

def _to_dict(data: list, keys: list):
    if not isinstance(data, list):
        raise type_error("data", data, "list", "_to_dict")
    elif not isinstance(keys, list):
        raise type_error("keys", keys, "list", "_to_dict")
    elif len(data[0]) != len(keys):
        raise value_error(len(data) > len(keys), data, keys)
    
    result = []
    for pos in range(len(data)):
        sub_pos = 0
        res_dict = {}
        for item in data[pos]:
            res_dict[str(keys[sub_pos])] = item
            sub_pos += 1
        
        result.append(res_dict)
        
    return result
    
