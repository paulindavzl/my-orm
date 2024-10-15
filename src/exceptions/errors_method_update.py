def type_error(var_name, var, expec):
    return TypeError(f"(MyORM.edit()) {var_name} expected a {expec} value but received an {type(var).__name__} ({var}) value. See the documentation at https://github.com/paulindavzl/my-orm")
    

def value_error(var):
    return ValueError(f"(MyORM.add()) kwargs expected a key and a value (column=value), but received {type(var).__name__} (var)! See the documentation at https://github.com/paulindavzl/my-orm")