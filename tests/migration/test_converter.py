import pytest
from src.migration.converter import convert_sql_to_postgres

def test_convert_primary_key():
    sql = "CREATE TABLE users (id INT PRIMARY KEY)"
    expected = "CREATE TABLE users (id INT CONSTRAINT pk_id PRIMARY KEY)"
    assert convert_sql_to_postgres(sql) == expected

def test_no_conversion_needed():
    sql = "CREATE TABLE users (id INT)"
    assert convert_sql_to_postgres(sql) == sql
