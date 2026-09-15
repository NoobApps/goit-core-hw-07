from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self,value):
        if len(value) !=0:
            super().__init__(value)
        else:
            raise ValueError ("Name cannot be empty")
		
class Phone(Field):
    def __init__(self, value:str) -> None :
        if len(value)==10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError("Phone number must be 10 digits like:0671234567")

class Birthday(Field):
    def __init__ (self, birthday : str):
        try:
            bday=datetime.strptime(birthday, "%Y.%m.%d")
            super().__init__(bday.date())
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    

# bd=Birthday("2022.04.12")
# print (bd)
