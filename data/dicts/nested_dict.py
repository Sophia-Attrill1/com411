def short_pattern():
  pattern = {
    "sequence":"101", "occourences":5    #creating a dictionary in a function
  }


  return pattern

def medium_pattern():
  pattern = {
    "sequence":"111000",
    "occourences":50
  }

  return pattern

def long_pattern():
  pattern = {
    "sequence":"11100011101010",
    "occourences":500
  }

  return pattern

def run():
  print("Analysing patterns...")

  patterns = {
    "short sequence":short_pattern(),
    "medium sequence":medium_pattern(), #putting all the dictionaries in one dictionary by
    "long sequence":long_pattern() #calling their functions 
  }

  print(patterns)

run()

#created a dictonary of dictionaries