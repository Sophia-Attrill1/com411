print("Please enter the number of lives.")
lives = int(input())

print("Please enter the energy level.")
energy = int(input())

print("Please enter the shield level.")
shield = int(input())

print("Stats have been set.")

#we have multiplied the lives, energy and shield by the symbol (string) to create the number of variables that were inputted 

print("Lives:   " ,lives * "♥")
print("Energy:   " ,energy * "♦")
print("Shield:   " ,shield * "♦")