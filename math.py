# Math Library Project
import math
def math_system():
    answer=input("1 Pi Value 2 e Value 3 Potence of 16 to 2 and square root 4 Round 6.4  4 Trigonometry with 65 grades 5 18 factorial 6 MCD of 64,32 7 Absolut Value of -58(Write Only The Number)")
    if answer == 1:
        print(f"The pi value is {math.pi}")
    elif answer == 2:
        print(f"The e value is {math.e}")
    elif answer == 3:
        number = 16
        square = math.sqrt(number)
        potence = math.pow(number, 2)
        print(f"The potence of 16 to 2 is {potence} and the square root of 16 is {square}")
    elif answer == 4:
        grades = 65
        radians = math.radians(grades)
        sen = math.sin(radians)
        cosen = math.cos(radians)
        print(f"Grades {grades}, sen {sen:.2f} and the cosen {cosen:.2f}")
    elif answer == 5:
        print(f"18 Factorial is {math.factorial(18)}")
    elif answer == 6:
        print(f"The MCD of 64,32 is {math.gcd(64, 32)}")
    elif answer == 7:
        print(f"The absolute value of -58 is {math.fabs(-58)}")
    else:
        print("Invalid option.")

math_system()
