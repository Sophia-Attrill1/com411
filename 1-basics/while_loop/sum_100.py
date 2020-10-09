
print("Calculating the sum of the first 100 numbers...")

#Firstly we use a print statement to state that we are calculating the first 100 numbers. Then we set our two variables "calculation" and "number" to 0. 

calculation = 0
number = 0

while number < 100:
  number += 1
  calculation += number
print("Done. the answer is {}".format(calculation))

#the "number" variable acts to loop round until it gets to 100 and stops.
#the "number" is added to the "calculation" which is 0. so it becomes 0 + 1.
#the "number" then becomes 2 and adds itself to the "calculation" and becomes 3. This
#process repeats until "number" has done 100 iterations (as the "number" variable is going up 1 digit at a time) and becomes equal to 100
#therefore it has added every number from 0-100. The answer is written in print and is displayed with a .format