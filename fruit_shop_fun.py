fruit = {}
add_cart=[]

def Menu(): 
	print("1. Add fruit :")
	print("2. Delete fruit :")
	print("3. search fruit  name and rate:")
	print("4. change a fruit name and rate:")
	print("5. display all fruit:")
	print("6. add a fruit in cart :")
	print("7. display cart :")
	print("8. exit")
def add_fruit():
	fruit_id = input("\tEnter fruit id :")
	if fruit_id not in fruit.keys():
		name = input("\tEnter fruit name: ")
		rate = int(input("\tEnter fruit rate: "))
		import_from= input("\tEnter the fruit import from: ")
		import_date =input("\tEnter  the fruit import date :")
		buy_price=int(input("\tEnter  the fruit price :"))
		temp ={
			"name":name,
			"rate":rate,
			"import_from":import_from,
			"import_date":import_date,
			"buy_price":buy_price,
			}
		fruit[fruit_id] = temp
	else:
		print("\tfruit id already Taken")

def delete_fruit():
	fruit_id = input("\tEnter fruit id :")
	if fruit_id not in fruit.keys():
		print("\tWrong fruit_id")
	else:
		del fruit[fruit_id]
		print("\t fruit is deleted successfully")


def search_fruit_menu():
        print("\t 1. Search fruit by name:")
        print("\t 2. Search fruit by rate:")

def search_fruit_by_name(fruit_id):
        flag = False
        name = input("\tEnter the name:")
        for i in fruit.values():
                if i["name"] == name :
                        flag = True
        if flag == True:
                print(f"\t{fruit_id} : {name} is found")
        else:
                print(f"\t{name} is not found")
def search_fruit_by_rate(fruit_id):
        flag = False
        rate = input("\tEnter the rate:")
        for i in fruit.values():
                if i["rate"] == rate :
                        flag = True
        if flag == False:
                print(f"\t{fruit_id} : {rate} is found")
        else:
                print(f"\t{rate} is not found")

def search_fruit():
            fruit_id = int(input("Enter fruit id :"))
            for fruit_id in fruit.keys(): 
                search_fruit_menu()
                choice =int( input("\tEnter the choice:"))
                if choice == 1:
                        search_fruit_by_name(fruit_id)
                elif choice == 2:
                        search_fruit_by_rate(fruit_id)
                else:
                        print("Wrong Choice")

def change_fruit_menu ():
    print("\t 1.change fruit by name:")
    print("\t 2.change fruit by rate:")
"""

def change_fruit_name(fruit_id):
        fruit_id =input("\tEnter fruit id :")
        if fruit_id not in fruit.keys:
                print("\tWrong fruit id")
        else:
  
                fruit[fruit_id]["name"] = input("\tEnter new fruit name :")

                print("\tfruit name changed succesfully ")

def change_fruit_rate(fruit_id):
        fruit_id =input("\tEnter fruit id :")
        if fruit_id not in fruit.keys:
                print("\tWrong fruit id")
        else:
                new_fruit_rate=input("\tEnter new rate name :")
                fruit[fruit_id]['rate'] = new_fruit_rate
                print("\tfruit name changed succesfully ")

"""
def change_fruit_by_name(fruit_id):
        new_name = input("\tEnter the fruit name to be change")
        fruit[fruit_id]["name"] = new_name
        	   

def change_fruit_by_rate(fruit_id):
        new_rate = input("\tEnter the fruit rate to be change")
        fruit[fruit_id]["rate"] = new_rate
	    	 

def change_fruit():
        fruit_id = int(input("Enter fruit id:"))
        for fruit_id in fruit.keys():
                change_fruit_menu()
                choice =int(input("\tEnter the choice:"))       
                if choice == 1:
                        change_fruit_by_name(fruit_id)
                elif choice == 2:
                        change_fruit_by_rate(fruit_id)
                else:
                        print("invalid Choice")


def display_fruit():
	for f_id,fruite in fruit.items():
		print(f"\t{f_id} : {fruite}\n")
	else:
		print("\t no fruit ")

def cart_menu():
	print("\t 1. Add to Cart")
	print("\t 2. delete to Cart")

def add_fruit_cart():
	num = int(input("\tEnter the fruit add to cart:"))
	if num not  in fruit.keys():
		print("\tinvalid no")
	else:
		add_cart.append(num)
		print("\tadded to cart")

def delete_fruit_cart():
    num = int(input("\tEnter the fruit delete to cart:"))
    if not num in fruit.keys():
        print("\t invalid no")
    else:
      	add_cart.remove(num)
        

def add_to_cart():
	for key,values in fruit.items():
                print(f"{key} : {values}\n")
	cart_menu()
	choice = int(input("\tEnter the choice :"))
	if choice == 1:
		add_fruit_cart()
	elif choice == 2:
		delete_fruit_cart()

	else:
		print("\tInvalid Choice")

def display_cart():
        for i in add_cart:
                print(f"\tnumber of items in cart {i}")


while True :
	Menu()
	ch = int(input("Enter the choice :"))
	if ch == 1 :
		add_fruit()
	elif ch == 2 :
		delete_fruit()
	elif ch == 3:
		 search_fruit()
	elif ch == 4:
		change_fruit()
	elif ch == 5:
		display_fruit()
	elif ch == 6:
		add_to_cart()
	elif ch == 7:
		display_cart()
	elif ch == 8:
		print("Exit")
		break
	else:
		print("Invalid choice")


