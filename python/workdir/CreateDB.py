from MyDatabase import my_open , my_query , my_close

#Data Source Nameのパラメータを辞書型変数で定義
dsn = {
    'host' : '172.31.0.10',  #ホスト名(IPアドレス)
    'port' : '3306',        #mysqlの接続ポート番号
    'user' : 'root',      #dbアクセスするためのユーザid
    'password' : '1234',    #ユーザidに対応するパスワード
    'database' : 'sampledb' #オープンするデータベース名
}


def create_database(database_name:str):
    """
    データベースの作成
    Args:
        database_name (str): 作成するデータベースの名前
    """
    
    sql = """
        DROP DATABESE IF EXISTS %s; 
        CREATE DATABASE IF NOT EXISTS %s;
    """
    sql = sql % (database_name, database_name)
    
    dbcon, cur = my_open(**dsn)
    my_query(sql, cur)
    my_close(dbcon, cur)


def create_table():
    """
    テーブルの作成
    """
    sql = """
        DROP TABLE IF EXISTS %s
        CREATE TABLE %s (
            
        )
        ;
    """


def insert_data():
    
    """データの入力"""