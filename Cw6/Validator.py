import re

class Validator:
    def __init__(self):
        pass
    @classmethod
    def is_valid_email(cls,email):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, email):
            return "The given mail is valid"
        else:
            return "The given mail is invalid"

e1 = Validator()
print(e1.is_valid_email('sachin.sharma@gmail.com'))


regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
print(re.fullmatch(regex,'sachin.sharma@gmail.com'))