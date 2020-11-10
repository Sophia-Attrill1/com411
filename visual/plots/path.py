import matplotlib.pyplot as plt

def coordinate():
  print("Please enter an x value")
  x = input()
  print("Please enter a y value")
  y = input()
  return (x, y)

def path(): #puts x and y into lists
  print("Retrieving path...")
  x_values = []
  y_values = []
  for loop in range(4):
    data = coordinate()
    x_values.append(data[0]) #appends items user inputted for the x value
    y_values.append(data[1]) #appends items user inputted for the y value
  return [x_values, y_values] #returns a list of list

def run():
  values = path()
  plt.plot(values[0], values[1], 'r--o')
  plt.xlabel("x values")
  plt.ylabel("y values")
  plt.show()

run()
