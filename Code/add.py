import streamlit as st
from database import load_data_emp,load_data_task,load_data_owner,load_data_vehicle,load_data_sub_task_info
from database import show_only_emp,show_only_task,show_only_owner,show_only_vehicle
def add_data_emp():
    col1,col2 = st.columns(2)
    with col1:
        e_id = st.number_input("Employee ID",step=1)
        phone_no = st.text_input("Phone No")
    with col2:
        f_name = st.text_input("First Name")
        l_name = st.text_input("Last Name")
        
    if st.button("Add Employee Data"):
        load_data_emp(e_id,f_name,l_name,phone_no)
        st.success("Successfully added:{} {}".format(f_name,l_name))
        
def add_data_task():
    col1,col2 = st.columns(2)
    with col1:
        task_id = st.number_input("Task ID",step = 1)
        task_name = st.text_input("Task Name")
        desp = st.text_area("Description")
        vehicle_id = st.selectbox("Vehicle ID",[i[0] for i in show_only_vehicle()])
    with col2:
        task_st = st.selectbox("Task Status",["Assigned","In Progress","Completed"])
        comp_date = st.date_input("Completion Date")
        e_id = st.selectbox("Employee ID",[i[0] for i in show_only_emp()])
    if st.button("Add Task Data"):
        load_data_task(task_id,task_name,desp,task_st,comp_date,e_id,vehicle_id)
        st.success("Successfully added: Task {}".format(task_id))
        
def add_data_owner():
    col1,col2 = st.columns(2)
    with col1:
        owner_id = st.number_input("Owner ID",step = 1)
        name = st.text_input("Name")
        phone_no = st.text_input("Phone No")
    with col2:
        addr = st.text_area("Address")
        
        
    if st.button("Add Owner Details"):
        load_data_owner(owner_id,name,addr,phone_no)
        st.success("Successfully added: {}".format(name))

def add_data_vehicle():
    col1,col2 = st.columns(2)
    with col1:
        vehicle_id = st.number_input("Vehicle ID",step=1)
        owner_id = st.selectbox("Owner ID",[i[0] for i in show_only_owner()])
        prob = st.text_area("Problem")
    with col2:
        make = st.text_input("Make")
        model = st.text_input("Model")
        e_id = st.selectbox("Employee ID",[i[0] for i in show_only_emp()])
        
    if st.button("Add Vehicle Details"):
        load_data_vehicle(vehicle_id,make,model,prob,owner_id,e_id)
        st.success("Successfully added : {}-{}".format(model,vehicle_id))
        
def add_data_sub_task_info():
    col1,col2 = st.columns(2)
    with col1:
        sub_task_id = st.number_input("Sub Task ID",step = 1)
        task_id = st.selectbox("Task ID",[i[0] for i in show_only_task()])
        remarks = st.text_area("Remarks")
           
    with col2:
        part_name = st.text_input("Part Name")
        quantity = st.number_input("Quantity",step=1)
        cost = st.number_input("Cost",step = 0.5)
        
        
    if st.button("Add Sub Task Details"):
        load_data_sub_task_info(sub_task_id,task_id,part_name,quantity,cost,remarks)
        st.success("Successfully added: {}-{}".format(task_id,sub_task_id))