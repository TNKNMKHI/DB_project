import streamlit as st
from login import login_form


def main():
    # ログインしてない場合はフォームのみを表示
    if login_form():
        UserName = st.session_state["username"]
        
        tab1 , tab2 = st.tabs(["マイページ","出席停止"])
        
        with tab1:
            st.subheader(f"{UserName}さんの情報")
        
        
        with tab2:
            st.subheader("出席停止の情報")




if __name__ == "__main__":
    main()
