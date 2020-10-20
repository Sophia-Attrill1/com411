where = input("I need to find a spare battery, where should I look? \n")

if (where == "in the bedroom"):
 bedroom = input("Where in the bedroom? \n")
 if (bedroom == "under the bed"):
  print("Found some shoes but no battery")
 else:
   print("Found some mess but no battery")

if (where == "in the bathroom"):
 bathroom = input("Where in the bathroom should I look? \n")
 if (bathroom == "in the bathtub"):
  print("Found a rubber duck but no battery")
 else:
   print("Found a wet surface but no battery")

if (where == "in the lab"):
 lab = input("Where in the lab should I look? \n")
 if (lab == "on the table"):
  print("Yes I found it!")
 else:
   print("Found some tools but no battery.")
  
else:
 print("I do not know where that is but I will keep looking.")
  