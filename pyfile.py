import random
import string
from pyscript import document

def generate_password(event):
    password_type = getPasswordType(event,document.querySelector("#password_type"))
    user_input = document.querySelector("#length_input")
    password = []
    length = 0
    if(user_input.value!=''):
        length = user_input.value
              
    for i in range(int(length)):
        password.append(random.choice(password_type))
    output_div = document.querySelector("#output")
    output_div.innerText = 'Your Password: ' + ''.join(password)


def getPasswordType(event,passwordType):
    available_chars = []
    chars =[]
    match passwordType.value:
        case 'number':
            chars = string.digits
        case 'characters':
            chars = string.ascii_letters
        case 'mixed':
            available_chars = [string.ascii_letters,string.digits,'!@#$']   
            for clist in available_chars:
                for item in clist:
                    chars.append(item)
        
    return chars
print("PYTHON SCRIPT IS CONNECTED")
