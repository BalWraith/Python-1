filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"];import os;os.system('cls')

for filename in filenames:
    filename = filename.replace("." , "-")
    print(filename)

print(filenames)


seconds = [1.23, 1.45, 1.02]
current = 1.11

seconds.append(current)
print(seconds)

















print('\n'*5)