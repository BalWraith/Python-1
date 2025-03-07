import random
print("One-Million-To-One")
print()
correct_num = random.randint(1,100000000)
while True:
    print(correct_num)
    guess = int(input("Guess a number?: "))
    if guess < correct_num:
        print("Too low")
    elif guess > correct_num:
        print("Too high")
    
    elif guess == correct_num:
        print("Correct!")
        break
    continue
    
print("You win!")
exit()