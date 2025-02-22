# Writing a sentence to a text file
with open("NAVE.txt", "w") as fi:
    fi.write("Hi WELCOME TO FILE HANDLING CONCEPTS go back to learning")                 

# Reading the content from the file and printing it
with open("output.txt", "r") as file:
    content = file.read()
    print(content)
