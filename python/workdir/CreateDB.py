from MyDatabase import my_open, my_query, my_close
import mysql.connector

# Data Source Nameのパラメータを辞書型変数で定義
dsn = {
    'host': '172.31.0.10',  # ホスト名(IPアドレス)
    'port': '3306',        # mysqlの接続ポート番号
    'user': 'root',      # dbアクセスするためのユーザid
    'password': '1234',    # ユーザidに対応するパスワード
    'database': 'sampledb' # オープンするデータベース名
}


def create_database(database_name: str):
    """
    データベースの作成
    Args:
        database_name (str): 作成するデータベースの名前
    """
    dsn_for_creation = dsn.copy()
    if 'database' in dsn_for_creation:
        del dsn_for_creation['database']
    
    dbcon = None
    cur = None
    try:
        dbcon = mysql.connector.connect(**dsn_for_creation)
        cur = dbcon.cursor()
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {database_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci")
        print(f"Database '{database_name}' created or already exists.")
    except mysql.connector.Error as err:
        print(f"Failed to create database: {err}")
    finally:
        if cur:
            cur.close()
        if dbcon:
            dbcon.close()


def create_tables():
    """
    テーブルの作成
    """
    # テーブル作成の順番を考慮（参照されるテーブルを先に作成）
    table_definitions = [
        """
        CREATE TABLE IF NOT EXISTS user (
            user_id INT PRIMARY KEY AUTO_INCREMENT,
            personal_number VARCHAR(10),
            affiliation VARCHAR(30),
            namae VARCHAR(30),
            phone_number VARCHAR(20),
            user_class VARCHAR(10),
            position VARCHAR(10),
            attendance_suspension BOOLEAN DEFAULT FALSE,
            password_hash VARCHAR(255),
            salt VARCHAR(32),
            delflag BOOLEAN DEFAULT FALSE,
            last_update DATETIME
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS suspension_control (
            suspension_control_id INT PRIMARY KEY AUTO_INCREMENT,
            user_id INT,
            start_date DATE,
            finish_date DATE,
            remarks TEXT,
            medical_institution_name VARCHAR(10),
            attending_physician VARCHAR(20),
            delflag BOOLEAN DEFAULT FALSE,
            last_update DATETIME,
            FOREIGN KEY (user_id) REFERENCES user(user_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS action (
            action_id INT PRIMARY KEY AUTO_INCREMENT,
            user_id INT,
            action_date DATE,
            action_time TIME,
            destination VARCHAR(50),
            transportation VARCHAR(50),
            departure VARCHAR(50),
            arrival VARCHAR(50),
            companion BOOLEAN,
            companion_relationship VARCHAR(50),
            companion_count VARCHAR(50),
            companion_name VARCHAR(50),
            mask_usage VARCHAR(50),
            delflag BOOLEAN DEFAULT FALSE,
            last_update DATETIME,
            FOREIGN KEY (user_id) REFERENCES user(user_id)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS physical_condition (
            physical_condition_id INT PRIMARY KEY AUTO_INCREMENT,
            user_id INT,
            condition_date DATE,
            condition_time TIME,
            body_temperature FLOAT,
            joint_muscle_pain BOOLEAN,
            fatigue BOOLEAN,
            headache BOOLEAN,
            sore_throat BOOLEAN,
            shortness_of_breath BOOLEAN,
            cough_sneeze BOOLEAN,
            nausea_vomiting BOOLEAN,
            abdominal_pain_diarrhea BOOLEAN,
            taste_disorder BOOLEAN,
            smell_disorder BOOLEAN,
            attendance_suspension BOOLEAN,
            suspension_control_id INT,
            delflag BOOLEAN DEFAULT FALSE,
            last_update DATETIME,
            FOREIGN KEY (user_id) REFERENCES user(user_id),
            FOREIGN KEY (suspension_control_id) REFERENCES suspension_control(suspension_control_id)
        )
        """
    ]

    dbcon, cur = None, None
    try:
        dbcon, cur = my_open(**dsn)
        for table_sql in table_definitions:
            table_name = table_sql.split("EXISTS ")[1].split(" (")[0].strip()
            try:
                my_query(table_sql, cur)
                print(f"Table '{table_name}' created or already exists.")
            except mysql.connector.Error as err:
                print(f"Failed to create table '{table_name}': {err}")

        dbcon.commit()
    except Exception as e:
        print(f"An error occurred during table creation: {e}")
        if dbcon:
            dbcon.rollback()
    finally:
        if dbcon and cur:
            my_close(dbcon, cur)

if __name__ == "__main__":
    print("Step 1: Creating database...")
    create_database(dsn['database'])
    
    print("\nStep 2: Creating tables...")
    create_tables()
    
    print("\nDatabase and tables setup complete.")