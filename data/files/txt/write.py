def search(file_name):
  print("Searching...")
  sections = [] #create two tuppels: sections and books
  books = []

  with open(file_name) as file:
    for line in file: #for each line in the file
      if (line.startswith("Section")): #if that line starts with "Section"
        parts = line.split(":") #then split it into two from the ":". Into [0] and [1] 
        sections.append(parts[1].replace('\n', '')) #append the second part [1] of the line.split to the list
      else:
        books.append(line.replace('\n', ''))

  print("Done!")

  return (sections, books)

def save(file_name, data):
  print("Saving...")
  with open(file_name, "w") as file: # w to write a file.
    file.write(f"Sections: {data[0]}") #display sections list in a string
    file.write(f"\nBooks: {data[1]}") #display books list in a string

  print("Done!")

def run():
  data = search("data/files/txt/books.txt") #store search() and the directory as a variable
  save("data/files/txt/section-books.txt", data) #run save() (our function that is used to write lines into the program) as our directory we want to paste our text to. run data as our second parameter which contains the reading of section-books

run()