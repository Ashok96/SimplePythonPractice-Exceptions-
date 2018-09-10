
try:
  f = open('corrupt_file.txt')
  raise Exception
except FileNotFoundError:
  print("Sorry, this file doesn't exist")
except Exception:
  print("Error!")
else: #only runs if try doesn't throw any exceptions
  print(f.read())
  f.close()
finally:
  print("Executing finally...") #runs no matter exception occurs or not

  
