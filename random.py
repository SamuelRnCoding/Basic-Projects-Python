#Random Library Project
import random
people_list=["John","Ana","Sophie","James"]
def function():
 answer=int(input("What action what do you want to do? 1 Select One 2 Select a group 3 Do a choice with weigths 4 Mix a list 5 Get a Number 6 Get a Code 7 Get a decimal 8 Get a decimal prediction 9 Get a quest with a promedium(Write Only The Number)"))

 if answer == 1:
       result1 = random.choice(people_list)
       print(f"The people selected is {result1}")
 elif answer == 2:
  group=random.sample(people_list,2)
  print(f"The group selected is {group}")
 elif answer == 3:
    weigth=random.choices(people_list, weights=[70,60,72,50])
    print(f"The person selected is {weigth}")
 elif answer == 4:
    mixed=random.shuffle(people_list)
    print(f"The mixed list is {mixed}")
 elif answer == 5:
    number=random.randint(1,100)
    print(f"The number selected is {number}")
 elif answer == 6:
    code=random.randrange(100,200,150)
    print(f"Your code is {code}")
 elif answer == 7:
    decimal=random.random(1.00,20.00)
    print(f"The decimal is {decimal}")
 elif answer == 8:
    prediction=random.uniform(1,100)
    print(f"Your decimal prediction is {prediction}")
 elif answer == 9:
    promedium=random.gauss(1.70)
    print(f"The heigth selected is {promedium}")
 else:
    print("Invalid Option,Only Write the Number,Please start again the project")


function()
