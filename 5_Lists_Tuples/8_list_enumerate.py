available_computer_parts = ['keyboard', 'mouse', 'monitor',
                            'printer', "scanner", "HDMI cable", "USB cable"]
added_computer_parts = []
choice = None
while choice != '0':
    for index, part in enumerate(available_computer_parts):
        print("{}.  {}".format(index+1, part))

    # Alternative way to display the list without using enumerate
    # for part in available_computer_parts:
    #     print("{}.  {}".format(available_computer_parts.index(part) + 1, part))

    choice = input(
        "Enter the number of the part you want to add to your list (or 0 to finish): ")
    if int(choice) <= len(available_computer_parts) and int(choice) > 0:
        added_computer_parts.append(available_computer_parts[int(choice) - 1])
    elif choice != '0':
        print("Invalid choice, please try again.")
print("You have added the following parts to your list: {}".format(
    added_computer_parts) if len(added_computer_parts) > 0 else "No parts added.")
