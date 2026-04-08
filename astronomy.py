def welcome():
    return "Welcome to the Astronomy Data Project"
System_On = True
while System_On == True:
    answer = input("What do you wanna to know? A Distance of the moon B Sun Distance C. Exit Please write the letter")

    if answer == "A":
        print("The distance of the moon is 384.000 km") 

    elif answer == "B":
        print("The distance of the sun is 149.600.000 km")

    elif answer == "C":
            print("Thanks for visit the Astronomy Data Project")
            System_On = False
    else:  print("Please write the letter A,B or C please")
