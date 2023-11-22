import controler

def user_login(username,password):
    if controler.login_validation(username,password):
        return True
   
    return False


def user_register():
    '''
    please enter 1 for user as a role 
    please enter 2 for admin as a role 
    '''
    username=input("enter the username : ")
    password=input("enter the password : ")
    name=input("enter the name : ")
    role=input("enter the role : ")

    user_register = controler.user_registeration(username,password,name,role)
    if user_register:
        print("user registeration successfully")
    else:
        print("user registeration failed")
    
    


def blood_donar():
    print("blood donar")
    
def blood_reciever():
    print("blood reciver")

def user_info():
    print("user information")

def update_user():
    print("update user")

def delete_user():
    print("delete user")





def user_input():
    number=int(input("enter the choice : "))
    return number

def user_login_func(n):
    if n==1:
        user_register()
    elif n==2:
        blood_donar()
    elif n==3:
        blood_reciever()
    elif n==4:
        user_info()
    elif n==5:
        update_user()
    elif n==6:
        delete_user()

    else:
        print("invalid choice")

def main():
    print("welcome to blood bank")
    print("enter 1 for login in blood bank")
    
    
    n=user_input()
    if n==1:
        username=input("enter the username : ")
        password=input("enter the password  : ")
        if user_login(username,password):
            print("login successfully")
            '''
            
            '''
            print("enter 1 for user registeration")
            print("enter 2 for blood donate")
            print("enter 3 for blood reciver")
            print("enter 4 for read all user information")
            print("enter 5 for Update a user")
            print("enter 6 for delete a user")
            print("any other number for exit")
            number = user_input()
            user_login_func(number)

        else:
            print("invalid username or password")
    else:
        print("invalid choice")
if __name__ == "__main__":
    main()