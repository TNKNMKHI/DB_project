#レコードを挿入するプログラム
from MyDatabase import my_open , my_query , my_close
import pandas as pd
import datetime
import hashlib
import os

# パスワードをハッシュ化する関数
def hash_password(password):
    salt = os.urandom(16).hex()
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed_password, salt

#Data Source Nameのパラメータを辞書型変数で定義
dsn = {
    'host': '172.31.0.10',
    'port': '3306',
    'user': 'root',
    'password': '1234',
    'database': 'sampledb'
}
dbcon,cur = my_open( **dsn )

#現在の日時を取得
dt_now = datetime.datetime.now()

i=0  #レコード件数カウント
#ファイルオープン
df = pd.read_csv("./sample_data/user_data.csv", header=0)

# CSVのヘッダーのtypoを修正
df.rename(columns={'lastupdate': 'latupdate'}, inplace=True)

#1行ずつ処理
for ind,rowdata in df.iterrows():
    
    print(f"Processing row : {rowdata.personal_number}")
    
    # userテーブルへのINSERT
    sqlstring_user = f"""
        INSERT INTO user
            (personal_number, affiliation, namae, phone_number, user_class, position, attendance_suspension, delflag, latupdate)
        VALUES
            ('{rowdata.personal_number}','{rowdata.affiliation}','{rowdata.namae}','{rowdata.phone_number}','{rowdata.user_class}','{rowdata.position}',{rowdata.attendance_suspension},{rowdata.delflag},'{dt_now}' )
    """
    my_query( sqlstring_user, cur )

    # パスワードのハッシュ化
    hashed_password, salt = hash_password(rowdata.login_pass)

    # user_authテーブルへのINSERT
    sqlstring_auth = f"""
        INSERT INTO user_auth
            (personal_number, password_hash, salt, last_update, delflag)
        VALUES
            ('{rowdata.personal_number}', '{hashed_password}', '{salt}', '{dt_now}', {rowdata.delflag})
    """
    my_query( sqlstring_auth, cur )

    i += 1

print(f"userテーブルとuser_authテーブルに{i} レコード追加しました")

#テーブルに書き込み
dbcon.commit()

#カーソルとDBコンソールのクローズ
my_close(dbcon,cur)
