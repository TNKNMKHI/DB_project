import streamlit as st
import hashlib # ハッシュ化のために必要
import secrets # セキュリティのために必要

def login_form():
    """
    ログインフォームを表示し、ユーザー認証を行う
    Returns:
        bool: ログイン成功ならTrue、失敗ならFalse
    """
    # テスト用のユーザー名とパスワードの辞書
    USER_CREDENTIALS = {
        "abeshinzo": "0708",
        "kagoike": "semi",
        "a": "a",
        "admin": "adminpass"
    }
    ADMIN_USERS = {"admin"}  # 管理者ユーザーのセット

    # セッション初期化（初回のみ）
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "username" not in st.session_state:
        st.session_state["username"] = ""
    if "is_admin" not in st.session_state:
        st.session_state["is_admin"] = False
    if "login_success" not in st.session_state:
        st.session_state["login_success"] = False

    if not st.session_state["logged_in"]:
        st.title("ログインページ")

        username = st.text_input("ユーザー名", key="login_username")
        password = st.text_input("パスワード", type="password", key="login_password")
        login_button = st.button("ログイン", key="login_button")

        # パスワードをハッシュ化（オプション）
        # password = password_hash(password)
        
        if login_button:
            if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.session_state["login_success"] = True
                st.session_state["is_admin"] = username in ADMIN_USERS  # 管理者かどうかを判定
                st.rerun()
            else:
                st.error("ユーザー名またはパスワードが間違っています。")
                return False

        # ログインフォームを表示
        return False
    
    else:
        st.session_state["login_success"] = False
        return True
    




def password_hash(password):
    """
    パスワードをハッシュ化する
    Args:
        password (str): ハッシュ化するパスワード
    Returns:
        tuple: ハッシュオブジェクト、ハッシュの16進数値、ソルト

    """
    # secretsモジュールを使ってランダムなソルトを生成
    salt = secrets.token_hex(16)

    # ソルトとSHA-256アルゴリズムを使ってパスワードをハッシュ化
    hash_object = hashlib.sha256((password + salt).encode())

    # ハッシュの16進数値を取得
    hash_hex = hash_object.hexdigest()
    
    return hash_object , hash_hex , salt


# テスト用
if __name__ == "__main__":
    password = ""
    hash_object, hash_hex, salt = password_hash(password)
    print(f"Hash: {hash_hex}\nSalt: {salt}\nHash Object: {hash_object}")
    