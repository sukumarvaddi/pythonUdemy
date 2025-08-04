parrot = "Norwegian Blue"
# print(parrot[0:6:2])  # Nre
# print(parrot[0:6:3])  # Nw

numbers = "9,223,372,036,854,775,807"
separators = numbers[1::4]
# print(separators)  # ,,,,,,
# print(numbers[0::4])  # 9230785


numbers = "9,223;372:036 854,775;807"
separators = numbers[1::4]  # ,;: ,;: ,;: ,;: ,;:
number = "".join(char if char not in separators else " " for char in numbers)

print(number.split())  # ['9', '223', '372', '036', '854', '775', '807']

print([int(number) for number in number.split()])
