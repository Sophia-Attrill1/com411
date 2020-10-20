#defining the function that gets the list of directions
def directions():
  directions = ("Move Forward", "Move Backward", "Turn Left", "Turn Right")
  return directions
#line 8 we store user defined function "directions" as a variable "way". we then use a 
#for loop and a len to print out every item in the new "way" list.
#the index variable is used to print out the index of the list
#we have used way[index] to make sure it prints the item in order of index
def menu():
  print("Please select a direction")
  way = directions()
  for index in range(len(way)):
    print("{} : {}".format(index, way[index]))

#defines function to run the program
def run():
  print(menu())


run()