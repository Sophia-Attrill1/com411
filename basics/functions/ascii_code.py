character = input("Program started! \n Please enter a standard character \n")

if len(character) == 1:
  value = ord(character)
  print("The ascii code for {} is {}".format(character, value))
else:
  print("One character please")