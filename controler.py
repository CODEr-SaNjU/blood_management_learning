import models

def login_validation(username, password):
    if username == "admin" and password == "admin":
        return True
    else:
        return False
    
def user_registeration(username, password,name,role):
    if models.create_user(username, password,name,role):
        return True
    else:
        return False