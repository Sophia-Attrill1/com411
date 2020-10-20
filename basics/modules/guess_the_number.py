import random as rnd


min_value = int(input("Please enter the minum value \n"))

max_value = int(input("Please enter the maximum value \n"))

random_number = (rnd.randrange(min_value, max_value))

print("I am thinking of a number between {} and {} . \n Can you guess what it is? ".format(min_value, max_value))

guess = 0

while(guess != random_number):
  print("Please enter a number:")
  guess = int(input())

  if (guess == random_number):
    print("Congratulations!")
    break
  elif (guess < random_number):
    print("Guess higher")
  else:
    print("Guess lower")
  
print("Game over!")
