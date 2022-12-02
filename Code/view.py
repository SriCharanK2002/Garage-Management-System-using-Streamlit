import streamlit as st
import pandas as pd
from database import show_data_emp,show_data_task,show_data_owner,show_data_vehicle,show_data_sub_task_info

def view_data_emp():
    res = show_data_emp()
    df = pd.DataFrame(res,columns = ["Employee ID","First Name","Last Name","Phone No"])
    
    # df = df[["Employee ID","First Name","Last Name","Phone No"]]
    st.dataframe(df)

def view_data_task():
    table = show_data_task()
    df = pd.DataFrame(table,columns = ["Task_ID","Task Name","Description","Task Status","Completion Date","Employee Assigned","Vehicle ID"])
    # df = [["Task_ID","Task Name","Description","Task Status","Completion Date","Employee Assigned"]]
    st.dataframe(df)

def view_data_owner():
    table = show_data_owner()
    df = pd.DataFrame(table,columns=["Owner ID","Name","Address","Phone No"])
    st.dataframe(df)

def view_data_vehicle():
    table = show_data_vehicle()
    df = pd.DataFrame(table,columns = ["Vehicle ID","Make","Model","Problem","Owner ID","Employee ID"])
    st.dataframe(df)

def view_data_sub_task_info():
    table = show_data_sub_task_info()
    df = pd.DataFrame(table,columns = ["Sub Task ID","Task ID","Part Name","Quantity","Cost","Remarks"])
    st.dataframe(df)
    