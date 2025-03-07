print()
print("\033[37m Welcome to Replit")
print()
# print("Please press enter to access our login system:")
print("REPLIT LOGIN SYSTEM")
print()
counter = 0
while counter < 3:
   user_name = input("What is your username: ").lower()
   password = input("What is your password: ").lower()
   if user_name == "michael" and password == "password":
      print("Welcom to Replit")
   elif user_name == "david" and password == "trash":
      print("Welcom to Replit")
   elif user_name == "james" and password == "bond":
      print("Welcom to Replit")
   elif user_name == "samantha" and password == "muffinbutt":
      print("Welcom to Replit")
   elif user_name == "bob" and password == "userbas":
      print("Welcom to Replit") 
   else:
      print("Whoops! I don't recognise that username and password, try again")
      counter += 1 
print("\033[31m I'm sorry you've reached the max number of attempts allowed by our system.\n Please wait 30 minutes before trying again")
   
   

