def search(file_name):
  print("Searching...")
  with open(file_name) as file: #open the file. With a "with" function it closes itself    
    lines = file.read().split('\n') #read the file and store it as a variable so we can print it in a for loop. Also split it with .split('\n') so
    for line in lines: #print every line that is in the file
      print(f"Looked in location {line}")

    print("Done!")

def run():
  search("data/files/txt/locations.txt") #running search() and giving it the directory path of what txt file it needs to open


run()