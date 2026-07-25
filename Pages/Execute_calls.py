from Database import tasks_collection
import streamlit as st
from CallerAgent import execute_pending_calls

# FUNCTION TO CREATE EXECUTE CALLS UI
def page_calls():
    st.title('Execute Calls')
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Execute Pending Calls') :
            result = execute_pending_calls()
            
            for line in result: 
                st.write(line)
    with col2:
        
        if st.button('Fetch Status'):
            st.write('Fetching Status for Tasks.....')
            
        st.divider()
        st.subheader('Task Board')
        
        for task in tasks_collection.find():
            print(task)
            st.write(
                f"{task['title']} - {task['status']} - {task['action']} - {task['name']}"
            )