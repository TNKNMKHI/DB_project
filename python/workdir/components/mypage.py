import streamlit as st
import pandas as pd
from components.connectingDB import get_db_connection
from datetime import date, timedelta

def show_mypage(UserName, personal_number):
    st.subheader(f"{UserName}さんのマイページ")

    dbcon, cur = None, None  # 初期化
    try:
        dbcon, cur = get_db_connection()

        # --- 今日の体調・行動記録が未入力かチェック ---
        today = date.today()
        sql_check = """
            SELECT EXISTS (
                SELECT 1 FROM physical_condition 
                WHERE personal_number = %s AND condition_date = %s
            )
        """
        cur.execute(sql_check, (personal_number, today))
        is_health_log_submitted = cur.fetchone()[0]

        sql_check_action = """
            SELECT EXISTS (
                SELECT 1 FROM action_record
                WHERE personal_number = %s AND action_record_date = %s
            )
        """
        cur.execute(sql_check_action, (personal_number, today))
        is_action_log_submitted = cur.fetchone()[0]

        if not is_health_log_submitted or not is_action_log_submitted:
            st.warning("本日の体調・行動記録が未入力です。入力をお願いします。")

        # --- 体調履歴の表示 ---
        st.markdown("### 体調履歴 (直近7日間)")
        seven_days_ago = today - timedelta(days=7)
        sql_health = """
            SELECT condition_date, body_temperature, 
                   GROUP_CONCAT(CASE WHEN joint_muscle_pain THEN '関節痛' END, 
                                CASE WHEN fatigue THEN '倦怠感' END, 
                                CASE WHEN headache THEN '頭痛' END, 
                                CASE WHEN sore_throat THEN '喉の痛み' END, 
                                CASE WHEN cough_sneeze THEN '咳/くしゃみ' END, 
                                CASE WHEN shortness_of_breath THEN '息苦しさ' END, 
                                CASE WHEN nausea_vomiting THEN '吐き気/嘔吐' END, 
                                CASE WHEN abdominal_pain_diarrhea THEN '腹痛/下痢' END, 
                                CASE WHEN taste_disorder THEN '味覚異常' END, 
                                CASE WHEN smell_disorder THEN '嗅覚異常' END
                               ) AS symptoms
            FROM physical_condition 
            WHERE personal_number = %s AND condition_date >= %s
            ORDER BY condition_date DESC
        """
        cur.execute(sql_health, (personal_number, seven_days_ago))
        health_data = cur.fetchall()
        if health_data:
            df_health = pd.DataFrame(health_data, columns=["日付", "体温", "症状"])
            df_health["症状"] = df_health["症状"].fillna("なし")
            st.dataframe(df_health, hide_index=True)
        else:
            st.info("体調履歴はありません。")

        # --- 行動履歴の表示 ---
        st.markdown("### 行動履歴 (直近7日間)")
        sql_activity = """
            SELECT action_record_date, destination, transportation, departure, arrival
            FROM action_record 
            WHERE personal_number = %s AND action_record_date >= %s
            ORDER BY action_record_date DESC
        """
        cur.execute(sql_activity, (personal_number, seven_days_ago))
        activity_data = cur.fetchall()
        if activity_data:
            df_activity = pd.DataFrame(activity_data, columns=["日付", "目的地", "交通手段", "出発地", "到着地"])
            st.dataframe(df_activity, hide_index=True)
        else:
            st.info("行動履歴はありません。")

    except Exception as e:
        st.error(f"データの読み込み中にエラーが発生しました: {e}")
    finally:
        if dbcon and dbcon.is_connected():
            cur.close()
            dbcon.close()

    # --- お知らせ（静的コンテンツ） ---
    st.markdown("### お知らせ")
    st.info("全体: 明日は健康診断があります.\n個人: 提出物の締切は明日です。")

    # --- メニューボタン（ページ遷移はmain.pyで管理） ---
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("体調入力"):
            st.session_state.page = "health_check"
            st.rerun()
        if st.button("出校停止報告"):
            st.session_state.page = "report_stop"
            st.rerun()
    with col2:
        if st.button("行動入力"):
            st.session_state.page = "activity_log"
            st.rerun()
        if st.button("履歴確認"):
            st.session_state.page = "history"
            st.rerun()
    with col3:
        if st.button("個人情報"):
            st.session_state.page = "user_info"
            st.rerun()
