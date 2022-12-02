import streamlit as st
from add import add_data_emp,add_data_task,add_data_owner,add_data_vehicle,add_data_sub_task_info
from view import view_data_emp,view_data_task,view_data_owner,view_data_vehicle,view_data_sub_task_info
from update import update_data_emp,update_data_task,update_data_owner,update_data_vehicle,update_data_sub_task_info
from delete import del_data_emp,del_data_task,del_data_owner,del_data_vehicle,del_data_sub_task_info

def main():
    st.title("Garage Management")
    tables = ['Employees','Task Info','Sub Task Details','Owners','Vehicles']
    choice1 = st.sidebar.selectbox("Tables",tables)
    
    op = ['Add','View','Update','Delete']
    choice2 = st.sidebar.selectbox("Operations",op)
    
    if choice1 == 'Employees':
        st.subheader("Employees Details")
    elif choice1 == 'Task Info':
        st.subheader("Tasks")
    elif choice1 == "Owners":
        st.subheader("Owners Details")
    elif choice1 == "Vehicles":
        st.subheader("Vehicles")
    elif choice1 == "Sub Task Details":
        st.subheader("Sub Task Details")
    
    if choice2 == "Add":
        match choice1:
            case 'Employees':add_data_emp()
            case 'Task Info':add_data_task()
            case 'Owners':add_data_owner()
            case 'Vehicles':add_data_vehicle()
            case 'Sub Task Details':add_data_sub_task_info()
    
    elif choice2 == "View":
        match choice1:
            case 'Employees':view_data_emp()
            case 'Task Info':view_data_task()
            case 'Owners':view_data_owner()
            case 'Vehicles':view_data_vehicle()
            case 'Sub Task Details':view_data_sub_task_info()
            
    elif choice2 == "Update":
        match choice1:
            case 'Employees':update_data_emp()
            case 'Task Info':update_data_task()
            case 'Owners':update_data_owner()
            case 'Vehicles':update_data_vehicle()
            case 'Sub Task Details':update_data_sub_task_info()
    
    elif choice2 == "Delete":
        match choice1:
            case 'Employees':del_data_emp()
            case 'Task Info':del_data_task()
            case 'Owners':del_data_owner()
            case 'Vehicles':del_data_vehicle()
            case 'Sub Task Details':del_data_sub_task_info()

if __name__ == "__main__":
    main()
