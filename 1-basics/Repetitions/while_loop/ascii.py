response = int(input("How many bars should be charged?"))
chargedbars = 1

while chargedbars < response:
  print("Charging" , "█" * chargedbars)
  chargedbars += 1

print("The battery is fully charged")