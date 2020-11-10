import matplotlib.pyplot as plt

def small():
  x = [3,4,4,3,3] #store coordinates in a tuple so we can use them in our plot
  y = [3,3,4,4,3] # to make a small square eg. x y = 3, 3 is plotted on the graph
  plt.plot(x, y, 'ro:') # red colour (r), markers are O (o), lines are dotted (:)

def medium():
  x = [2,5,5,2,2]
  y = [2,2,5,5,2]
  plt.plot(x, y, 'gs--') #green (g), square marker (s), dashed line (--)

def large():
  x = [1,1,6,6,1]
  y = [1,6,6,1,1]
  plt.plot(x, y, 'bp-') #blue (b), pentagon marker (p), straight line(-)

def run():
  small() #run each function which plots the lines in the graph
  medium()
  large()
  plt.show() # display the graph

run()



