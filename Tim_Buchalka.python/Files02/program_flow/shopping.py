import os;os.system('cls')
shopping_list = ["milk","pasta","eggs","spam","bread","rice"]

# for item in shopping_list:

      ## if item does not equal spam print that item
#     if item != "spam":
#         print("Buy " + item)

# for item in shopping_list:

#     ## if the item is spam the for loop will skip it and print out the next item in the list
#     if item == "spam":
#         continue
    
#     print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        break
    
    print("Buy " + item)















print('\n'*8)