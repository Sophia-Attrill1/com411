# Ask user to enter their name
print("What is your name human?")
name = input()
print("It is nice to meet you human", name)

#read in users name
name = input("What is your name human?")
#comma and plus are used as a seperator for the print statement
print("Nice to meet you human", name, ".")
#read users name with space between human and the name
print("Nice to meet you " + name + ".")
#easiest way is to use {} and then .format(variable))
print("Nice to meet you {}.".format(name))