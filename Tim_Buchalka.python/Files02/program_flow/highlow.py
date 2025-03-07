import os; os.system('cls')
low = 1
high = 1000

print("Please think of a number between {} and {}".format(low,high))
input("Press ENTER to start")

guess = 1
while True:
    ## guess == (high - low) // 2 + low 
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower")
    
























print('\n'*8)