from sqlalchemy import inspect

class SqlUtils():
    def table_name(model: str):
        return inspect(model).local_table.name # It will get the currente table name
