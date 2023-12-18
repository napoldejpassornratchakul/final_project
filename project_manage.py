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


def initializing():
    # here are things to do in this function:
    # create an object to read an input csv file, persons.csv
    person_data = ReadCsv("persons.csv")
    login_data = ReadCsv("login.csv")
    project_data = ReadCsv("Project_table.csv")
    member_pending_data = ReadCsv("Member_pending_request.csv")
    advisor_pending_data = ReadCsv("Advisor_pending_request.csv")

    # create a 'persons' table
    person_table = Table("persons", person_data.read())
    project_table = Table("Project_table", project_data.read())
    login_table = Table("login", login_data.read())
    member_pending_table = Table("Member_pending_request", member_pending_data.read())
    advisor_pending_table = Table("Advisor_pending_request", advisor_pending_data.read())

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


def login():
    main_list = []
    search_login = data.search("login")
    username = str(input("What is your username: "))
    password = str(input("What is your password: "))
    for i in range(len(search_login.table)):
        if search_login.table[i]["username"] == username and search_login.table[i]["password"] == password:
            main_list.append(search_login.table[i]["ID"])
            main_list.append(search_login.table[i]["role"])
            return main_list
        elif search_login.table[i]["username"] != username and search_login.table[i]["password"] != password:
            continue
        elif i > len(search_login.table):
            return None


def exit(table_name):
    search_table = data.search(table_name)
    my_file = open(table_name + ".csv", "w")
    writer = csv.writer(my_file)
    x = search_table.table[0].keys()
    writer.writerow(x)
    for dict in search_table.table:
        writer.writerow(dict.values())
    with open(table_name + ".csv", "r") as myFile:
        print(myFile.read())


class Student:
    def __init__(self):
        self.ID = val[0]
        self.member_info = data.search("Member_pending_request")
        self.project_id = ""
        self.login_info = data.search("login")
        self.type = val[1]

        self.project_table = data.search("Project_table")
        self.lead = copy.copy(Lead())

    def lead_or_member(self):
        filter_member_table = self.member_info.filter(lambda x : x["to_be_member"] == self.ID)
        if self.type == "student":
            for i in self.login_info.table:
                if i["ID"] == self.ID:
                        create_project_or_not = str(input("Do you want to create project?(Yes/No): "))
                        if create_project_or_not == "Yes":
                            if len(filter_member_table.table) > 0:
                                print(f"You need to deny all member request first to create the project")
                                break
                                sys.exit()
                            self.login_info.update_row("ID", self.ID, "role", "lead")
                            print("You are now leader")
                            self.lead.create_project()
                            sent_invitation_to_student = str(input(f"Do you want to sent to student(Yes/No): "))
                            if sent_invitation_to_student == "Yes":
                                self.lead.sent_invitation()
                            sent_invitation_to_advisor = str(input(f"Do you want to sent to advisor(Yes/No): "))
                            if sent_invitation_to_advisor == "Yes":
                                self.lead.sent_invitation_to_advisor()

                        elif create_project_or_not == "No":
                            responses = ""
                            while responses != "accept":
                                see_invite = self.see_invitation()
                                if len(see_invite) == 0:
                                    break
                                print(see_invite)
                                which_project = str(input("which project do you want to be member(give me project ID): "))
                                responses = str(input("accept/deny: "))
                                self.response(responses, which_project)
                                if responses == "accept":
                                    self.login_info.update_row("ID", self.ID, "role", "Member")
                                    filter_project_id = self.project_table.filter(
                                        lambda x: x["Project_ID"] == which_project)
                                    num = ""
                                    for i in filter_project_id.table:
                                        if i["Member1"] == "":
                                            num = "Member1"
                                        elif i["Member1"] != "":
                                            num = "Member2"
                                        else:
                                            print(f"group is fulled")
                                            sys.exit()
                                    self.project_table.update_row("Project_ID", which_project, num, self.ID)
                                    print("Status updated")
                                    exit("Project_table")
                                elif responses == "deny" and len(see_invite) > 0:
                                    continue
                                else:
                                    break
                        else:
                            continue
            return exit("login")

    def see_invitation(self):
        member_pending_filter = self.member_info.filter(lambda x: x["to_be_member"] == self.ID).filter(
            lambda x: x["Responses"] == "pending")
        return member_pending_filter.table

    def response(self, responses, project_id):
        self.project_id = project_id
        if responses == "accept":
            self.member_info.update_row("Project_ID", self.project_id, "Responses", "Accepted")
            exit("Member_pending_request")
        elif responses == "deny":
            self.member_info.update_row("Project_ID", project_id, "Responses", "Denied")
            exit("Member_pending_request")


class Lead:

    def __init__(self):
        digit1, digit2, digit3, digit4, digit5, digit6 = random.sample([str(x) for x in range(10)], 6)
        self.project_id = digit1 + digit2 + digit3 + digit4 + digit5 + digit6
        self.member_pending = data.search("Member_pending_request")
        self.who_received = ""
        self.deadline = ""
        self.advisor_pending = data.search("Advisor_pending_request")
        self.login_table = data.search("login")
        self.project_table = data.search("Project_table")
        self.ID = val[0]

    def create_project(self):
        project_info = data.search("Project_table")

        title = str(input("Title project: "))

        dict = {"Project_ID": self.project_id, "Title": title, "Leader": self.ID, "Member1": None, "Member2": None,
                "Advisor": None,
                "Status": None, "Evaluator": None}
        give_deadline = str(input(f"DD/MM/YYYY: "))
        self.deadline = give_deadline
        project_info.insert_row(dict)
        exit("Project_table")

    def sent_invitation(self):
        login_info = data.search("login")
        member_pending = data.search("Member_pending_request")
        login_info_student = login_info.filter(lambda x: x["role"] == "student")
        print(login_info_student)
        self.who_received = str(input("who student do you want to sent invitation: "))
        dict = {"Project_ID": self.project_id, "to_be_member": self.who_received, "Responses": "pending",
                "Responses_date": "1111"}
        member_pending.insert_row(dict)
        exit("Member_pending_request")

    def see_detail(self):
        project_detail = self.project_table.filter(lambda x: x["Leader"] == self.ID)
        print(f"Project detail")
        print("-------------")
        print(project_detail)
        print("-------------")

    def sent_invitation_to_advisor(self):
        filter_table_faculty = self.login_table.filter(lambda x: x["role"] == "faculty")
        print(filter_table_faculty)
        who_advisor = str(input("Who do you want to be your advisor: "))
        dict = {"Project_ID": self.project_id, "to_be_advisor": who_advisor, "Response": "pending",
                "Responses_date": "1111"}
        self.advisor_pending.insert_row(dict)
        exit("Advisor_pending_request")

    def update_status(self):
        filter_project_table = self.project_table.filter(lambda x: x["Leader"])
        print(filter_project_table)
        which_project = str(input(f"Which project that you want to update status(give me project ID): "))
        progress = str(input("How is your progressing of project: "))
        self.project_table.update_row("Project_ID", which_project, "Status", progress)
        exit("Project_table")


class Member:
    def __init__(self, ID):
        self.ID = ID
        self.project_table = data.search("Project_table")
        self.Class_lead = Lead()
        self.project_id = Lead().project_id

    def see_project_table(self):
        print(self.project_table)

    def update_status(self):
        progress = str(input("How is your progressing of project: "))
        self.project_table.update_row("Project_ID", self.project_id, "Status", progress)
        exit("Project_table")


class Faculty:
    def __init__(self):
        self.ID = val[0]
        self.type = val[1]
        self.project_table = data.search("Project_table")
        self.login_table = data.search("login")
        self.advisor_pending_table = data.search("Advisor_pending_request")
        self.Class_advisor = Advisor()

    def see_request(self):
        print(self.advisor_pending_table.filter(lambda x: x["to_be_advisor"] == self.ID))

    def see_project(self):
        print(self.project_table)

    def response(self):
        advisor_filter = self.advisor_pending_table.filter(lambda x: x["to_be_advisor"] == self.ID).filter(
            lambda x: x["Response"] == "pending")
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
            self.advisor_pending_table.update_row("Project_ID", which_project_advisor, "Response", "Accepted")
            print(f"You are now Advisor")
            self.login_table.update_row("ID", self.ID, "role", "advisor")
            project_table = self.project_table.filter(lambda x: x["Project_ID"] == which_project_advisor)
            project_table.update_row("Project_ID", which_project_advisor, "Advisor", self.ID)
            exit("login")
            exit("Project_table")

        elif responses == "deny":
            self.advisor_pending_table.update_row("Project_ID", which_project_advisor, "Response", "Denied")
            self.login_table.update_row("ID", self.ID, "role", "faculty")
            exit("login")
        exit("Advisor_pending_request")

    def eval_project(self):
        print(self.project_table.filter(lambda x: x["Status"] == "").filter(lambda x: x["Evaluator"] == self.ID))
        choose_project = str(input("Which project you gonna give response: "))
        pass_or_reject = str(input("give Pass or reject: "))
        if pass_or_reject == "pass":
            self.project_table.update_row("Project_ID", choose_project, "Status", pass_or_reject)
            exit("Project_table")
            self.login_table.update_row("ID", self.ID, "role", "Faculty")
            exit("login")
        elif pass_or_reject == "reject":
            reason = str(input(f"reason and feedback. why you give them rejected: "))
            dict = {"Comment": {reason}}
            project_filter_table = self.project_table.filter(lambda x: x["Status"] == "reject").filter(
                lambda x: x["Project_ID"] == choose_project)
            project_filter_table.insert_row(dict)
            exit("Project_table")


class Advisor:
    def __init__(self):
        self.ID = val[0]
        self.advisor_pending_table = data.search("Advisor_pending_request")
        self.login_table = data.search("login")
        self.project_table = data.search("Project_table")

    def sent_approve(self):
        self.see()

        sent_approve = str(input(f"Approve this project or not: "))
        if sent_approve == "Approve":
            self.project_table.update_row("Advisor", self.ID, "Status", sent_approve)

        elif sent_approve == "Reject":
            self.project_table.update_row("Advisor", self.ID, "Status", sent_approve)

        exit("Project_table")

    def see(self):
        project_table = self.project_table.filter(lambda x: x["Advisor"] == self.ID)
        print(project_table)


class Admin:
    def __init__(self):
        self.project_table = data.search("Project_table")
        self.login_table = data.search("login")
        self.advisor_pending_table = data.search("Advisor_pending_request")
        self.person_table = data.search("persons")
        self.member_pending_table = data.search("Member_pending_request")
        self.input_table = None
        self.project_id = None

    def change_and_update(self):
        print(f"1.persons\n"
              f"2.login\n"
              f"3.Advisor_pending_request\n"
              f"4.Project_table\n"
              f"5.Member_pending_request")

        what_table = str(input("what table you gonna change/update(write table_name not number): "))
        self.input_table = data.search(what_table)
        print(self.input_table)
        if what_table == "login" or what_table == "persons":
            give_me_id = str(input("give me Person ID that you gonna change value: "))
        elif what_table == "Project_table" or what_table == "Advisor_pending_request" or what_table == "Member_pending_request":
            give_me_project_id = str(input("give me Project ID that you gonna change value: "))
        can_change = self.input_table.table[0].keys()
        print(f"which one you gonna change")
        list_can_change = list(can_change)
        print(list_can_change)
        select_number = int(input("choose by number: "))
        if what_table == "persons" or what_table == "login" or what_table == "Advisor_pending_request":
            if select_number == 1:
                original_value = str(input("Which value you gonna change/update to: "))
                changed_value = str(input("what value you gonna change from original: "))
                self.input_table.update_row(list_can_change[0], original_value, list_can_change[0], changed_value)
                if what_table == "persons":
                    self.login_table.update_row(list_can_change[0], original_value, list_can_change[0], changed_value)
                    exit("login")
                    for i in self.project_table.table:
                        if i["Leader"] == original_value:
                            self.project_id = i["Project_ID"]
                            self.project_table.update_row("Project_ID", self.project_id, "Leader", changed_value)
                            exit("Project_table")
                        elif i["Member1"] == original_value:
                            self.project_id = i["Project_ID"]
                            self.project_table.update_row("Project_ID", self.project_id, "Member1", changed_value)
                            exit("Project_table")
                        elif i["Member2"] == original_value:
                            self.project_id = i["Project_ID"]
                            self.project_table.update_row("Project_ID", self.project_id, "Member2", changed_value)
                            exit("Project_table")
                    for j in self.advisor_pending_table.table:
                        if j["to_be_advisor"] == original_value:
                            self.project_id = j["Project_ID"]
                            self.advisor_pending_table.update_row("Project_ID", self.project_id, "to_be_advisor",
                                                                  changed_value)
                            exit("Advisor_pending_request")
                elif what_table == "login":
                    self.person_table.update_row(list_can_change[0], original_value, list_can_change[0], changed_value)
                    for i in self.project_table.table:
                        if i["Leader"] == original_value:
                            self.project_id = i["Project_ID"]
                            self.project_table.update_row("Project_ID", self.project_id, "Leader", changed_value)
                            exit("Project_table")
                        elif i["Member1"] == original_value:
                            self.project_id = i["Project_ID"]
                            self.project_table.update_row("Project_ID", self.project_id, "Member1", changed_value)
                            exit("Project_table")
                        elif i["Member2"] == original_value:
                            self.project_id = i["Project_ID"]
                            self.project_table.update_row("Project_ID", self.project_id, "Member2", changed_value)
                            exit("Project_table")
                    exit("persons")
                elif what_table == "Advisor_pending_request":
                    for i in self.project_table.table:
                        if i["Project_ID"] == original_value:
                            self.project_table.update_row(list_can_change[0], original_value, list_can_change[0],
                                                          changed_value)
                            exit("Project_table")
                    for j in self.member_pending_table.table:
                        if j["Project_ID"] == original_value:
                            self.member_pending_table.update_row(list_can_change[0], original_value, list_can_change[0],
                                                                 changed_value)
                            exit("Member_pending_request")
                exit(what_table)
            elif select_number == 2:
                original_value = str(input("Which value you gonna change/update to: "))
                changed_value = str(input("what value you gonna change from original: "))
                if what_table == "persons" or what_table == "login":
                    self.input_table.update_row(list_can_change[0], give_me_id, list_can_change[1], changed_value)
                    exit(what_table)
                elif what_table == "Advisor_pending_request":
                    self.input_table.update_row(list_can_change[0], give_me_project_id, list_can_change[1],
                                                changed_value)
                    exit(what_table)

            elif select_number == 3:
                original_value = str(input("Which value you gonna change/update to: "))
                changed_value = str(input("what value you gonna change from original: "))
                if what_table == "persons" or what_table == "login":
                    self.input_table.update_row(list_can_change[0], give_me_id, list_can_change[2], changed_value)
                    exit(what_table)
                elif what_table == "Advisor_pending_request":
                    self.input_table.update_row(list_can_change[0], give_me_project_id, list_can_change[2],
                                                changed_value)
                    exit(what_table)

            elif select_number == 4:
                original_value = str(input("Which value you gonna change/update to: "))
                changed_value = str(input("what value you gonna change from original: "))
                self.input_table.update_row(list_can_change[0], give_me_id, list_can_change[3], changed_value)
                if what_table == "persons":
                    self.login_table.update_row(list_can_change[0], give_me_id, "role", changed_value)
                    exit("login")
                elif what_table == "login":
                    self.person_table.update_row(list_can_change[0], give_me_id, "type", changed_value)
                    exit("persons")
                exit(what_table)

        elif what_table == "Project_table":
            if select_number == 1:
                original_value = str(input("Which value you gonna change/update to: "))
                changed_value = str(input("what value you gonna change from original: "))
                self.input_table.update_row(list_can_change[0], original_value, list_can_change[0], changed_value)
                for i in self.advisor_pending_table.table:
                    if i["Project_ID"] == original_value:
                        self.advisor_pending_table.update_row(list_can_change[0], original_value, list_can_change[0],
                                                              changed_value)
                        exit("Advisor_pending_request")
                for j in self.member_pending_table.table:
                    if j["Project_ID"] == original_value:
                        self.member_pending_table.update_row(list_can_change[0], original_value, list_can_change[0],
                                                             changed_value)
                        exit("Member_pending_request")
                exit(what_table)
            elif select_number == 2:
                original_value = str(input("Which value you gonna change/update to: "))
                changed_value = str(input("what value you gonna change from original: "))
                self.input_table.update_row(list_can_change[1], original_value, list_can_change[1], changed_value)
                exit(what_table)
            elif select_number == 3:
                original_value = str(input("Which value you gonna change/update to: "))
                changed_value = str(input("what value you gonna change from original: "))
                self.input_table.update_row(list_can_change[2], original_value, list_can_change[2], changed_value)
                for i in self.login_table.table:
                    if i["ID"] == original_value:
                        self.login_table.update_row("ID", original_value, "ID", changed_value)
                for j in self.person_table.table:
                    if j["ID"] == original_value:
                        self.person_table.update_row("ID", original_value, "ID", changed_value)
                exit("login")
                exit("persons")
                exit(what_table)
            elif select_number == 4:
                original_value = str(input("Which value you gonna change/update to: "))
                changed_value = str(input("what value you gonna change from original: "))
                self.input_table.update_row(list_can_change[3], original_value, list_can_change[3], changed_value)
                for i in self.login_table.table:
                    if i["ID"] == original_value:
                        self.login_table.update_row("ID", original_value, "ID", changed_value)
                for j in self.person_table.table:
                    if j["ID"] == original_value:
                        self.person_table.update_row("ID", original_value, "ID", changed_value)
                exit("login")
                exit("persons")
                exit(what_table)

            elif select_number == 5:
                original_value = str(input("Which value you gonna change/update to: "))
                changed_value = str(input("what value you gonna change from original: "))
                self.input_table.update_row(list_can_change[4], original_value, list_can_change[4], changed_value)
                for i in self.login_table.table:
                    if i["ID"] == original_value:
                        self.login_table.update_row("ID", original_value, "ID", changed_value)
                for j in self.person_table.table:
                    if j["ID"] == original_value:
                        self.person_table.update_row("ID", original_value, "ID", changed_value)
                exit("login")
                exit("persons")
                exit(what_table)
            elif select_number == 6:
                original_value = str(input("Which value you gonna change/update to: "))
                changed_value = str(input("what value you gonna change from original: "))
                self.input_table.update_row(list_can_change[5], original_value, list_can_change[5], changed_value)
                for i in self.login_table.table:
                    if i["ID"] == original_value:
                        self.login_table.update_row("ID", original_value, "ID", changed_value)
                for j in self.person_table.table:
                    if j["ID"] == original_value:
                        self.person_table.update_row("ID", original_value, "ID", changed_value)
                exit("login")
                exit("persons")
                exit(what_table)
            elif select_number == 7:
                original_value = str(input("Which value you gonna change/update to: "))
                changed_value = str(input("what value you gonna change from original: "))
                self.input_table.update_row(list_can_change[6], original_value, list_can_change[6], changed_value)
                exit(what_table)
        elif what_table == "Member_pending_request":
            if select_number == 1:
                original_value = str(input("Which value you gonna change/update to: "))
                changed_value = str(input("what value you gonna change from original: "))
                self.input_table.update_row(list_can_change[0], original_value, list_can_change[0], changed_value)
                for i in self.advisor_pending_table.table:
                    if i["Project_ID"] == original_value:
                        self.advisor_pending_table.update_row(list_can_change[0], original_value, list_can_change[0],
                                                              changed_value)
                        exit("Advisor_pending_request")
                for j in self.project_table.table:
                    if j["Project_ID"] == original_value:
                        self.project_table.update_row(list_can_change[0], original_value, list_can_change[0],
                                                      changed_value)
                        exit("Project_table")
                exit(what_table)
            elif select_number == 2:
                original_value = str(input("Which value you gonna change/update to: "))
                changed_value = str(input("what value you gonna change from original: "))
                self.input_table.update_row(list_can_change[0], give_me_project_id, list_can_change[1], changed_value)
                exit(what_table)
            elif select_number == 3:
                original_value = str(input("Which value you gonna change/update to: "))
                changed_value = str(input("what value you gonna change from original: "))
                self.input_table.update_row(list_can_change[0], give_me_project_id, list_can_change[2], changed_value)
                exit(what_table)

            elif select_number == 4:
                original_value = str(input("Which value you gonna change/update to: "))
                changed_value = str(input("what value you gonna change from original: "))
                self.input_table.update_row(list_can_change[0], give_me_project_id, list_can_change[2], changed_value)
                exit(what_table)

    def choose_who_gonna_prove(self):
        print("Available faculty")
        print(self.project_table)
        select_project_id = str(input(f"which group you gonna choose evaluator for them: "))
        print(self.login_table.filter(lambda x: x["role"] == "faculty"))
        choose_evaluator = str(input(f"choose evaluator for student project: "))
        self.project_table.update_row("Project_ID", select_project_id, "Evaluator", choose_evaluator)
        self.login_table.update_row("ID", choose_evaluator, "role", "Evaluator")
        self.project_table.update_row("Project_ID", select_project_id, "Status", choose_evaluator)
        exit("Project_table")
        exit("login")

    def see(self):
        print(f"1.Project_table\n"
              f"2.login\n"
              f"3.Advisor_pending_request\n"
              f"4.Member_pending_request\n"
              f"5.person")
        what_see = str(input(f"what do you want to see table: "))
        print(data.search(what_see))


data = initializing()
val = login()
if val[1] == "student":
    s1 = Student()
    while True:
        print(f"1.lead or member\n"
              f"2.see invitation\n"
              f"3.sent responses\n"
              f"4.Exit")
        what_do = str(input(f"What do you want to do: "))
        if what_do == "4":
            break
        elif what_do == "1":
            s1.lead_or_member()
            print()
        elif what_do == "2":
            s1.see_invitation()
        elif what_do == "3":
            which_project = str(input("Which project that you want to sent responses: "))
            what_is_your_response = str(input("What is your response: "))
            s1.response(what_is_your_response, which_project)


if val[1] == 'admin':
    a1 = Admin()
    print(f"1.see\n"
          f"2.edit\n"
          f"3.select evaluator\n"
          f"4.Exit")
    what_do = str(input(f"What do you want to do: "))
    if what_do == "1":
        a1.see()
        print()
    elif what_do == "2":
        a1.change_and_update()
        print()
    elif what_do == "3":
        a1.choose_who_gonna_prove()
        print()

elif val[1] == "advisor":
    ad = Advisor()
    while True:
        print("1.see\n"
              "2.sent approve\n"
              "3.Exit")
        what_do = str(input(f"what do you want to do: "))
        if what_do == "3":
            break
        elif what_do == "1":
            ad.see()
            print()
        elif what_do == "2":
            ad.sent_approve()
            print()
elif val[1] == "lead":
    l1 = Lead()
    while True:
        print(f"1.Create project\n"
              f"2.Sent invitation to student who want to \n"
              f"3.See project detail\n"
              f"4.sent invitation to advisor\n"
              f"5.update prpject status\n"
              f"6.Exit.")
        what_do = str(input(f"what do you want to do(Choose by number): "))
        if what_do == "6":
            break
        elif what_do == "1":
            l1.create_project()
            print()
        elif what_do == "2":
            l1.sent_invitation()
            print()
        elif what_do == "3":
            l1.see_detail()
            print()
        elif what_do == "4":
            l1.sent_invitation()
            print()
        elif what_do == "5":
            l1.update_status()
            print()
elif val[1] == "Member":
    m1 = Member()
    while True:
        print(f"1.See project\n"
              f"2.Update status of project\n"
              f"3.Exit")
        what_do = str(input(f"What do you want to do: "))
        if what_do == "3":
            break
        elif what_do == "1":
            m1.see_project_table()
            print()
        elif what_do == "2":
            m1.update_status()
            print()

elif val[1] == "faculty":
    f1 = Faculty()
    while True:
        print(f"1.See who invite to be advisor\n"
              f"2.See project detail\n"
              f"3.Sent_responses\n"
              f"4.Eval_Project\n"
              f"5.Exit")
        what_do = str(input(f"What do you want to do: "))
        if what_do == "5":
            break
        elif what_do == "1":
            f1.see_request()
            print()
        elif what_do == "2":
            f1.see_project()
            print()
        elif what_do == "3":
            f1.response()
            print()
        elif what_do == "4":
            f1.eval_project()
            print()
