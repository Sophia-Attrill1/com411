number = int(input("Please input a number\n"))
#the user inputs a number to calculate the factorial of
count = 0
total = 1
#the "count" variable goes through X amount of iterations until it is equal to the "number"
#variable. 
while count < number:
  count += 1
  total *= count

#"total" is * by the count which is then added to the total. Then the new total is * by the
#new count which has had 1 added to it. This calculation calculates the factorial of a the #number that was entered by the user
print("The factorial is", total)
#prints the calculation