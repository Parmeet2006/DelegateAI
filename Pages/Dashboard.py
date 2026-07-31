import streamlit as st
from CallerAgent import fetch_conversation_status
from Pages.DashboardData import dashboard_stats

# function to display dashboard
def page_dashboard():

    st.title("Good Afternoon 👋")
    st.caption("Welcome To Prompt2Phone")
    stats = dashboard_stats()
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📋 Pending", stats["pending"])
    with col2:
        st.metric("✅ Completed", stats["completed"])
    with col3:
        st.metric("📞 Calls", stats["calls"])
    with col4:
        st.metric("📊 Total", stats["total"])
    st.divider()

    if stats["pending"] == 0:

        st.success(
            "✨ You're all caught up!\n\n"
            "DelegateAI doesn't have anything waiting for you."
        )

    else:

        st.info(
            f"""
### 🤖 DelegateAI Summary

You currently have **{stats['pending']}** pending tasks.

📞 Calls : **{stats['calls']}**

📧 Emails : **{stats['emails']}**

💬 Messages : **{stats['messages']}**
"""
        )

    if st.button("Fetch Conversation Status"):
        result = fetch_conversation_status()

        for line in result:
            st.write(line)