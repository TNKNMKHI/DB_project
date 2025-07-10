from python.workdir.connectDB.MyDatabase import my_open, my_query, my_close
import mysql.connector

def create_database(database_name: str):
    """
    データベースの作成
    Args:
        database_name (str): 作成するデータベースの名前
    """
    dsn_for_creation = dsn.copy()
    if 'database' in dsn_for_creation:
        del dsn_for_creation['database']
    
    dbcon = None
    cur = None
    try:
        dbcon = mysql.connector.connect(**dsn_for_creation)
        cur = dbcon.cursor()
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {database_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci")
        print(f"Database '{database_name}' created or already exists.")
    except mysql.connector.Error as err:
        print(f"Failed to create database: {err}")
    finally:
        if cur:
            cur.close()
        if dbcon:
            dbcon.close()
