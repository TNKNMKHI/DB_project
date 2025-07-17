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
df = pd.read_csv("./sample_data/action_record_data.csv", header=0)

# CSVのヘッダーのtypoを修正
df.rename(columns={'action_record_Time': 'action_record_time', 'aestination': 'destination'}, inplace=True)

#1行ずつ処理
for ind,rowdata in df.iterrows():

    sqlstring = f"""
        INSERT INTO action_record
            (personal_number, action_record_date, action_record_time, destination, transportation, departure, arrival, companion, companion_relationship, companion_count, companion_name, mask_usage, delflag, lastupdate)
        VALUES
            ('{rowdata.personal_number}','{rowdata.action_record_date}','{rowdata.action_record_time}','{rowdata.destination}','{rowdata.transportation}','{rowdata.departure}','{rowdata.arrival}',{rowdata.companion},'{rowdata.companion_relationship}',{rowdata.companion_count},'{rowdata.companion_name}','{rowdata.mask_usage}',{rowdata.delflag},'{dt_now}' )
    """
    #print( sqlstring )  #for debug
    my_query( sqlstring, cur )   #1レコード挿入
    i += 1

print(f"action_recordテーブルに{i} レコード追加しました")

#テーブルに書き込み
dbcon.commit()

#カーソルとDBコンソールのクローズ
my_close(dbcon,cur)