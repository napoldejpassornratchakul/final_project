# Final project for 2023's 219114/115 Programming I
* Starting files for part 1
  - database.py
  - project_manage.py
  - persons.csv
on the part initializing function:
  - this function just added the table to database, and return database

on login function:
   - this function will ask the username and password from the user to get his/her ID and role:
   - if the input there are not match any name in login csv. it will return None

on the exit function part:
  - I have adapted the function by get the parameter called table name, However, it can run correctly 


on the class Student:
 -there are 3 functions
first function called lead_or_member:
this function will ask user whether "you want to create project or not":
---if Yes--------
if user answered is "Yes" it will automatically updated status of that user to be lead:
and also run create.project(). let me explain the create.project(): 
if you run create_project() it will ask you Title of project and ask for deadline, then it will add project to Project_table.csv
automatically. after that it will ask you whether do you want to sent invitation to member and advisor or not:

----if No------
if user answered is "No" it will print member_pending_request of that user automatically and 
it will ask user which project ID that you want to sent response.
if response of user is accept. it will updated status of Project_table on the member1 or member2 column and
member_pending_request table will also update, and login table will update role of user too.


on the class Lead:
there are 5 functions:
1.create_project the explained of this function on above
2.sent_invitation to member is the function that sent the invitation to the member and the member_pending_request will update:
3.see detail of his/her project
4.sent_invitation to advisor is the function that sent the invitation to the advisor and the advisor_pending_request will update
5.update_status is function that update status project_table like how was going on what is your progress now:

class Member
there are 2 functions:
1.see_project_table just print the project detail
2.update_status is function that update status project_table like how was going on what is your progress now:


class Faculty:
there are 4 functions:
1.see_request function just print advisor_pending_request
2.see_project function just print all project table
3.response function is sent response whether accept or deny to be advisor:
if accept, the role will update to advisor.
4.eval_project = if there are project that need to be eval, so can run this function
if can run it wil ask user that do you gonna give them pass or reject. if reject it will have to ask user why you give them]
reject and feedback


class Advisor:
there are 2 functions:
1.sent_approve is sent approve that this project is ready to eval
2.see function see detail of project

class Admin
there are 3 functions:
1.change_update function will ask user which table you gonna change and what/who do you want to change
2.choose_gonna_prove function is admin will choose other normal faculty or advisor who gonna prove each project:
because the advisor who own their project should not be eval by him/herself. IT WILL BIAS!!!!
3.see function will ask user which table that he/her want to see


How to run my project:
first it will run function login to get the ID and role of user:
by asking username and password:

if role of that person match to any if condition it will ask the user that what do you want to do:
by answer by number

my Bugs:
since I tested all, I have not encountered with the bugs yet. but I'm not sure with the admin class
because, it's quite complicated code but after I tested all there is not bug, it can change value correctly
for example. If I change the ID of the user who be lead on the project table. both of them will change too:

my missing:
I think my missing point is sometime you need to login twice to get the role that you want: because, early there are have
only 3 role, so sometime you need to login twice




