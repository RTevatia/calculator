from cal_fun import CalFunc

print("Calucalor for two numbers. Press 'q' to quit")
while True:
    num_1 = input("Enter first number: ")
    if num_1 == "q":
        break
    num_2 = input("Enter second number: ")
    if num_2 == "q":
        break

    cf = CalFunc(num_1, num_2)

    print("'1' to divide; '2' to mulitply; '3' to add; and '4' to subtract")
    func = input("Enter: ")

    if int(func) == 1:
        print("{} / {} = {}".format(num_1, num_2, cf.divide()))
    elif int(func) == 2:
        print("{} * {} = {}".format(num_1, num_2, cf.multiply()))
    elif int(func) == 3:
        print("{} + {} = {}".format(num_1, num_2, cf.add()))
    elif int(func) == 4:
        print("{} - {} = {}".format(num_1, num_2, cf.subtract()))
    else:
        print("Enter a number from 1-4.")
