name = input("Beep boop! Hello Human! What is your name? \n")
#the user enters a name and the bot remembers the string code
botname = input(name+ ", huh, that's a nice name! \n Say " + name + " could you please help build me? \n First things first I need a name! Would you please name me, " + name + "? \n" )
#lefteye, righteye and mouth are left as inputs as they can be any character or number as they will not be calculated 
lefteye = input("So my name is " + botname + "... \n Could you make me a face " + name + "? \n Please enter a character for my left eye. \n")

righteye = input ("Nice! Now enter a character for my right eye.")

mouth = input ("Awesome! Now enter a character for my mouth")
#the inputs the user put in earlier are now shown in the robot in a .format function to make it easier to place
print("##########")
print("# {}   {}  #".format(lefteye, righteye))
print("#   {}    #".format(mouth))
print("##########")

weight = float(input("Wow! Do you think I will make many friends with this face? \n Anyway " + name + " I need to test my functionality by calculating your BMI. \n Could you please tell me your weight in kilograms?"))
#weight and height are float numbers because they are going to be calculated
height = float(input("How tall are you (in metres) " + name + "?"))
#the bmi is weight divided by height to the power of 2. the power of 2 is written as **2
bmi = weight / height**2
#the bmi is calcualted and rounded to two demical places
bmi = round(bmi, 2)
#the bmi is said as a string format
print(name + " your BMI is" , str(bmi) + ".")