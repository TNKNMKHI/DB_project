import streamlit as st
from login import login_form
from pages.mypage import show_mypage
from pages.report_stop import show_report_stop


def main():
    # ログインしてない場合はフォームのみを表示
    if not login_form():
        return # ログインしていない場合はここで終了

    UserName = st.session_state["username"]

    # ログイン後のページを表示
    st.write(f"Welcome, {UserName}!")
        



if __name__ == "__main__":
    main()
