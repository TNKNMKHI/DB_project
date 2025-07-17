#レコードを挿入するプログラム
from MyDatabase import my_open , my_query , my_close
import pandas as pd
import datetime

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
df = pd.read_csv("./sample_data/suspension_control_data.csv", header=0)

# # CSVのヘッダーのtypoを修正
# df.rename(columns={'lastupdate': 'lastupdate'}, inplace=True)

#1行ずつ処理
for ind,rowdata in df.iterrows():
    
    sqlstring = f"""
        INSERT INTO suspension_control
            (personal_number, sc_start, sc_finish, remarks, medical_institution_name, attending_physician, delflag, lastupdate)
        VALUES
            ('{rowdata.personal_number}','{rowdata.sc_start}','{rowdata.sc_finish}','{rowdata.remarks}','{rowdata.medical_institution_name}','{rowdata.attending_physician}',{rowdata.delflag},'{dt_now}' )
    """
    #print( sqlstring )  #for debug
    my_query( sqlstring, cur )   #1レコード挿入
    i += 1

print(f"suspension_controlテーブルに{i} レコード追加しました")

#テーブルに書き込み
dbcon.commit()

#カーソルとDBコンソールのクローズ
my_close(dbcon,cur)