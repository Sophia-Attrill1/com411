mountains = int(input("How many mountains should I display?"))
#The code asks for how many mountains the user wishes to display
print("Displaying...")
#the code below displays the number of mountains that was inputted by the user in the 
#variable "mountains". The variable mountain is a variable that is local to the loop #"for" and only exists inside the for loop. We have used "mountain" to demonstrate an #individual number inside of the "mountains" variable and therefore will print the entered
#number of values
for mountain in range (mountains):
  print("""
           __
          /  \\_  
         /^    \\
        /  ^    \\_
      _/ ^ ^     ^\\
     /  ^     ^    \\


     """)

print("Done!")