import os
os.system("cls")
menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"], 
    ["egg", "spam"], 
    ["egg", "bacon", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
]


# for meal in menu:
#     for index in range(len(meal) - 1, -1, -1):
#         if meal[index] == "spam":
#             del meal[index]
        
#     print(meal)

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item, end=", ")
    print()


