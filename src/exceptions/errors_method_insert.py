def type_error(var_name, var, expec):
    return TypeError(f"(MyORM.add()) {var_name} expected a {expec} value but received an {type(var).__name__} ({var}) value. See the documentation at https://github.com/paulindavzl/my-orm")
    

def type_error_args(arg):
    return TypeError(f"(MyORM.add()) All arg values ​​must be strings. {arg} is an {type(arg).__name__}. See the documentation at https://github.com/paulindavzl/my-orm")
    

def value_error(*args):
    return ValueError(f"(MyORM.add()) The number of values ​({len(args[0])}) does not mean the number of columns ({len(args[1])})! See the documentation at https://github.com/paulindavzl/my-orm")