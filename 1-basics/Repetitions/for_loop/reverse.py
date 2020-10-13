<<<<<<< HEAD
phrase = input("What phrase do you see?\n")
#the end="" makes sure that the next print phrase[position] is on the same line. 
print("\nReversing...\nThe phrase is ", end="")
#the range functions counts all the characters that the variable "phrase" holds #and the "position" variable instructs the "phrase" to be outputted in a -1 #reversed) order
for position in range(len(phrase) - 1, -1, -1):
    print(phrase[position], end="")
=======
magicword = input("What phrase do you see?")
>>>>>>> origin/master
