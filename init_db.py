import psycopg2
from psycopg2 import sql

# Database connection details
dbname = 'postgres'  # Connect to the default database to create a new one
user = 'postgres'
password = 'example'
host = 'localhost'
port = '5434'

# New database details
new_dbname = 'rag-1234'

# Connect to the PostgreSQL server
connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
connection.autocommit = True

try:
    # Create a cursor object
    cursor = connection.cursor()

    # Check if the database exists
    cursor.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), [new_dbname])
    exists = cursor.fetchone()

    if not exists:
        # Create the new database
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(new_dbname)))
        print(f"Database {new_dbname} created successfully.")

    # Connect to the new database to enable the vector plugin
    connection.close()
    connection = psycopg2.connect(dbname=new_dbname, user=user, password=password, host=host, port=port)
    cursor = connection.cursor()

    # Enable the vector plugin
    cursor.execute("CREATE EXTENSION IF NOT EXISTS vector")
    print(f"Vector plugin enabled successfully on database {new_dbname}.")

finally:
    # Close the cursor and connection
    cursor.close()
    connection.close()