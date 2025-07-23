import streamlit as st
import hashlib
from connectDB.MyDatabase import my_open, my_close
import secrets

# --- データベース関連 ---
dsn = {
    'host': '172.31.0.10',
    'port': '3306',
    'user': 'root',
    'password': '1234',
    'database': 'sampledb'
}

def verify_password(password, hashed_password, salt):
    """入力されたパスワードが保存されているハッシュと一致するか検証する"""
    # DB登録時のハッシュ生成方法に合わせる
    salt = secrets.token_hex(16)
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    st.write(f"Verifying password: {password}, Hashed: {hashed_password}, Salt: {salt}")
    return hashed_password

def get_user_credentials(personal_number):
    """データベースからユーザーの認証情報を取得する"""
    sql = """
        SELECT u.user_id, u.position, ua.password_hash, ua.salt
        FROM user u
        JOIN user_auth ua ON u.personal_number = ua.personal_number
        WHERE u.personal_number = %s AND u.delflag = FALSE
    """
    dbcon, cur = None, None
    try:
        dbcon, cur = my_open(**dsn)
        cur.execute(sql, (personal_number,))
        return cur.fetchone()
    except Exception as e:
        st.error(f"データベース接続エラー: {e}")
        return None
    finally:
        if dbcon:
            my_close(dbcon, cur)

# --- ログインフォーム ---
def login_form():
    """ログインフォームを表示し、ユーザー認証を行う"""
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
        st.session_state["username"] = ""
        st.session_state["is_admin"] = False

    if not st.session_state["logged_in"]:
        st.title("ログインページ")

        # personal_numberをログインIDとして使用
        personal_number = st.text_input("個人番号", key="login_personal_number")
        password = st.text_input("パスワード", type="password", key="login_password")
        login_button = st.button("ログイン", key="login_button")

        if login_button:
            user_data = get_user_credentials(personal_number)
            
            if user_data:
                user_id, position, hashed_password, salt = user_data
                if verify_password(password, hashed_password, salt):
                    st.session_state["logged_in"] = True
                    st.session_state["username"] = personal_number
                    st.session_state["personal_number"] = personal_number
                    st.session_state["is_admin"] = (position == 'admin')
                    st.rerun()
                else:
                    st.error("個人番号またはパスワードが間違っています。")
                    # st.write("個人番号:", personal_number)  
                    # st.write("パスワード:", password)  # デバッグ用に表示（本番では削除すること）
                    st.write(user_data)
            else:
                st.error("個人番号またはパスワードが間違っています。")
                # st.write("個人番号:", personal_number)  
                # st.write("パスワード:", password)
                # st.write(user_data)
        return False
    else:
        return True

if __name__ == "__main__":
    login_form()