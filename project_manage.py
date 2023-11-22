# BEGIN part 1

# import database module
from database import *
import random
import csv

# define a funcion called initializing


def initializing():

# here are things to do in this function:
    # create an object to read an input csv file, persons.csv
    data = ReadCsv()

    # create a 'persons' table
    person_table = Table("person",data.read())


    # add the 'persons' table into the database
    my_DB = DB()
    my_DB.insert(person_table)


    # the 'login' table has the following keys (attributes):
        # person_id
        # username
        # password
        # role




    # create a 'login' table
    login = []
    for i in range(len(person_table.table)):
        login.append({})





    # a person_id is the same as that in the 'persons' table
        login[i]["person_id"] = person_table.table[i]["ID"]

    # let a username be a person's first name followed by a dot and the first letter of that person's last name
        login[i]["username"] = person_table.table[i]["fist"] + "." + person_table.table[i]["last"][0]

    # let a password be a random four digits string
        digit1, digit2, digit3, digit4 = random.sample([str(x) for x in range(10)], 4)
        login[i]["password"] = digit1 + digit2 + digit3 + digit4

    # let the initial role of all the students be Member
        if person_table.table[i]["type"] == "student":
            login[i]["type"] = "Member"

    # let the initial role of all the faculties be Faculty
        elif person_table.table[i]["type"] == "faculties":
            login[i]["type"] = "Faculty"

    #let add the admin role
        elif person_table.table[i]["type"] == "admin":
            login[i]["type"] = "admin"

    # create a login table by performing a series of insert operations; each insert adds a dictionary to a list
    login_table = Table("login", login)

    # add the 'login' table into the database
    my_DB.insert(login_table)
    return my_DB



# define a funcion called login

def login():
     my_DB = initializing()
     search_login = my_DB.search("login")
     print(search_login)
     username = str(input("What is your username: "))
     password = str(input("What is your password: "))
     for i in range(len(search_login.table)):
         if search_login.table[i]["username"] == username and search_login.table[i]["password"] == password:
            return f'[{search_login.table[i]["person_id"]} , {search_login.table[i]["type"]}]'
         else:
            return None


def exit(table_name):

    my_data = initializing()
    search_table = my_data.search(table_name)
    my_file = open(table_name+".csv","w")
    writer = csv.writer(my_file)
    x = search_table.table[0].keys()
    writer.writerow(x)
    for dict in search_table.table:
        writer.writerow(dict.values())
    my_file.close()
    myFile = open(table_name+".csv","r")
    print(myFile.read())
    myFile.close()







# here are things to do in this function:
# write out all the tables that have been modified to the corresponding csv files
# By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above


# here are things to do in this function:
   # add code that performs a login task
        # ask a user for a username and password
        # returns [person_id, role] if valid, otherwise returning None

# make calls to the initializing and login functions defined above


exit("login")
# END part 1

# CONTINUE to part 2 (to be done for the next due date)

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id

# if val[1] = 'admin':
    # do admin related activities
# elif val[1] = 'advisor':
    # do advisor related activities
# elif val[1] = 'lead':
    # do lead related activities
# elif val[1] = 'member':
    # do member related activities
# elif val[1] = 'faculty':
# do faculty related activities
