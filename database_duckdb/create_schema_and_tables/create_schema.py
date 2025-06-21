'''
In this part the tables schemas will be created to be used later on in DBT
'''

import duckdb
import os

# Database Name
db_name = 'finance_db'

# Create the path
os.makedirs("database_duckdb/duckdb_files", exist_ok=True)

# Connect the database in the folder
con = duckdb.connect(f"database_duckdb/duckdb_files/{db_name}.duckdb")

# Create the schemas if they don't already exist
con.execute("CREATE SCHEMA IF NOT EXISTS bronze;")
con.execute("CREATE SCHEMA IF NOT EXISTS silver;")
con.execute("CREATE SCHEMA IF NOT EXISTS gold;")