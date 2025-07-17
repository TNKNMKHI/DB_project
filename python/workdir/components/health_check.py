import streamlit as st
import datetime
from components.connectingDB import get_db_connection
from connectDB.MyDatabase import my_open, my_close

def show_health_check():
    st.header("体調入力")

    if "personal_number" not in st.session_state or not st.session_state.get("logged_in"):
        st.warning("このページを表示するにはログインが必要です。")
        return

    personal_number = st.session_state["personal_number"]
    username = st.session_state["username"]

    with st.form("health_check_form", clear_on_submit=True):
        today = datetime.date.today()
        now = datetime.datetime.now().time()
        st.info(f"日付: {today.strftime('%Y年%m月%d日')}")
        st.info(f"氏名: {username}")

        st.markdown("---")

        body_temperature = st.number_input("1. 今朝の体温（℃）", min_value=34.0, max_value=42.0, step=0.1, format="%.1f")

        st.markdown("2. 現在、以下の症状はありますか？（あてはまるもの全てにチェック）")
        col1, col2 = st.columns(2)
        with col1:
            joint_muscle_pain = st.checkbox("関節・筋肉の痛み")
            fatigue = st.checkbox("体のだるさ（倦怠感）")
            headache = st.checkbox("頭痛")
            sore_throat = st.checkbox("のどの痛み")
            cough_sneeze = st.checkbox("咳、くしゃみ")
        with col2:
            shortness_of_breath = st.checkbox("息苦しさ")
            nausea_vomiting = st.checkbox("吐き気・嘔吐")
            abdominal_pain_diarrhea = st.checkbox("腹痛・下痢")
            taste_disorder = st.checkbox("味覚の異常")
            smell_disorder = st.checkbox("嗅覚の異常")

        # 出校可否の判定（仮）
        symptoms_checked = any([
            joint_muscle_pain, fatigue, headache, sore_throat, cough_sneeze,
            shortness_of_breath, nausea_vomiting, abdominal_pain_diarrhea,
            taste_disorder, smell_disorder
        ])
        high_fever = body_temperature >= 37.5
        attendance_suspension = high_fever or symptoms_checked

        if attendance_suspension:
            st.warning("指定の症状または37.5℃以上の発熱が確認されたため、「出校停止」となります。速やかに出校停止報告を行ってください。")

        submitted = st.form_submit_button("送信")

    if submitted:
        try:
            dbcon, cur = get_db_connection()
            sql = """
                INSERT INTO physical_condition (
                    personal_number, condition_date, condition_time, body_temperature,
                    joint_muscle_pain, fatigue, headache, sore_throat, shortness_of_breath,
                    cough_sneeze, nausea_vomiting, abdominal_pain_diarrhea,
                    taste_disorder, smell_disorder, attendance_suspension, lastupdate
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
            """
            values = (
                personal_number, today, now, body_temperature,
                joint_muscle_pain, fatigue, headache, sore_throat, shortness_of_breath,
                cough_sneeze, nausea_vomiting, abdominal_pain_diarrhea,
                taste_disorder, smell_disorder, attendance_suspension
            )
            cur.execute(sql, values)
            dbcon.commit()
            st.success("本日の体調を記録しました。")
            st.balloons()
        except Exception as e:
            st.error(f"データベースへの登録中にエラーが発生しました: {e}")
        finally:
            if 'dbcon' in locals() and dbcon.is_connected():
                cur.close()
                dbcon.close()
