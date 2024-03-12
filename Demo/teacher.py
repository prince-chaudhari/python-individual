class Teacher:
    userId = ''
    password = 0
    name = ''
    primary_subj = ''
    secondary_subj = ''
    mail = ''
    phone = ''
    mystudents = []

    def __init__(self, name, primary_subj, secondary_subj, mail, phone):
        self.name = name
        self.primary_subj = primary_subj
        self.secondary_subj = secondary_subj
        self.mail = mail
        self.phone = phone


        
