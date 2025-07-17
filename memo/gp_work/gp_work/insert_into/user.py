#レコードを挿入するプログラム
from MyDatabase import my_open , my_query , my_close
import pandas as pd
import datetime

#Data Source Nameのパラメータを辞書型変数で定義
dsn = {
    'host' : '172.30.0.10',  #ホスト名(IPアドレス)
    'port' : '3306',        #mysqlの接続ポート番号
    'user' : 'root',      #dbアクセスするためのユーザid
    'password' : '1234',    #ユーザidに対応するパスワード
    'database' : 'dbrongp' #オープンするデータベース名
}
dbcon,cur = my_open( **dsn )

#現在の日時を取得
dt_now = datetime.datetime.now()

i=0  #レコード件数カウント
#ファイルオープン
df = pd.read_csv("./sample_data/user_data.csv", header=0)
#1行ずつ処理
for ind,rowdata in df.iterrows():
    
    sqlstring = f"""
        INSERT INTO user
            (personal_number, affiliation, namae, phone_number, user_class, position, attendance_suspension, login_pass, delflag, lastupdate)
        VALUES
            ('{rowdata.personal_number}','{rowdata.affiliation}','{rowdata.namae}','{rowdata.phone_number}','{rowdata.user_class}','{rowdata.position}',{rowdata.attendance_suspension},'{rowdata.login_pass}',{rowdata.delflag},'{dt_now}' )
    """
    #print( sqlstring )  #for debug
    my_query( sqlstring, cur )   #1レコード挿入
    i += 1

print(f"userテーブルに{i} レコード追加しました")

#テーブルに書き込み
dbcon.commit()

#カーソルとDBコンソールのクローズ
my_close(dbcon,cur)
