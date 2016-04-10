#!/usr/bin/env python3


from faker import Factory
import random
import csv
POSTNOMINALS = ('Dr.', 'Miss', 'Mr.', 'Mrs.', 'Ms.')

class userobject:
    
    
    def __init__(self, name, address):
        u_ac_int = random.randint(0, 10)
        
        for st in POSTNOMINALS:
            name = name.replace(st, '', 1)
            name = name.lstrip()
        self.name = name
        self.address = address
        self.samAccountName = str(name[:name.find(' ')] + str(u_ac_int))
        self.ParentOU = 'OU=Unassigned-Users, DC=BOSHED, DC=org, DC=uk'
    
    def return_userobject(self):
        return self
    
def Get_User_input():
    try:
        n_users = int(input('how many users will you require? '))
        return n_users
    
    except ValueError as e:
        print('caught % error, please enter an integer (1-5000)')
        return 0
     
def faker_user_objects(n_users):
    user_objects = []
    
    for x in range(0, n_users):
        F_Engine = Factory.create()
        New_U_Object = userobject(F_Engine.name(), F_Engine.address())
        # New_U_Object = userobject.return_userobject(New_U_Object)
        user_objects.append(New_U_Object)
    return user_objects

def write_csv(user_objects):
    try:
        with open('names.csv', 'w') as csvfile:
            fieldnames = ['name', 'samAccountName', 'ParentOU', 'Address']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
            writer.writeheader()
            for x in user_objects:
              
                writer.writerow({'name' : x.name,'samAccountName' : x.samAccountName, 'ParentOU' : x.ParentOU, 'Address' : x.address})
                       
            csvfile.close()
            
    except IOError:
        print('Failed to write names.csv.  Does it exist already?')
                    
def main():
    user_int=0
    while user_int == 0:
        user_int = Get_User_input()
        user_objects = faker_user_objects(user_int)
        write_csv(user_objects)
        
if __name__ == '__main__':
    main()
    
        

    
    
        
    
        
    