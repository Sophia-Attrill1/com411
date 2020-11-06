def observed():
  observations = []

  for count in range(7):
    print("Please enter an item:")
    item = input()
    observations.append(item)
  
  return observations

def run():
  print("Counting observations")
  observations = observed()
  observations_list = set()
  for observation in observations:
    occourences = observations.count(observation) #counting the number of obs
    observations_list.add( (observation, occourences) ) #adding obs and occ to list

  for key, value in observations_list: #printing out the list
    print(f"{key} observed {occourences} times.")

run()