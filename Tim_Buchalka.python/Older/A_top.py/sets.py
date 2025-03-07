import os
from re import M
os.system("cls")

#This is a set {}
# A set can not hold a list, or set
# sets are unordered
mySet = {1, 2, 3, 4, 5, 5, 5, 5, "apple", 11.45, False}

# print(mySet)

mySet2 = set()
mySet2.add("banana")
mySet2.add("mango")
mySet2.add("kiwi")
mySet2.add("apple")

# print(mySet2)

mySet2.remove("kiwi")


# print(mySet2)

set1 = {1,2,3,4,}
set2 = {3,4,5,6,7}

#union (|) pipe
print(set1 | set2)

#intersection (&)
print(set1 & set2)

#difference
#takes both lists and only prints the differences
print(set1 - set2)
print(set2 - set1)

print("\n"*4)

