def steps():
  likelihoods = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)] #storing data in the tuple
  return likelihoods

def run():
  all_steps = steps() #storing steps as a variable
  good_steps = []
  bad_steps = []
  for step in all_steps: #looping through each item in likelihoods and counting them
    if step[1] > 50:
      bad_steps.append(step) #we cannot use +=1 as we are adding to a list so we must use append
    else:
      good_steps.append(step)

  print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}") #printing out results using a len funciton which counts the amount of items in the list and presents them to us

run()

