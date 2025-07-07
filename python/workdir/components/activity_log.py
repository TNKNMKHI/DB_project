import streamlit as st
import datetime

def show_activity_log():
    st.header("行動入力")

    # ログインしているか確認
    if "username" not in st.session_state or not st.session_state["logged_in"]:
        st.warning("このページを表示するにはログインが必要です。")
        return

    st.info("感染症対策のため、日々の行動を記録してください。")

    # --- フォームの作成 ---
    with st.form("activity_log_form"):
        username = st.session_state["username"]
        
        # 日付
        activity_date = st.date_input("日付", datetime.date.today())
        
        # 時間
        col1, col2 = st.columns(2)
        with col1:
            start_time = st.time_input("開始時間", datetime.time(9, 0))
        with col2:
            end_time = st.time_input("終了時間", datetime.time(10, 0))

        # 場所
        location = st.text_input("場所・施設名")

        # 同行者
        companions = st.text_input("同行者（複数人の場合はカンマ区切りで入力）")

        # 行動内容
        details = st.text_area("行動内容（具体的に）", height=150)

        # 送信ボタン
        submitted = st.form_submit_button("この行動を記録する")

    # --- 送信後の処理 ---
    if submitted:
        # 入力チェック（場所と行動内容は必須とする）
        if not location or not details:
            st.error("場所と行動内容を入力してください。")
        else:
            # 収集したデータ
            activity_data = {
                "username": username,
                "date": activity_date,
                "start_time": start_time,
                "end_time": end_time,
                "location": location,
                "companions": [name.strip() for name in companions.split(",")] if companions else [],
                "details": details
            }

            # 本来はここでDB保存処理
            # from MyDatabase import save_activity_data
            # save_activity_data(activity_data)

            st.success("行動を記録しました。")
            
            # 記録内容を表示（デバッグ用）
            st.write("--- 記録された内容 ---")
            st.write(activity_data)
