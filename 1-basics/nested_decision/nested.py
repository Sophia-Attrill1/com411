bookcover = input("What kind of cover does this book have? (hard/soft) \n")

if (bookcover == "soft"):
  perfectbound = input ("Is the book perfect bound?")

  if (perfectbound == "yes"):
   print("Soft with perfect bound good!")
  elif (perfectbound == "no"):
    print("Soft non perfect bound good")
  else:
   print("What are you trying to say?")

if (bookcover == "hard"):
 perfectbound = input("Is the book perfect bound?")

 if (perfectbound == "yes"):
   print("I sure do like hard perfect bound!")
 elif (perfectbound == "no"):
   print("Hard not perfect cover good!")
 else:
   print("Not sure what you mean")

<<<<<<< HEAD
=======
else:
  print("I don't know what you're saying")
>>>>>>> origin/master
