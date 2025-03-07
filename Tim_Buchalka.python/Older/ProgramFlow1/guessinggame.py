import os, random
os.system("cls")

def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The String that the user will see, when
        they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
      temp = input(prompt)
      if temp.isnumeric():
         return int(temp)
      
      print(" {0} is not a valid number".format(temp))


help(get_integer)

highest = 1000
answer = random.randint(1,highest)#Return random integer in range [a, b], including both end points.
print(answer)   #TODO: Remove after
guess = 0 # initialise to any number that doesn't equal the answer
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
 guess = get_integer(": ")

 if guess == 0:
    break
 if guess == answer:
     print("Well done, you guessed it ")
     break
 else:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
  

    
print("\n"*2)
    
