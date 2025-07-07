import streamlit as st
import hashlib # ハッシュ化のために必要

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

    # セッション初期化（初回のみ）
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "username" not in st.session_state:
        st.session_state["username"] = ""
    if "login_success" not in st.session_state:
        st.session_state["login_success"] = False

    if not st.session_state["logged_in"]:
        st.title("ログインページ")

        username = st.text_input("ユーザー名", key="login_username")
        password = st.text_input("パスワード", type="password", key="login_password")
        login_button = st.button("ログイン", key="login_button")

        if login_button:
            if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.session_state["login_success"] = True
                st.rerun()
            else:
                st.error("ユーザー名またはパスワードが間違っています。")
                return False

        if st.session_state["login_success"]:
            st.success("ログイン成功！")
            st.session_state["login_success"] = False

        return False
    else:
        st.session_state["login_success"] = False
        return True