import re

def validate_user(username, minlen):
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen <= 0 :
        raise ValueError("minlen bust be at least 1")
    
    #Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    #Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', username):
        return False
    #Usernames can't begin with an number
    if not username[0].isalpha():
        return False
    return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False
print(validate_user("0000",1))