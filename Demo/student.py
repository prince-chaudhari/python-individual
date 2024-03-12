class Student:
    userId = ''
    password = 0
    name = ''
    enrollment_id = 0
    merit_rank = 0
    email = ''
    phone = ''
    department = ''
    roll_no = 0
    class_alloted = ''
    city = ''
    mentor = ''

    def __init__(self, name, id, rank, mail, phone, city):
        self.name = name
        self.enrollment_id = id
        self.merit_rank = rank
        self.email = mail
        self.phone = phone
        self.city = city

    def get_merit_rank(self):
        return self.merit_rank
