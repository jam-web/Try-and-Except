print("Which two numbers do you want to add together?")

(user_input1) = float(input("Input your first number: "))

(user_input2) = float(input("Input your second number: "))

try: 
  print(user_input1 + user_input2)
except: 
  print("Error, please enter at least one number")