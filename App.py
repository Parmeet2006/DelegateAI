# Application File
# Prompt2Phone : Type the task. AI makes the call.
import json
import streamlit as st
from Database import save_contacts
from Pages.Save_task import page_tasks
from Pages.Execute_calls import page_calls
from Pages.Dashboard import page_dashboard


def main():
    st.set_page_config(page_title='Agentic', layout='wide', initial_sidebar_state='auto')
    # Save contacts in the database
    # save_contacts()
    dashboard= st.Page(page_dashboard, title='Dashboard', icon='🏠')
    save_tasks= st.Page(page_tasks, title='Save Task', icon='💬')
    execute_calls = st.Page(page_calls, title='Execute Calls', icon='👨')

    pg = st.navigation([dashboard,save_tasks,execute_calls])
    pg.run()

if __name__ == '__main__':
    main()