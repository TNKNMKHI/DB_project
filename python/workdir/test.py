#pr0401　Flaskモジュールで，DBアクセス&データ分析
from MyDatabase import my_open , my_query , my_close
import pandas as pd

#Data Source Nameのパラメータを辞書型変数で定義
dsn = {
    'host' : '172.31.0.10',  #ホスト名(IPアドレス)
    'port' : '3306',        #mysqlの接続ポート番号
    'user' : 'root',      #dbアクセスするためのユーザid
    'password' : '1234',    #ユーザidに対応するパスワード
    'database' : 'sampledb' #オープンするデータベース名
}

#flaskモジュールのインポートと実体化　<== お決まり
from flask import Flask, render_template , request
app = Flask(__name__ ,static_folder="static")

@app.route("/")
def top():
    return ("<h2>テスト</h2>")


#プログラム起動
app.run(host="localhost",port=5000,debug=True)