import models

def login_validation(username, password):
    if username == "admin" and password == "admin":
        return True
    else:
        return False
    
def user_registeration(username, name, password, role):
    if models.create_user(username, name, password, role):
        return True
    else:
        return False