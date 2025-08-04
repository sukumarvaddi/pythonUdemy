even = [0, 2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)  # Combine even and odd lists
print("Combined list:", even)
another_list = even
even.sort()
print("Sorted list:", even)
print(another_list)

even.sort(reverse=True)

print("Sorted list:", even)
print(another_list)  # Display the sorted list
