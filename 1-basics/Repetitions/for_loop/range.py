brightness = int(input("What level of brightness is required?\n"))
#the variable "bright" now holds the value of "brightness +1" which goes up by two every
#time
for bright in range(2, brightness + 1 , 2):
   print("Beep's brightness level:", "*" * bright)
   print("Bop's brightness level:", "*" * bright)

print("Adjustments complete!")