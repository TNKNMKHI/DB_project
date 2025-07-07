import streamlit as st
import datetime

def show_health_check():
    st.header("体調入力")

    # ログインしているか確認
    if "username" not in st.session_state or not st.session_state["logged_in"]:
        st.warning("このページを表示するにはログインが必要です。")
        return

    # --- フォームの作成 ---
    with st.form("health_check_form"):
        # 日付（自動入力）
        today = datetime.date.today()
        st.info(f"日付: {today.strftime('%Y年%m月%d日')}")

        # 学籍番号・氏名（ログイン情報から取得）
        username = st.session_state["username"]
        st.info(f"氏名: {username}") # ここではユーザー名を氏名として扱う

        st.markdown("---")

        # 体温
        temperature = st.number_input("1. 今朝の体温を測定し、記入してください。", min_value=34.0, max_value=42.0, step=0.1, format="%.1f")

        # 体調チェック
        st.markdown("2. 現在、以下の症状はありますか？（あてはまるもの全てにチェック）")
        symptoms = {
            "cough": st.checkbox("咳"),
            "sore_throat": st.checkbox("のどの痛み"),
            "fatigue": st.checkbox("体のだるさ"),
            "shortness_of_breath": st.checkbox("息苦しさ"),
            "headache": st.checkbox("頭痛"),
        }
        other_symptom = st.text_input("その他の症状があれば記入してください。")

        # 味覚・嗅覚
        st.markdown("3. 最近、食べ物の味やにおいを感じにくくなったことがありますか？")
        taste_smell_issue = st.radio("", ("いいえ", "はい"), key="taste_smell", horizontal=True)

        # 同居人の体調
        st.markdown("4. 同居している方に、発熱や風邪の症状がある方はいますか？")
        family_health_issue = st.radio("", ("いいえ", "はい"), key="family_health", horizontal=True)
        
        # その他
        st.markdown("5. その他、気になる点があれば記入してください。")
        other_notes = st.text_area("（自由記述）", height=150)

        # 送信ボタン
        submitted = st.form_submit_button("送信")

    # --- 送信後の処理 ---
    if submitted:
        # ここで入力されたデータをデータベースに保存する処理を呼び出す
        # (今回はダミーで成功メッセージを表示)
        
        # 収集したデータ（例）
        health_data = {
            "date": today,
            "username": username,
            "temperature": temperature,
            "symptoms": [s for s, checked in symptoms.items() if checked],
            "other_symptom": other_symptom,
            "taste_smell_issue": taste_smell_issue == "はい",
            "family_health_issue": family_health_issue == "はい",
            "other_notes": other_notes
        }
        
        # 本来はここでDB保存処理
        # from MyDatabase import save_health_data
        # save_health_data(health_data)
        
        st.success("本日の体調を記録しました。")
        st.balloons()
        
        # フォームの各値を表示（デバッグ用）
        st.write("--- 登録された内容 ---")
        st.write(health_data)
