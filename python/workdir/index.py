import streamlit as st
from login import login_form

if __name__ == "__main__":
    
    # ログインしてない場合はフォームのみを表示
    if login_form():
        UserName = st.session_state["username"]
        st.write(f"ようこそ{UserName}")
        
        tab1 , tab2 = st.tabs(["マイページ","出席停止"])
        
        with tab1:
            st.subheader(f"{UserName}さんの情報")
    
    
    
    

    
    