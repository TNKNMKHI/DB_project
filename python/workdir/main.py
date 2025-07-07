import streamlit as st
from login import login_form
from pages.mypage import show_mypage
from pages.report_stop import show_report_stop


def main():
    # ログインしてない場合はフォームのみを表示
    if not login_form():
        return # ログインしていない場合はここで終了

    UserName = st.session_state["username"]
    st.write(f"Welcome, {UserName}!")

    # タブでページ切り替え
    tab1, tab2 = st.tabs(["マイページ", "報告停止"])
    
    with tab1:
        show_mypage(UserName)
    with tab2:
        show_report_stop()


if __name__ == "__main__":
    main()
