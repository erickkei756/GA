# hw11_problem1_2


import random
import sys

random_number = random.randint(0,10)
print(random_number)

# problem 1 + 2
try:
  while True:
    user_guess = int(input("Guess a number. "))
    print(f"You guessed {user_guess}")

    if user_guess == random_number:
      print("You've guessed correctly.")
      break
    elif user_guess > random_number:
      print(f"{user_guess} is too high. Please try again. ")
    else:
      print(f"{user_guess} is too low. Please try again. ")

except:
  message = "D'oh! That is NOT a number, Bart! Please enter an actual number. "
  print(message)
