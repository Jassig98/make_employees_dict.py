# Author: Jasmine Singh
# Github Username: Jassig98
# Date: November 15, 2022
# Description: Takes 4 values and uses them to initialize data members. Takes list of names, ID numbers, salaries, and email addresses to create employee object, adds them to dictionary.

class Employee:
    def __init__(self, name, ID_number, salary, email):

        self.name = name
        self.ID_number = ID_number
        self.salary = salary
        self.email_address = email

    def make_employee_dict(list_names, list_ID, list_salary, list_email):
        employee_dict = {}
        list_len= len (list_ID)

        for i in range (list_len):

            name= list_names[i]
            id_num= list_ID[i]
            salary=list_salary[i]
            email= list_email[i]

            employee_dict[id_num]= Employee (name, id_num, salary, email)

            return emplyee_dict