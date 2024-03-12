from email_validator import validate_email, EmailNotValidError
import random

class Hod:
    name = ''
    userId = ''
    password = 0
    mail = ''
    phone = ''

    def is_valid_emailid(self):
        try:
            v = validate_email(self.mail) 
            return True
        except EmailNotValidError as e:
            return False

    def is_valid_number(self):
        if len(self.phone) != 10: return False
        for i in self.phone:
            temp = ord(i)
            if not(temp >= 48 and temp <= 57): return False
        return True    
    
    def generate_userid(self):
        arr = self.name.split()
        return arr[0] + self.phone[0:3]
    
    def generate_pass(self):
        min = 10000
        max = 99999
        print(random.randrange(max - min + 1) + min)
        return random.randrange(max - min + 1) + min