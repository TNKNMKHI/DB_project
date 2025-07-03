import streamlit as st

def login_form():
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

    if not st.session_state["logged_in"]:
        st.title("ログインページ")

        username = st.text_input("ユーザー名")
        password = st.text_input("パスワード", type="password")

        if st.button("ログイン"):
            if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.success("ログイン成功！")
                return True
            else:
                st.error("ユーザー名またはパスワードが間違っています。")
                return False
        return False
    else:
        return True