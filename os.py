import os
from datetime import datetime

def starting():
    answer = input("Do you want to know where you are? (Yes, No): ")
    clean_answer = answer.title()
    
    if clean_answer == "Yes":
        print(f"You are in {os.getcwd()}")
    
    elif clean_answer == "No":
        answer2 = input("Do you want to create a carpet named System? (Yes, No): ")
        cleaned = answer2.title()
        
        if cleaned == "Yes":
            actually = datetime.now()
            # Seguridad: solo crear si no existe
            if not os.path.exists("System"):
                os.mkdir("System")
                print(f"System Carpet Created at {actually}")
            else:
                print("The carpet 'System' already exists.")
        else:
            print("Invalid Option, only write Yes or No")

starting()

