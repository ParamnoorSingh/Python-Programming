# WAP to calculate area of triangle and check if it is right angled or not

def right_angle(l):
    l.sort()
    h = l[-1]
    p = l[1]
    b = l[0]
    if (h**2) == ((p**2) + (b**2)):
        s = (h+p+b)/2
        area = (s*(s-h)*(s-p)*(s-b))**(1/2)
        print("It is a right angled triangle")
        print("area of triangle is: ",area)
    else:
        s = (h+p+b)/2
        area = (s*(s-h)*(s-p)*(s-b))**(1/2)
        print("It is not a right angled triangle")
        print("area of triangle is: ",area)

l = [3,4,5]
right_angle(l)