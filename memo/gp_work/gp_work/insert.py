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

#userテーブルに挿入
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

#action_recordテーブルに挿入
#現在の日時を取得
dt_now = datetime.datetime.now()

i=0  #レコード件数カウント
#ファイルオープン
df = pd.read_csv("./sample_data/action_record_data.csv", header=0)
#1行ずつ処理
for ind,rowdata in df.iterrows():

    sqlstring = f"""
        INSERT INTO action_record
            (personal_number, action_record_date, action_record_Time, aestination, transportation, departure, arrival, companion, companion_relationship, companion_count, companion_name, mask_usage, delflag, lastupdate)
        VALUES
            ('{rowdata.personal_number}','{rowdata.action_record_date}','{rowdata.action_record_Time}','{rowdata.aestination}','{rowdata.transportation}','{rowdata.departure}','{rowdata.arrival}',{rowdata.companion},'{rowdata.companion_relationship}',{rowdata.companion_count},'{rowdata.companion_name}','{rowdata.mask_usage}',{rowdata.delflag},'{dt_now}' )
    """
    #print( sqlstring )  #for debug
    my_query( sqlstring, cur )   #1レコード挿入
    i += 1

print(f"action_recordテーブルに{i} レコード追加しました")

#テーブルに書き込み
dbcon.commit()


#physical_conditionテーブルを挿入
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


#suspension_controlテーブルに挿入
#現在の日時を取得
dt_now = datetime.datetime.now()

i=0  #レコード件数カウント
#ファイルオープン
df = pd.read_csv("./sample_data/suspension_control_data.csv", header=0)
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
