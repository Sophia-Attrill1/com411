def escape_by(plan):
 
  if plan == "jumping over":
    print("We cannot escape that way! The boulder is too big!")
  elif plan == "running around":
    print("we cannot escape that way! boulder is moving too fast")
  elif plan == "going deeper":
    print("That might just work! lets go deeper!")
  else:
    print("We cannot escape that way! the boulder is in the way!")


plan = input("How do we escape? \n")
escape_by(plan)