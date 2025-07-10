import streamlit as st
import hashlib # ハッシュ化のために必要
import secrets # セキュリティのために必要

# --- パスワード関連の関数 ---

def hash_password(password):
    """
    新しいパスワードのハッシュとソルトを生成する
    """
    salt = secrets.token_hex(16)
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed_password, salt

def verify_password(password, hashed_password, salt):
    """
    入力されたパスワードが保存されているハッシュと一致するか検証する
    """
    return hashed_password == hashlib.sha256((password + salt).encode()).hexdigest()

# --- ユーザー情報 ---

# 本来はデータベースで管理します
# ここではサンプルのため、ハッシュ化されたパスワードとソルトを辞書で管理します。
# 'password' には 'adminpass' をハッシュ化したものを設定
# 'salt' はハッシュ化時に使用したソルト
USER_CREDENTIALS = {
    "admin": {
        "hashed_password": "cfc44a7c8c98e9a6aeff943b0aa83deba796058de8c380e4488880a0be00ead9",
        "salt": "e8e0358534d87591762df6e1b1b91798"
    },
    "abeshinzo": {
        "hashed_password": "c6a0c6f7cf8f3e04a3a3d1b8b9b8a0e7e6e5e4d3c2b1a09876543210fedcba98",
        "salt": "0123456789abcdef0123456789abcdef"
    },
     "kagoike": {
        "hashed_password": "f1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2",
        "salt": "fedcba9876543210fedcba9876543210"
    }
}
ADMIN_USERS = {"admin"}  # 管理者ユーザーのセット


def login_form():
    """
    ログインフォームを表示し、ユーザー認証を行う
    Returns:
        bool: ログイン成功ならTrue、失敗ならFalse
    """
    # セッション初期化（初回のみ）
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "username" not in st.session_state:
        st.session_state["username"] = ""
    if "is_admin" not in st.session_state:
        st.session_state["is_admin"] = False

    if not st.session_state["logged_in"]:
        st.title("ログインページ")

        username = st.text_input("ユーザー名", key="login_username")
        password = st.text_input("パスワード", type="password", key="login_password")
        login_button = st.button("ログイン", key="login_button")

        if login_button:
            user_data = USER_CREDENTIALS.get(username)
            if user_data and verify_password(password, user_data["hashed_password"], user_data["salt"]):
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.session_state["is_admin"] = username in ADMIN_USERS
                st.rerun()
            else:
                st.error("ユーザー名またはパスワードが間違っています。")
                return False
        return False
    else:
        return True


# --- パスワードハッシュ生成用（開発者向け） ---
def developer_tool():
    st.header("Developer Tool: Password Hash Generator")
    plain_password = st.text_input("Enter password to hash:")
    if st.button("Generate Hash"):
        if plain_password:
            new_hash, new_salt = hash_password(plain_password)
            st.write("Generated Hash and Salt:")
            st.code(f'"hashed_password": "{new_hash}",\n"salt": "{new_salt}"')
        else:
            st.warning("Please enter a password.")


if __name__ == "__main__":
    st.set_page_config(layout="wide")
    # ログインフォームの表示
    login_form()

    # 開発者向けのハッシュ生成ツールを表示
    # 本番環境ではこの部分は削除してください
    st.sidebar.title("管理用")
    if st.sidebar.checkbox("パスワード生成ツールを表示"):
        developer_tool()
    