numbtosum = int(input("How many numbers should I sum up?\n"))
#the user inputs the amount of sums will be added together which is held in the
#variable "numtosum"
summed = 0
#"summed" variable is the iteration number and will have 1 added to it each #iteration until it holds the same value as the user entered number "numbtosum"
#"summed" variable is also used to tell the user how many times they need to input
#a new number to calculate
total = 0

while (summed < numbtosum):
  print("Please enter number", summed, "of", numbtosum, )
  number = int(input())
  summed += 1
  total += number

#the "number" that the user enters will be added to the total and then be #replenished with the next number a user inputs. It will repeat this process #until the iterations stop


print("The sum is", total )

#the total is printed when the user has finished entering values into the "number"
#variable. 

