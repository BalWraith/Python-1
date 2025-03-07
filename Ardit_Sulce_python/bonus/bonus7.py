filenames = ["1.doc", "1.report", "1.presentation"];import os;os.system('cls')

## replaces . with - and adds .txt to the end 
filenames = [filename.replace('.','-') + '.txt' for filename in filenames]

print(filenames)




## LIST COMPREHENSION CHALLENGE
names = ["john smith", "jay santi", "eva kuki"]
## Caps the first letter is each word of this list
names = [name.replace(name,name.title()) for name in names  ]

print(names)

## Counts each char in the string
usernames = ["john 1991", "alberta1970", "magnola2000"]
usernames = [len(username) for username in usernames]
print(usernames)

## Turns each string into a float
user_entries = ['10', '19.1', '20']
user_entries = [float(user) for user in user_entries]
print(user_entries)

## Takes each num and multiply it by 2
numbers = [10, 20, 30]
numbers = [num*2 for num in numbers]
print(numbers)

## Turns the nums in the string to a float and adds them together 
user_input = ['10', '19.1' , '20']
user_input = [float(user) for user in user_input]
print(sum(user_input))





 












print('\n'*8)