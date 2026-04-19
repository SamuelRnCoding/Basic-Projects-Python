#Time Library Project
import time
def time_data():
  answer=input("Hi welcome what option you're going to select: 1 Do a reaction test 2 Look the hour 3 Look the time with a format Only Write the number")
  if answer == "1":
     start=time.time()
     input("Press enter the fastest")
     finish=time.time()
     total=finish - start
     print(f"Your reaction time is {total:.2f}")
  elif answer == "2":
     print(f"The actual hour is {time.ctime()}")
  elif answer == "3":
     format=time.strftime("%d/%m/%y")
     print(f"The time is {format}")
time_data()
