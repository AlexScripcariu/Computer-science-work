first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

full_name = first_name + " " + last_name

if len(first_name) < 5: 
    print(full_name.upper())
else:
    print(full_name.lower())