import streamlit as st
from datetime import date


def show_mypage(UserName):
    st.subheader(f"{UserName}さんのマイページ")

    # 未入力アラート（ダミー）
    st.warning("本日の体調・行動記録が未入力です。入力をお願いします。")

    # 体調履歴（ダミーデータ）
    st.markdown("### 体調履歴")
    health_data = [
        {"日付": "2025-07-09", "体温": "36.5", "症状": "なし"},
        {"日付": "2025-07-08", "体温": "36.7", "症状": "咳"},
    ]
    st.table(health_data)

    # 行動履歴（ダミーデータ）
    st.markdown("### 行動履歴")
    activity_data = [
        {"日付": "2025-07-09", "行動": "自宅"},
        {"日付": "2025-07-08", "行動": "出校"},
    ]
    st.table(activity_data)

    # お知らせ（ダミーデータ）
    st.markdown("### お知らせ")
    st.info("全体: 明日は健康診断があります。\n個人: 提出物の締切は明日です。")

    # メニューボタン
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("体調入力")
        st.button("出校停止報告")
    with col2:
        st.button("行動入力")
        st.button("履歴確認")
    with col3:
        st.button("個人情報")
