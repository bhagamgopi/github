
employee = {} 
team = {}
 
def add_employee():
    emp_id = input("\tEnter employee id")
    if emp_id not in employee.keys():
        employee[emp_id] ={
	    "name":input("\tEnter name: "),
	    "age":int(input("\tEnter age :")),
	    "gender":input("\tEnter the gender :"),
	    "salary":int(input("\tEnter salary: "))
	     }
    else:
        print("\tSerial No already Taken")

def delete_employee ():
    emp_id = input("\tEnter employee id :")
    if emp_id not in employee.keys():
        print("\tWrong emp_id")
    else:
        del employee[emp_id]
        print("\t employee is succesfully deleted ")

def search_emp_by_name():
        name = input("\t\tEnter employee  name ")       
        flag = False
        for i in employee.values():
                if i["name"] == name: 
                        print(f"\t\t{i['name']} | {i['age']} | {i['gender']}  | {i['salary']}")
                        flag = True
                        break
        if flag == False :
                print("\t\tNot flag")
def change_employee_data ():
    print("\t1.chnage by name")
    print("\t2.change by age")
    print("\t3.change by gender")
    print("\t4.change by salary")
    print("\t5.exit")

def change_employee_name():
    emp_id = input("\tEnter employee id:")
    if emp_id not in employee.keys():
        print("\tWrong employee id")
    else:
        employee[emp_id]['name'] = input("\tEnter new employee  name")
        print("\t employee name changed successfully")
def change_employee_age():
    emp_id = input("\tEnter employee id :")
    if emp_id not in employee.keys():
        print("\tWrong employee id")
    else:
        employee[emp_id]['age'] = int(input("\tEnter new employee age"))
        print("\t employee age changed successfully")
def change_employee_gender():
    emp_id= input("\tEnter employee id:")
    if emp_id not in employee.keys():
        print("\tWrong employee id")
    else:
        employee[emp_id]['gender'] = input("\tEnter new employee gender")
        print("\t employee gender changed successfully")

def change_employee_salary():
    emp_id = input("\tEnter employee id")
    if emp_id not in employee.keys():
        print("\tWrong employee id")
    else:
        employee[emp_id]['salary'] = input("\tEnter new employee  salary")
        print("\t employee salary  changed successfully")

def change_employee():
	while True:
		change_employee_data()
		ch = int(input("\tEnter your choice"))
		if ch == 1:
			change_employee_name()
		elif ch == 2:
	
			change_employee_age()
		elif ch == 3:
			
			change_employee_gender()
		elif ch == 4:
			change_employee_salary()
		elif ch ==5:
			break
		else:
			print("Invalid choice")	

def display_employee():
    for serial,employe in employee.items():
        print(f"\t{serial} | {employe['name']} | {employe['age']} | {employe['gender']} | {employe['salary']} ")

def main_menu():
    print("1. Add employee")
    print("2. Delete employee")
    print("3. Search employee")
    print("4. Display all employee")
    print("5. Change a employee name in the list") 
    print("6. Manage All team")
    print("7. exit")

def manage_all_team_menu():
    print("\t1.Create team")
    print("\t2.Display team")
    print("\t3.Manage team(Particular)")
    print("\t4.Delete team")
    print("\t5.Exit")

def manage_all_team():
	while True:
		manage_all_team_menu()
		ch = int(input("\tEnter your choice "))
		if ch == 1:
			create_team()
		elif ch == 2:
			display_team()
		elif ch == 3:
			manage_team()
		elif ch == 4:
			delete_team()
		elif ch == 5:
			break
		else:
			print("\tInvalid choice")	

def create_team():
    team_name = input("\tEnter team  name: ")
    team[team_name] = []
    print(f'{team_name} team created successfully ')

def delete_team():
    team_name = input("\tEnter team name: ")
    if team_name in team.keys():
        del team[team_name]
               
    else:
        print("\tWrong  team")



def display_team():
    for key,value in team.items():
        name_string = ""
        for i in value:
            name_string = name_string +"|"+employee[i]["name"]
        print(f"{key} ===> {name_string}")
  

def manage_team_menu():
    print("\t\t1.Add Member")
    print("\t\t2.Delete Member")
    print("\t\t3.display Members")


def add_member(team_name):
 
    emp_id = input("\t\tEnter the employee id of emloyee ")
    if emp_id in employee.keys():
        team[team_name].append(serial_no)
    else:
        print("\t\tWrong employee id")

def display_member(team_name):
    name_string=""
    for i in team[team_name]:
        name_string = name_string +"|"+i+"."+employee[i]["name"]
    print(f"{name_string}")

def delete_member(team_name):
    emp_id = int(input('\t\tEnter employee id: '))
    if emp_id not in team[team_name]:
        print("\t\t wrong employee id")
    else:
        team[team_name].remove(emp_id)
        print("employee removed from team")


def manage_team():
    team_name = input("\t\tEnter team name ")
    manage_team_menu()
    ch = int(input("\t\t Enter your Choice "))
    if ch == 1:
        add_member(team_name)
    elif ch == 2:
        display_member(team_name)
    elif ch == 3:
        delete_member(team_name)
    else:
        print("\tInvalid choice")
    
while True:
	main_menu()
	ch = int(input("Enter your choice:"))

	if ch == 1:
		add_employee()
	elif ch == 2:
		delete_employee()
	elif ch == 3:
		search_employee()
	elif ch == 4:
		display_employee()
	elif ch == 5:
		change_employee_name()
	elif ch == 6:
		manage_all_team()
	elif ch == 7:
		break;
	else:
		print("Invalid Choice")






























