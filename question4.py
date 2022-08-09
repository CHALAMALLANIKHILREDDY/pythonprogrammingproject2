import math
def roots(a,b,c):
    d = b*b-(4*a*c)
    sqr_d = (d)**0.5
    if d > 0:
        print("The roots are real and different")
        print((-b+sqr_d)/(2*a))
        print((-b - sqr_d) / (2 * a))
    elif d == 0:
        print("The roots are real and equal")
        print(-b/(2*a))
    else:
        print("the roots are complex")
        print(- b / (2 * a), " + i", sqr_d)
        print(- b / (2 * a), " - i", sqr_d)
    return 0
a = int(input("enter the quotient of second_order term:"))
b = int(input("enter the quotient of first_order term:"))
c = int(input("enter the quotient of constant term:"))
if a == 0:
    print("You have entered wrong quadratic equation")
else:
    roots(a,b,c)