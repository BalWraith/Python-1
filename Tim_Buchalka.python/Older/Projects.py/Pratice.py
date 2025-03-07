import os 
os.system("cls")


high = 10
low = 0
count = low
while count < high:
    num = input("Pick a number between {} and {} ".format(low,high))
    num = int(num)+ high % high
    print(num)






print("\n"*2)

