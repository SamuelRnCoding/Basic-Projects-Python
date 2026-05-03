import time
import pandas as pd
import csv
document="document.txt"
sheet="workspacing.csv"
def programme():
    time.sleep(4)
    print("Visualizer 2.0 Loading Program...")
    time.sleep(2)
    option=input("Select one option: 1 Write a File 2 Read the file 3 Add 2 lines to the file 4 Write a Sheet 5 Read the Sheet")
    if option == "1":
        print("Writing Document.txt")
        time.sleep(3)
        with open(document,'w') as file:
            file.write("Document File\n")
            file.write("Github is incredible\n")
            print(f"The file {document} has been created successfully")
    elif option == "2":
        try:
            with open(document,'r') as file:
                reader=file.read()
                print(reader)
        except FileNotFoundError:
            print("Error 1(File don't exsists)")
    elif option == "3":
        print("Adding 2 lines")
        time.sleep(2)
        with open(document,'a') as file:
            file.write("Visualizer 2.0\n")
            file.write("Offitial Version\n")
            print("Lines added")
    elif option == "4":
        print("Creating sheet.csv")
        time.sleep(2)
        with open(sheet,'w',newline='',encoding='utf=8') as file:
            writer=csv.writer(file)
            writer.writerow(["Product","Price"])
            writer.writerow(["Apples",2.99])
            writer.writerow(["Milk",6.20])
            print(f"The file {sheet} has been created succesfully")
    elif option == "5":
        print("Loading Sheet")
        time.sleep(2)
        st_view=pd.read_csv(sheet)
        print(st_view)

programme()
