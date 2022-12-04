#!/usr/bin/env python
import snowflake.connector
import os

# Gets the version
print('getting connector')
ctx = snowflake.connector.connect(
    user=os.getenv('SNOWFLAKE_PYTHON_USER'),
    password=os.getenv('SNOWFLAKE_PYTHON_PWD'),
    account=os.getenv('SNOWFLAKE_PYTHON_ACCT')
    )
print("getting cursor")
cs = ctx.cursor()
print("executing statement")
try:
    cs.execute("SELECT current_version()")
    one_row = cs.fetchone()
    print(one_row[0])
finally:
    cs.close()
ctx.close()

