There will be a project, member_pending_, login, advisor_pending_ table 

what student can see and do:
        if there are pending requests to become members of already created projects:
            you can choose Accept or deny to be member of this project, then the project table will be updated:
        in other way:
            if you denied all member request, you can choose to be leader of the project:
                the project and login table will be updated. In addition, if you want more members to do this project. you can sent out the invitation to 
                only student role not a member and leader role.

- (Every students are 'Member')
- after login, check if that student is in any group or not

- if IN GROUP
- stay member
- cannot create project

- if NOT IN GROUP
- allow to create a project


                


What leader can see and do:
    as a leader, you can see project status, such as (pending member, pending advisor or ready to solicit an advisor). Additionally, cam see who has responded 
    to the request sent out, then member_pending_request table will be updated. Furthermore, as a leader, you can send out requests to a potential advisor, but
    can only do one at a time and it must be after all potential members have accepted or denied the requests: advisor__pending__request table will be updated.
    In addition, student who choose leader role can see the faculty name on the table:
                and sent the invitation to the faculty role to be advisor of his/her project. 
    and can make a vote to the group of member whether who advisor that they gonna choose according to the person table.


What member can see and do:
    as a member: can see pending member or advisor, and can see and modify project information. 
    then project table and see who has responded to the requests sent out:
    and make a vote
    
    
    




there are two faculty types:
    first type : A normal faculty who is not an advisor:
        Action:
            1.can see request to be a supervisor
            2.send response denying to serve as an advisor
            3.see details of all this project
            4.Evaluate the project(on the proposal.md)
    second type: advising faculty:
        Action:
            1.See request to be a supervisor
            2.send accept or deny response for project advisor or not
            3.see detail of all the project
            4.Evaluate the project(on the proposal.md)
            5.Approve the project 


As admin:
        Managing the database:
            Action:
                Can update all the tables there

On my project:
    I will add the status of member column in login.csv. because As I mentioned. we cannot know that member guys are have a group or not.
- 
- (Every students are 'Member')
- after login, check if that student is in any group or not

- if IN GROUP
- stay member
- cannot create project

- if NOT IN GROUP
- allow to create a project


                
