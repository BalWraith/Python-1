import os
os.system("cls")

for i in range(1,13):
    print("No. {0:2} squared is {1:3} and cubed os {2:4}".format(i, i ** 2, i ** 3))

print()


for i in range(1,13):
    print("No. {0:2} squared is {1:>3} and cubed os {2:>4}".format(i, i ** 2, i ** 3))

print()
# os.system("cls")

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7))
os.system("cls")
for i in range(1,13):
    print("No. {} squared is {} and cubed os {:4}".format(i, i ** 2, i ** 3))

print("\n" * 2)
