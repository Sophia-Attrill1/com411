
print("What phrase do you see?")
phrase = input()
#the user inputs the code that will be reversed
print("\nReversing...\nThe phrase is ", end="")
#reversed is set to "" so it can join onto the end="" function
reversed = ""
#for each letter than is in the phrase is reversed
for letter in phrase:
    reversed = letter + reversed
#the output is printed 
print(reversed) 
  