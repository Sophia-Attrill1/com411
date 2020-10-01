print("What is your name human?")
name = input()

print("How old are you (in years)")
age = int(input())

print("How tall are you (in meters)?")
height = float(input())

print("How much do you weigh (in kilograms)?")
weight = float(input())

bmi = weight / height**2

roundedBmi = round (bmi, 2)

print("{} You are {} years old and your bmi is {}".format(name, age, roundedBmi))