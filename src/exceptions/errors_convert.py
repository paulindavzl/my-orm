def type_error(var_name: str, var, expec: str, funct: str):
    return TypeError(f"({funct}()) {var_name} expected a {expec}, but received a {type(var).__name__}")
    

def value_error(status: bool, data, keys):
    if status:
        err = f"(_to_dict()) data tem mais valores que keys ({len(data)} > {len(keys)})!"
    else:
        err = f"(_to_dict()) data tem menos valores que keys ({len(data)} < {len(keys)})!"
        
    return ValueError(err)