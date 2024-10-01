"""
Este módulo valida algumas informações

Note:
    Tanto este módulo quanto suas funções não devem ser acessadas diretamente pelo usuário, são de uso interno do sistema!
    
Functions:
    _is_valid_dbs_data(data: dict): verifica se os dados de conexão com o banco de dados possui as informações necessárias
"""

def _is_valid_dbs_data(data: dict):
    """verifica se os dados de conexão com o banco de dados possui as informações necessárias
        Args:
            data (dict): informações de conexão com o banco de dados"""
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
            

