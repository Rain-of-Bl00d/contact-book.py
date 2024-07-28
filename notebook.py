import re
import unicodedata
print("        ___\/ Welcome to the Contact Book \/___      ")
print("        ---------------------------------------      ")
print("Name    |   Number   |  Gmail")
class NoteBook:
    def __init__(self):
        self.contact_dict = {}
        
    def adddetails(self, name, number, gmail):
        self.contact_dict[name] = (str(number)+" | "+str(gmail))
    
    def remove_details(self, name):
        del(self.contact_dict[name])
    
    def showdetails(self):
        for name in self.contact_dict:
            print(name+" | ", self.contact_dict[name])
        print("-------------")
    
    def search_item(self, name):
        print(name+" | ",self.contact_dict[name])
        print("-------------")
    
    def update(self, name, new_number, new_gmail):
        self.contact_dict[name] = (str(new_number)+" | "+str(new_gmail))

def is_valid_phone_number(number):
    pattern = re.compile(r'^\+?\d{1,4}?[-.\s]?(\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}$')
    
    if pattern.match(number):
        digits_only = re.sub(r'\D', '', number)
        if len(digits_only) < 10:
            return False, "Phone number must contain at least 10 digits."
        return True, ""
    else:
        return False, "Invalid phone number format."

number = input()

is_valid, message = is_valid_phone_number(number)

if is_valid:
    print("Phone number is valid.")
else:
    print(f"Error: {message}")


gmail = input()
def is_emoji(gmail):
    flag1 = True
    # Check if the character is in the 'So' (Symbol, Other) category
    for i in gmail:
        if(unicodedata.category(i) == 'So'):
            flag1 = False
    if(flag1):
        return(flag1)
        print("Validated Email !!")
    else:
        return(flag1)
        print("Inalidate Email !!")

def validation1(gmail):
    spec_char = "!#$%^&*()[]{}\?/|><"
    flag2 = True
    if(len(gmail) >= 16):
        if(gmail[0].isalpha() ):
            for i in spec_char:
                if(i in gmail):
                    flag2=(False)
        else:
            return(False)
            return('First charecter must be an alphabet')
    else:
        return("Invalid Email !!")
        return("length of the emali must be greater than 6")
    
    if(flag2):
        return(flag2)
        print("validated Email")
    else:
        return(flag2)
        print("Invalid Email !!")

def validation2(gmail):
    if(gmail[len(gmail)-10:] == "@gmail.com"):
        return(True)
    else:
        return(False)

if( (validation1(gmail)) and (is_emoji(gmail)) and (validation2(gmail))):
    print(" All Set!😃--continue :) ")
else:
    raise ValueError("Cannot Enter Gmail")

ob = NoteBook()
ob.adddetails("Abhilash", number, gmail)
ob.showdetails()
