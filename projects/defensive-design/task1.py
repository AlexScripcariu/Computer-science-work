while True:
    try:
        pin = int(input("Please enter a 4 digit pin: "))
        
        if len(str(pin)) != 4:
            print("Please enter a pin 4 digits long. Error code: 2")
            continue
    except ValueError:
        print("Please enter it 4 digits long and all numbers! (1-9). Error code: 1")
        continue

    print("New Pin accepted. Thank you.")
    break