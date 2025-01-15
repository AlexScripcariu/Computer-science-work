while True:
    try:
        phone_number = int(input("Please enter a phone number: "))

        if not len(str(phone_number)):
            print("You must not leave it blank! Error code 3.") 
    except ValueError:
        print("Please enter only numbers! Error code 1.")
        continue

    print("Thank you for your input")
    break