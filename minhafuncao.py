import re as r
from email_validator import validate_email

def validar_email(email):
    char_email = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'

    if r.search(char_email , email):
        return True
    
    else:
        return False

