def type_error(var_name: str, var, expect: str):
    return TypeError(f"(MyORM.make()) {var_name} expected an {expect}, but received a {type(var).__name__} ({var}). See the documentation at https://github.com/paulindavzl/my-orm.")


def value_error(var_name: str, var, expected: str):
    return ValueError(f"(MyORM.make()) The tuple {var_name} expected {expected}. Currently it has {len(var)} ({var}).. See the documentation at https://github.com/paulindavzl/my-orm.")