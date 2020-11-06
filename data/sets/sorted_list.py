def observed():
  observations = [] #create an empty set
  for count in range(5): #repeat process 5 times
    print("please enter a value:")
    item = input()
    observations.append(item) #appends the users input to the list
  return observations #returns set

def removed_observations(observations):

  is_running = True

  while(is_running):
    print("Do you wish to remove an observation yes OR no")
    answer = input()

    if answer == "yes":
      print("what would you like to remove")
      to_remove = input()
      observations.remove(to_remove) #removes the item from the list that the user input
    else:
      is_running = False

def run():
  observations = observed() #running observed() function
  removed_observations(observations) #running the function that removes things

  observations_set = set()
  
  for observation in observations:
    occurences = observations.count(observation) #count returns the number of oc in a value
    observations_set.add( (observation, occurences) )

  for key, value in sorted(observations_set):
    print(f"{key} observed {value} times")

run()