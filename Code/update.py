import streamlit as st
import pandas as pd
from database import show_data_emp,show_only_emp,show_based_on_emp,edit_data_emp
from database import show_data_task,show_only_task,show_based_on_task,edit_data_task
from database import show_data_owner,show_only_owner,show_based_on_owner,edit_data_owner
from database import show_data_vehicle,show_only_vehicle,show_based_on_vehicle,edit_data_vehicle
from database import show_data_sub_task_info,show_based_on_sub_task_info,edit_data_sub_task_info

def update_data_emp():
    table = show_data_emp()
    df = pd.DataFrame(table,columns = ["Employee ID","First Name","Last Name","Phone No"])
    with st.expander("Employee Data"):
        st.dataframe(df)
    
    list_of_emp = [i[0] for i in show_only_emp()]
    select_emp = st.selectbox("Employee to Edit",list_of_emp)
    selected_emp = show_based_on_emp(select_emp)
    if selected_emp:
        e_id = selected_emp[0][0]
        f_name = selected_emp[0][1]
        l_name = selected_emp[0][2]
        phone_no = selected_emp[0][3]
    
        col1,col2 = st.columns(2)
        with col1:
            new_e_id = st.number_input("Employee ID",e_id,disabled=True,step=1)
            new_phone_no = st.text_input("Phone No",phone_no)
        with col2:
            new_f_name = st.text_input("First Name",f_name)
            new_l_name = st.text_input("Last Name",l_name)
            
        if st.button("Update Employee"):
            edit_data_emp(new_f_name,new_l_name,new_phone_no,e_id)
            st.success("Successfully updated:{} {}".format(f_name,l_name))
        
        result = show_data_emp()
        df = pd.DataFrame(result,columns = ["Employee ID","First Name","Last Name","Phone No"])
        with st.expander("Updated data"):
            st.dataframe(df)

def update_data_task():
    table = show_data_task()
    df = pd.DataFrame(table,columns = ["Task_ID","Task Name","Description","Task Status","Completion Date","Employee Assigned","Vehicle ID"])
    with st.expander("Current Tasks"):
        st.dataframe(df)
    
    list_of_task = [i[0] for i in show_only_task()]
    select_task = st.selectbox("Task to Edit",list_of_task)
    selected_task = show_based_on_task(select_task)
    if selected_task:
        task_id = selected_task[0][0]
        task_name = selected_task[0][1]
        desp = selected_task[0][2]
        task_st = selected_task[0][3]
        comp_date = selected_task[0][4]
        e_id = selected_task[0][5]
        vehicle_id = selected_task[0][6]
        
        col1,col2 = st.columns(2)
        with col1:
            new_task_id = st.number_input("Task ID",task_id,disabled=True,step=1)
            new_task_name = st.text_input("Task Name",task_name)
            new_desp = st.text_area("Description",desp)
        with col2:
            choices = ["Assigned","In Progress","Completed"]
            new_task_st = st.selectbox("Task Status",choices,index=choices.index(task_st))
            new_comp_date = st.date_input("Completion Date",comp_date)
            # new_e_id = st.number_input("Employee Assigned",e_id)
            new_e_id = st.selectbox("Employee Assigned",[i[0] for i in show_only_emp()],index = [i[0] for i in show_only_emp()].index(e_id))
            new_vehicle_id = st.selectbox("Vehicle ID",[i[0] for i in show_only_vehicle()],disabled=True,index=[i[0] for i in show_only_vehicle()].index(vehicle_id))
            
        if st.button("Update Tasks"):
            edit_data_task(new_task_name,new_desp,new_task_st,new_comp_date,new_e_id,task_id)
            st.success("Successfully updated: Task {}".format(new_task_id))
def update_data_owner():
    table = show_data_owner()
    df = pd.DataFrame(table,columns=["Owner ID","Name","Address","Phone No"])
    with st.expander("Owner Details"):
        st.dataframe(df)
        
    list_of_owner = [(i[0],i[1]) for i in show_only_owner()]
    select_owner = st.selectbox("Owner to edit details of",list_of_owner)
    selected_owner = show_based_on_owner(select_owner[0])
    if selected_owner:
        owner_id = selected_owner[0][0]
        name = selected_owner[0][1]
        addr = selected_owner[0][2]
        phone_no = selected_owner[0][3]
        
    col1,col2 = st.columns(2)
    with col1:
        new_owner_id = st.number_input("Owner ID",owner_id,disabled=True,step=1)
        new_name = st.text_input("Name",name)
        new_phone_no = st.text_input("Phone No",phone_no)
    with col2:
        new_addr = st.text_area("Address",addr)
        
        
    if st.button("Update Owner Details"):
        edit_data_owner(new_name,new_addr,new_phone_no,owner_id)
        st.success("Successfully updated: Task {}".format(new_owner_id))

def update_data_vehicle():
    table = show_data_vehicle()
    df = pd.DataFrame(table,columns = ["Vehicle ID","Make","Model","Problem","Owner ID","Employee ID"])
    with st.expander("Vehicle Details"):
        st.dataframe(df)
    
    list_of_vehicle = [i[0] for i in show_only_vehicle()]
    select_vehicle = st.selectbox("Vehicle to edit details of",list_of_vehicle)
    selected_vehicle = show_based_on_vehicle(select_vehicle)
    if selected_vehicle:
        vehicle_id = selected_vehicle[0][0]
        make = selected_vehicle[0][1]
        model = selected_vehicle[0][2]
        prob = selected_vehicle[0][3]
        owner_id = selected_vehicle[0][4]
        e_id = selected_vehicle[0][5]
    
    col1,col2 = st.columns(2)
    with col1:
        vehicle_id = st.number_input("Vehicle ID",vehicle_id,disabled=True)
        new_owner_id = st.selectbox("Owner ID",[i[0] for i in show_only_owner()],disabled=True)
        new_prob = st.text_area("Problem",prob)
    with col2:
        new_make = st.text_input("Make",make)
        new_model = st.text_input("Model",model)
        new_e_id = st.selectbox("Employee ID",[i[0] for i in show_only_emp()])
    if st.button("Update Vehicle Details"):
        edit_data_vehicle(new_make,new_model,new_prob,new_owner_id,new_e_id,vehicle_id)
        st.success("Successfully Updated : {}-{}".format(model,vehicle_id))

def update_data_sub_task_info():
    table = show_data_sub_task_info()
    df = pd.DataFrame(table,columns = ["Sub Task ID","Task ID","Part Name","Quantity","Cost","Remarks"])
    with st.expander("Sub Task Details"):    
        st.dataframe(df)
    list_of_sub_task_info = [(i[1],i[0]) for i in show_data_sub_task_info()]
    select_sub_task_info = st.selectbox("sub task details to edit",list_of_sub_task_info)
    selected_sub_task_info = show_based_on_sub_task_info(select_sub_task_info[1],select_sub_task_info[0])
    
    if selected_sub_task_info:
        sub_task_id = selected_sub_task_info[0][0]
        task_id = selected_sub_task_info[0][1]
        part_name = selected_sub_task_info[0][2]
        quantity = selected_sub_task_info[0][3]
        cost = selected_sub_task_info[0][4]
        remarks = selected_sub_task_info[0][5]
        
    col1,col2 = st.columns(2)
    with col1:
        sub_task_id = st.number_input("Sub Task ID",sub_task_id,disabled=True)
        task_id = st.number_input("Task ID",task_id,disabled=True)
        new_remarks = st.text_area("Remarks",remarks) 
    with col2:
        new_part_name = st.text_input("Part Name",part_name)
        new_quantity = st.number_input("Quantity",quantity,step = 1)
        new_cost = st.number_input("Cost",cost,step = 0.5)
        
    if st.button("Update Sub Task Details"):
        edit_data_sub_task_info(new_part_name,new_quantity,new_cost,new_remarks,sub_task_id,task_id)
        st.success("Successfully added: {}-{}".format(task_id,sub_task_id))