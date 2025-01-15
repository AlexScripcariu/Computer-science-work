# generates the sequence 1, 10, 100 etc.
sequence = [i for i in range(0, 110, 10)]
sequence[0] = 1

while True:
    try:
        selected_number = int(input("Please enter a number: "))

        if selected_number not in sequence:
            print("Number not accepted. Error code 5.") 
    except ValueError:
        print("Please enter only numbers! Error code 1.")
        continue

    print("Number accepted!")
    break