# BEGIN part 1
import sys

# import database module
from database import *
import random
import csv
import os
import random
import sys
import copy

# define a funcion called initializing
# logins = []
# with open(os.path.join(__location__, 'login.csv')) as f:
#     rows = csv.DictReader(f)
#     for r in rows:
#         logins.append(dict(r))
#
# person = []
# with open(os.path.join(__location__, 'persons.csv')) as f:
#     rows = csv.DictReader(f)
#     for r in rows:
#         person.append(dict(r))
#
# member_pending =  []
# with open(os.path.join(__location__, 'Member_pending_request.csv')) as f:
#     rows = csv.DictReader(f)
#     for r in rows:
#         member_pending.append(dict(r))

def initializing():

# here are things to do in this function:
    # create an object to read an input csv file, persons.csv
    person_data = ReadCsv("persons.csv")
    login_data = ReadCsv("login.csv")
    project_data = ReadCsv("Project_table.csv")
    member_pending_data = ReadCsv("Member_pending_request.csv")
    advisor_pending_data = ReadCsv("Advisor_pending_request.csv")

    # create a 'persons' table
    person_table = Table("person",person_data.read())
    project_table = Table("Project_table",project_data.read())
    login_table = Table("login", login_data.read())
    member_pending_table = Table("Member_pending_request",member_pending_data.read())
    advisor_pending_table = Table("Advisor_pending_request",advisor_pending_data.read())


    # add the 'persons' table into the database
    my_DB = DB()
    my_DB.insert(person_table)
    my_DB.insert(login_table)
    my_DB.insert(project_table)
    my_DB.insert(member_pending_table)
    my_DB.insert(advisor_pending_table)

    # create a login table by performing a series of insert operations; each insert adds a dictionary to a list

    # add the 'login' table into the database
    return my_DB

    # the 'login' table has the following keys (attributes):
        # person_id
        # username
        # password
        # role




    # create a 'login' table
    # login = []
    # for i in range(len(person_table.table)):
    #     login.append({})
    #
    #
    #
    #
    #
    # # a person_id is the same as that in the 'persons' table
    #     login[i]["person_id"] = person_table.table[i]["ID"]
    #
    # # let a username be a person's first name followed by a dot and the first letter of that person's last name
    #     login[i]["username"] = person_table.table[i]["fist"] + "." + person_table.table[i]["last"][0]
    #
    # let a password be a random four digits string
    #     digit1, digit2, digit3, digit4 = random.sample([str(x) for x in range(10)], 4)
    #     login[i]["password"] = digit1 + digit2 + digit3 + digit4

    # # let the initial role of all the students be Member
    #     if person_table.table[i]["type"] == "student":
    #         login[i]["type"] = "Member"
    #
    # # let the initial role of all the faculties be Faculty
    #     elif person_table.table[i]["type"] == "faculties":
    #         login[i]["type"] = "Faculty"
    #
    # #let add the admin role
    #     elif person_table.table[i]["type"] == "admin":
    #         login[i]["type"] = "admin"




# define a funcion called login

def login():
     main_list = []
     search_login = data.search("login")
     username = str(input("What is your username: "))
     password = str(input("What is your password: "))
     for i in range(len(search_login.table)):
         if search_login.table[i]["username"] == username and search_login.table[i]["password"] == password:
             # return f'[{search_login.table[i]["person_id"]} , {search_login.table[i]["type"]}]' #should return list
            main_list.append(search_login.table[i]["ID"])
            main_list.append(search_login.table[i]["role"])
            return main_list
         elif search_login.table[i]["username"] != username and search_login.table[i]["password"] != password:
             continue
         elif i > len(search_login.table):
             return None





def exit(table_name):
    search_table = data.search(table_name)
    my_file = open(table_name+".csv","w")
    writer = csv.writer(my_file)
    x = search_table.table[0].keys()
    writer.writerow(x)
    for dict in search_table.table:
        writer.writerow(dict.values())
    # my_file.close()
    # myFile = open(table_name+".csv","r")
    # print((myFile.read()))
    # myFile.close()
    with open(table_name + ".csv", "r") as myFile:
        print(myFile.read())




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




# END part 1

# CONTINUE to part 2 (to be done for the next due date)

# based on the return value for login, activate the code that performs activities according to the role defined for that person_id





#
#
# class Login:
#     def __init__(self,person_id):
#         self.person_id = person_id
#
#     def return_type(self):
#         for i in my_person_table.table:
#             if i["ID"] == str(self.person_id):
#                 return i["type"]
#


class Student:
    def __init__(self,person_id):
        self.ID = str(person_id)
        self.member_info = data.search("Member_pending_request")
        self.project_id = ""
        self.login_info = data.search("login")
        self.type = val[1]
        self.id = val[0]
        self.project_table = data.search("Project_table")
        self.lead = copy.copy(Lead())


    # def see_invitation(self):
    #     login_info = data.search("login")
    #     if self.ID in login_info:
    #

    def lead_or_member(self):
        if self.type == "student":
            for i in self.login_info.table:
                if i["ID"] == self.ID: #need indicator
                    create_project_or_not = str(input("Do you want to create project?: "))
                    if create_project_or_not == "Yes":
                        self.login_info.update_row("ID",self.ID,"role","lead")

                        self.lead.create_project()
                        num_of_invite = int(input("How many do you want to sent: "))

                        for i in range(num_of_invite):
                            self.lead.sent_invitation()
                        self.lead.see_detail()
                        self.lead.sent_invitation_to_advisor()

                    elif create_project_or_not == "No":
                        responses = ""
                        while responses != "accept":
                            self.see_invitation()
                            which_project = str(input("which project do you want to be member: "))
                            responses = str(input("accept/deny: "))
                            self.response(responses,which_project)
                            if responses == "accept":
                                self.login_info.update_row("ID", self.ID, "role", "Member")
                                filter_project_id  = self.project_table.filter(lambda x: x["Project_ID"] == which_project)
                                for i in filter_project_id.table:
                                    if i["Member1"] == None:
                                        num = "Member1"
                                    elif i["Member1"] != None:
                                        num = "Member2"
                                    else:
                                        print(f"group is fulled")
                                        sys.exit()
                                self.project_table.update_row("Project_ID",which_project,num,self.ID)
                                exit("Project_table")

                    else:
                        continue
        return exit("login")


    def see_invitation(self):
        member_pending_filter = self.member_info.filter(lambda x: x["to_be_member"] == self.ID)
        print(member_pending_filter)

    def response(self,responses,project_id):
        self.project_id = project_id
        if responses == "accept":
            self.member_info.update_row("Project_ID",self.project_id,"Responses", "Accepted")
            exit("Member_pending_request")
        elif responses == "deny":
            self.member_info.update_row("Project_ID", project_id, "Responses", "Denied")
            exit("Member_pending_request")




class Lead:

    def __init__(self):
        digit1, digit2, digit3, digit4,digit5,digit6= random.sample([str(x) for x in range(10)], 6)
        self.project_id = digit1+digit2+digit3+digit4+digit5+digit6
        self.member_pending = data.search("Member_pending_request")
        self.who_received = ""
        self.deadline = ""
        self.advisor_pending = data.search("Advisor_pending_request")
        self.login_table = data.search("login")



    def create_project(self):
        project_info = data.search("Project_table")
        your_ID = str(input("What is your ID: "))
        title = str(input("Title project: "))
        self.deadline = str(input("Deadline: DD/MM/YYYY"))
        dict = {}
        dict["Project_ID"] = self.project_id
        dict["Title"] = title
        dict["Leader"] = your_ID
        dict["Member1"] = None
        dict["Member2"] = None
        dict["Advisor"] = None
        dict["Status"] = None
        project_info.insert_row(dict)
        exit("Project_table")


    def sent_invitation(self):
        login_info = data.search("login")
        member_pending = data.search("Member_pending_request")
        login_info_student = login_info.filter(lambda x: x["role"] == "student")
        print(login_info_student)
        self.who_received = str(input("who student do you want to sent: "))
        dict = {"Project_ID": self.project_id, "to_be_member": self.who_received, "Responses": "pending", "Responses_date": "1111"}
        member_pending.insert_row(dict)
        exit("Member_pending_request")

    def see_detail(self):
        member_pending_table = self.member_pending.filter(lambda x: x["to_be_member"] == self.who_received)
        print(f"Project detail")
        print("-------------")
        print(member_pending_table)
        print(f"Deadline: {self.deadline}")

    def sent_invitation_to_advisor(self):
        filter_table_faculty = self.login_table.filter(lambda x: x["role"] == "faculty")
        print(filter_table_faculty)
        who_advisor = str(input("Who do you want to be your advisor: "))
        dict = {"Project_ID": self.project_id, "to_be_advisor": who_advisor, "Response": "pending", "Responses_date": "1111"}
        self.advisor_pending.insert_row(dict)
        exit("Advisor_pending_request")







class Member:
    def __init__(self,ID):
        self.ID = ID
        self.project_table =  data.search("Project_table")

    def see_project_table(self):
        print(self.project_table)




class Faculty:
    def __init__(self):
        self.ID = val[0]
        self.type = val[1]
        self.project_table = data.search("Project_table")
        self.login_table = data.search("login")
        self.advisor_pending_table = data.search("Advisor_pending_request")
        self.Class_advisor = Advisor()

    def see_request(self):
        print(self.advisor_pending_table)

    def response(self):
        advisor_filter = self.advisor_pending_table.filter(lambda x: x["to_be_advisor"] == self.ID).filter(lambda x: x["Response"] == "pending")
        print(advisor_filter)
        which_project_advisor = str(input("Which project you gonna sent response: "))
        temp_list = []
        for i in advisor_filter.table:
            temp_list.append(i["Project_ID"])
        while which_project_advisor not in temp_list:
            print(f"Wrong Project_ID")
            which_project_advisor = str(input("Which project you gonna sent response: "))
        responses = str(input(f"accept/denied:from({self.ID}) "))
        if responses == "accept":
            self.advisor_pending_table.update_row("Project_ID", which_project_advisor, "Response", responses)
            self.login_table.update_row("ID",self.ID,"role","advisor")
            project_table = self.project_table.filter(lambda x: x["Project_ID"] == which_project_advisor)
            project_table.update_row("Project_ID",which_project_advisor,"Advisor",self.ID)
            exit("login")
            exit("Project_table")

        elif responses == "deny":
            self.advisor_pending_table.update_row("Project_ID", which_project_advisor, "Response", responses)
            self.login_table.update_row("ID", self.ID, "role", "faculty")
            exit("login")
        exit("Advisor_pending_request")



    # def normal_or_advisor(self):
    #     normal_or_advisor = str(input("Do you want to be normal faculty or advisor: "))
    #     if normal_or_advisor == "normal faculty":
    #         self.login_table.update_row("ID", self.ID, "role", "faculty")
    #
    #     elif normal_or_advisor == "advisor":
    #         self.login_table.update_row("ID",self.ID,"role","advisor")
    #         self.Class_advisor.sent_responses()
    #     exit("login")

class Advisor:
    def __init__(self):
        self.ID = val[0]
        self.advisor_pending_table = data.search("Advisor_pending_request")
        self.login_table = data.search("login")
        self.Project_table = data.search("Project_table")

    def sent_approve(self):
        sent_approve = str(input(f"Do you approve "))





    # def sent_responses(self):
    #         advisor_filter = self.advisor_pending_table.filter(lambda x: x["to_be_advisor"] == self.ID).filter(lambda x: x["Response"] == "pending")
    #         print(advisor_filter)
    #         which_project_advisor = str(input("Which project you gonna sent response: "))
    #         temp_list = []
    #         for i in advisor_filter.table:
    #             temp_list.append(i["Project_ID"])
    #         while which_project_advisor not in temp_list:
    #             print(f"Wrong Project_ID")
    #             which_project_advisor = str(input("Which project you gonna sent response: "))
    #         responses = str(input(f"accept/denied:from({self.ID}) "))
    #         self.advisor_pending_table.update_row("Project_ID",which_project_advisor,"Response",responses)
    #         exit("Advisor_pending_request")


# class Normal_fac:
#     def __init__(self):
#         self.ID = val[0]
#         self.project_table = data.search("Project_table")
#
#     def see_all_project(self):
#         print(self.project_table)
#
#     def see_request_advisor(self):
#

# class Normal_faculty:
#     def __init__(self):
#         self.ID = val[0]
#         self.

# class normal_faculty:








    # def sent_response(self):
    #
    #
    #
    #
    #







    # def invitation(self):
    #     for i in updated_Status:
    #         if i["Status"] == "Leader":
    #






data = initializing()
val = login()
print(val)#from login table

f1 = Faculty()
f1.response()




# s1 = Student(5687866)
# s1.lead_or_member()

# l1 = Lead(9898118)
# l1.sent_invitation()

# if val[1] == 'admin':
#     # do admin related activities
#     pass
#
# elif val[1] = 'advisor'
#     # do advisor related activities
#     pass
# elif val[1] = 'lead':
#     do lead related activities
# elif val[1] = 'member':
#     do member related activities
# elif val[1] = 'faculty':
# do faculty related activities
