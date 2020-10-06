first = int(input("Please enter the first number"))
second = int(input("Please enter the second number"))
third = int(input("Please enter the third number"))

counteven = 0
countodd = 0

if (first % 2 == 0):
  counteven += 1
else:
  countodd += 1

if (second % 2 == 0):
  counteven += 1
else:
  countodd += 1

if (third % 2 == 0):
  counteven += 1
else:
  countodd += 1

print("You put {} even and {} odd numbers".format(counteven, countodd))