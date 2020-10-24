def liklihood():
  likelihoods = [50, 38, 27, 99, 4]
  return min(likelihoods), max(likelihoods) #return the minumum and maximum item in the tuple list. min(likelihoods) has an index of 0 and max(likelehoods) has an index of 1

def run():
  theindex = liklihood()
  print(f"Minimum liklihood of falling: {theindex[0]}%")
  print(f"Maximum liklihood of falling: {theindex[1]}%")

run()

