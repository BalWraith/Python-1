import os
os.system("cls")

for i in range(1,11):
    for j in range(1,11):
        print("{0:2} times {1} is {2:3}".format(j, i, i *j))
    print("--------------------------------")
        

print("\n"*3)