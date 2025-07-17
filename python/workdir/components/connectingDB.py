import SQLAlchemy

#Data Source Nameのパラメータを辞書型変数で定義
dsn = {
    'host': '172.31.0.10',
    'port': '3306',
    'user': 'root',
    'password': '1234',
    'database': 'sampledb'
}

def create_engine():
    """SQLAlchemyのエンジンを作成して返す"""
    # データベースの接続情報
    connection_string = f"mysql+pymysql://{dsn['user']}:{dsn['password']}@{dsn['host']}:{dsn['port']}/{dsn['database']}"
    
    # データベースに接続
    engine = SQLAlchemy.create_engine(connection_string, echo=True)
    
    return engine

def execute_query(engine, query, params=None):
    """SQLクエリを実行する"""
    with engine.connect() as connection:
        if params:
            result = connection.execute(query, params)
        else:
            result = connection.execute(query)
        return result.fetchall()