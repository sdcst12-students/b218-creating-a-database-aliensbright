#!python3

import sqlite3
import tkinter as tk
window = tk.Tk()
window.title("tk")
window.maxsize(1600,800)

"""Assignment: Create a database for a veterinarian. You will need to create your own tables and choose the variable types that best suit these fields/columns. 
There will be 3 tables: 
customers id : primary key integer 
fname: first name 
lname: last name 
phone: phone number 
email: email address 
address: physical address 
city: city where they live 
postalcode: their postal code

pets id: primary key integer 
name: pet name type: dog or cat 
breed: description of breed (example German Sheperd, Mixed, Persion) 
birthdate: birthdate of pet (could be used to calculate their age) 
ownerID: to match the ID number in customers ID

visits id: primary key integer 
ownerid: the id of the owner who brought in their pet. Matches primary key of owner table 
petid: the id of the pet that was brought in. Matches primary key of pets table 
details: details what the visit was about. Could be quite lengthy! 
cost: how much was the visit 
paid: how much has been paid so far, used to find outstanding debts

Create a program that allows you to interface with this database. We will be doing this in parts over the next few classes.

Part 1. Create a function that will add a new customer.
Ask the user for their relevant details and add them to the customers table Optional enhancements. Ideas for Check for duplicates:

Check to see if there is already a username with the same phone number or email before adding and warn that the customer already exists
List all users with the same last name and ask for confirmation before adding
Create a function that will allow you to search for a customer by any part of their record. Example: search for all customers with a specific last name Optional Enhancements.

search for all users that partially match a specific last name
search for multiple criteria"""


file = 'dbase.db'
connection = sqlite3.connect(file)
#print(connection)

cursor = connection.cursor()


qCustomerInfoCreation = """
create table if not exists vetcustomersinfo (
    fname tinytext,
    lname tinytext,
    phone tinytext,
    email tinytext,
    address tinytext,
    city tinytext,
    pCode tinytext);
"""
cursor.execute(qCustomerInfoCreation)
r1 = cursor.fetchall()

qPetInfoCreation = """
create table if not exists petInfo (
    id integer primary key autoincrement,
    petName tinytext,
    type tinytext,
    breed tinytext,
    birthdate date,
    ownerID tinytext);
"""
cursor.execute(qPetInfoCreation)
r2 = cursor.fetchall()

qVisitsCreation = """
create table if not exists visits (
    id integer primary key autoincrement,
    ownerID tinytext,
    petID tinytext,
    details text,
    cost tinyint,
    paid tinyint);
"""
cursor.execute(qVisitsCreation)
r3 = cursor.fetchall()


###Testing to see if I can add a customer
listOfEmail = []
listOfPhone = []



window.title("tk")
window.minsize(200,400)


txt1 = tk.Entry(window, width=10, highlightthickness=2)
txt1.config(highlightcolor= "black" , highlightbackground= "black")




txt2 = tk.Entry(window, width=10, highlightthickness=2)
txt2.config(highlightcolor= "black" , highlightbackground= "black")




label = tk.Label(window, text="x", width= 10)
button = tk.Button(window, text="=", width= 10)


txt3 = tk.Entry(window, width=10, highlightthickness=2)
txt3.config(highlightcolor= "black" , highlightbackground= "black")


txt1.grid(row=0, column=0)
label.grid(row=0, column=1)
txt2.grid(row=0, column=2)
button.grid(row=0,column=3)
txt3.grid(row=0,column=4)


window.mainloop()

while True:
    while True:
        print('\nPlease enter in all the info below,\nremove any spaces.')
        fname = input('  First Name: ')
        lname = input('  Last Name: ')
        phone = input('  Phone Number (input only the digits): ')
        email = input('  Full Email: ')
        address = input('  Home Address: ')
        city = input('  City: ')
        pCode = input('  Postal Code: ')
        try: #Ensure that only email matches one custonmer
            for i in listOfEmail:
                assert email != i
            listOfEmail.append(email)
        except:
            print("Email already linked to a customer.\n Would you like to replace demographics?") 
        try: #Ensure that only one phone number matches one customer
            assert int(phone)
            for i in listOfPhone:
                assert email != i
            listOfPhone.append(phone)
        except:
            listOfEmail.remove(email)
            print("\nCurrent phone number alread.\nPlease use another phone number.")
            break
        print(f'\n\nPlease check your info,\n\n  First Name: {fname}\n  Last Name: {lname}\n  Phone Number: {phone}\n  Email: {email}\n  Address: {address}\n  City: {city}\n  Postal Code: {pCode}')
        check = input('\nAnswer "Yes" if all of the info is correct,\nAnswer "No" if some info is incorrect: ')
        if check=='Yes':
            cursor.execute(f"insert into vetcustomersinfo (fname,lname,phone,email,address,city,pCode) values ('{fname}','{lname}','{phone}','{email}','{address}','{city}','{pCode}');")
            print('Input Complete\n')
        else:
            listOfEmail.remove(email)
            listOfPhone.remove(phone)
            print('Please reenter all of your info.')