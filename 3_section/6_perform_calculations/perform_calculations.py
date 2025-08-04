a = 12
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)  # integer division, rounded down toward minus infinity
print(a % b)  # modulus, remainder of the division
print(a**b)  # exponentiation, a to the power of b
print(a**0.5)  # square root
print(a**(1/3))  # cube root
print(a**(1/4))  # fourth root
print()

for i in range(1, 5):
    print(i)
print()

for i in range(1, a//b):
    print(i)


for i in range(1, a/b):  # produces error as a/b is float
    print(i)
