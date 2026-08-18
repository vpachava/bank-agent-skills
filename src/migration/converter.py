def convert_sql_to_postgres(sql_query: str) -> str:
    if "PRIMARY KEY" in sql_query:
        return sql_query.replace("PRIMARY KEY", "CONSTRAINT pk_id PRIMARY KEY")
    return sql_query
