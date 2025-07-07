import streamlit as st
from pages.login import login_form
from pages.mypage import show_mypage
from pages.report_stop import show_report_stop
from pages.notice import show_notice 


def main():
    # ログインしてない場合はフォームのみを表示
    if not login_form():
        return # ログインしていない場合はここで終了

    UserName = st.session_state["username"]
    st.markdown(f"### Welcome, {UserName}!")

    # タブでページ切り替え
    MenuList = ["お知らせ", "マイページ", "出席停止生徒一覧"]
    tab1, tab2,tab3 = st.tabs(MenuList)
    
    with tab1:
        show_notice()
        
    with tab2:
        show_mypage(UserName)
        
    with tab3:
        show_report_stop()


if __name__ == "__main__":
    main()
