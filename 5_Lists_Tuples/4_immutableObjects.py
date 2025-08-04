result = True
another_result = result

print(id(result))
print(id(another_result))

result = False
print(id(result))
print("_"*80)
result = "another string"
print(id(result))
result2 = "another string"
print(id(result2))
result3 = result2+"ish"
print(id(result3))
