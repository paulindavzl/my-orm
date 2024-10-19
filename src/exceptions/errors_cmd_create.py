def type_error(var_name: str, var_error, expected: str, funct_name: str) -> TypeError:
    return TypeError(f"Unexpected '{type(var_error).__name__}' ({var_error}) in {funct_name}(). {var_name} expects a value of type '{expected}'. See the documentation at https://github.com/paulindavzl/my-orm.")
    

def value_error(var_name: str, var_error, expected: str, funct_name: str) -> ValueError:
    return ValueError(f"The value passed in '{var_name}' ({var_error}) is incorrect! {funct_name}() expects the value in '{expected}' format for the variable '{var_name}'. See the documentation at https://github.com/paulindavzl/my-orm")


def value_error_dbms(dbms_error: str, supported: list) -> ValueError:
    sup = ", ".join(supported)
    
    return ValueError(f"MyORM does not support '{dbms_error}'! Currently supported DBMSs are: {sup}. See the documentation at https://github.com/paulindavzl/my-orm")
   