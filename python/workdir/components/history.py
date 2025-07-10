import streamlit as st
import pandas as pd

def show_history():
    st.header("履歴確認")

    tabs = st.tabs(["体調履歴", "行動履歴", "出校停止履歴"])

    # 体調履歴（ダミーデータ）
    with tabs[0]:
        st.markdown("#### 体調履歴")
        health_df = pd.DataFrame([
            {"日付": "2025-07-09", "体温": "36.5", "症状": "なし"},
            {"日付": "2025-07-08", "体温": "36.7", "症状": "咳"},
        ])
        st.dataframe(health_df)
        st.download_button("CSVダウンロード", data=health_df.to_csv(index=False), file_name="health_history.csv")

    # 行動履歴（ダミーデータ）
    with tabs[1]:
        st.markdown("#### 行動履歴")
        activity_df = pd.DataFrame([
            {"日付": "2025-07-09", "行動": "自宅"},
            {"日付": "2025-07-08", "行動": "出校"},
        ])
        st.dataframe(activity_df)
        st.download_button("CSVダウンロード", data=activity_df.to_csv(index=False), file_name="activity_history.csv")

    # 出校停止履歴（ダミーデータ）
    with tabs[2]:
        st.markdown("#### 出校停止履歴")
        stop_df = pd.DataFrame([
            {"開始日": "2025-07-01", "終了日": "2025-07-03", "理由": "発熱"},
            {"開始日": "2025-06-10", "終了日": "2025-06-12", "理由": "インフルエンザ"},
        ])
        st.dataframe(stop_df)
        st.download_button("CSVダウンロード", data=stop_df.to_csv(index=False), file_name="stop_history.csv")
