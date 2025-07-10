import streamlit as st
from datetime import date


def show_report_stop():
    st.subheader("出席停止の情報")

    # 出校停止報告フォーム
    st.markdown("### 出校停止報告")
    reason = st.text_area("出校停止理由")
    start_date = st.date_input("開始日", value=date.today())
    end_date = st.date_input("終了日", value=date.today())
    if st.button("報告"):
        st.success("出校停止を報告しました（ダミー）")

    st.markdown("---")
    # 出校停止履歴（ダミーデータ）
    st.markdown("### 出校停止履歴")
    stop_history = [
        {"開始日": "2025-07-01", "終了日": "2025-07-03", "理由": "発熱"},
        {"開始日": "2025-06-10", "終了日": "2025-06-12", "理由": "インフルエンザ"},
    ]
    st.table(stop_history)

