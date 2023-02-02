create database project_garage;

create table Employee(
	employee_id INT,
	f_name varchar(20),
	l_name varchar(20),
	phone_no varchar(10),
	PRIMARY KEY(employee_id)
);


create table Owner(
	owner_id int,
	name varchar(50),
	addr TEXT,
	phone_no varchar(10),
	PRIMARY Key(owner_id)
);

create table Vehicle(
	vehicle_id int,
	make varchar(20),
	model varchar(20),
	Problem TEXT,
	owner_id int,
	employee_id int,
	PRIMARY KEY(vehicle_id),
	FOREIGN KEY(owner_id) REFERENCES Owner(owner_id),
	FOREIGN Key(employee_id) REFERENCES Employee(employee_id)
);

create table Task_info(
	task_id int,
	task_name varchar(30),
	Description TEXT,
	task_status varchar(15),
	Completion_date DATE,
	employee_id int,
	vehicle_id int,
	PRIMARY KEY(task_id),
	FOREIGN KEY(employee_id) REFERENCES Employee(employee_id)
	FOREIGN KEY(vehicle_id) REFERENCES Vehicle(vehicle_id)
);

create table sub_task_info(
	sub_task_id int,
	task_id int,
	part_name varchar(20),
	quantity int,
	cost float(2),
	remarks TEXT,
	PRIMARY KEY(task_id,sub_task_id),
	FOREIGN KEY(task_id) REFERENCES Task_info(task_id)
);

create table Invoice(
	invoice_id int AUTO_INCREMENT,
	invoice_amt float(2),
	total_amt float(2),
	customer_id int,
	task_id int,
	FOREIGN KEY(customer_id) REFERENCES owner(owner_id),
	FOREIGN KEY(task_id) REFERENCES Task_info(task_id),
	PRIMARY KEY(invoice_id)
);

/*function to get the total invoice amount given the owner_id*/

delimiter $$
create function get_invoice_amt(owner_id int)
returns float(2)
begin
	declare amt float(2);
	select sum(total_amt) into amt from Invoice where customer_id = owner_id;
	return amt;
end
$$
delimiter ;
/*Example query of the above function*/ 

select Owner.name,get_invoice_amt(Invoice.customer_id) from Invoice JOIN Owner ON Invoice.customer_id = 
Owner.owner_id;

/*procedure to invoice details to load into Invoice table*/
delimiter $$
create procedure get_invoice(id int)
begin
	declare amt float(2);
	declare total_amt float(2);
	declare customer_id int;
	declare task_id int;
	declare done int default 0;
	declare c cursor for Select 
		sum(sub_task_info.cost),sum(sub_task_info.cost)*1.18,Owner.owner_id,Task_info.task_id 
		from sub_task_info,Owner,Task_info,vehicle where sub_task_info.task_id = Task_info.task_id and 
		Owner.owner_id = vehicle.owner_id and Vehicle.vehicle_id = Task_info.vehicle_id and 
		Task_info.task_id = id group by Task_info.task_id;
	open c;
		fetch c into amt,total_amt,customer_id,task_id;
		insert into Invoice(invoice_id,invoice_amt,total_amt,customer_id,task_id)
		values(NULL,amt,total_amt,customer_id,task_id);
	close c;
end
$$

/*trigger to invoke get_invoice procedure to load Invoice table once a task is marked as 'Completed'*/
delimiter $$
create trigger insert_invoice after update on Task_info for each row
begin
	declare st Varchar(15);
	select task_status into st from Task_info where task_id = old.task_id;
	if st = 'Completed' then
		call get_invoice(old.task_id);
	end if;
end
$$

--Joing tables

/* join query to get the details of the vehicle and the owner */
select Vehicle.vehicle_id,Vehicle.make,Vehicle.model,Vehicle.Problem,Owner.name,Owner.addr,
Owner.phone_no from Vehicle JOIN Owner where Vehicle.owner_id = Owner.owner_id;

/* join query to get task description and sub tasks */
select Task_info.task_name,Task_info.Description,sub_task_info.part_name,sub_task_info.quantity,
sub_task_info.cost,sub_task_info.remarks from Task_info inner join sub_task_info where 
Task_info.task_id = sub_task_info.task_id;

/* join query to get owner and invoice details */
select Owner.name,Owner.phone_no,Invoice.invoice_amt,Invoice.total_amt from Owner inner join Invoice 
where Owner.owner_id = Invoice.customer_id;

/* join query to get task and invoice details */
select Task_info.task_name,Invoice.invoice_amt from Task_info Inner join Invoice where 
Task_info.task_id = Invoice.task_id;

--Aggregate functions

/* count the number of tasks in each status */
select task_status,count(*) as Tasks from Task_info group by task_status;

/* count the number makes of vehicles */
select make,count(*) as Vehicles from Vehicle group by make;

/* count the number of vehicles in each model */
select model,count(*) as Vehicles from Vehicle group by model;

/* count the number tasks by task name */
select task_name,count(*) as Tasks from Task_info group by task_name order by Tasks DESC;

/* find row with max and min invoice amount with customer id*/
select invoice_amt,customer_id from Invoice where invoice_amt = (select max(invoice_amt) from 
Invoice) OR invoice_amt = (select min(invoice_amt) from Invoice);

/* find total amount of all invoices */
select sum(invoice_amt) as Total from Invoice;


--Set operations

/* find vehicles in which the problem is not resolved */
select Vehicle.vehicle_id,Vehicle.make,Vehicle.model,Vehicle.Problem from Vehicle where 
Vehicle.vehicle_id not in (select Vehicle.vehicle_id from Vehicle inner join Task_info where 
Vehicle.vehicle_id = Task_info.vehicle_id and Task_info.task_status = 'completed');

/* find owner who have not paid the bill */
select Owner.name,Owner.phone_no from Owner where Owner.owner_id not in (select Invoice.customer_id 
from Invoice);

/* find employee not in vehicle */
select Employee.employee_id,Employee.f_name,Employee.l_name from Employee where Employee.employee_id 
not in (select Vehicle.employee_id from Vehicle);

/* find task not in invoice */
select Task_info.task_id,Task_info.task_name from Task_info where Task_info.task_id not in 
(select Invoice.task_id from Invoice);

/* find owners with a vehicle using intersect*/
select Owner.name,Owner.phone_no from Owner inner join Vehicle where Owner.owner_id = Vehicle.owner_id