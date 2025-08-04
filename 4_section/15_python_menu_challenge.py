
choice = None
while choice != "0":
    print("Please select a number option from the list below:")
    print("1: Learn Python")
    print("2: Learn Java")
    print("3: Go Swimming")
    print("4: Have Dinner")
    print("5: Go to Bed")
    print("0: Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("You chose to learn Python!")
    elif choice == "2":
        print("You chose to learn Java!")
    elif choice == "3":
        print("You chose to go swimming!")
    elif choice == "4":
        print("You chose to have dinner!")
    elif choice == "5":
        print("You chose to go to bed!")
    else:
        print("Invalid choice. Please try again.")
