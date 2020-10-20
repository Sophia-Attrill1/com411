#putting items into the list
def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu(): #creating a function for indexing the list 
  print("Please select a direction")
  way = directions()
  for index in range(len(way)):
    print("{} : {}".format(index, way[index]))
 
  directionindex = int(input()) #asking the user to input a number in range of way
  return way[directionindex]

def run():
  route = [] #creating an empty list called route
  print("Working out escape route...")
 #adding each user input to the list
  for iteration in range(5):
    direction = menu() #grabbing menu which has returned value of "way"
    route.append(direction)
 #printing the list 
  print("Escape route: {}".format(route))

run()
