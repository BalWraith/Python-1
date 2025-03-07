import os;os.system('cls')
## 1ST START
shopping_list = ["milk","pasta","eggs","spam","bread","rice"]

item_to_find = "eggs"
found_at = None

# ## this for loop takes the full length of the shopping_list
for index in range(len(shopping_list)):

    ## this for loop goes through the shopping_list until it finds the value assigned to the variable item_to_find
    ## idex is the number value of everything in the list
    if shopping_list[index] == item_to_find:

        ## sets the value of found_at to the index 
        found_at = index
# 1ST END


## 2ND START
shopping_list = ["milk","pasta","eggs","spam","bread","rice"]

item_to_find = "eggs"
found_at = None

## if item_to_find is in the shopping_list found_at will equal the index value of the item 
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

## if item_to_find is in the list than found_at will equal the index value of that variable
if found_at is not None:
    print("Item found at position {}".format(found_at))

## if item_to_find is not in the shopping_list than the else block will execute
else:
    print("{} not found".format(item_to_find))
## 2ND END













print('\n'*8)