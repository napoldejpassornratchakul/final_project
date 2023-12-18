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
 -there are 3 function
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
if response of user is accept. it will updated status of Project_table

