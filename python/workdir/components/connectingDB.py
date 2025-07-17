import mysql.connector

# Data Source Nameのパラメータを辞書型変数で定義
dsn = {
    'host': '172.31.0.10',
    'port': '3306',
    'user': 'root',
    'password': '1234',
    'database': 'sampledb'
}

def get_db_connection():
    """データベース接続とカーソルを取得する"""
    try:
        dbcon = mysql.connector.connect(**dsn)
        cur = dbcon.cursor(dictionary=True) # 結果を辞書型で受け取る
        return dbcon, cur
    except mysql.connector.Error as err:
        # st.error(f"データベース接続エラー: {err}") # Streamlitコンポーネント内でのみ使用可能
        print(f"データベース接続エラー: {err}") # コンソールへの出力
        return None, None
