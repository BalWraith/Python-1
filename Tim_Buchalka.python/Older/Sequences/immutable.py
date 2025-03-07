# result = True
# another_result = result
# print(id(result))           # id returns the idenity of an object
# print(id(another_result))

# result = False
# print(id(result))

result = "Correct"
another_result = result
print(result)

print(another_result)

result += "ish"
print(id(result))
print()
print(another_result)
