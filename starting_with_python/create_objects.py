#!/usr/bin/env python
import snowflake.connector
import os

# Gets the version

ctx = snowflake.connector.connect(
    user=os.getenv('SNOWFLAKE_USER'),
    password=os.getenv('SNOWFLAKE_PWD'),
    account=os.getenv('SNOWFLAKE_ACCT')
    )

cs = ctx.cursor()

try:
    cs.execute('CREATE WAREHOUSE IF NOT EXISTS tiny_warehouse_mg')
    cs.execute('USE WAREHOUSE tiny_warehouse_mg')
    cs.execute('CREATE DATABASE IF NOT EXISTS testdb')
    cs.execute('USE DATABASE testdb')
    cs.execute('CREATE SCHEMA IF NOT EXISTS testschema')
    cs.execute('USE SCHEMA testschema')
    cs.execute('CREATE OR REPLACE TABLE ' 
        'test_table(col1 integer, col2 string)')
    cs.execute("INSERT INTO test_table(col1, col2) "
        "VALUES(123, 'test string1'),(456, 'test string2')")
    
    print("First row in table is:")
    col1, col2 = cs.execute("SELECT col1, col2 FROM test_table").fetchone()
    print('{0}, {1}'.format(col1, col2))

    print("All rows in table are:")
    for (col1, col2) in cs.execute("SELECT col1, col2 FROM test_table"):
	    print('{0}, {1}'.format(col1, col2))

finally:
    cs.close()
ctx.close()

