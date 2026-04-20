# Datetime Libary Project
from datetime import timedelta,datetime
def timing():
    answer = input("Write Only The Number: 1 Now the actual day 2 Know what day is it in 200 days")
    if answer == "1":
        actually=datetime.now()
        print(f"The actual day is {actually.strftime("%d/%m/%Y")}")

    elif answer == "2":
       now_time=datetime.now()
       time_future=timedelta(days=200)
       in_time= time_future + now_time
       print(f"In 200 days will be {in_time.strftime("%d/%m/%Y")}")
timing()
