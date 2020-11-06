def search(file_name):
  print("Searching...")
  sections = []
  books = []
  with open (file_name) as file:
    for line in file:
      if (line.startswith("Sections")):
        parts = line.split(":") #if line starts with sections it gets split at the : into two parts [0] and [1]
        sections.append(parts[1].replace('\n', '')) #append the string that comes after     the word "sections" as we split them.
      else:
        books.append(line.replace('\n', '')) #if the line doesnt start with sections then we append it to the books list

  print("Done!")

  return(sections, books)

def save (file_name, dataList):
  print("Saving...")
  with open (file_name, "w" ) as file:
    file.write("Sections: ")
    for section in dataList[0]:
      file.write(f"{section},")

    file.write("Books: ")
    for book in dataList[1]:
      file.write(f"{book},")

  print("Done!")

def run():
  data = search("data/files/txt/books.txt")
  save("data/files/txt/section-books.txt", data)

run()
