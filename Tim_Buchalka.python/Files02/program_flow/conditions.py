import os; os.system("cls")
age = int(input("How old are you? "))

## age is greater than or equal to 16 AND age is less than or equal to 65
if age >= 16 and age <= 65:
    pass

## Simpler than the code above
## if 16 is less or equal to age. age is less than or equal to 65
# if 16 <= age <= 65:

if age in range(16,66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")

print("-"*80)

if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")


















print('\n'*8)