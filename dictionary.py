# Dictionary Demo Project
people_demo = {
    "Max": {"Name":"Max","Age": 28, "Work":"Developer"},
    "Emma": {"Name":"Emma", "Age": 21, "Work":"Professor"},
    "Noah": {"Name": "Noah", "Age": 35, "Work": "Advanced Developer"}
}
def start_system ():
    print("Welcome to the Dictionary Demo Project")
terminal=input("Write a Name(Max,Emma or Noah)").title()
if terminal in people_demo:
    identify=people_demo[terminal]
    print(f"The name is {identify["Name"]}")
    print(f"The age is {identify["Age"]}")
    print(f"The work is {identify["Work"]}")
else:
    print("User not founded")
