import streamlit as st
import pandas as pd
from database import show_data_emp,rm_data_emp,show_only_emp
from database import show_data_task,rm_data_task,show_only_task
from database import show_data_owner,rm_data_owner,show_only_owner
from database import show_data_vehicle,rm_data_vehicle,show_only_vehicle,show_based_on_vehicle
from database import show_data_sub_task_info,rm_data_sub_task_info,show_based_on_sub_task_info

def del_data_emp():
    table = show_data_emp()
    df = pd.DataFrame(table,columns = ["Employee ID","First Name","Last Name","Phone No"])
    with st.expander("Employee Data"):
        st.dataframe(df)
        
    list_of_emp = [i[0] for i in show_only_emp()]
    selected_emp = st.selectbox("Employee to delete",list_of_emp)
    # selected_emp = show_based_on_emp(select_emp)
    st.warning("Do you want to delete '{}'??".format(selected_emp))
    
    if st.button("Delete Employee"):
        rm_data_emp(selected_emp)
        st.success("Deleted Successfully")
    result = show_data_emp()
    df = pd.DataFrame(result,columns = ["Employee ID","First Name","Last Name","Phone No"])
    with st.expander("Updated Data"):
        st.dataframe(df)

def del_data_task():
    table = show_data_task()
    df = pd.DataFrame(table,columns = ["Task_ID","Task Name","Amount","Description","Task Status","Completion Date","Employee Assigned"])
    with st.expander("Current Tasks"):
        st.dataframe(df)
    
    list_of_task = [i[0] for i in show_only_task()]
    selected_task = st.selectbox("Task to delete",list_of_task)
    # selected_task = show_based_on_task(select_task)
    st.warning("Do you want to delete {}?".format(selected_task))
    
    if st.button("Delete Task"):
        rm_data_task(selected_task)
        st.success("Deleted Successfully")
    result = show_data_task()    
    df = pd.DataFrame(result,columns = ["Task_ID","Task Name","Amount","Description","Task Status","Completion Date","Employee Assigned"])
    with st.expander("Current Tasks"):
        st.dataframe(df)
    

def del_data_owner():
    table = show_data_owner()
    df = pd.DataFrame(table,columns=["Owner ID","Name","Address","Phone No"])
    with st.expander("Owner Details"):
        st.dataframe(df)
    list_of_owner = [i[0] for i in show_only_owner()]
    selected_owner = st.selectbox("Owner to delete details",list_of_owner)
    # selected_owner = show_based_on_owner(select_owner)
    st.warning("Do you want to delete {}?".format(selected_owner))
    
    if st.button("Delete Owner Details"):
        rm_data_owner(selected_owner)
        st.success("Deleted Successfully")
    result = show_data_owner()
    df = pd.DataFrame(result,columns=["Owner ID","Name","Address","Phone No"])
    with st.expander("Owner Details"):
        st.dataframe(df)

def del_data_vehicle():
    table = show_data_vehicle()
    df = pd.DataFrame(table,columns = ["Vehicle ID","Make","Model","Problem","Owner ID","Task ID","Employee ID"])
    with st.expander("Vehicle Details"):
        st.dataframe(df)
    list_of_vehicle = [i[0] for i in show_only_vehicle()]
    selected_vehicle = st.selectbox("Vehicle to delete",list_of_vehicle)
    selected_vehicle = show_based_on_vehicle(selected_vehicle)
    if selected_vehicle:
        vehicle_id = selected_vehicle[0][0]
        model = selected_vehicle[0][2]
    st.warning("Do you want to delete {}-{}?".format(vehicle_id,model))
    if st.button("Delete Vehicle Details"):
        rm_data_vehicle(vehicle_id)
        st.success("Deleted Successfully")
    result = show_data_vehicle()
    df = pd.DataFrame(result,columns = ["Vehicle ID","Make","Model","Problem","Owner ID","Task ID","Employee ID"])
    with st.expander("Vehicle Details"):
        st.dataframe(df)
    

def del_data_sub_task_info():
    table = show_data_sub_task_info()
    df = pd.DataFrame(table,columns = ["Sub Task ID","Task ID","Part Name","Quantity","Cost","Remarks"])
    with st.expander("Sub Task Details"):    
        st.dataframe(df)
        
    list_of_sub_sub_task_info = [(i[1],i[0]) for i in show_data_sub_task_info()]
    
    select_sub_task_info = st.selectbox("sub task details to edit",list_of_sub_sub_task_info)
    selected_sub_task_info = show_based_on_sub_task_info(select_sub_task_info[1],select_sub_task_info[0])
    if selected_sub_task_info:
        sub_task_id = selected_sub_task_info[0][0]
        task_id = selected_sub_task_info[0][1]
    st.warning("Do you want to delete {}-{}".format(task_id,sub_task_id))
    if st.button("Delete Sub Task"):
        rm_data_sub_task_info(sub_task_id,task_id)
        st.success("Deleted Successfully")
    result = show_data_sub_task_info()
    df = pd.DataFrame(result,columns = ["Sub Task ID","Task ID","Part Name","Quantity","Cost","Remarks"])
    st.dataframe(df)
    