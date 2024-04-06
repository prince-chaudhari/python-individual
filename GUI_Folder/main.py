import matplotlib.pyplot as plt
import random
from datetime import datetime
from email_validator import validate_email, EmailNotValidError
# import resource
import sys
import os
from PyQt5.uic import loadUi
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDialog, QAction
sys.path.append("D:\\Projects_Sem-3\\Python-I_Individual\\Demo")
from hod import Hod
from tabulate import tabulate

class WelcomeScreen(QDialog):
    def __init__(self, classes, p, widget):
        self.classes = classes
        self.p = p
        self.widget = widget
        super(WelcomeScreen, self).__init__()
        loadUi("welcome.ui", self)
        ClassForFaculty.p = p
        AppointHod.p = p
        self.nextBtn.clicked.connect(self.go_classForFaculty)

    def go_classForFaculty(self):
        cnt = 0
        cff1 = ClassForFaculty_1(self.classes, self.widget, cnt)
        self.widget.addWidget(cff1)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)


class ClassForFaculty(QDialog):

    def add_menu(self, obj):
        python_faculties = self.p.get_python_faculties()
        fsd_faculties = self.p.get_fsd_faculties()
        de_faculties = self.p.get_de_faculties()
        ps_faculties = self.p.get_ps_faculties()

        obj.pythonFaculty.addItems(python_faculties)
        obj.fsdFaculty.addItems(fsd_faculties)
        obj.deFaculty.addItems(de_faculties)
        obj.psFaculty.addItems(ps_faculties)

    def add_faculties(obj, classObj):
        classObj.python_faculty = obj.pythonFaculty.currentText()
        classObj.fsd_faculty = obj.fsdFaculty.currentText()
        classObj.de_faculty = obj.deFaculty.currentText()
        classObj.ps_faculty = obj.psFaculty.currentText()


class ClassForFaculty_1(QDialog):
    def __init__(self, classes, widget, cnt):
        self.classes = classes
        self.cnt = cnt
        self.widget = widget
        super(ClassForFaculty_1, self).__init__()
        loadUi("classForFaculty_1.ui", self)
        widget.setFixedWidth(920)
        widget.setFixedHeight(480)

        self.whichClass.setText(f"Enter the faculty for class {self.classes[self.cnt].id}")
        c = ClassForFaculty()
        c.add_menu(self)
        self.submit.clicked.connect(self.nextPage)

    def nextPage(self):
        ClassForFaculty.add_faculties(self, self.classes[self.cnt])
        self.cnt += 1
        cff2 = ClassForFaculty_2(self.classes, self.widget, self.cnt)
        self.widget.addWidget(cff2)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)


class ClassForFaculty_2(QDialog):
    def __init__(self, classes, widget, cnt):
        self.classes = classes
        self.cnt = cnt
        self.widget = widget
        super(ClassForFaculty_2, self).__init__()
        loadUi("classForFaculty_2.ui", self)
        widget.setFixedWidth(920)
        widget.setFixedHeight(480)

        self.whichClass.setText(f"Enter the faculty for class {
                                self.classes[self.cnt].id}")
        c = ClassForFaculty()
        c.add_menu(self)
        self.submit.clicked.connect(self.nextPage)

    def nextPage(self):
        ClassForFaculty.add_faculties(self, self.classes[self.cnt])
        self.cnt += 1
        cff2 = ClassForFaculty_3(self.classes, self.widget, self.cnt)
        self.widget.addWidget(cff2)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)


class ClassForFaculty_3(QDialog):
    def __init__(self, classes, widget, cnt):
        self.cnt = cnt
        self.classes = classes
        self.widget = widget
        super(ClassForFaculty_3, self).__init__()
        loadUi("classForFaculty_3.ui", self)
        widget.setFixedWidth(920)
        widget.setFixedHeight(480)

        self.whichClass.setText(f"Enter the faculty for class {
                                self.classes[self.cnt].id}")
        c = ClassForFaculty()
        c.add_menu(self)
        self.submit.clicked.connect(self.nextPage)

    def nextPage(self):
        ClassForFaculty.add_faculties(self, self.classes[self.cnt])
        self.cnt += 1
        cff2 = ClassForFaculty_4(self.classes, self.widget, self.cnt)
        self.widget.addWidget(cff2)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)


class ClassForFaculty_4(QDialog):
    def __init__(self, classes, widget, cnt):
        self.cnt = cnt
        self.classes = classes
        self.widget = widget
        super(ClassForFaculty_4, self).__init__()
        loadUi("classForFaculty_4.ui", self)
        widget.setFixedWidth(920)
        widget.setFixedHeight(480)

        self.whichClass.setText(f"Enter the faculty for class {
                                self.classes[self.cnt].id}")
        c = ClassForFaculty()
        c.add_menu(self)
        self.submit.clicked.connect(self.nextPage)

    def nextPage(self):
        ClassForFaculty.add_faculties(self, self.classes[self.cnt])
        self.cnt += 1
        cff2 = ClassForFaculty_5(self.classes, self.widget, self.cnt)
        self.widget.addWidget(cff2)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)


class ClassForFaculty_5(QDialog):
    def __init__(self, classes, widget, cnt):
        self.cnt = cnt
        self.classes = classes
        self.widget = widget
        super(ClassForFaculty_5, self).__init__()
        loadUi("classForFaculty_5.ui", self)
        widget.setFixedWidth(920)
        widget.setFixedHeight(480)

        self.whichClass.setText(f"Enter the faculty for class {
                                self.classes[self.cnt].id}")
        c = ClassForFaculty()
        c.add_menu(self)
        self.submit.clicked.connect(self.nextPage)

    def nextPage(self):
        ClassForFaculty.add_faculties(self, self.classes[self.cnt])
        self.cnt += 1
        cff2 = ClassForFaculty_6(self.classes, self.widget, self.cnt)
        self.widget.addWidget(cff2)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)


class ClassForFaculty_6(QDialog):
    def __init__(self, classes, widget, cnt):
        self.cnt = cnt
        self.classes = classes
        self.widget = widget
        super(ClassForFaculty_6, self).__init__()
        loadUi("classForFaculty_6.ui", self)
        widget.setFixedWidth(920)
        widget.setFixedHeight(480)

        self.whichClass.setText(f"Enter the faculty for class {
                                self.classes[self.cnt].id}")
        c = ClassForFaculty()
        c.add_menu(self)
        self.submit.clicked.connect(self.nextPage)

    def nextPage(self):
        ClassForFaculty.add_faculties(self, self.classes[self.cnt])
        appoint_hod = AppointHod(self.widget)
        self.widget.addWidget(appoint_hod)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)


class AppointHod(QDialog):
    hod = Hod()

    def __init__(self, widget):
        self.widget = widget
        super(AppointHod, self).__init__()
        loadUi("appointHod.ui", self)
        widget.setFixedWidth(803)
        widget.setFixedHeight(575)

        self.hodBtn.clicked.connect(self.nextPage)

    def nextPage(self):
        self.hod.name = hodName = self.hodName.text()
        self.hod.mail = hodEmail = self.hodEmail.text()
        self.hod.phone = hodNumber = self.hodNumber.text()

        if (len(hodName) == 0 or len(hodEmail) == 0 or len(hodNumber) == 0):
            self.error.setText("Please fill all fields!!")
            return
        elif (not (self.hod.is_valid_emailid())):
            self.error.setText("Please Enter valid email id!!")
            return
        elif (not (self.hod.is_valid_number())):
            self.error.setText("Please Enter valid number!!")
            return
        else:
            self.hod.userId = self.hod.generate_userid()
            self.hod.password = self.hod.generate_pass()
            self.p.storeToDatabase(self.hod)
            f = open("D:\\Projects_Sem-3\\Python-I_Individual\\done.txt", "w")
            LoginScreen.hod = self.hod
            login = LoginScreen(self.widget, self.p)
            self.widget.addWidget(login)
            self.widget.setCurrentIndex(self.widget.currentIndex() + 1)


class LoginScreen(QDialog):
    def __init__(self, widget, p):
        self.widget = widget
        HodLoginScreen.p = p
        FacultyLoginScreen.p = p
        StudentLoginScreen.p = p
        SearchFacultyForStudent.p = p
        ClassFaculty.p = p
        SearchClass.p = p
        SearchStudent.p = p
        FacultyStudents.p = p
        FacultyClasses.p = p
        UpdateStudent.p = p
        ChangeProperties.p = p
        RemoveStudent.p = p
        SearchFacultyForHod.p = p
        MsgToStudent.p = p
        GiveMarks.p = p
        StudentProgress.p = p
        ChangePropertiesStudent.p = p
        ChangePropertiesHod.p = p

        widget.setFixedWidth(861)
        widget.setFixedHeight(631)

        if (not (os.path.exists("D:\\Projects_Sem-3\\Python-I_Individual\\notice.txt"))):
            self.send_instruction_for_change_personal_details()
            self.send_userid_password_to_Hod()

        super(LoginScreen, self).__init__()
        loadUi("login.ui", self)
        widget.setFixedWidth(961)
        widget.setFixedHeight(432)
        self.hodBtn.clicked.connect(self.go_hod_interface)
        self.facultyBtn.clicked.connect(self.go_faculty_interface)
        self.studentBtn.clicked.connect(self.go_student_interface)

    def go_hod_interface(self):
        hod_screen = HodLoginScreen(self.widget)
        self.widget.addWidget(hod_screen)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def go_faculty_interface(self):
        faculty_screen = FacultyLoginScreen(self.widget)
        self.widget.addWidget(faculty_screen)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def go_student_interface(self):
        student_screen = StudentLoginScreen(self.widget)
        self.widget.addWidget(student_screen)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def send_instruction_for_change_personal_details(self):
        content = '''If Any Student Want To Change Their Personal Details Then They Can Send Me Message In Personal In Below Format:

Enrollment no: your enrollment number
Field you want to change: new value

For example if you want to change your email Then,                                                                               
Enrollment no: 50384869
Email: mheinzel5r@cam.ac.uk '''

        now = datetime.now()

        f = open("D:\\Projects_Sem-3\\Python-I_Individual\\notice.txt", 'a')

        f.write(now.strftime("%d/%m/%Y %H:%M:%S") + " :\n" + content + "\n\n")

        f.close()

    def send_userid_password_to_Hod(self):
        os.mkdir(
            f"D:\\Projects_Sem-3\\Python-I_Individual\\Hod\\{self.hod.name}")
        f = open(
            f"D:\\Projects_Sem-3\\Python-I_Individual\\Hod\\{self.hod.name}\\personal.txt", 'a')

        f.write(f"UserID: {self.hod.userId}\nPassword: {self.hod.password}")
        f.close()


class HodLoginScreen(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(HodLoginScreen, self).__init__()
        loadUi("hodLoginScreen.ui", self)
        widget.setFixedWidth(803)
        widget.setFixedHeight(561)

        self.userId.findChildren(QAction)[0].setIcon(QIcon("cross_btn.png"))
        self.password.findChildren(QAction)[0].setIcon(QIcon("cross_btn.png"))

        self.backBtn.clicked.connect(self.backPage)
        self.submitBtn.clicked.connect(self.nextPage)

    def nextPage(self):

        response = self.p.check_valid_hod(
            self.userId.text(), self.password.text())
        if response != "":
            self.error.setText(response)
            return

        hod_screen = HodScreen(self.widget)
        self.widget.addWidget(hod_screen)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def backPage(self):

        login = LoginScreen(self.widget, self.p)
        self.widget.addWidget(login)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)


class FacultyLoginScreen(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(FacultyLoginScreen, self).__init__()
        loadUi("facultyLoginScreen.ui", self)
        widget.setFixedWidth(803)
        widget.setFixedHeight(558)

        self.userId.findChildren(QAction)[0].setIcon(QIcon("cross_btn.png"))
        self.password.findChildren(QAction)[0].setIcon(QIcon("cross_btn.png"))

        self.backBtn.clicked.connect(self.backPage)
        self.submitBtn.clicked.connect(self.nextPage)

    def nextPage(self):

        response = self.p.check_valid_faculty(
            self.userId.text(), self.password.text())
        if response != "":
            self.error.setText(response)
            return

        faculty_screen = FacultyScreen(self.widget)
        self.widget.addWidget(faculty_screen)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def backPage(self):

        login = LoginScreen(self.widget, self.p)
        self.widget.addWidget(login)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)


class StudentLoginScreen(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(StudentLoginScreen, self).__init__()
        loadUi("studentLoginScreen.ui", self)
        widget.setFixedWidth(803)
        widget.setFixedHeight(563)

        self.userId.findChildren(QAction)[0].setIcon(QIcon("cross_btn.png"))
        self.password.findChildren(QAction)[0].setIcon(QIcon("cross_btn.png"))

        self.backBtn.clicked.connect(self.backPage)
        self.submitBtn.clicked.connect(self.nextPage)

    def nextPage(self):

        if (len(self.userId.text()) == 0 or len(self.password.text()) == 0):
            self.error.setText("Please fill all fields!!")
            return

        response = self.p.check_valid_student(
            self.userId.text(), self.password.text())
        if response != "":
            self.error.setText(response)
            return
        student_screen = StudentScreen(self.widget)
        self.widget.addWidget(student_screen)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def backPage(self):

        login = LoginScreen(self.widget, self.p)
        self.widget.addWidget(login)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)


class StudentScreen(QDialog):
    def __init__(self, widget):
        self.widget = widget
        StudentAuthorityScreen.name = self.name
        super(StudentScreen, self).__init__()
        loadUi("studentScreen.ui", self)
        widget.setFixedWidth(915)
        widget.setFixedHeight(432)

        self.studentName.setText(f"Welcome {self.name}!!")
        self.backBtn.clicked.connect(self.backPage)
        self.nextBtn.clicked.connect(self.authorityPage)
        self.studentActivity.clicked.connect(self.activityPage)

    def backPage(self):

        student_login = StudentLoginScreen(self.widget)
        self.widget.addWidget(student_login)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def authorityPage(self):
        student_authority = StudentAuthorityScreen(self.widget)
        self.widget.addWidget(student_authority)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def activityPage(self):
        student_activity = StudentActivityScreen(self.widget)
        self.widget.addWidget(student_activity)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)


class StudentActivityScreen(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(StudentActivityScreen, self).__init__()
        loadUi("studentActivityScreen.ui", self)
        widget.setFixedWidth(911)
        widget.setFixedHeight(431)

        self.backBtn.clicked.connect(self.backPage)
        self.updateBtn.clicked.connect(self.updateProfile)
        self.progressBtn.clicked.connect(self.showProgress)

    def backPage(self):

        student_screen = StudentScreen(self.widget)
        self.widget.addWidget(student_screen)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def showProgress(self):

        student_progress = StudentProgress(self.widget)
        self.widget.addWidget(student_progress)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
    
    def updateProfile(self):

        update_profile = UpdateProfileStudent(self.widget)
        self.widget.addWidget(update_profile)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

class UpdateProfileStudent(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(UpdateProfileStudent, self).__init__()
        loadUi("updateProfileStudent.ui", self)
        widget.setFixedWidth(891)
        widget.setFixedHeight(481)

        list = ["1 :- User Id", "2 :- Password"]
        self.option.addItems(list)

        self.backBtn.clicked.connect(self.backPage)
        self.changeBtn.clicked.connect(self.changeProperties)
    
    def backPage(self):

        student_activity_screen = StudentActivityScreen(self.widget)
        self.widget.addWidget(student_activity_screen)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
    
    def changeProperties(self):

        change_properties = ChangePropertiesStudent(self.widget, self.option.currentText())
        self.widget.addWidget(change_properties)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

class ChangePropertiesStudent(QDialog):
    def __init__(self, widget, field):
        self.widget = widget
        super(ChangePropertiesStudent, self).__init__()
        self.field = field
        loadUi("changePropertiesStudent.ui", self)
        widget.setFixedWidth(920)
        widget.setFixedHeight(481)

        self.text.findChildren(QAction)[0].setIcon(QIcon("cross_btn.png"))

        self.done.hide()
        self.error.hide()

        if self.field == "1 :- User Id":
            self.text.setText(self.s.userId)
            self.whichField.setText("Enter new User id")
        elif self.field == "2 :- Password":
            self.text.setText(str(self.s.password))
            self.whichField.setText("Enter new Password")

        self.backBtn.clicked.connect(self.backPage)
        self.changeBtn.clicked.connect(self.changeProperties)

    def backPage(self):

        update_profile = UpdateProfileStudent(self.widget)
        self.widget.addWidget(update_profile)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
    
    def changeProperties(self):
        content = self.text.text()

        if (len(content) == 0):
            self.error.setText("Please fill all fields!!")
            self.error.show()
            return
        
        if self.field == "1 :- User Id":

            self.done.show()

            self.whichField.hide()
            self.text.hide()
            self.changeBtn.hide()
            self.error.hide()

            self.p.update_userid_to_database_student(
                content, self.s.enrollment_id)

        elif self.field == "2 :- Password":
            for i in content:
                if ord(i) >= 48 and ord(i) <= 57:
                    break
                else:
                    self.error.setText("Please Enter password in digits!!")
                    self.error.show()
                    return

            self.done.show()

            self.whichField.hide()
            self.text.hide()
            self.changeBtn.hide()
            self.error.hide()

            self.p.update_password_to_database_student(
                content, self.s.enrollment_id)


class StudentProgress(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(StudentProgress, self).__init__()
        loadUi("studentProgress.ui", self)
        widget.setFixedWidth(911)
        widget.setFixedHeight(541)

        self.studentName.setText(
            f"{self.name} choose an option to see progress!!")

        self.mydb = self.p.connector()
        self.mycursor = self.mydb.cursor()

        query = f"select id from students where Name = '{self.name}'"
        self.mycursor.execute(query)
        self.student_id = self.mycursor.fetchone()

        self.error.hide()

        self.backBtn.clicked.connect(self.backPage)
        self.test_1.clicked.connect(self.showT1)
        self.test_2.clicked.connect(self.showT2)
        self.test_3.clicked.connect(self.showT3)
        self.test_4.clicked.connect(self.showT4)
        self.final_result.clicked.connect(self.showFinalResult)

    def backPage(self):

        student_activity_screen = StudentActivityScreen(self.widget)
        self.widget.addWidget(student_activity_screen)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def showT1(self):
        self.error.hide()
        query = "select t1_python from sem_3_exam where student_id = %s"
        self.mycursor.execute(query, (self.student_id[0], ))
        result = self.mycursor.fetchone()

        if result[0] == -1:
            self.error.setText("No data available for Test 1")
            self.error.show()
            return
        else:
            query1 = "select t1_python,t1_fsd,t1_de,t1_ps from sem_3_exam where student_id = %s"
            self.mycursor.execute(query1, (self.student_id[0], ))
            result = self.mycursor.fetchall()

            marks = []
            for i in result[0]:
                marks.append(i)
            mylabels = [f"Python({result[0][0]})", f"FSD({result[0][1]})", f"DE({result[0][2]})", f"PS({result[0][3]})"]

            plt.pie(marks, labels=mylabels, autopct="%.2f%%")
            plt.legend(title="T1 Exam:")
            plt.show()

    def showT2(self):
        self.error.hide()
        query = "select t2_python from sem_3_exam where student_id = %s"
        self.mycursor.execute(query, (self.student_id[0], ))
        result = self.mycursor.fetchone()

        if result[0] == -1:
            self.error.setText("No data available for Test 2")
            self.error.show()
            return
        else:
            query1 = "select t2_python,t2_fsd,t2_de,t2_ps from sem_3_exam where student_id = %s"
            self.mycursor.execute(query1, (self.student_id[0], ))
            result = self.mycursor.fetchall()

            marks = []
            for i in result[0]:
                marks.append(i)
            mylabels = [f"Python({result[0][0]})", f"FSD({result[0][1]})", f"DE({result[0][2]})", f"PS({result[0][3]})"]

            plt.pie(marks, labels=mylabels, autopct="%.2f%%")
            plt.legend(title="T2 Exam:")
            plt.show()

    def showT3(self):
        self.error.hide()
        query = "select t3_python from sem_3_exam where student_id = %s"
        self.mycursor.execute(query, (self.student_id[0], ))
        result = self.mycursor.fetchone()

        if result[0] == -1:
            self.error.setText("No data available for Test 3")
            self.error.show()
            return
        else:
            query1 = "select t3_python,t3_fsd,t3_de,t3_ps from sem_3_exam where student_id = %s"
            self.mycursor.execute(query1, (self.student_id[0], ))
            result = self.mycursor.fetchall()

            marks = []
            for i in result[0]:
                marks.append(i)
            mylabels = [f"Python({result[0][0]})", f"FSD({result[0][1]})", f"DE({result[0][2]})", f"PS({result[0][3]})"]

            plt.pie(marks, labels=mylabels, autopct="%.2f%%")
            plt.legend(title="T3 Exam:")
            plt.show()

    def showT4(self):
        self.error.hide()
        query = "select t4_python from sem_3_exam where student_id = %s"
        self.mycursor.execute(query, (self.student_id[0], ))
        result = self.mycursor.fetchone()

        if result[0] == -1:
            self.error.setText("No data available for Test 4")
            self.error.show()
            return
        else:
            query1 = "select t4_python,t4_fsd,t4_de,t4_ps from sem_3_exam where student_id = %s"
            self.mycursor.execute(query1, (self.student_id[0], ))
            result = self.mycursor.fetchall()

            marks = []
            for i in result[0]:
                marks.append(i)
            mylabels = [f"Python({result[0][0]})", f"FSD({result[0][1]})", f"DE({result[0][2]})", f"PS({result[0][3]})"]

            plt.pie(marks, labels=mylabels, autopct="%.2f%%")
            plt.legend(title="T4 Exam:")
            plt.show()

    def showFinalResult(self):
        self.error.hide()
        query = "select t1_python,t2_python,t3_python,t4_python from sem_3_exam where student_id = %s"
        self.mycursor.execute(query, (self.student_id[0], ))
        result = self.mycursor.fetchall()

        if result[0][0] == -1 or result[0][1] == -1 or result[0][2] == -1 or result[0][3] == -1:
            self.error.setText("No data available for final result")
            self.error.show()
            return
        else:
            query1 = "select t1_python,t1_fsd,t1_de,t1_ps,t2_python,t2_fsd,t2_de,t2_ps,t3_python,t3_fsd,t3_de,t3_ps,t4_python,t4_fsd,t4_de,t4_ps from sem_3_exam where student_id = %s"
            self.mycursor.execute(query1, (self.student_id[0], ))
            result = self.mycursor.fetchall()

            marks_t1 = []
            marks_t2 = []
            marks_t3 = []
            marks_t4 = []

            for i, j in enumerate(result[0]):
                if i < 4:
                    marks_t1.append(j)
                elif i < 8:
                    marks_t2.append(j)
                elif i < 12:
                    marks_t3.append(j)
                elif i < 16:
                    marks_t4.append(j)

            sum_t1 = sum(marks_t1)
            sum_t2 = sum(marks_t2)
            sum_t3 = sum(marks_t3)
            sum_t4 = sum(marks_t4)

            final_result = []
            final_result.append(sum_t1)
            final_result.append(sum_t2)
            final_result.append(sum_t3)
            final_result.append(sum_t4)

            mylabels = [f"Test-1({sum_t1})", f"Test-2({sum_t2})",
                        f"Test-3({sum_t3})", f"Test-4({sum_t4})"]

            plt.pie(final_result, labels=mylabels, autopct="%.2f%%")
            plt.legend(title="Sem-3:")
            plt.show()


class StudentAuthorityScreen(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(StudentAuthorityScreen, self).__init__()
        loadUi("studentAuthorityScreen.ui", self)
        widget.setFixedWidth(911)
        widget.setFixedHeight(555)

        self.studentName.setText(f"{self.name} choose an operation")
        self.backBtn.clicked.connect(self.backPage)
        self.nextBtn1.clicked.connect(self.searchFaculty)
        self.nextBtn2.clicked.connect(self.classFaculty)
        self.nextBtn3.clicked.connect(self.checkNotice)
        self.nextBtn4.clicked.connect(self.checkMessage)
        self.nextBtn5.clicked.connect(self.giveFeedback)
        self.nextBtn6.clicked.connect(self.searchClass)
        self.nextBtn7.clicked.connect(self.msgToHod)

    def backPage(self):

        student_screen = StudentScreen(self.widget)
        self.widget.addWidget(student_screen)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def searchFaculty(self):
        search_faculty = SearchFacultyForStudent(self.widget)
        self.widget.addWidget(search_faculty)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def classFaculty(self):
        class_faculty = ClassFaculty(self.widget)
        self.widget.addWidget(class_faculty)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def checkNotice(self):
        class_faculty = CheckNotice(self.widget, "1")
        self.widget.addWidget(class_faculty)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def checkMessage(self):
        class_faculty = CheckMessage(self.widget)
        self.widget.addWidget(class_faculty)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def giveFeedback(self):
        class_faculty = GiveFeedback(self.widget)
        self.widget.addWidget(class_faculty)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def searchClass(self):
        class_faculty = SearchClass(self.widget, "1")
        self.widget.addWidget(class_faculty)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def msgToHod(self):
        msg_to_hod = MsgToHod(self.widget)
        self.widget.addWidget(msg_to_hod)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)


class SearchFacultyForStudent(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(SearchFacultyForStudent, self).__init__()
        loadUi("searchFacultyForStudent.ui", self)
        widget.setFixedWidth(915)
        widget.setFixedHeight(474)

        self.backBtn.clicked.connect(self.backPage)
        self.searchBtn.clicked.connect(self.search)

        self.searchName.findChildren(
            QAction)[0].setIcon(QIcon("cross_btn.png"))

        self.hidden = False

    def backPage(self):

        student_authority = StudentAuthorityScreen(self.widget)
        self.widget.addWidget(student_authority)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def search(self):

        name = self.searchName.text().lower()

        for i, j in enumerate(self.p.faculty):
            if self.p.faculty[i][2].lower() == name:
                self.error.hide()
                self.facultyName.show()
                self.facultyMail.show()
                self.primarySub.show()
                self.secondarySub.show()
                self.facultyName.setText(f"Name: {self.p.faculty[i][2]}")
                self.facultyMail.setText(f"E-mail: {self.p.faculty[i][5]}")
                self.primarySub.setText(
                    f"Primary subject: {self.p.faculty[i][3]}")
                self.secondarySub.setText(f"Secondary subject: {self.p.faculty[i][4]}")
                return

        self.hidden = True
        if self.hidden:
            self.error.show()
            self.facultyName.hide()
            self.facultyMail.hide()
            self.primarySub.hide()
            self.secondarySub.hide()
            self.error.setText("Faculty not found")


class ClassFaculty(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(ClassFaculty, self).__init__()
        loadUi("classFaculty.ui", self)
        widget.setFixedWidth(911)
        widget.setFixedHeight(394)

        self.showClassFaculty()
        self.backBtn.clicked.connect(self.backPage)

    def backPage(self):

        student_authority = StudentAuthorityScreen(self.widget)
        self.widget.addWidget(student_authority)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def showClassFaculty(self):
        std_class_id = self.s.class_alloted.lower()
        for i in self.p.classes:
            if std_class_id == i.id.lower():
                self.classId.setText(f"Class id {i.id}")
                self.pythonFaculty.setText(
                    f"Python faculty: {i.python_faculty}")
                self.fsdFaculty.setText(f"FSD faculty: {i.fsd_faculty}")
                self.deFaculty.setText(f"DE faculty: {i.de_faculty}")
                self.psFaculty.setText(f"PS faculty: {i.ps_faculty}")
                return


class CheckNotice(QDialog):
    def __init__(self, widget, val):
        self.widget = widget
        super(CheckNotice, self).__init__()
        loadUi("checkNotice.ui", self)
        widget.setFixedWidth(913)
        widget.setFixedHeight(498)
        self.val = val
        self.showNotice()
        self.backBtn.clicked.connect(self.backPage)

    def backPage(self):
        if self.val == "1":
            student_authority = StudentAuthorityScreen(self.widget)
            self.widget.addWidget(student_authority)
            self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        else:
            faculty_authority = FacultyAuthorityScreen(self.widget)
            self.widget.addWidget(faculty_authority)
            self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def showNotice(self):
        if (not (os.path.exists("D:\\Projects_Sem-3\\Python-I_Individual\\notice.txt"))):
            self.error.setText("No notice yet !!")
            return
        f = open("D:\\Projects_Sem-3\\Python-I_Individual\\notice.txt", 'r')
        self.textPara.setText(f.read())

        f.close()


class CheckMessage(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(CheckMessage, self).__init__()
        loadUi("checkMessage.ui", self)
        widget.setFixedWidth(913)
        widget.setFixedHeight(536)

        self.showMessage()
        self.backBtn.clicked.connect(self.backPage)

    def backPage(self):

        student_authority = StudentAuthorityScreen(self.widget)
        self.widget.addWidget(student_authority)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def showMessage(self):
        f = open(
            f"D:\\Projects_Sem-3\\Python-I_Individual\\students\\{self.s.name}\\msg.txt", 'r')
        content = f.read()
        if (content == ""):
            self.error.setText("No message yet !!")
            return
        self.textPara.setText(content)

        f.close()


class GiveFeedback(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(GiveFeedback, self).__init__()
        loadUi("giveFeedback.ui", self)
        widget.setFixedWidth(913)
        widget.setFixedHeight(576)
        self.done.hide()

        self.backBtn.clicked.connect(self.backPage)
        self.sendBtn.clicked.connect(self.sendFeedback)

    def backPage(self):

        student_authority = StudentAuthorityScreen(self.widget)
        self.widget.addWidget(student_authority)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def sendFeedback(self):
        content = self.textPara.toPlainText()
        if content == "":
            return

        self.done.show()
        self.textPara.hide()

        f = open("D:\\Projects_Sem-3\\Python-I_Individual\\feedback.txt", 'a')

        f.write("Sender: " + self.s.name + "\n")
        f.write("Feedback: " + content + "\n\n")

        f.close()


class SearchClass(QDialog):
    def __init__(self, widget, val):
        self.widget = widget
        self.val = val
        super(SearchClass, self).__init__()
        loadUi("searchClass.ui", self)
        widget.setFixedWidth(955)
        widget.setFixedHeight(593)

        self.searchClassId.findChildren(
            QAction)[0].setIcon(QIcon("cross_btn.png"))

        self.students.hide()
        self.backBtn.clicked.connect(self.backPage)
        self.searchBtn.clicked.connect(self.showClass)

    def backPage(self):

        if self.val == "1":
            student_authority = StudentAuthorityScreen(self.widget)
            self.widget.addWidget(student_authority)
            self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        elif self.val == "2":
            faculty_authority = FacultyAuthorityScreen(self.widget)
            self.widget.addWidget(faculty_authority)
            self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        else:
            hod_authority = HodAuthorityScreen(self.widget)
            self.widget.addWidget(hod_authority)
            self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def showClass(self):
        self.students.clear()
        self.error.hide()
        self.students.hide()
        self.pythonFaculty.hide()
        self.fsdFaculty.hide()
        self.deFaculty.hide()
        self.psFaculty.hide()
        self.text.hide()

        class_id = self.searchClassId.text()
        if class_id == "":
            return

        flag = False

        for i in self.p.classes:
            if class_id.lower() == i.id.lower():
                class_content = i
                flag = True
                break

        if not (flag):
            self.error.show()
            self.error.setText(f"No {class_id} class id exists !!")
            return
        else:
            self.students.show()
            self.pythonFaculty.show()
            self.fsdFaculty.show()
            self.deFaculty.show()
            self.psFaculty.show()
            self.text.show()

            std_list = []
            cnt = 1
            for i in class_content.students:
                std_list.append(f"{cnt} - {i.name}")
                cnt += 1

            self.students.addItems(std_list)
            self.pythonFaculty.setText(
                f"Python faculty: {class_content.python_faculty}")
            self.fsdFaculty.setText(
                f"FSD faculty: {class_content.fsd_faculty}")
            self.deFaculty.setText(f"DE faculty: {class_content.de_faculty}")
            self.psFaculty.setText(f"PS faculty: {class_content.ps_faculty}")
            self.text.setText(f"{class_id} class students: ")
            return


class MsgToHod(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(MsgToHod, self).__init__()
        loadUi("msgToHod.ui", self)
        widget.setFixedWidth(928)
        widget.setFixedHeight(677)
        self.done.hide()

        self.backBtn.clicked.connect(self.backPage)
        self.sendBtn.clicked.connect(self.sendNotice)

    def backPage(self):

        student_authority = StudentAuthorityScreen(self.widget)
        self.widget.addWidget(student_authority)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def sendNotice(self):
        content = self.textPara.toPlainText()
        if content == "":
            return

        now = datetime.now()

        os.mkdir(f"D:\\Projects_Sem-3\\Python-I_Individual\\Hod\\Change Details")
        os.mkdir(
            f"D:\\Projects_Sem-3\\Python-I_Individual\\Hod\\Change Details\\{self.name}")
        f = open(f"D:\\Projects_Sem-3\\Python-I_Individual\\Hod\\Change Details\\{self.name}\\instruction.txt", 'a')

        f.write(now.strftime("%d/%m/%Y %H:%M:%S") + " :\n" + content + "\n\n")

        f.close()

        self.done.show()

        self.label.hide()
        self.textPara.hide()
        self.sendBtn.hide()


class FacultyScreen(QDialog):
    def __init__(self, widget):
        self.widget = widget
        FacultyAuthorityScreen.name = self.name
        super(FacultyScreen, self).__init__()
        loadUi("facultyScreen.ui", self)
        widget.setFixedWidth(915)
        widget.setFixedHeight(432)

        self.facultyName.setText(f"Welcome {self.name}!!")
        self.backBtn.clicked.connect(self.backPage)
        self.nextBtn.clicked.connect(self.authorityPage)
        # self.studentActivity.clicked.connect(self.nextPage)

    def backPage(self):

        faculty_login = FacultyLoginScreen(self.widget)
        self.widget.addWidget(faculty_login)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def authorityPage(self):
        faculty_authority = FacultyAuthorityScreen(self.widget)
        self.widget.addWidget(faculty_authority)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)


class FacultyAuthorityScreen(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(FacultyAuthorityScreen, self).__init__()
        loadUi("facultyAuthorityScreen.ui", self)
        widget.setFixedWidth(915)
        widget.setFixedHeight(459)

        self.facultyName.setText(f"{self.name} choose an operation")
        self.backBtn.clicked.connect(self.backPage)
        self.nextBtn1.clicked.connect(self.searchStudent)
        self.nextBtn2.clicked.connect(self.yourStudents)
        self.nextBtn3.clicked.connect(self.checkNotice)
        self.nextBtn4.clicked.connect(self.yourClasses)
        self.nextBtn5.clicked.connect(self.searchClass)

    def backPage(self):

        faculty_screen = FacultyScreen(self.widget)
        self.widget.addWidget(faculty_screen)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def searchStudent(self):
        search_student = SearchStudent(self.widget, "1")
        self.widget.addWidget(search_student)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def yourStudents(self):
        faculty_student = FacultyStudents(self.widget)
        self.widget.addWidget(faculty_student)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def checkNotice(self):
        check_notice = CheckNotice(self.widget, "2")
        self.widget.addWidget(check_notice)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def yourClasses(self):
        faculty_class = FacultyClasses(self.widget)
        self.widget.addWidget(faculty_class)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def searchClass(self):
        search_class = SearchClass(self.widget, "2")
        self.widget.addWidget(search_class)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)


class SearchStudent(QDialog):
    def __init__(self, widget, val):
        self.widget = widget
        self.val = val
        super(SearchStudent, self).__init__()
        loadUi("searchStudent.ui", self)
        widget.setFixedWidth(916)
        widget.setFixedHeight(593)

        self.option.addItem("Search by name")
        self.option.addItem("Search by id")

        self.search.setPlaceholderText("Enter the data of student")

        self.search.findChildren(QAction)[0].setIcon(QIcon("cross_btn.png"))

        self.backBtn.clicked.connect(self.backPage)
        self.searchBtn.clicked.connect(self.searchStudent)

    def backPage(self):

        if self.val == "1":
            faculty_authority = FacultyAuthorityScreen(self.widget)
            self.widget.addWidget(faculty_authority)
            self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
        else:
            hod_authority = HodAuthorityScreen(self.widget)
            self.widget.addWidget(hod_authority)
            self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def searchStudent(self):
        flag = False
        option = self.option.currentText()

        if option == "Search by name":
            if self.search == "":
                return
            else:
                name_input = self.search.text().lower()
                for i in self.p.selected_student:
                    if name_input == i.name.lower():

                        self.rollNo.show()
                        self.name.show()
                        self.id.show()
                        self.rank.show()
                        self.emailId.show()
                        self.number.show()
                        self.department.show()
                        self.classId.show()
                        self.city.show()
                        self.mentor.show()

                        self.error.hide()

                        self.printData(i)
                        flag = True
                        return

                if not (flag):
                    self.rollNo.hide()
                    self.name.hide()
                    self.id.hide()
                    self.rank.hide()
                    self.emailId.hide()
                    self.number.hide()
                    self.department.hide()
                    self.classId.hide()
                    self.city.hide()
                    self.mentor.hide()

                    self.error.show()
                    self.error.setText("Student not found !!")
                    return
        elif option == "Search by id":

            if self.search == "":
                return
            else:
                id_input = self.search.text()
                for i in self.p.selected_student:
                    if id_input == str(i.enrollment_id):

                        self.rollNo.show()
                        self.name.show()
                        self.id.show()
                        self.rank.show()
                        self.emailId.show()
                        self.number.show()
                        self.department.show()
                        self.classId.show()
                        self.city.show()
                        self.mentor.show()

                        self.error.hide()

                        self.printData(i)
                        flag = True
                        return

                if not (flag):
                    self.rollNo.hide()
                    self.name.hide()
                    self.id.hide()
                    self.rank.hide()
                    self.emailId.hide()
                    self.number.hide()
                    self.department.hide()
                    self.classId.hide()
                    self.city.hide()
                    self.mentor.hide()

                    self.error.show()
                    self.error.setText("Student not found !!")
                    return

    def printData(self, student):
        self.rollNo.setText(f"Roll No: {student.roll_no}")
        self.name.setText(f"Name: {student.name}")
        self.id.setText(f"Enrollment id: {student.enrollment_id}")
        self.rank.setText(f"Merit rank: {student.merit_rank}")
        self.emailId.setText(f"Email-id: {student.email}")
        self.number.setText(f"Phone number: {student.phone}")
        self.department.setText(f"Department: {student.department}")
        self.classId.setText(f"Class: {student.class_alloted}")
        self.city.setText(f"City: {student.city}")
        self.mentor.setText(f"Mentor Name: {student.mentor}")


class FacultyStudents(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(FacultyStudents, self).__init__()
        loadUi("facultyStudents.ui", self)
        widget.setFixedWidth(916)
        widget.setFixedHeight(462)

        self.showStudents()
        self.backBtn.clicked.connect(self.backPage)

    def backPage(self):

        faculty_authority = FacultyAuthorityScreen(self.widget)
        self.widget.addWidget(faculty_authority)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def showStudents(self):
        cnt = 1

        self.students.addItem("Sr no.   Name    Enrollment id")
        temp_list = self.t[7].split("\n")
        for i in range(len(temp_list)-1):
            for j in self.p.selected_student:
                if temp_list[i] == j.name:
                    id = j.enrollment_id
                    break
            self.students.addItem(f"{cnt}   {temp_list[i]}   {id}")

            cnt += 1


class FacultyClasses(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(FacultyClasses, self).__init__()
        loadUi("facultyClasses.ui", self)
        widget.setFixedWidth(920)
        widget.setFixedHeight(480)

        self.showClasses()
        self.backBtn.clicked.connect(self.backPage)

    def backPage(self):

        faculty_authority = FacultyAuthorityScreen(self.widget)
        self.widget.addWidget(faculty_authority)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def showClasses(self):
        self.error.hide()
        self.label.hide()
        self.classId.hide()

        temp_set = set()
        for i in self.p.classes:
            if self.t[2] == i.python_faculty:
                temp_set.add(f"{i.id}   Python")
            if self.t[2] == i.fsd_faculty:
                temp_set.add(f"{i.id}   FSD")
            if self.t[2] == i.de_faculty:
                temp_set.add(f"{i.id}   DE")
            if self.t[2] == i.ps_faculty:
                temp_set.add(f"{i.id}   PS")

        if len(temp_set) == 0:
            self.error.show()
            return
        else:
            self.label.show()
            self.classId.show()
            self.classId.addItems(temp_set)
            return


class HodScreen(QDialog):
    def __init__(self, widget):
        self.widget = widget
        HodAuthorityScreen.name = self.name
        super(HodScreen, self).__init__()
        loadUi("hodScreen.ui", self)
        widget.setFixedWidth(915)
        widget.setFixedHeight(432)

        self.hodName.setText(f"Welcome {self.name}!!")
        self.backBtn.clicked.connect(self.backPage)
        self.nextBtn.clicked.connect(self.authorityPage)
        self.hodActivity.clicked.connect(self.activityPage)

    def backPage(self):

        hod_login = HodLoginScreen(self.widget)
        self.widget.addWidget(hod_login)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def authorityPage(self):
        hod_authority = HodAuthorityScreen(self.widget)
        self.widget.addWidget(hod_authority)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def activityPage(self):
        hod_authority = HodActivityScreen(self.widget)
        self.widget.addWidget(hod_authority)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)


class HodActivityScreen(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(HodActivityScreen, self).__init__()
        loadUi("hodActivityScreen.ui", self)
        widget.setFixedWidth(915)
        widget.setFixedHeight(432)

        self.backBtn.clicked.connect(self.backPage)
        self.updateBtn.clicked.connect(self.updateProfile)
        self.marksBtn.clicked.connect(self.giveMarks)

    def giveMarks(self):
        give_marks = GiveMarks(self.widget)
        self.widget.addWidget(give_marks)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def backPage(self):

        hod_screen = HodScreen(self.widget)
        self.widget.addWidget(hod_screen)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def updateProfile(self):

        update_profile = UpdateProfileHod(self.widget)
        self.widget.addWidget(update_profile)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

class UpdateProfileHod(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(UpdateProfileHod, self).__init__()
        loadUi("updateProfileHod.ui", self)
        widget.setFixedWidth(891)
        widget.setFixedHeight(481)

        list = ["1 :- User Id", "2 :- Password"]
        self.option.addItems(list)

        self.backBtn.clicked.connect(self.backPage)
        self.changeBtn.clicked.connect(self.changeProperties)
    
    def backPage(self):

        hod_activity_screen = HodActivityScreen(self.widget)
        self.widget.addWidget(hod_activity_screen)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
    
    def changeProperties(self):

        change_properties = ChangePropertiesHod(self.widget, self.option.currentText())
        self.widget.addWidget(change_properties)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

class ChangePropertiesHod(QDialog):
    def __init__(self, widget, field):
        self.widget = widget
        super(ChangePropertiesHod, self).__init__()
        self.field = field
        loadUi("changePropertiesHod.ui", self)
        widget.setFixedWidth(920)
        widget.setFixedHeight(481)

        self.text.findChildren(QAction)[0].setIcon(QIcon("cross_btn.png"))

        self.done.hide()
        self.error.hide()

        if self.field == "1 :- User Id":
            self.text.setText(self.userId)
            self.whichField.setText("Enter new User id")
        elif self.field == "2 :- Password":
            self.text.setText(str(self.password))
            self.whichField.setText("Enter new Password")

        self.backBtn.clicked.connect(self.backPage)
        self.changeBtn.clicked.connect(self.changeProperties)

    def backPage(self):

        update_profile = UpdateProfileHod(self.widget)
        self.widget.addWidget(update_profile)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
    
    def changeProperties(self):
        content = self.text.text()

        if (len(content) == 0):
            self.error.setText("Please fill all fields!!")
            self.error.show()
            return
        
        if self.field == "1 :- User Id":

            self.done.show()

            self.whichField.hide()
            self.text.hide()
            self.changeBtn.hide()
            self.error.hide()

            self.p.update_userid_to_database_hod(
                content, self.name)

        elif self.field == "2 :- Password":
            for i in content:
                if ord(i) >= 48 and ord(i) <= 57:
                    break
                else:
                    self.error.setText("Please Enter password in digits!!")
                    self.error.show()
                    return

            self.done.show()

            self.whichField.hide()
            self.text.hide()
            self.changeBtn.hide()
            self.error.hide()

            self.p.update_password_to_database_hod(
                content, self.name)


class GiveMarks(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(GiveMarks, self).__init__()
        loadUi("giveMarks.ui", self)
        widget.setFixedWidth(916)
        widget.setFixedHeight(650)

        self.backBtn.clicked.connect(self.backPage)

        test_list = ["Test-1", "Test-2", "Test-3", "Test-4"]
        self.test_option.addItems(test_list)

        class_list = ["D1", "D2", "D3", "D4", "D5", "D6"]
        self.class_option.addItems(class_list)

        self.python_marks.hide()
        self.fsd_marks.hide()
        self.de_marks.hide()
        self.ps_marks.hide()
        self.submit.hide()
        self.label_3.hide()
        self.student_option.hide()
        self.marks_error.hide()
        self.give_random.hide()
        self.done.hide()

        self.mydb = self.p.connector()
        self.mycursor = self.mydb.cursor()

        self.searchBtn.clicked.connect(self.showScreen)
        self.submit.clicked.connect(self.addMarks)
        self.give_random.clicked.connect(self.giveRandom)

    def backPage(self):

        hod_activity_screen = HodActivityScreen(self.widget)
        self.widget.addWidget(hod_activity_screen)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def giveRandom(self):
        for i in range(1, 181):
            if self.test_option.currentText() == "Test-1":
                query1 = "update sem_3_exam set t1_python = %s where student_id = %s;"
                query2 = "update sem_3_exam set t1_fsd = %s where student_id = %s;"
                query3 = "update sem_3_exam set t1_de = %s where student_id = %s;"
                query4 = "update sem_3_exam set t1_ps = %s where student_id = %s;"
            elif self.test_option.currentText() == "Test-2":
                query1 = "update sem_3_exam set t2_python = %s where student_id = %s;"
                query2 = "update sem_3_exam set t2_fsd = %s where student_id = %s;"
                query3 = "update sem_3_exam set t2_de = %s where student_id = %s;"
                query4 = "update sem_3_exam set t2_ps = %s where student_id = %s;"
            elif self.test_option.currentText() == "Test-3":
                query1 = "update sem_3_exam set t3_python = %s where student_id = %s;"
                query2 = "update sem_3_exam set t3_fsd = %s where student_id = %s;"
                query3 = "update sem_3_exam set t3_de = %s where student_id = %s;"
                query4 = "update sem_3_exam set t3_ps = %s where student_id = %s;"
            elif self.test_option.currentText() == "Test-4":
                query1 = "update sem_3_exam set t4_python = %s where student_id = %s;"
                query2 = "update sem_3_exam set t4_fsd = %s where student_id = %s;"
                query3 = "update sem_3_exam set t4_de = %s where student_id = %s;"
                query4 = "update sem_3_exam set t4_ps = %s where student_id = %s;"

            val1 = (random.randint(0, 25), i)
            val2 = (random.randint(0, 25), i)
            val3 = (random.randint(0, 25), i)
            val4 = (random.randint(0, 25), i)

            self.mycursor.execute(query1, val1)
            self.mycursor.execute(query2, val2)
            self.mycursor.execute(query3, val3)
            self.mycursor.execute(query4, val4)
            self.mydb.commit()

            if self.test_option.currentText() == "Test-1":
                self.giveNotice("Test-1") 

    def giveNotice(self, whichTest):
        if whichTest == "Test-1":
            query1 = "select student_id,t1_python,t1_fsd,t1_de,t1_ps from sem_3_exam"
            self.mycursor.execute(query1)

            students_marks_list = self.mycursor.fetchall()
            students_marks_sum_list = []

            
            for i in students_marks_list:
                students_marks_sum_list.append((i[0], sum([i[1],i[2],i[3],i[4]])))

            students_marks_sum_list.sort(key=lambda k : k[1], reverse=True)

            self.printResultNotice("Test-1", students_marks_sum_list, students_marks_list)
        elif whichTest == "Test-2":
            query1 = "select student_id,t2_python,t2_fsd,t2_de,t2_ps from sem_3_exam"
            self.mycursor.execute(query1)

            students_marks_list = self.mycursor.fetchall()
            students_marks_sum_list = []

            
            for i in students_marks_list:
                students_marks_sum_list.append((i[0], sum([i[1],i[2],i[3],i[4]])))

            students_marks_sum_list.sort(key=lambda k : k[1], reverse=True)

            self.printResultNotice("Test-2", students_marks_sum_list)
        elif whichTest == "Test-3":
            query1 = "select student_id,t3_python,t3_fsd,t3_de,t3_ps from sem_3_exam"
            self.mycursor.execute(query1)

            students_marks_list = self.mycursor.fetchall()
            students_marks_sum_list = []

            
            for i in students_marks_list:
                students_marks_sum_list.append((i[0], sum([i[1],i[2],i[3],i[4]])))

            students_marks_sum_list.sort(key=lambda k : k[1], reverse=True)

            self.printResultNotice("Test-3", students_marks_sum_list)
        elif whichTest == "Test-4":
            query1 = "select student_id,t4_python,t4_fsd,t4_de,t4_ps from sem_3_exam"
            self.mycursor.execute(query1)

            students_marks_list = self.mycursor.fetchall()
            students_marks_sum_list = []

            
            for i in students_marks_list:
                students_marks_sum_list.append((i[0], sum([i[1],i[2],i[3],i[4]])))

            students_marks_sum_list.sort(key=lambda k : k[1], reverse=True)

            self.printResultNotice("Test-4", students_marks_sum_list)

    def printResultNotice(self, whichTest, student_list, marks_list):
        if whichTest == "Test-1":
            f = open(f"D:\\Projects_Sem-3\\Python-I_Individual\\Test_1.txt", 'w')
            header = ['Rank','Branch','Roll No.','Enrollment No.','Div','Student Name','Python Out of 25','FSD Out of 25','DE Out of 25','PS Out of 25','Test-1 Out of 100']
            query1 = "select Enrollment_ID,Department,Roll_No,Class,Name from students where id = %s"
            rank_cnt = 1
            temp_cnt = 1
            prev_student_marks = 0
            data = []
            cnt = 0

            for i in student_list:
                self.mycursor.execute(query1, (i[0], ))
                student_data = self.mycursor.fetchall()

                if prev_student_marks != i[1]:
                    rank_cnt = temp_cnt

                temp_data = []
                for j in marks_list:
                    if j[0] == i[0]:
                        temp_data.extend([rank_cnt,student_data[0][1],student_data[0][2],student_data[0][0],student_data[0][3],student_data[0][4],j[1],j[2],j[3],j[4],i[1]])
                        break

                data.append(temp_data)
                temp_cnt += 1
                cnt += 1
                prev_student_marks = i[1]
            table = tabulate(data, headers=header, tablefmt="grid")
            f.write(table)

            f.close()
        elif whichTest == "Test-2":
            f = open(f"D:\\Projects_Sem-3\\Python-I_Individual\\Test_2.txt", 'w')
            header = ['Rank','Branch','Roll No.','Enrollment No.','Div','Student Name','Test-2']
            query1 = "select Enrollment_ID,Class,Name from students where id = %s"
            rank_cnt = 1
            temp_cnt = 1
            prev_student_marks = 0
            data = []
            cnt = 0

            for i in student_list:
                self.mycursor.execute(query1, (i[0], ))
                student_data = self.mycursor.fetchall()

                if prev_student_marks != i[1]:
                    rank_cnt = temp_cnt

                temp_data = []
                for j in marks_list:
                    if j[0] == i[0]:
                        temp_data.extend([rank_cnt,student_data[0][1],student_data[0][2],student_data[0][0],student_data[0][3],student_data[0][4],j[1],j[2],j[3],j[4],i[1]])
                        break

                data.append(temp_data)
                temp_cnt += 1
                cnt += 1
                prev_student_marks = i[1]
            table = tabulate(data, headers=header, tablefmt="grid")
            f.write(table)

            f.close()
        elif whichTest == "Test-3":
            f = open(f"D:\\Projects_Sem-3\\Python-I_Individual\\Test_3.txt", 'w')
            header = ['Rank','Branch','Roll No.','Enrollment No.','Div','Student Name','Test-3']
            query1 = "select Enrollment_ID,Class,Name from students where id = %s"
            rank_cnt = 1
            temp_cnt = 1
            prev_student_marks = 0
            data = []
            cnt = 0

            for i in student_list:
                self.mycursor.execute(query1, (i[0], ))
                student_data = self.mycursor.fetchall()

                if prev_student_marks != i[1]:
                    rank_cnt = temp_cnt

                temp_data = []
                for j in marks_list:
                    if j[0] == i[0]:
                        temp_data.extend([rank_cnt,student_data[0][1],student_data[0][2],student_data[0][0],student_data[0][3],student_data[0][4],j[1],j[2],j[3],j[4],i[1]])
                        break

                data.append(temp_data)
                cnt += 1
                temp_cnt += 1
                prev_student_marks = i[1]
            table = tabulate(data, headers=header, tablefmt="grid")
            f.write(table)
            f.close()
        elif whichTest == "Test-4":
            f = open(f"D:\\Projects_Sem-3\\Python-I_Individual\\Test_4.txt", 'w')
            header = ['Rank','Branch','Roll No.','Enrollment No.','Div','Student Name','Test-4']
            query1 = "select Enrollment_ID,Class,Name from students where id = %s"
            rank_cnt = 1
            temp_cnt = 1
            prev_student_marks = 0
            data = []
            cnt = 0

            for i in student_list:
                self.mycursor.execute(query1, (i[0], ))
                student_data = self.mycursor.fetchall()

                if prev_student_marks != i[1]:
                    rank_cnt = temp_cnt
                
                temp_data = []
                for j in marks_list:
                    if j[0] == i[0]:
                        temp_data.extend([rank_cnt,student_data[0][1],student_data[0][2],student_data[0][0],student_data[0][3],student_data[0][4],j[1],j[2],j[3],j[4],i[1]])
                        break

                data.append(temp_data)
                cnt += 1
                temp_cnt += 1
                prev_student_marks = i[1]
            table = tabulate(data, headers=header, tablefmt="grid")
            f.write(table)
            f.close()

    def showScreen(self):
        self.student_option.clear()
        self.done.hide()
        self.marks_error.hide()

        self.python_marks.setText("")
        self.fsd_marks.setText("")
        self.de_marks.setText("")
        self.ps_marks.setText("")

        for i in self.p.classes:
            if i.id == self.class_option.currentText():
                for j in i.students:
                    self.student_option.addItem(j.name)
                break

        self.python_marks.show()
        self.fsd_marks.show()
        self.de_marks.show()
        self.ps_marks.show()
        self.submit.show()
        self.label_3.show()
        self.student_option.show()
        self.give_random.show()

    def addMarks(self):
        try:
            if len(self.python_marks.text()) == 0 or len(self.fsd_marks.text()) == 0 or len(self.de_marks.text()) == 0 or len(self.ps_marks.text()) == 0:
                self.marks_error.show()
                self.marks_error.setText("Please fill all fields!!")
                return
            elif int(self.python_marks.text()) > 25 or int(self.fsd_marks.text()) > 25 or int(self.de_marks.text()) > 25 or int(self.ps_marks.text()) > 25:
                self.marks_error.show()
                self.marks_error.setText("Please give marks below 25!!")
                return
            elif int(self.python_marks.text()) < 0 or int(self.fsd_marks.text()) < 0 or int(self.de_marks.text()) < 0 or int(self.ps_marks.text()) < 0:
                self.marks_error.show()
                self.marks_error.setText("Please give marks above 0!!")
                return
            else:

                query = f"select id from students where Name = '{
                    self.student_option.currentText()}'"
                self.mycursor.execute(query)
                student_id = self.mycursor.fetchone()

                if self.test_option.currentText() == "Test-1":
                    query1 = "update sem_3_exam set t1_python = %s where student_id = %s;"
                    query2 = "update sem_3_exam set t1_fsd = %s where student_id = %s;"
                    query3 = "update sem_3_exam set t1_de = %s where student_id = %s;"
                    query4 = "update sem_3_exam set t1_ps = %s where student_id = %s;"
                elif self.test_option.currentText() == "Test-2":
                    query1 = "update sem_3_exam set t2_python = %s where student_id = %s;"
                    query2 = "update sem_3_exam set t2_fsd = %s where student_id = %s;"
                    query3 = "update sem_3_exam set t2_de = %s where student_id = %s;"
                    query4 = "update sem_3_exam set t2_ps = %s where student_id = %s;"
                elif self.test_option.currentText() == "Test-3":
                    query1 = "update sem_3_exam set t3_python = %s where student_id = %s;"
                    query2 = "update sem_3_exam set t3_fsd = %s where student_id = %s;"
                    query3 = "update sem_3_exam set t3_de = %s where student_id = %s;"
                    query4 = "update sem_3_exam set t3_ps = %s where student_id = %s;"
                elif self.test_option.currentText() == "Test-4":
                    query1 = "update sem_3_exam set t4_python = %s where student_id = %s;"
                    query2 = "update sem_3_exam set t4_fsd = %s where student_id = %s;"
                    query3 = "update sem_3_exam set t4_de = %s where student_id = %s;"
                    query4 = "update sem_3_exam set t4_ps = %s where student_id = %s;"

                val1 = (int(self.python_marks.text()), student_id[0])
                val2 = (int(self.fsd_marks.text()), student_id[0])
                val3 = (int(self.de_marks.text()), student_id[0])
                val4 = (int(self.ps_marks.text()), student_id[0])

                self.mycursor.execute(query1, val1)
                self.mycursor.execute(query2, val2)
                self.mycursor.execute(query3, val3)
                self.mycursor.execute(query4, val4)
                self.mydb.commit()

                self.marks_error.hide()
                self.python_marks.hide()
                self.fsd_marks.hide()
                self.de_marks.hide()
                self.ps_marks.hide()
                self.submit.hide()
                self.label_3.hide()
                self.student_option.hide()
                self.give_random.hide()
                self.done.show()

        except:
            self.marks_error.show()
            self.marks_error.setText("Please give marks in integer!!")
            return

    # def sendNotice(self):


class HodAuthorityScreen(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(HodAuthorityScreen, self).__init__()
        loadUi("hodAuthorityScreen.ui", self)
        widget.setFixedWidth(911)
        widget.setFixedHeight(551)

        self.hodName.setText(f"{self.name} choose an operation")
        self.backBtn.clicked.connect(self.backPage)
        self.nextBtn1.clicked.connect(self.searchStudent)
        self.nextBtn2.clicked.connect(self.updateStudent)
        self.nextBtn3.clicked.connect(self.removeStudent)
        self.nextBtn4.clicked.connect(self.searchFaculty)
        self.nextBtn5.clicked.connect(self.notice)
        self.nextBtn6.clicked.connect(self.checkFeedback)
        self.nextBtn7.clicked.connect(self.msgToStudent)
        self.nextBtn8.clicked.connect(self.searchClass)

    def backPage(self):

        hod_screen = HodScreen(self.widget)
        self.widget.addWidget(hod_screen)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def searchStudent(self):
        search_student = SearchStudent(self.widget, "2")
        self.widget.addWidget(search_student)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def updateStudent(self):
        update_student = UpdateStudent(self.widget)
        self.widget.addWidget(update_student)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def removeStudent(self):
        remove_student = RemoveStudent(self.widget)
        self.widget.addWidget(remove_student)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def searchFaculty(self):
        search_faculty = SearchFacultyForHod(self.widget)
        self.widget.addWidget(search_faculty)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def notice(self):
        send_notice = GiveNotice(self.widget)
        self.widget.addWidget(send_notice)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def checkFeedback(self):
        check_feedback = CheckFeedback(self.widget)
        self.widget.addWidget(check_feedback)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def msgToStudent(self):
        msg_to_student = MsgToStudent(self.widget)
        self.widget.addWidget(msg_to_student)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def searchClass(self):
        Search_class = SearchClass(self.widget, "3")
        self.widget.addWidget(Search_class)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)


class UpdateStudent(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(UpdateStudent, self).__init__()
        loadUi("updateStudent.ui", self)
        widget.setFixedWidth(916)
        widget.setFixedHeight(593)

        self.label1.hide()
        self.option2.hide()
        self.changeBtn.hide()

        self.search.setPlaceholderText("Enter the data of student")

        self.search.findChildren(QAction)[0].setIcon(QIcon("cross_btn.png"))

        self.option.addItem("Search by name")
        self.option.addItem("Search by id")

        self.backBtn.clicked.connect(self.backPage)
        self.searchBtn.clicked.connect(self.searchStudent)
        self.changeBtn.clicked.connect(self.showOptions)

    def searchStudent(self):
        self.option2.clear()
        flag = False
        option = self.option.currentText()

        if option == "Search by name":
            if self.search == "":
                return
            else:
                name_input = self.search.text().lower()
                for i in self.p.selected_student:
                    if name_input == i.name.lower():

                        self.label1.show()
                        self.option2.show()
                        self.changeBtn.show()

                        self.error.hide()

                        flag = True

                        self.student = i

                        self.option2.addItem("1 :- Email ID")
                        self.option2.addItem("2 :- Phone number")
                        self.option2.addItem("3 :- City")

                        return

                if not (flag):
                    self.label1.hide()
                    self.option2.hide()
                    self.changeBtn.hide()

                    self.error.show()
                    self.error.setText("Student not found !!")
                    return
        elif option == "Search by id":
            if self.search == "":
                return
            else:
                id_input = self.search.text()
                for i in self.p.selected_student:
                    if id_input == str(i.enrollment_id):

                        self.label1.show()
                        self.option2.show()
                        self.changeBtn.show()

                        self.error.hide()

                        flag = True

                        self.student = i

                        self.option2.addItem("1 :- Email ID")
                        self.option2.addItem("2 :- Phone number")
                        self.option2.addItem("3 :- City")

                        return

                if not (flag):
                    self.label1.hide()
                    self.option2.hide()
                    self.changeBtn.hide()

                    self.error.show()
                    self.error.setText("Student not found !!")
                    return

    def showOptions(self):

        change_properties = ChangeProperties(
            self.widget, self.option2.currentText(), self.student)
        self.widget.addWidget(change_properties)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def backPage(self):

        hod_authority = HodAuthorityScreen(self.widget)
        self.widget.addWidget(hod_authority)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)


class ChangeProperties(QDialog):
    def __init__(self, widget, field, student):
        self.widget = widget
        super(ChangeProperties, self).__init__()
        loadUi("changeProperties.ui", self)
        widget.setFixedWidth(920)
        widget.setFixedHeight(480)
        self.field = field
        self.student = student

        self.text.findChildren(QAction)[0].setIcon(QIcon("cross_btn.png"))

        self.done.hide()
        self.error.hide()

        if self.field == "1 :- Email ID":
            self.text.setText(self.student.email)
            self.whichField.setText("Enter new Email id")
        elif self.field == "2 :- Phone number":
            self.text.setText(self.student.phone)
            self.whichField.setText("Enter new Phone number")
        elif self.field == "3 :- City":
            self.text.setText(self.student.city)
            self.whichField.setText("Enter new City")

        self.backBtn.clicked.connect(self.backPage)
        self.changeBtn.clicked.connect(self.changeProperty)

    def backPage(self):

        update_student = UpdateStudent(self.widget)
        self.widget.addWidget(update_student)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def changeProperty(self):
        content = self.text.text()

        if (len(content) == 0):
            self.error.setText("Please fill all fields!!")
            self.error.show()
            return

        if self.field == "1 :- Email ID":
            if (not (self.is_valid_emailid(content))):
                self.error.setText("Please Enter valid email id!!")
                self.error.show()
                return

            self.done.show()

            self.whichField.hide()
            self.text.hide()
            self.changeBtn.hide()
            self.error.hide()

            self.p.update_email_to_database_student(
                content, self.student.enrollment_id)

        elif self.field == "2 :- Phone number":
            if (not (self.is_valid_number(content))):
                self.error.setText("Please Enter valid number!!")
                self.error.show()
                return

            self.done.show()

            self.whichField.hide()
            self.text.hide()
            self.changeBtn.hide()
            self.error.hide()

            self.p.update_number_to_database_student(
                content, self.student.enrollment_id)

        elif self.field == "3 :- City":
            self.done.show()

            self.whichField.hide()
            self.text.hide()
            self.changeBtn.hide()
            self.error.hide()

            self.p.update_city_to_database_student(
                content, self.student.enrollment_id)

    def is_valid_emailid(self, content):
        try:
            v = validate_email(content)
            return True
        except EmailNotValidError as e:
            return False

    def is_valid_number(self, content):
        if len(content) != 10:
            return False
        for i in content:
            temp = ord(i)
            if not (temp >= 48 and temp <= 57):
                return False
        return True


class RemoveStudent(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(RemoveStudent, self).__init__()
        loadUi("removeStudent.ui", self)
        widget.setFixedWidth(925)
        widget.setFixedHeight(692)

        self.text.hide()
        self.ans.hide()
        self.done.hide()

        self.search.findChildren(QAction)[0].setIcon(QIcon("cross_btn.png"))

        self.backBtn.clicked.connect(self.backPage)
        self.searchBtn.clicked.connect(self.searchStudent)

    def backPage(self):

        hod_authority = HodAuthorityScreen(self.widget)
        self.widget.addWidget(hod_authority)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def searchStudent(self):
        flag = False

        if self.search == "":
            return
        else:
            id_input = self.search.text()
            for i in self.p.selected_student:
                if id_input == str(i.enrollment_id):

                    self.rollNo.show()
                    self.name.show()
                    self.id.show()
                    self.rank.show()
                    self.emailId.show()
                    self.number.show()
                    self.department.show()
                    self.classId.show()
                    self.city.show()
                    self.mentor.show()
                    self.text.show()
                    self.ans.show()

                    self.error.hide()
                    self.done.hide()

                    self.printData(i)
                    flag = True

                    self.ans.clicked.connect(self.removeStudent)
                    self.p.selected_student.remove(i)

                    return

            if not (flag):
                self.rollNo.hide()
                self.name.hide()
                self.id.hide()
                self.rank.hide()
                self.emailId.hide()
                self.number.hide()
                self.department.hide()
                self.classId.hide()
                self.city.hide()
                self.mentor.hide()
                self.text.hide()
                self.ans.hide()

                self.error.show()
                self.error.setText("Student not found !!")
                return

    def printData(self, student):
        self.rollNo.setText(f"Roll No: {student.roll_no}")
        self.name.setText(f"Name: {student.name}")
        self.id.setText(f"Enrollment id: {student.enrollment_id}")
        self.rank.setText(f"Merit rank: {student.merit_rank}")
        self.emailId.setText(f"Email-id: {student.email}")
        self.number.setText(f"Phone number: {student.phone}")
        self.department.setText(f"Department: {student.department}")
        self.classId.setText(f"Class: {student.class_alloted}")
        self.city.setText(f"City: {student.city}")
        self.mentor.setText(f"Mentor Name: {student.mentor}")

    def removeStudent(self):

        mydb = self.p.connector()
        mycursor = mydb.cursor()

        query = "DELETE from students WHERE Enrollment_ID = %s"
        val = (int(self.search.text()), )

        mycursor.execute(query, val)

        mydb.commit()

        self.done.show()

        self.rollNo.hide()
        self.name.hide()
        self.id.hide()
        self.rank.hide()
        self.emailId.hide()
        self.number.hide()
        self.department.hide()
        self.classId.hide()
        self.city.hide()
        self.mentor.hide()
        self.text.hide()
        self.ans.hide()
        self.error.hide()


class SearchFacultyForHod(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(SearchFacultyForHod, self).__init__()
        loadUi("searchFacultyForHod.ui", self)
        widget.setFixedWidth(915)
        widget.setFixedHeight(672)

        self.backBtn.clicked.connect(self.backPage)
        self.searchBtn.clicked.connect(self.search)

        self.searchName.findChildren(
            QAction)[0].setIcon(QIcon("cross_btn.png"))

        self.text.hide()
        self.students.hide()

        self.hidden = False

    def backPage(self):

        hod_authority = HodAuthorityScreen(self.widget)
        self.widget.addWidget(hod_authority)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def search(self):

        name = self.searchName.text().lower()
        if type(self.p.faculty[0]) != tuple:
            for i, j in enumerate(self.p.faculty):
                if self.p.faculty.name.lower() == name:
                    self.error.hide()

                    self.facultyName.show()
                    self.facultyMail.show()
                    self.primarySub.show()
                    self.secondarySub.show()
                    self.facultyNumber.show()
                    self.text.show()
                    self.students.show()

                    self.facultyName.setText(f"Name: {self.p.faculty.name}")
                    self.facultyMail.setText(f"E-mail: {self.p.faculty.mail}")
                    self.primarySub.setText(
                        f"Primary subject: {self.p.faculty.primary_subj}")
                    self.secondarySub.setText(f"Secondary subject: {
                                              self.p.faculty.secondary_subj}")
                    self.facultyNumber.setText(
                        f"Phone: {self.p.faculty.phone}")

                    temp_list = self.p.faculty.mystudents.split("\n")

                    for i in temp_list:
                        self.students.addItem(i)

                    return
        else:

            for i, j in enumerate(self.p.faculty):
                if self.p.faculty[i][2].lower() == name:
                    self.error.hide()

                    self.facultyName.show()
                    self.facultyMail.show()
                    self.primarySub.show()
                    self.secondarySub.show()
                    self.facultyNumber.show()
                    self.text.show()
                    self.students.show()

                    self.facultyName.setText(f"Name: {self.p.faculty[i][2]}")
                    self.facultyMail.setText(f"E-mail: {self.p.faculty[i][5]}")
                    self.primarySub.setText(
                        f"Primary subject: {self.p.faculty[i][3]}")
                    self.secondarySub.setText(f"Secondary subject: {
                                              self.p.faculty[i][4]}")
                    self.facultyNumber.setText(
                        f"Phone: {self.p.faculty[i][6]}")

                    temp_list = self.p.faculty[i][7].split("\n")

                    for i in temp_list:
                        self.students.addItem(i)

                    return

        self.hidden = True
        if self.hidden:
            self.error.show()

            self.facultyName.hide()
            self.facultyMail.hide()
            self.primarySub.hide()
            self.secondarySub.hide()
            self.facultyNumber.hide()
            self.text.hide()
            self.students.hide()
            self.error.setText("Faculty not found")


class GiveNotice(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(GiveNotice, self).__init__()
        loadUi("giveNotice.ui", self)
        widget.setFixedWidth(928)
        widget.setFixedHeight(575)

        self.done.hide()

        self.backBtn.clicked.connect(self.backPage)
        self.sendBtn.clicked.connect(self.sendNotice)

    def backPage(self):

        hod_authority = HodAuthorityScreen(self.widget)
        self.widget.addWidget(hod_authority)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def sendNotice(self):
        content = self.textPara.toPlainText()
        if content == "":
            return

        now = datetime.now()

        f = open("D:\\Projects_Sem-3\\Python-I_Individual\\notice.txt", 'a')

        f.write(now.strftime("%d/%m/%Y %H:%M:%S") + " :\n" + content + "\n\n")

        f.close()

        self.done.show()

        self.label.hide()
        self.textPara.hide()
        self.sendBtn.hide()


class CheckFeedback(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(CheckFeedback, self).__init__()
        loadUi("checkFeedback.ui", self)
        widget.setFixedWidth(911)
        widget.setFixedHeight(574)

        self.error.hide()
        self.showFeedback()
        self.backBtn.clicked.connect(self.backPage)

    def backPage(self):

        hod_authority = HodAuthorityScreen(self.widget)
        self.widget.addWidget(hod_authority)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def showFeedback(self):
        if (not (os.path.exists("D:\\Projects_Sem-3\\Python-I_Individual\\feedback.txt"))):
            self.error.show()
            self.error.setText("No notice yet !!")
            return
        f = open("D:\\Projects_Sem-3\\Python-I_Individual\\feedback.txt", 'r')
        self.textPara.setText(f.read())

        f.close()


class MsgToStudent(QDialog):
    def __init__(self, widget):
        self.widget = widget
        super(MsgToStudent, self).__init__()
        loadUi("msgToStudent.ui", self)
        widget.setFixedWidth(928)
        widget.setFixedHeight(677)

        self.search.findChildren(QAction)[0].setIcon(QIcon("cross_btn.png"))

        self.done.hide()
        self.error.hide()
        self.label.hide()
        self.textPara.hide()
        self.sendBtn.hide()

        self.backBtn.clicked.connect(self.backPage)
        self.searchBtn.clicked.connect(self.searchStudent)
        self.sendBtn.clicked.connect(self.sendNotice)

    def backPage(self):

        hod_authority = HodAuthorityScreen(self.widget)
        self.widget.addWidget(hod_authority)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def searchStudent(self):
        flag = False

        if self.search == "":
            return
        else:
            name_input = self.search.text().lower()
            for i in self.p.selected_student:
                if name_input == i.name.lower():
                    flag = True

                    self.label.show()
                    self.textPara.show()
                    self.sendBtn.show()

                    self.error.hide()

                    self.student = i

                    return

        if not (flag):
            self.label.hide()
            self.textPara.hide()
            self.sendBtn.hide()

            self.error.show()
            return

    def sendNotice(self):
        content = self.textPara.toPlainText()
        if content == "":
            return

        now = datetime.now()

        f = open(
            f"D:\\Projects_Sem-3\\Python-I_Individual\\students\\{self.student.name}\\msg.txt", 'a')

        f.write(now.strftime("%d/%m/%Y %H:%M:%S") + " :\n" + content + "\n\n")

        f.close()

        self.done.show()

        self.label.hide()
        self.textPara.hide()
        self.sendBtn.hide()
        self.error.hide()
