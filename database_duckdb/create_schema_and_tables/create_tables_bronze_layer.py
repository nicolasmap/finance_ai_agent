'''
In this part the tables will be created in Bronze Layer from CSV Files
'''

import duckdb
import os

# Create directory for database files if it doesn't exist
os.makedirs("database_duckdb/duckdb_files", exist_ok=True)

# Define paths for CSV files and DuckDB database
csv_path = "database_duckdb/bronze_layer_csvs"
db_path = "database_duckdb/duckdb_files/meu_banco.duckdb"

# Connect to DuckDB database (creates it if it doesn't exist)
con = duckdb.connect(db_path)

# Create schema for Bronze Layer if it doesn't exist
con.execute("CREATE SCHEMA IF NOT EXISTS bronze;")

# Create tables in Bronze Layer from CSV files
con.execute(f"""
    CREATE OR REPLACE TABLE bronze.customers AS
    SELECT * FROM read_csv_auto('{csv_path}/stg_customers.csv', HEADER=TRUE)
""")
con.execute(f"""
    CREATE OR REPLACE TABLE bronze.channels AS
    SELECT * FROM read_csv_auto('{csv_path}/stg_channels.csv', HEADER=TRUE)
""")
con.execute(f"""
    CREATE OR REPLACE TABLE bronze.transactions AS
    SELECT * FROM read_csv_auto('{csv_path}/stg_transactions.csv', HEADER=TRUE)
""")

# Basic validation queries - preview top 5 rows from each table
print("✅ Customers:")
print(con.execute("SELECT * FROM bronze.customers LIMIT 5").fetchdf())

print("\n✅ Channels:")
print(con.execute("SELECT * FROM bronze.channels LIMIT 5").fetchdf())

print("\n✅ Transactions:")
print(con.execute("SELECT * FROM bronze.transactions LIMIT 5").fetchdf())

# Close connection
con.close()
