import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="project_garage"
)

c = db.cursor()

# Employee Table

def show_data_emp():
    c.execute("Select * from employee")
    data = c.fetchall()
    return data

def show_only_emp():
    c.execute("Select employee_id from employee")
    data = c.fetchall()
    return data

def show_based_on_emp(e_id):
    c.execute("Select * from employee where employee_id = {}".format(e_id))
    data = c.fetchall()
    return data

def load_data_emp(e_id,f_name,l_name,phone_no):
    c.execute("Insert into employee(employee_id,f_name,l_name,phone_no) values(%s,%s,%s,%s)",(e_id,f_name,l_name,phone_no))
    db.commit()

def edit_data_emp(new_f_name,new_l_name,new_phone_no,e_id):
    c.execute("Update employee set f_name = %s,l_name = %s,phone_no = %s where employee.employee_id = %s",(new_f_name,new_l_name,new_phone_no,e_id))
    data = c.fetchall()
    db.commit()
    return data

def rm_data_emp(e_id):
    c.execute("Delete from employee where employee_id = '{}'".format(e_id))
    db.commit()


# Task Info Table
def show_data_task():
    c.execute("Select * from task_info")
    data = c.fetchall()
    return data

def show_only_task():
    c.execute("Select task_id from task_info")
    data = c.fetchall()
    return data

def show_based_on_task(task_id):
    c.execute("Select * from task_info where task_id = {}".format(task_id))
    data = c.fetchall()
    return data
    
def load_data_task(task_id,task_name,desp,task_st,comp_date,e_id,vehicle_id):
    c.execute("Insert into task_info(task_id,task_name,Description,task_status,Completion_date,employee_id,vehicle_id) values(%s,%s,%s,%s,%s,%s,%s)",(task_id,task_name,desp,task_st,comp_date,e_id,vehicle_id))
    db.commit()
    
def edit_data_task(new_task_name,new_desp,new_task_st,new_comp_date,new_e_id,task_id):
    c.execute("Update task_info set task_name = %s,Description = %s,task_status = %s,Completion_date = %s,employee_id = %s where task_id = %s",(new_task_name,new_desp,new_task_st,new_comp_date,new_e_id,task_id))
    data = c.fetchall()
    db.commit()
    return data

def rm_data_task(task_id):
    c.execute("Delete from task_info where task_id = {}".format(task_id))
    db.commit()

# Owner Table

def show_data_owner():
    c.execute("Select * from owner")
    data = c.fetchall()
    return data

def show_only_owner():
    c.execute("Select owner_id,name from owner")
    data = c.fetchall()
    return data

def show_based_on_owner(owner_id):
    c.execute("Select * from owner where owner_id = {}".format(owner_id))
    data = c.fetchall()
    return data    

def load_data_owner(owner_id,name,addr,phone_no):
    c.execute("Insert into owner(owner_id,name,addr,phone_no) values(%s,%s,%s,%s)",(owner_id,name,addr,phone_no))
    db.commit()
    
def edit_data_owner(new_name,new_addr,new_phone_no,owner_id):
    c.execute("Update owner set name = %s,addr = %s,phone_no = %s where owner_id = %s",(new_name,new_addr,new_phone_no,owner_id))
    data = c.fetchall()
    db.commit()
    return data
    
def rm_data_owner(owner_id):
    c.execute("Delete from owner where owner_id = {}".format(owner_id))
    db.commit()

#Vehicle Table
def show_data_vehicle():
    c.execute("Select * from vehicle")
    data = c.fetchall()
    return data    

def show_only_vehicle():#vehicle_id only
    c.execute("Select vehicle_id from vehicle")
    data = c.fetchall()
    return data

def show_based_on_vehicle(vehicle_id):
    c.execute("Select * from vehicle where vehicle_id = {}".format(vehicle_id))
    data = c.fetchall()
    return data    

def load_data_vehicle(vehicle_id,make,model,prob,owner_id,e_id):
    c.execute("Insert into vehicle(vehicle_id,make,model,Problem,owner_id,employee_id) values(%s,%s,%s,%s,%s,%s)",(vehicle_id,make,model,prob,owner_id,e_id))
    db.commit()
    
def edit_data_vehicle(new_make,new_model,new_prob,new_owner_id,new_e_id,vehicle_id):
    c.execute("Update vehicle set make = %s,model = %s,problem = %s,owner_id = %s,employee_id = %s where vehicle_id = %s",(new_make,new_model,new_prob,new_owner_id,new_e_id,vehicle_id))
    data = c.fetchall()
    db.commit()
    return data

def rm_data_vehicle(vehicle_id):
    c.execute("Delete from vehicle where vehicle_id = {}".format(vehicle_id))
    db.commit()

# Task Details Table
def show_data_sub_task_info():
    c.execute("Select * from sub_task_info")
    data = c.fetchall()
    return data

def show_only_sub_task_info():
    c.execute("Select sub_task_id,task_id from sub_task_info")
    data = c.fetchall()
    return data

def show_based_on_sub_task_info(sub_task_id,task_id):
    c.execute("Select * from sub_task_info where sub_task_id = %s AND task_id = %s",(sub_task_id,task_id))
    data = c.fetchall()
    return data

def load_data_sub_task_info(sub_task_id,task_id,part_name,quantity,cost,remarks):
    c.execute("Insert into sub_task_info(sub_task_id,task_id,part_name,quantity,cost,remarks) values(%s,%s,%s,%s,%s,%s)",(sub_task_id,task_id,part_name,quantity,cost,remarks))
    db.commit()
    
def edit_data_sub_task_info(new_part_name,new_quantity,new_cost,new_remarks,sub_task_id,task_id):
    c.execute("Update sub_task_info set part_name = %s,quantity = %s,cost = %s,remarks = %s where sub_task_id = %s and task_id = %s",(new_part_name,new_quantity,new_cost,new_remarks,sub_task_id,task_id))
    data = c.fetchall()
    db.commit()
    return data

def rm_data_sub_task_info(sub_task_id,task_id):
    c.execute("Delete from teask_details where sub_task_id = %s and task_id = %s",(sub_task_id,task_id))
    db.commit()
