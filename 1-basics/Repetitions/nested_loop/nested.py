rows = int(input("How many rows should I have?"))
columns = int(input("How many columns should I have?"))
#the rows in our range functions tells the for loop how many times to repeat the following code and will finish with a print() to display it on the next line (which acts like a row). for the specified amount of columns it will print ":)" and then the end="" function will tell it to repeat the print function in the nested code again on the same line eg. if you wanted 5 columns the for statement would loop 5 times and display :) :) :) :) :) all on the same line because of the end="" function.
for row in range (0, rows, 1):
  for column in range (0, columns, 1):  #this nested will loop how many times you
    print(":)", end="")                 #tell it to
  print()