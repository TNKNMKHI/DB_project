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
df = pd.read_csv("./sample_data/physical_condition_data.csv", header=0)
#1行ずつ処理
for ind,rowdata in df.iterrows():
    
    sqlstring = f"""
        INSERT INTO physical_condition
            (personal_number, condition_date, condition_time, body_temperature, joint_muscle_pain, fatigue, headache, sore_throat, shortness_of_breath, cough_sneeze, nausea_vomiting, abdominal_pain_diarrhea, taste_disorder, smell_disorder, attendance_suspension ,delflag, lastupdate)
        VALUES
            ('{rowdata.personal_number}','{rowdata.condition_date}','{rowdata.condition_time}',{rowdata.body_temperature},{rowdata.joint_muscle_pain},{rowdata.fatigue},{rowdata.headache},{rowdata.sore_throat},{rowdata.shortness_of_breath},{rowdata.cough_sneeze},{rowdata.nausea_vomiting},{rowdata.abdominal_pain_diarrhea},{rowdata.taste_disorder},{rowdata.smell_disorder},{rowdata.attendance_suspension},{rowdata.delflag},'{dt_now}' )
    """
    #print( sqlstring )  #for debug
    my_query( sqlstring, cur )   #1レコード挿入
    i += 1

print(f"physical_conditionテーブルに{i} レコード追加しました")

#テーブルに書き込み
dbcon.commit()

#カーソルとDBコンソールのクローズ
my_close(dbcon,cur)
