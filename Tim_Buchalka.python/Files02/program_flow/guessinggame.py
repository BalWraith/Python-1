## LOW LEVEL CODE 
import os,random;os.system('cls')

hightest = 1000
answer = random.randint(1,hightest)
print(answer) ## TODO: Remove after testing

print("Please guess a number between 1 and {} enter {} to quit: ".format(hightest,0))
guess = 0 ## initialise to any number that doesn't equal the answer range

## Instructors way
# while guess != answer:
#     guess = int(input())

#     if guess == 0: ## break out of the while loop
#         break
#     if guess == answer: ## correct answer break out of the loop
#         print("Well done, you guessed it ")
#         break
#     else: ## if the guess is not right or 0 than this block will execute
#         if guess < answer: ## answer is higher than the guess
#             print("Please guess higher")
#         else: #guess must be greater than answer
#             print("Please guess lower")

        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it ")
        # else:
        #     print("Sorry you have not guessed correctly")
        

## My way
# while guess:
#     if guess == 0:
#         print("Ok you can leave the game")
#         break
#     elif guess < answer:
#         print("Please guess higher")
#         guess = int(input())
        
#     elif guess > answer:
#         print("Please guess lower")
#         guess = int(input())
#     else:
#         print("Well done you got it right")
#         break


# if guess != answer:
    # if guess < answer: ## answer is higher than the guess
        # print("Please guess higher")
    # else: #guess must be greater than answer
        # print("Please guess lower")
    # guess = int(input())
    # if guess == answer:
        # print("Well done, you guessed it ")
    # else:
        # print("Sorry you have not guessed correctly")
# else:
    # print("You got it the first time")

        





































## Challenge 
# change the condition on line 6 to 
# if guess == answer:
# then change the program to give the correct results
# if guess == answer:
#     print("You got it the first time")
# else:
#     if guess < answer: ## answer is higher than the guess
#         print("Please guess higher")
#     else: #guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it ")
#     else:
#         print("Sorry you have not guessed correctly")


# ## This code has duplicate code which should always be avoided 
# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# # elif guess == answer:
# else:
#     print("You got it the first time")
























print('\n' *8)