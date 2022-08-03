"""
 __  __     __  __     __    __     ______     ______   ______     ______     __  __    
/\ \/ /    /\ \/\ \   /\ "-./  \   /\  __ \   /\__  _\ /\  ___\   /\  ___\   /\ \_\ \   
\ \  _"-.  \ \ \_\ \  \ \ \-./\ \  \ \  __ \  \/_/\ \/ \ \  __\   \ \ \____  \ \  __ \  
 \ \_\ \_\  \ \_____\  \ \_\ \ \_\  \ \_\ \_\    \ \_\  \ \_____\  \ \_____\  \ \_\ \_\ 
  \/_/\/_/   \/_____/   \/_/  \/_/   \/_/\/_/     \/_/   \/_____/   \/_____/   \/_/\/_/ 
                                                                                        
                                                                                        
 _____     ______     __   __   ______     __         ______     ______   ______     ______     ______    
/\  __-.  /\  ___\   /\ \ / /  /\  ___\   /\ \       /\  __ \   /\  == \ /\  ___\   /\  == \   /\  ___\   
\ \ \/\ \ \ \  __\   \ \ \'/   \ \  __\   \ \ \____  \ \ \/\ \  \ \  _-/ \ \  __\   \ \  __<   \ \___  \  
 \ \____-  \ \_____\  \ \__|    \ \_____\  \ \_____\  \ \_____\  \ \_\    \ \_____\  \ \_\ \_\  \/\_____\ 
  \/____/   \/_____/   \/_/      \/_____/   \/_____/   \/_____/   \/_/     \/_____/   \/_/ /_/   \/_____/ 

[+] ==================================== [+]

        Author: Lance Kenji Parce

[+] ==================================== [+]

"""
import os
import time
import itertools
from operator import*

admin_users = {'admin':'admin_pass','admin1':'admin_pass1','admin2':'admin_pass2'}
cashier_users = {'cashier':'cashier_pass','cashier1':'cashier_pass1','cashier2':'cashier_pass2'}

#List of Items
itemID = ['item001','item002','item003','item004','item005','item006','item007','item008','item009','item010']
itemName = ["Ball", "Pen", "Pencil", "Eraser", "Ruler", "Towel", "Watch", "Mask", "Mug", "Fan"]
unitPrice = [20, 10, 7, 8, 10, 10, 100, 1, 20, 100]
stockIn = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
stockOut = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

colors = ['Red', 'Black', 'White']

choose_login = '''
[+] ================ [+]
    Choose Login
[+] ================ [+]
[1] Administrator
[2] Cashier
'''

def product():
    os.system('cls')
    print("[+] ================================================================================================= [+]")
    print("    Item ID\t\tItem Name\t\tUnit Price\t\tStock In\tStock Out")
    print("[+] ================================================================================================= [+]")
    m = 1
    while m < len(itemID):
        for (a, b, c, d, e) in zip(itemID, itemName, unitPrice, stockIn, stockOut):
            print("["+str(m-1)+"] "+a+"\t\t"+b+"\t\t\t"+str(c)+"\t\t\t"+str(d)+"\t\t"+str(e)+"\t\t")
            m = m+1
    print("[+] ================================================================================================= [+]")
    print("[1] Add Product")
    print("[2] Edit Product")
    print("[3] Delete Product")
    print("[4] Back")
    product_action = int(input("Choose: "))
    if product_action == 1:
        print("[+] ================================ [+]")
        add_itemID = input("Item ID: ")
        itemID.append(add_itemID)
        add_itemName = input("Item Name: ")
        itemName.append(add_itemName)
        add_unitPrice = int(input("Unit Price: "))
        unitPrice.append(add_unitPrice)
        add_stockIn = int(input("Stock In: "))
        stockIn.append(add_stockIn)
        stockOut.append(0)
        print("Done adding "+add_itemID+"!")
        time.sleep(1)
        product()
    elif product_action == 2:
        print("[+] ================================ [+]")
        choose_itemID = int(input("Choose Number from the List Above: "))
        add_itemID = input("Item ID: ")
        itemID[choose_itemID] = add_itemID
        add_itemName = input("Item Name: ")
        itemName[choose_itemID] = add_itemName
        add_unitPrice = int(input("Unit Price: "))
        unitPrice[choose_itemID] = add_unitPrice
        add_stockIn = int(input("Stock In: "))
        stockIn[choose_itemID] = add_stockIn
        print("Done editing "+itemID[choose_itemID]+"!")
        time.sleep(1)
        product()
    elif product_action == 3:
        print("[+] ================================ [+]")
        choose_itemID = int(input("Choose Number from the List Above: "))
        print("Done deleting "+itemName[choose_itemID]+"!")
        itemID.pop(choose_itemID)
        itemName.pop(choose_itemID)
        unitPrice.pop(choose_itemID)
        stockIn.pop(choose_itemID)
        stockOut.pop(choose_itemID)
        time.sleep(1)
        product()
    elif product_action == 4:
        admin_main()

def user_crud():
    os.system('cls')
    admin_keys = list(admin_users.keys())
    admin_values = list(admin_users.values())
    cashier_keys = list(cashier_users.keys())
    cashier_values = list(cashier_users.values())
    print("[+] ================================ [+]")
    print("Admin Accounts")
    for (a, b) in zip(admin_keys, admin_values):
        print("Username: "+a+" | Password: "+b)
    print("Cashier Accounts")
    for (c, d) in zip(cashier_keys, cashier_values):
        print("Username: "+c+" | Password: "+d)
    print("[+] ================================ [+]")
    print("[1] Add Admin")
    print("[2] Add Cashier")
    print("[3] Edit Admin")
    print("[4] Edit Cashier")
    print("[5] Delete Admin")
    print("[6] Delete Cashier")
    print("[7] Back")
    user_action = int(input("Choose: "))
    if user_action == 1:
        print("[+] ================================ [+]")
        add_user = input("Username: ")
        add_pass = input("Password: ")
        admin_users[add_user] = add_pass
        print("Done adding "+add_user+"!")
        time.sleep(1)
        user_crud()
    elif user_action == 2:
        print("[+] ================================ [+]")
        add_user = input("Username: ")
        add_pass = input("Password: ")
        cashier_users[add_user] = add_pass
        print("Done adding "+add_user+"!")
        time.sleep(1)
        user_crud()
    elif user_action == 3:
        print("[+] ================================ [+]")
        choose_username = input("Username: ")
        if choose_username in admin_users:
            edit_pass = input("New Password: ")
            admin_users[choose_username] = edit_pass
            print("Done editing "+choose_username+"!")
            time.sleep(1)
            user_crud()
        else:
            print("USERNAME DOES NOT EXIST!")
            time.sleep(1)
            user_crud()
    elif user_action == 4:
        print("[+] ================================ [+]")
        choose_username = input("Username: ")
        if choose_username in cashier_users:
            edit_pass = input("New Password: ")
            cashier_users[choose_username] = edit_pass
            print("Done editing "+choose_username+"!")
            time.sleep(1)
            user_crud()
        else:
            print("USERNAME DOES NOT EXIST!")
            time.sleep(1)
            user_crud()
    elif user_action == 5:
        print("[+] ================================ [+]")
        choose_username = input("Username: ")
        if choose_username in admin_users:
            admin_users.pop(choose_username)
            print("Done deleting "+choose_username+"!")
            time.sleep(1)
            user_crud()
        else:
            print("USERNAME DOES NOT EXIST!")
            time.sleep(1)
            user_crud()
    elif user_action == 6:
        print("[+] ================================ [+]")
        choose_username = input("Username: ")
        if choose_username in cashier_users:
            edit_pass = input("New Password: ")
            cashier_users.pop(choose_username)
            print("Done deleting "+choose_username+"!")
            time.sleep(1)
            user_crud()
        else:
            print("USERNAME DOES NOT EXIST!")
            time.sleep(1)
            user_crud()
    elif user_action == 7:
        admin_main()

def purchase():
    os.system("cls")
    customer_name = input("Customer Name: ")
    file = open(customer_name+".txt", 'a')
    file.write("[+] ==================== RECEIPT ==================== [+]\nCustomer Name: "+customer_name+"\n")
    print("[+] ================================================================================================= [+]")
    print("    Item ID\t\tItem Name\t\tUnit Price\t\tStock In\tStock Out")
    print("[+] ================================================================================================= [+]")
    i = 1
    while i < len(itemID):
        for (a, b, c, d, e) in zip(itemID, itemName, unitPrice, stockIn, stockOut):
            print("["+str(i-1)+"] "+a+"\t\t"+b+"\t\t\t"+str(c)+"\t\t\t"+str(d)+"\t\t"+str(e)+"\t\t")
            i = i+1
    how_many = int(input("How much items do you want to buy?: "))

    total_price = []
    total_price1 = 0
    for j in range(how_many):
        item = int(input("["+str(j+1)+"] Choose the Number of Product (Only One): "))
        print("Item ID: "+itemID[item])
        print("Item Name: "+itemName[item])
        print("Unit Price: "+str(unitPrice[item]))
        file.write("Item ID: "+itemID[item]+"\n")
        file.write("Item Name: "+itemName[item]+"\n")
        file.write("Unit Price: "+str(unitPrice[item])+"\n")
        for k in range(len(colors)):
            print("["+str(k)+"] "+colors[k])
        sub_attribute = int(input("Choose the Number of Color: "))
        qty = int(input("Quantity: "))
        total = qty*unitPrice[item]
        total_price.append(int(total))
        file.write("Color: "+colors[sub_attribute]+"\n")
        file.write("Quantity: "+str(qty)+"\n")
        file.write("Cost: $"+str(total)+"\n")
        stockIn[item] = stockIn[item] - qty
        stockOut[item] = stockOut[item] + qty
        file.write("=========================================================\n")
    for l in total_price:
        total_price1 = add(l, 0)+total_price1
    print(total_price)
    print("Total Price: "+str(total_price1))
    file.write("Total Price: "+str(total_price1)+"\n")
    amount = int(input("How much cash: "))
    file.write("Amount Paid: "+str(amount)+"\n")
    change = amount-total_price1
    print("Change: $"+str(change))
    file.write("Change: "+str(change)+"\n")
    file.write("[+] ==================== RECEIPT ==================== [+]"+"\n")
    file.close()
    os.system('cls')
    file = open(customer_name+".txt", 'r')
    file_contents = file.read()
    print(file_contents)
    file.close()
    os.remove(customer_name+".txt")
    time.sleep(5)
    print("[1] Transact Again")
    print("[2] Back to Login")
    choicee = int(input("Choose: "))
    if choicee == 1:
        purchase()
    elif choicee == 2:
        start()
    else:
        print("Wrong Choice, Logging Out.")
        exit()

def cashier_main():
    os.system('cls')
    print("[+] ============================== [+]")
    print("[1] Add Purchase Record")
    print("[2] Log Out")
    choose_admin = int(input("Choose: "))
    if choose_admin == 1:
        purchase()
    elif choose_admin == 2:
        os.system('cls')
        print("Thank you!")
        exit()

def admin_main():
    os.system('cls')
    print("[+] ============================== [+]")
    print("[1] Add Purchase Record")
    print("[2] Product Management (Add, Edit, Delete)")
    print("[3] Account Management (Add, Edit, Delete)")
    print("[4] Log Out")
    choose_admin = int(input("Choose: "))
    if choose_admin == 1:
        purchase()
    elif choose_admin == 2:
        product()
    elif choose_admin == 3:
        user_crud()
    elif choose_admin == 4:
        os.system('cls')
        print("Thank you!")
        exit()

def check_login(user_list,username,password):
    if(username,password) in user_list.items():
        return 1
    else:
        return 2

def admin():
    os.system('cls')
    username = input("Username: ")
    password = input("Password: ")

    login_result = check_login(admin_users,username,password)
    if login_result == 1:
        os.system('cls')
        print("[+] ============================== [+]")
        print("Welcome: "+username)
        admin_main()
    else:
        print("Login Failed!")
        time.sleep(1)
        os.system('cls')
        admin()

def cashier():
    os.system('cls')
    username = input("Username: ")
    password = input("Password: ")

    login_result = check_login(cashier_users,username,password)
    if login_result == 1:
        cashier_main()
    else:
        print("Login Failed!")
        time.sleep(1)
        os.system('cls')
        cashier()

def start():
    os.system('cls')
    print(choose_login)
    login_choice = int(input("Choose: "))
    if login_choice == 1:
        admin()
    elif login_choice == 2:
        cashier()
    else:
        print("Wrong Choice! Repeating ")
        start()

start()
