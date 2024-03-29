import os,sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
sys.path.append("D:\\Projects_Sem-3\\Python-I_Individual\\GUI_Folder")
sys.path.append("D:\\Projects_Sem-3\\Python-I_Individual\\Demo")
from main import *
from student import Student
from teacher import Teacher
from Class import Class
import random

import mysql.connector as mc

class Project:
    branch = 2
    capacity = num_class = 0
    subjects = []
    total_students = []
    selected_student = []
    faculty = []
    classes = []

    def main_logic(self):
        if(not(os.path.exists("D:\\Projects_Sem-3\\Python-I_Individual\\done.txt"))):
            arr = ["CE", "IT"]

            self.capacity = self.branch * 90
            self.num_class = self.capacity / 30    

            self.subjects.append("Python")
            self.subjects.append("FSD")
            self.subjects.append("PS")   
            self.subjects.append("DE")

            self.storedata()
            self.select_student()
        else:
            self.load_data()

# Project.main_logic()

    def storedata(self):
        student_data = open("D:\\Projects_Sem-3\\Python-I_Individual\\data\\Student Data.txt","r")

        line = student_data.readline()

        while line != '':
            data = line.split(',')

            enrollment_id =  int(data[0])
            name = data[1]
            merit_rank = int(data[2])
            phone = data[3]
            mail = data[4]
            city = data[5]

            s = Student(name, enrollment_id, merit_rank, mail, phone, city)
            self.total_students.append(s)
            line = student_data.readline()

        faculty_data = open("D:\\Projects_Sem-3\\Python-I_Individual\\data\\faculty_data.txt","r")    

        line1 = faculty_data.readline()

        while line1 != '':
            data1 = line1.split(',')

            t = Teacher(data1[0], data1[1], data1[2], data1[3], data1[4])
            
            temp = data1[0].split()
            t.userId = temp[0] + data1[4][0:3]

            min = 10000
            max = 99999
            t.password = random.randrange(max - min + 1) + min
            
            self.faculty.append(t)

            line1 = faculty_data.readline() 

    def select_student(self):
        self.total_students.sort(key = lambda obj : obj.merit_rank)  

        cnt = 1

        for i in self.total_students:
            i.roll_no = cnt
            cnt += 1

            self.selected_student.append(i)

            if(cnt > self.capacity):
                break       

        ce = 1
        it = 1

        for i in self.selected_student:
            os.mkdir(f"D:\\Projects_Sem-3\\Python-I_Individual\\students\\{i.name}")
            f = open(f"D:\\Projects_Sem-3\\Python-I_Individual\\students\\{i.name}\\msg.txt", 'w')
            f.close()

            if i.roll_no <= 90:
                i.department = "CE"
                i.roll_no = ce
                ce += 1
            elif i.roll_no > 90 and i.roll_no <= 180:
                i.department = "IT"
                i.roll_no = it
                it += 1

            arr = i.name.split()

            i.userId = arr[0] + i.phone[0:3]

            min = 10000
            max = 99999
            i.password = random.randrange(max - min + 1) + min        

        temp_list = self.selected_student
        random.shuffle(temp_list)

        start = 0
        end = 17

        for i in self.faculty:
            temp = []

            for j in range(start, end+1):
                temp.append(temp_list[j])
                s = temp_list[j]
                s.mentor = i.name

            start = end + 1
            end += 18
                                     
            i.mystudents = temp

        for i in self.faculty:
            os.mkdir(f"D:\\Projects_Sem-3\\Python-I_Individual\\Faculties\\{i.name}")
            f = open(f"D:\\Projects_Sem-3\\Python-I_Individual\\Faculties\\{i.name}\\mystudent.txt", 'w')

            for j in i.mystudents:
                f.write(j.name + "\n")

            f.close()

        count1 = 1
        count2 = 1
    
        for i in self.selected_student:
            i.class_alloted = "D" + str(count1)

            count2 += 1

            if count2 == 31:
                c = Class("D" + str(count1))
                self.classes.append(c)
                count1 += 1
                count2 = 1
                print(c.id)

        for i in self.classes:
            temp1 = []

            os.mkdir(f"D:\\Projects_Sem-3\\Python-I_Individual\\class\\{i.id}")
            f = open(f"D:\\Projects_Sem-3\\Python-I_Individual\\class\\{i.id}\\students.txt", 'w')

            for j in self.selected_student:
                if j.class_alloted == i.id:
                    f.write(j.name + "\n")
                    temp1.append(j)

            i.students = temp1 


        app = QApplication(sys.argv)
        widget = QtWidgets.QStackedWidget()
        welcome = WelcomeScreen(self.classes, Project(), widget)
        widget.addWidget(welcome)
        widget.setFixedWidth(950)
        widget.setFixedHeight(700)
        widget.show()
        sys.exit(app.exec_())

    def get_python_faculties(self):
        temp_list = []
        for i in self.faculty:  
            if i.primary_subj == 'Python' or i.secondary_subj == 'Python':
                temp_list.append(i.name)

        return temp_list
                
    def get_fsd_faculties(self):
        temp_list = []
        for i in self.faculty:
            if i.primary_subj == 'FSD' or i.secondary_subj == 'FSD':
                temp_list.append(i.name)

        return temp_list 
               
    def get_de_faculties(self):
        temp_list = []
        for i in self.faculty:
            if i.primary_subj == 'DE' or i.secondary_subj == 'DE':
                temp_list.append(i.name)

        return temp_list 
               
    def get_ps_faculties(self):
        temp_list = []
        for i in self.faculty:
            if i.primary_subj == 'PS' or i.secondary_subj == 'PS':
                temp_list.append(i.name)

        return temp_list        

    def connector(self):
        mydb = mc.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "python_project"
        )
        return mydb
    
    def storeToDatabase(self, hodObj):
        mydb = self.connector()
        mycursor = mydb.cursor()
        query1 = "INSERT INTO students (UserId,password,Name,Enrollment_ID,Merit_Rank, Mail, Phone, Department, Roll_No, Class, City, Mentor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        for i in self.selected_student:
            value = (i.userId, i.password, i.name, i.enrollment_id, i.merit_rank, i.email, i.phone, i.department, i.roll_no, i.class_alloted, i.city, i.mentor)

            mycursor.execute(query1,value)
            mydb.commit()

        query2 = "INSERT INTO faculties (UserId,password,Name,Primary_subject,Secondary_subject, Mail, Phone, myStudent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

        for i in self.faculty:

            f = open(f"D:\\Projects_Sem-3\\Python-I_Individual\\Faculties\\{i.name}\\mystudent.txt", 'r')
            content = f.read()

            value = (i.userId, i.password, i.name, i.primary_subj, i.secondary_subj, i.mail, i.phone, content)

            mycursor.execute(query2,value)
            mydb.commit()

        query3 = "INSERT INTO hod (UserId,password,name,phone,mail) VALUES (%s, %s, %s, %s, %s)"
        value = (hodObj.hod.userId,hodObj.hod.password,hodObj.hod.name,hodObj.hod.phone,hodObj.hod.mail)

        mycursor.execute(query3,value)
        mydb.commit()

        query4 = "INSERT INTO class (ID,python_faculty,fsd_faculty,de_faculty,ps_faculty,students) VALUES (%s, %s, %s, %s, %s, %s)"

        for i in self.classes:
            
            with open(f"D:\\Projects_Sem-3\\Python-I_Individual\\class\\{i.id}\\students.txt", 'r') as f:
                content = f.read()
                print(f"-------{i.id}--------")
                print(content)
                print("-----------------")
                value = (i.id, i.python_faculty, i.fsd_faculty, i.de_faculty, i.ps_faculty, content)

                mycursor.execute(query4, value) 
                mydb.commit()
                f.close()
        
        # f = open(f"D:\\Projects_Sem-3\\Python-I_Individual\\class\\abc\\students.txt", 'r')
        # content = f.readlines()
        # print(content,"prince") 
        # query5 = "INSERT INTO class (students) VALUES (%s)"
        # value = (content,)
        # mycursor.execute(query5, value)
        # mydb.commit()

    def load_data(self):
        mydb = self.connector()
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM students")

        myresult1 = mycursor.fetchall()

        for i in myresult1:
            s = Student(i[2], i[3], i[4], i[5], i[6], i[10])
            
            s.userId = i[0]
            s.password = i[1]
            s.department = i[7]
            s.class_alloted = i[9]
            s.roll_no = i[8]
            s.mentor = i[11]

            self.selected_student.append(s) 
        
        mycursor.execute("SELECT * FROM faculties")

        myresult2 = mycursor.fetchall()

        for i in myresult2:
            t = Teacher(i[2], i[3], i[4], i[5], i[6])
            self.selected_student.append(s)

            content = i[7]

            print(content)


p = Project()
p.main_logic()   