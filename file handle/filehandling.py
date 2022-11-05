file_builder = open("pythonfile.txt", "w+")
file_builder.write("LOL")
file_builder.close()

# open the file using open() function
file = open("pythonfile.txt")
 
# Reading from file
print(file.read())


# open the file using open() function
file = open("pythonfile.txt")
   
# Reading from file
print(file.read())
 
# closing the file
file.close() 


filename = 'pythonfile.txt'

# Open the file in write mode and store the content in file_object
with open(filename, 'w') as file_object:
    file_object.write("Python write to file\n")


# Python program to keep the old content of the file
# when using write.
  
# Opening the file with append mode
file = open("pythonfile.txt", "a+")
  
# reach at first
file.seek(0)
  
# Reading the file
content = file.read()
  
# view file content
print(content)
  
# Content to be added
content = "\n\n#This Content is added through the program"
  
# Writing the file
file.write(content)
  
# Closing the opened file
file.close()


# Open a file with access mode 'a'
file_object = open('pythonfile.txt', 'a')
# Append 'hello' at the end of file
file_object.write('\n hello')
# Close the file
file_object.close()
# Open a file with access mode 'a'
file_object = open('pythonfile.txt', 'a')
# Append 'hello' at the end of file
file_object.write('\n hello')
# Close the file
file_object.close()

import os
os.remove("sample.txt")
