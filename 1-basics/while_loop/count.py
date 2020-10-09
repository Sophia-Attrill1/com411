avoid = int(input("How many live cables must I avoid?"))

livecables = 0

while (livecables < avoid):
  livecables += 1
  print("Avoiding done! {} live cables avoided".format(livecables))

print("All live cables have been avoided") 