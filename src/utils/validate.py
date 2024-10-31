def _is_valid_dbs_data(data: dict):
    dbs_type = data.get("dbs")
    if not dbs_type:
        return {"result": False, "missing": "dbs"}
    
    match dbs_type:
        case "sqlite":
            if not data.get("path"):
                return {"result": False, "missing": "path"}
            return {"result": True}
        case "mysql":
            if not data.get("user"):
                return {"result": False, "missing": "user"}
            elif not data.get("password"):
                return {"result": False, "missing": "password"}
            elif not data.get("host"):
                return {"result": False, "missing": "host"}
            elif not data.get("database"):
                return {"result": False, "missing": "database"}
            return {"result": True}
        case "postgres":
            if not data.get("user"):
                return {"result": False, "missing": "user"}
            elif not data.get("password"):
                return {"result": False, "missing": "password"}
            elif not data.get("host"):
                return {"result": False, "missing": "host"}
            elif not data.get("database"):
                return {"result": False, "missing": "database"}
            return {"result": True}