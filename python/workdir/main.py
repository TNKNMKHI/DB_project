import streamlit as st
from login import login_form
from mypage import show_mypage


def main():
    # ログインしてない場合はフォームのみを表示
    if login_form():
        UserName = st.session_state["username"]
        
        tab1 , tab2 = st.tabs(["マイページ","出席停止"])
        
        with tab1:
            show_mypage(UserName)
        
        
        with tab2:
            




if __name__ == "__main__":
    main()
