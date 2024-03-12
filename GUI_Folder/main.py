import sys,os
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
sys.path.append("D:\\Projects_Sem-3\\Python-I_Individual\\Demo")
from hod import Hod

class WelcomeScreen(QDialog):
    def __init__(self,classes,p,widget):
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
        cff1 = ClassForFaculty_1(self.classes,self.widget,cnt)     
        self.widget.addWidget(cff1)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

class ClassForFaculty(QDialog):

    def add_menu(self,obj):
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
    def __init__(self,classes,widget, cnt):
        self.classes = classes
        self.cnt = cnt
        self.widget = widget
        super(ClassForFaculty_1, self).__init__()
        loadUi("classForFaculty_1.ui", self)

        self.whichClass.setText(f"Enter the faculty for class {self.classes[self.cnt].id}")      
        c = ClassForFaculty()   
        c.add_menu(self) 
        self.submit.clicked.connect(self.nextPage)

    def nextPage(self):
        ClassForFaculty.add_faculties(self, self.classes[self.cnt]) 
        self.cnt += 1
        cff2 = ClassForFaculty_2(self.classes,self.widget, self.cnt)     
        self.widget.addWidget(cff2)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

class ClassForFaculty_2(QDialog):
    def __init__(self,classes,widget, cnt):
        self.classes = classes
        self.cnt = cnt
        self.widget = widget
        super(ClassForFaculty_2, self).__init__()
        loadUi("classForFaculty_2.ui", self)

        self.whichClass.setText(f"Enter the faculty for class {self.classes[self.cnt].id}")   
        c = ClassForFaculty()   
        c.add_menu(self) 
        self.submit.clicked.connect(self.nextPage)

    def nextPage(self):
        ClassForFaculty.add_faculties(self, self.classes[self.cnt]) 
        self.cnt += 1
        cff2 = ClassForFaculty_3(self.classes,self.widget, self.cnt)     
        self.widget.addWidget(cff2)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

class ClassForFaculty_3(QDialog):
    def __init__(self,classes,widget, cnt):
        self.cnt = cnt
        self.classes = classes
        self.widget = widget
        super(ClassForFaculty_3, self).__init__()
        loadUi("classForFaculty_3.ui", self)

        self.whichClass.setText(f"Enter the faculty for class {self.classes[self.cnt].id}")      
        c = ClassForFaculty()   
        c.add_menu(self) 
        self.submit.clicked.connect(self.nextPage)

    def nextPage(self):
        ClassForFaculty.add_faculties(self, self.classes[self.cnt]) 
        self.cnt += 1
        cff2 = ClassForFaculty_4(self.classes,self.widget, self.cnt)     
        self.widget.addWidget(cff2)
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

class ClassForFaculty_4(QDialog):
    def __init__(self,classes,widget, cnt):
        self.cnt = cnt
        self.classes = classes
        self.widget = widget
        super(ClassForFaculty_4, self).__init__()
        loadUi("classForFaculty_4.ui", self)

        self.whichClass.setText(f"Enter the faculty for class {self.classes[self.cnt].id}")      
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

        self.hodBtn.clicked.connect(self.nextPage)

    def nextPage(self):
        self.hod.name = hodName = self.hodName.text()
        self.hod.mail = hodEmail = self.hodEmail.text()
        self.hod.phone = hodNumber = self.hodNumber.text()

        if(len(hodName) == 0 or len(hodEmail) == 0 or len(hodNumber) == 0):
            self.error.setText("Please fill all fields!!")
            return
        elif(not(self.hod.is_valid_emailid())):
            self.error.setText("Please Enter valid email id!!")
            return
        elif(not(self.hod.is_valid_number())):
            self.error.setText("Please Enter valid number!!")
            return
        else:
            self.hod.userId = self.hod.generate_userid()
            self.hod.password = self.hod.generate_pass()
            self.p.storeToDatabase(self)
            f = open("D:\\Projects_Sem-3\\Python-I_Individual\\done.txt", "w")
            appoint_hod = AppointHod(self.widget)     
            self.widget.addWidget(appoint_hod)
            self.widget.setCurrentIndex(self.widget.currentIndex() + 1)