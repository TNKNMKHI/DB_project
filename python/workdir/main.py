import streamlit as st
from login import login_form
from pages.mypage import show_mypage
from pages.report_stop import show_report_stop


def main():
    # ログインしてない場合はフォームのみを表示
    if login_form():
        UserName = st.session_state["username"]
        
        # ログイン後のページを表示
        



if __name__ == "__main__":
    main()
