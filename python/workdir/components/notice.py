import streamlit as st
from datetime import datetime


def show_notice(UserName=None, is_admin=False):
    """お知らせページを表示する関数
    UserName: ユーザー名（個人お知らせ用）
    is_admin: 管理者フラグ
    """
    st.subheader("お知らせ")

    # 全体お知らせ（ダミーデータ）
    st.markdown("#### 全体お知らせ")
    all_notices = [
        {"日付": "2025-07-10", "内容": "明日は健康診断があります。"},
        {"日付": "2025-07-08", "内容": "夏季休暇のお知らせ。"},
    ]
    for n in all_notices:
        st.info(f"[{n['日付']}] {n['内容']}")

    # 個人お知らせ（ダミーデータ）
    st.markdown("#### 個人お知らせ")
    personal_notices = [
        {"日付": "2025-07-10", "内容": f"{UserName}さん、提出物の締切は明日です。"}
    ] if UserName else []
    for n in personal_notices:
        st.success(f"[{n['日付']}] {n['内容']}")

    # 管理者向け：お知らせ投稿フォーム
    if is_admin:
        st.markdown("---")
        st.markdown("#### お知らせ投稿（管理者用）")
        notice_type = st.radio("投稿先", ("全体", "個人"))
        content = st.text_area("お知らせ内容")
        if notice_type == "個人":
            target_user = st.text_input("対象ユーザー名")
        else:
            target_user = None
        if st.button("投稿"):
            st.success("お知らせを投稿しました（ダミー）")
