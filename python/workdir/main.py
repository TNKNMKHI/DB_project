import streamlit as st
from components.login import login_form
from components.mypage import show_mypage
from components.report_stop import show_report_stop
from components.notice import show_notice
from components.health_check import show_health_check
from components.activity_log import show_activity_log
from components.history import show_history

def main():
    # ログインしてない場合はフォームのみを表示
    if not login_form():
        return # ログインしていない場合はここで終了

    UserName = st.session_state["username"]
    is_admin = st.session_state.get("is_admin", False)  # is_adminフラグを取得

    st.markdown(f"### Welcome, {UserName}!")
    
    # for debug
    # st.write("is admin : ",is_admin)

    # ユーザー種別で表示を切り替え
    if is_admin:
        st.markdown("## 管理者ページ")
        # 管理者メニュー
        AdminMenuList = ["未入力者管理", "症状注意者管理", "出校停止者管理", "お知らせ投稿"]
        admin_tab1, admin_tab2, admin_tab3, admin_tab4 = st.tabs(AdminMenuList)

        with admin_tab1:
            st.write("未入力者管理ページです") # ダミー
        with admin_tab2:
            st.write("症状注意者管理ページです") # ダミー
        with admin_tab3:
            show_report_stop() # 既存のものを流用
        with admin_tab4:
            st.write("お知らせ投稿ページです") # ダミー

    else: # 一般ユーザー
        # タブでページ切り替え
        MenuList = ["お知らせ","マイページ", "体調入力", "行動入力", "出校停止報告", "履歴確認"]
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(MenuList)
        
        with tab1:
            show_notice()
        
        with tab2:
            show_mypage(UserName, st.session_state["personal_number"])
            
        with tab3:
            show_health_check()
            
        with tab4:
            show_activity_log()
            
        with tab5:
            show_report_stop()
        
        with tab6:
            show_history()


if __name__ == "__main__":
    main()
