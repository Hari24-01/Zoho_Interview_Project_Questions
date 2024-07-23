# 2. Employee Record Management System
# Objective: Build an employee record management application.
# Requirements:
# - Create a system to manage employee records.
# - Allow adding, updating, and deleting employee records.
# - Implement search functionality based on different criteria (name, department, etc.).
# - Display reporting hierarchy of employees.
# - Handle edge cases such as circular references in the reporting structure.

import mysql.connector as mysql

class ManagementSystem():
    data=mysql.connect(
        host="localhost",
        user="root",
        password="",
        database="Record"
    )
    # print(data)
    db=data.cursor(buffered=True)
    db.execute("CREATE DATABASE IF NOT EXISTS Record")
    # db.execute("USE Record")
    db.execute("CREATE TABLE IF NOT EXISTS employee(ID INT(6) PRIMARY KEY,name VARCHAR(50) NOT NULL,department VARCHAR(25) NOT NULL,age INT(4),gender CHAR(10),location VARCHAR(25))")
    # db.execute("DESC employee")
    # for i in db:
    #     print(i)
    # df=pd.DataFrame(db.fetchall(),columns=db.column_names)
    # print(df)
    def __int__(self):
          pass

    def new_entry(self,*agrs):
        self.db.execute(f"INSERT INTO employee(ID,name,department,age,gender,location) VALUES{agrs}")
        self.data.commit()
        return "++++++++++++++++++++++++DATA STORED+++++++++++++++++++++++++++++++++++"
    
    def update(self,search,value,update_col,val):
        if search=="name" or search=="department" or search=="gender" or search=="location" :
            col=f"{search} = '{value}'"
            self.db.execute(f"SELECT * FROM employee WHERE {col}")
            print("BEFORE UPDATE : ",self.db.fetchall())
            for i in range(0,len(update_col)):
                if update_col[i]=="name" or update_col[i]=="department" or update_col[i]=="gender" or update_col[i]=="location" :
                    change=f"{update_col[i]} = '{val[i]}'"
                    self.db.execute(f"UPDATE employee SET {change} WHERE {col}")
                    self.db.execute(f"SELECT * FROM employee WHERE {col}")
                else:
                    change=f"{update_col[i]} = {val[i]}"
                    self.db.execute(f"UPDATE employee SET {change} WHERE {col}")
                    self.db.execute(f"SELECT * FROM employee WHERE {col}")
        else:
            col=f"{search} = {value}"
            self.db.execute(f"SELECT * FROM employee WHERE {col}")
            print("BEFORE UPDATE : ",self.db.fetchall())
            if update_col[i]=="name" or update_col[i]=="department" or update_col[i]=="gender" or update_col[i]=="location" :
                    change=f"{update_col[i]} = '{val[i]}'"
                    self.db.execute(f"UPDATE employee SET {change} WHERE {col}")
                    self.db.execute(f"SELECT * FROM employee WHERE {col}")
            else:
                change=f"{update_col[i]} = {val[i]}"
                self.db.execute(f"UPDATE employee SET {change} WHERE {col}")
                self.db.execute(f"SELECT * FROM employee WHERE {col}")
        
        return self.db.fetchall()

    
    def display(self,*agrs):
        
        if agrs[0]=="name" or agrs[0]=="department" or agrs[0]=="gender" or agrs[0]=="location" :
            col=f"{agrs[0]} = '{agrs[1]}'"
            self.db.execute(f"SELECT * FROM employee WHERE {col}")
        else:
            col=f"{agrs[0]} = {agrs[1]}"
            self.db.execute(f"SELECT * FROM employee WHERE {col}")
        return "EMPLOYEE DATA DELETED"
    
    def delete(self,search,value):
        if search=="name" or search=="department" or search=="gender" or search=="location" :
            col=f"{search} = '{value}'"
            self.db.execute(f"DELETE FROM employee WHERE {col}")
        else:
            col=f"{search} = {value}"
            self.db.execute(f"DELETE FROM employee WHERE {col}")
        return "EMPLOYEE DATA DELETED"
    





empl=ManagementSystem()
print("""__________________________Welcome__________________________""")  
print("""_________________CHOICE ANY OPTION FROM 1-5_________________""")
print("1.ADD NEW EMPLOYEE DATA")
print("2.UPDATE EXIST EMPLOYEE DATA")
print("3.DISPLAY EMPLOYEE DETIALS")
print("4.REMOVE EMPLOYEE FROM THE COMPANY")
print("5.EXIT")

choice=0
while choice!=5:

    choice=int(input("ENTER CHOICE FROM 1-5 : "))

    if choice == 1:
        print("ENTER NEW EMPLOYEE RECORD : ")
        id=int(input("ENTER YOUR 6-DIGIT EMPLOYEE ID : "))
        emp_name=str(input("ENTER EMPLOYEE NAME : "))
        dep=str(input("ENTER YOUR DEPARTMENT : "))
        age=int(input("ENTER YOUR EMPLOYEE AGE : "))
        gen=str(input("ENTER male OR female : "))
        loc=str(input("ENTER EMPLOYEE LOCATION :"))
        print(empl.new_entry(id,emp_name,dep,age,gen,loc))

    if choice == 2:
        arr=["ID","name","department","age","gender","location"]
        print(f"SEARCH EMPLOYEE WITH {arr}")
        arr=["name","department","age","gender","location"]
        sear=str(input("ENTER ACCORDING TO WHICH SEARCH VALUE AS GIVEN LIST ABOVE : "))
        value=str(input(f"ENTER EMPLOYEE {sear} : "))
        up=list(map(str,input(f"CHOICE COLUMNS TO UPDATE FROM THE LIST {arr}  : ").split()))
        
        val=[]
        for i in range(0,len(up)):
            a=input("ENTER THE VALUES AS PRE MENTIONED NUMBER OF COLUMNS : ")
            val.append(a)
        
        print(empl.update(sear,value,up,val))

        print("*************************SUCESSFUL UPDATED*************************")

    if choice == 3:
        arr=["ID","name","department","age","gender","location"]
        print(f"SEARCH EMPLOYEE WITH {arr}")
        sear=str(input("ENTER ACCORDING TO WHICH SEARCH VALUE AS GIVEN LIST ABOVE : "))
        value=str(input(f"ENTER EMPLOYEE {sear} : "))
        for i in range(0,6):
            print("_________________",arr[i],":",empl.display(sear,value)[0][i],"_________________")

    if choice == 4:
        arr=["ID","name","department","age","gender","location"]
        print(f"SEARCH EMPLOYEE WITH {arr}")
        sear=str(input("ENTER VALUE TO DELETE AS GIVEN LIST ABOVE : "))
        value=str(input(f"ENTER EMPLOYEE {sear} TO DELETE : "))

        print(empl.delete(sear,value))


    if choice > 5 or choice <= 0:
        print("_________________ENTER A VALID CHOICE !!_________________")
