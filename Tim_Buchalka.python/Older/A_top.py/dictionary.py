import os
os.system("cls")

# myDict = {key1: value1, key2: value2, ...}

fruit = {"apple":1, "banana": 2, "cherry": 3}

print(fruit)

#add

fruit["grape"] = 5

print(fruit)

#access

print(fruit["apple"])

#delete

del fruit["banana"]

print(fruit)

fruit["apple"] = 4

fruit["kiwi"] = 3

print(fruit)

print("grape" + "cherry")
print("\n"*3)