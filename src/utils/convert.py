def _to_dict(data: list, keys: list):
    
    result = []
    for pos in range(len(data)):
        sub_pos = 0
        res_dict = {}
        for item in data[pos]:
            res_dict[str(keys[sub_pos])] = item
            sub_pos += 1
        
        result.append(res_dict)
        
    return result
    
