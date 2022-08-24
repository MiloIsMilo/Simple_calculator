from calculation import Calculation

print("Simple calculator!\n")

flag = True
calculations = float(input("Enter first number: "))
while flag:
    try:
        print("First number: " + str(calculations))
        num_1 = float(input("Enter second number: "))
        choice_flag = True
        while choice_flag:
            try:
                choice = int(input("\n1. addition\t (" + str(calculations) + " + " + str(num_1) +
                                   ")\n2. subtraction\t (" + str(calculations) + " - " + str(num_1) +
                                   ")\n3. multiplication\t (" + str(calculations) + " * " + str(num_1) +
                                   ")\n4. division\t (" + str(calculations) + " / " + str(num_1) +
                                   ")\n5. reset" +
                                   "\n6. close" +
                                   "\n(1-6): "))
            except ValueError:
                print("Error! Enter a int number (1-6)!\n")
            else:
                if choice >= 1 and choice <= 6:
                    choice_flag = False
                else:
                    print("Error! Enter a int number (1-6)!\n")
    except ValueError:
        print("Error! Enter a number!\n")
    else:
        calculation = Calculation(num_1, calculations)
        if choice == 1:
            calculations = calculation.addition()
            print("")
        elif choice == 2:
            calculations = calculation.subtraction()
            print("")
        elif choice == 3:
            calculations = calculation.multiplication()
            print("")
        elif choice == 4:
            try:
                calculations = calculation.division()
                print("")
            except ZeroDivisionError:
                print("Error! You can't division by 0!\n")
        elif choice == 5:
            calculations = calculation.reset()
        elif choice == 6:
            print("\nClosing calculator\n")
            flag = False
        else:
            print("Error! Enter a int number (1-6)!\n")

