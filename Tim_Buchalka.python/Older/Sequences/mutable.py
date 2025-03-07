import os
os.system("cls")

shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "bread",
                 "rice"
                 ]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]#adds cookies to the shopping_list
print(shopping_list)
print(id(shopping_list))
print(another_list)

a = b = c = d = e = f = another_list
print(a)

print("Adding cream")
b.append("cream")
print(c)
print(d)






print("\n"*3)