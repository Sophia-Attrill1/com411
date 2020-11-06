import os

def cwd():
  path = os.getcwd() #gets path to current working directory
  print(f"Current Working Folder Path: {path}")
  print("The folder contains the following:")
  for cwdfile in os.listdir(path): #returns a list containing entries in directory
   print(cwdfile)

def run():
  print("Processing")
  cwd()

run()