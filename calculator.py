from cal_fun import CalFunc

while True:
    print("\nCalucalor for two numbers. Press 'q' to quit")
    num_1 = input("Enter first number (or 'q' to quit): ")
    if num_1 == "q":
        break
    num_2 = input("Enter second number (or 'q' to quit): ")
    if num_2 == "q":
        break

    # Check for value error.
    while True:
        try:
            cf = CalFunc(num_1, num_2)
        except ValueError:
            print("You must have a number!")
            break

        print("'1' to divide; '2' to mulitply; '3' to add; and '4' to subtract")
        func = input("Enter: ")

        # Check if func is integer
        try:
            if int(func) > 0 and int(func) < 5:
                if int(func) == 1:
                    print("{} / {} = {}".format(num_1, num_2, cf.divide()))
                elif int(func) == 2:
                    print("{} * {} = {}".format(num_1, num_2, cf.multiply()))
                elif int(func) == 3:
                    print("{} + {} = {}".format(num_1, num_2, cf.add()))
                elif int(func) == 4:
                    print("{} - {} = {}".format(num_1, num_2, cf.subtract()))
            else:
                print("Please enter only 1-4")
        except ValueError:
            print("Please enter only 1-4")

        # Leave the second while loop
        break
