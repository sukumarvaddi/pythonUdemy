computer_parts = ['CPU', 'GPU', 'RAM', 'SSD', 'Motherboard']
print(computer_parts)
del computer_parts[2]  # Remove 'RAM'
print(computer_parts)

min_valid = 50
max_valid = 100


# Fill the list with 20 random numbers between 1 and 300 not sorted
numbers_list = [45, 12, 78, 34, 56, 89, 23, 67, 90,
                11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 200]

# Flawed logic: This will not work as expected because modifying the list while iterating can cause index errors and skip elements.
for index, value in enumerate(numbers_list):
    if value < 50 or value > 100:
        del numbers_list[index]
print(numbers_list)

numbers_list = [45, 12, 78, 34, 56, 89, 23, 67, 90,
                11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 200]

print("__"*80)

# Corrected logic: Iterate the list in reverse order to avoid skipping elements when deleting.
for index in range(len(numbers_list)-1, -1, -1):
    if numbers_list[index] < min_valid or numbers_list[index] > max_valid:
        del numbers_list[index]
print(numbers_list)

numbers_list = [45, 12, 78, 34, 56, 89, 23, 67, 90,
                11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 200]
# using reversed

# using list comprehension to filter the list.
numbers_list = [45, 12, 78, 34, 56, 89, 23, 67, 90,
                11, 22, 33, 44, 55, 66, 77, 88, 99, 100, 200]

top_index = len(numbers_list)-1
for index, value in enumerate(reversed(numbers_list)):
    if value < min_valid or value > max_valid:
        del numbers_list[top_index - index]
print(numbers_list)

filtered_numbers = [
    num for num in numbers_list if min_valid <= num <= max_valid]
print(filtered_numbers)
