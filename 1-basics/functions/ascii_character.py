number = int(input("Program started! \n Please enter an ASCII code \n"))

if(abs(number) in range(32, 126)):
  print("The character represented by the ASCII code {} is {}".format(number, chr(number)))
else:
 print("An error as occoured!")

print("Done")