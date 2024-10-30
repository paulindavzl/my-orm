def _is_valid_dbs_data(data: dict):
    dbs_type = data.get("dbs")
    if not dbs_type:
        return {"result": False, "missing": "dbs"}
    
    match dbs_type:
        case "sqlite":
            if not data.get("url"):
                return {"result": False, "missing": "url"}
            return {"result": True}
        case "my_sql":
            pass
            

