# Ask user for an input for marking
print("What strange markings do you see?")
markings = input()

print("\nIdentifying...\n")
#we have used the for loop and included in the range "len(markings)" which counts #each character of the value of "markings" then displays them in the print.
#in the code "markings[count]" the "count" is indexing every letter that is in
#the "markings" and outputting each letter as it does iterations round the for #code
for count in range(0, len(markings), 1):
    print("index", count, ":", markings[count])