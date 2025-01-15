while True:
    try:
        age = int(input("Please enter your age: "))

        if 0 <= age <= 120:
            print("Age out of range! (0-120 yrs) Error code 4.") 
    except ValueError:
        print("Please enter only numbers! Error code 1.")
        continue

    print("Age accepted!")
    break