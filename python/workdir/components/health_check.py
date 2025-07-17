import streamlit as st
import datetime
from connectDB.MyDatabase import my_open, my_close

def show_health_check():
    st.header("体調入力")

    # ログインしているか確認
    if "personal_number" not in st.session_state or not st.session_state.get("logged_in"):
        st.warning("このページを表示するにはログインが必要です。")
        return

    # --- フォームの作成 ---
    with st.form("health_check_form"):
        today = datetime.date.today()
        st.info(f"日付: {today.strftime('%Y年%m月%d日')}")

        # 学籍番号・氏名（ログイン情報から取得）
        username = st.session_state["username"]
        st.info(f"氏名: {username}")

        st.markdown("---")

        # 体温
        body_temperature = st.number_input("1. 今朝の体温を測定し、記入してください。", min_value=34.0, max_value=42.0, step=0.1, format="%.1f")

        # 体調チェック
        st.markdown("2. 現在、以下の症状はありますか？（あてはまるもの全てにチェック）")
        joint_muscle_pain = st.checkbox("関節・筋肉痛")
        fatigue = st.checkbox("体のだるさ")
        headache = st.checkbox("頭痛")
        sore_throat = st.checkbox("のどの痛み")
        shortness_of_breath = st.checkbox("息苦しさ")
        cough_sneeze = st.checkbox("咳・くしゃみ")
        nausea_vomiting = st.checkbox("吐き気・嘔吐")
        abdominal_pain_diarrhea = st.checkbox("腹痛・下痢")

        st.markdown("3. 最近、味覚・嗅覚に異常はありますか？")
        taste_disorder = st.checkbox("味覚の異常")
        smell_disorder = st.checkbox("嗅覚の異常")

        # 送信ボタン
        submitted = st.form_submit_button("送信")

    # --- 送信後の処理 ---
    if submitted:
        # ログイン情報からpersonal_numberを取得
        personal_number = st.session_state.get("personal_number")
        if not personal_number:
            st.error("ログイン情報が見つかりません。再度ログインしてください。")
            return

        now_time = datetime.datetime.now().time()

        health_data = {
            "personal_number": personal_number,
            "condition_date": today,
            "condition_time": now_time,
            "body_temperature": body_temperature,
            "joint_muscle_pain": joint_muscle_pain,
            "fatigue": fatigue,
            "headache": headache,
            "sore_throat": sore_throat,
            "shortness_of_breath": shortness_of_breath,
            "cough_sneeze": cough_sneeze,
            "nausea_vomiting": nausea_vomiting,
            "abdominal_pain_diarrhea": abdominal_pain_diarrhea,
            "taste_disorder": taste_disorder,
            "smell_disorder": smell_disorder,
            "attendance_suspension": False,  # デフォルト値
            "delflag": False,
            "latupdate": datetime.datetime.now()
        }

        try:
            db_con, cur = my_open()
            if db_con:
                sql = '''
                    INSERT INTO physical_condition (
                        personal_number, condition_date, condition_time, body_temperature,
                        joint_muscle_pain, fatigue, headache, sore_throat, shortness_of_breath,
                        cough_sneeze, nausea_vomiting, abdominal_pain_diarrhea,
                        taste_disorder, smell_disorder, attendance_suspension, delflag, latupdate
                    ) VALUES (
                        %(personal_number)s, %(condition_date)s, %(condition_time)s, %(body_temperature)s,
                        %(joint_muscle_pain)s, %(fatigue)s, %(headache)s, %(sore_throat)s, %(shortness_of_breath)s,
                        %(cough_sneeze)s, %(nausea_vomiting)s, %(abdominal_pain_diarrhea)s,
                        %(taste_disorder)s, %(smell_disorder)s, %(attendance_suspension)s, %(delflag)s, %(latupdate)s
                    )
                '''
                cur.execute(sql, health_data)
                db_con.commit()
                st.success("本日の体調を記録しました。")
                st.balloons()
            else:
                st.error("データベースに接続できませんでした。")
        except Exception as e:
            st.error(f"データの登録中にエラーが発生しました: {e}")
        finally:
            if 'db_con' in locals() and db_con.is_connected():
                my_close(db_con, cur)