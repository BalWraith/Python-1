import random
print("One-Million-To-One")
print()
correct_num = random.randint(1,100000000)
guess_count = 0
while True:
      print(correct_num)
      guess = int(input("Guess a number?: "))
      if guess < 0:
        print("I'm done I don't want to play this anymore")
        exit()
      elif guess < correct_num:
          print("Too low")
          guess_count += 1
      elif guess > correct_num:
          guess_count += 1
          print("Too high") 

      elif guess == correct_num:
          print("Correct!")
          break
      continue

print("You guessed the number in", guess_count, "attempts")
exit()