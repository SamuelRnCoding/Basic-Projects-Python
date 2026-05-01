# Visualizer 1.0 Program
import os
import time
document="document_file.txt"
def filling():
    time.sleep(5)
print("Welcome to Visualizer 1.0 Program")
answer=input("1 Write the file 2 Read the File 3 Add 2 more lines to the file 4 Exit(Only write the number)")
if answer == "1":
    print("The program is loading for you.....")
    time.sleep(3)
    with open(document,'w') as file:
        file.write("Document File\n")
        file.write("GitHub is incredible\n")
        file.write("Python Project\n")
        print(f"File {document} has been created successfully")
elif answer == "2":
 try:
    print("The file is loading,please wait a while....")
    time.sleep(3)
    with open(document,'r') as file:
     document_open=file.read()
    print(document_open)
 except FileNotFoundError:
    print("Error 1(The File don't exsists)")
elif answer == "3":
    print("Adding 2 lines more....")
    time.sleep(3)
    with open(document,'a') as file:
        file.write("Support this project\n")
        file.write("This will be much helpful\n")
        print("Lines added successfully")
elif answer == "4":
    print("Thanks for use the program")
else:
    print("Error 2(Invalid Option,Only write the number)")


filling()
