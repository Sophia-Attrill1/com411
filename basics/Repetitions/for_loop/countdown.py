distance = int(input("How far are we from the cave?\n"))
#user inputs a distance
for steps in range (distance):
  print(distance, "steps remaining!")
  distance -= 1
#for loop reads the number of the "distance" variable and prints the amount of "distance" there is remaining then subtracts 1 until "distance" reaches 0 then the loop ends
print("We have reached the cave!")