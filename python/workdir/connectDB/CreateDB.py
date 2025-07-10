from MyDatabase import my_open, my_query, my_close
import mysql.connector
import hashlib
import secrets

# Data Source Nameのパラメータを辞書型変数で定義
dsn = {
    'host': '172.31.0.10',
    'port': '3306',
    'user': 'root',
    'password': '1234',
    'database': 'sampledb'
}

def hash_password(password):
    """新しいパスワードのハッシュとソルトを生成する"""
    salt = secrets.token_hex(16)
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed_password, salt

def create_database(database_name: str):
    """データベースの作成"""
    dsn_for_creation = dsn.copy()
    if 'database' in dsn_for_creation:
        del dsn_for_creation['database']
    
    try:
        dbcon = mysql.connector.connect(**dsn_for_creation)
        cur = dbcon.cursor()
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {database_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci")
        print(f"Database '{database_name}' created or already exists.")
    except mysql.connector.Error as err:
        print(f"Failed to create database: {err}")
    finally:
        if 'dbcon' in locals() and dbcon.is_connected():
            cur.close()
            dbcon.close()

def create_tables():
    """テーブルの作成"""
    # 既存のテーブルを一度削除して再作成（開発用）
    # 本番環境ではこのDROP文は削除してください
    table_definitions = [
        "DROP TABLE IF EXISTS physical_condition, action, suspension_control, user_auth, user;",
        """
        CREATE TABLE IF NOT EXISTS user (
            user_id INT PRIMARY KEY AUTO_INCREMENT,
            personal_number VARCHAR(10) UNIQUE,
            affiliation VARCHAR(30),
            namae VARCHAR(30),
            phone_number VARCHAR(20),
            user_class VARCHAR(10),
            position VARCHAR(10),
            attendance_suspension BOOLEAN DEFAULT FALSE,
            delflag BOOLEAN DEFAULT FALSE,
            last_update DATETIME
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS user_auth (
            auth_id INT PRIMARY KEY AUTO_INCREMENT,
            user_id INT UNIQUE,
            password_hash VARCHAR(255) NOT NULL,
            salt VARCHAR(32) NOT NULL,
            FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
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

    try:
        dbcon, cur = my_open(**dsn)
        for table_sql in table_definitions:
            try:
                # 複数のSQL文が含まれている可能性があるので、multi=Trueで実行
                for result in cur.execute(table_sql, multi=True):
                    pass # 結果を消費
                # テーブル名を取得して表示（簡易的な方法）
                if "CREATE TABLE" in table_sql:
                    table_name = table_sql.split("EXISTS ")[1].split(" (")[0].strip()
                    print(f"Table '{table_name}' processed.")
            except mysql.connector.Error as err:
                print(f"Failed to execute query: {err}")

        dbcon.commit()
    except Exception as e:
        print(f"An error occurred during table creation: {e}")
        if 'dbcon' in locals() and dbcon.is_connected():
            dbcon.rollback()
    finally:
        if 'dbcon' in locals() and dbcon.is_connected():
            my_close(dbcon, cur)

def insert_sample_user():
    """サンプル管理者ユーザーの登録"""
    try:
        dbcon, cur = my_open(**dsn)
        
        # 既にadminユーザーが存在するか確認
        cur.execute("SELECT user_id FROM user WHERE personal_number = 'admin'")
        if cur.fetchone():
            print("Sample user 'admin' already exists.")
            return

        # 1. userテーブルに管理者情報を登録
        user_sql = """
            INSERT INTO user (personal_number, namae, position, last_update)
            VALUES (%s, %s, %s, NOW())
        """
        user_data = ('admin', '管理者', 'admin')
        cur.execute(user_sql, user_data)
        
        # 登録したユーザーのIDを取得
        user_id = cur.lastrowid
        
        # 2. パスワードをハッシュ化
        password = "adminpass"
        hashed_password, salt = hash_password(password)
        
        # 3. user_authテーブルにパスワード情報を登録
        auth_sql = """
            INSERT INTO user_auth (user_id, password_hash, salt)
            VALUES (%s, %s, %s)
        """
        auth_data = (user_id, hashed_password, salt)
        cur.execute(auth_sql, auth_data)
        
        dbcon.commit()
        print("Sample user 'admin' with password 'adminpass' has been created.")
        
    except Exception as e:
        print(f"An error occurred during sample user insertion: {e}")
        if 'dbcon' in locals() and dbcon.is_connected():
            dbcon.rollback()
    finally:
        if 'dbcon' in locals() and dbcon.is_connected():
            my_close(dbcon, cur)


if __name__ == "__main__":
    print("Step 1: Creating database...")
    create_database(dsn['database'])
    
    print("\nStep 2: Creating tables...")
    create_tables()
    
    print("\nStep 3: Inserting sample user...")
    insert_sample_user()
    
    print("\nDatabase setup complete.")