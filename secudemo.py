# Security Demo Project
sequence=["John","Ana","Liam"]
def welcome():
 print("Welcome to the Security Demo Project")
System_On = True
biometric=input("Write a name the names registered are John,Ana and Liam")
if biometric in sequence:
        print("Person autenticaded")
else:
        print("Person didn't exsist")
