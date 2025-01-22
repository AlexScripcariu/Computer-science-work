# asks the user for their username and password
username = input("Please enter your username: ")
password = input(f"Please set a password, {username}: ")


while True:
    
    lowerPass = password.lower()
    if len(password) < 8:   # checking the password is atleast 8 characters:
        print("Your password needs to be atleast 8 characters.")
        password = input(f"Please set a password, {username}: ")
        continue
    elif password == lowerPass:
        # if the password.lower is equal to the normal password then ALL chars are lowercase
        # if it not equal then it must mean there is atleast 1 uppercase. 
        print("Your password needs to have 1 uppercase letter!")
        password = input(f"Please set a password, {username}: ")
        continue
    
    

    break
    