print("""1. Circle
2. Square
3. Rectangle
4. Right angled triangle""")
n=int(input("Choose a figure:-"))
if n<5:
    if n==1:
        print("""1. Area of circle
2. Volume of sphere""")
        m=int(input("State your choice of operation:-"))
        if m<3:
            r=float(input("Enter radius of figure:-"))
            if m==1:
                print("Area of circle:-",(22/7)*(r**2))
            elif m==2:
                print("Volume of sphere:-",(4/3)*(22/7)*r**3)
        else:
            print("No operation can be performed since you have chosen a Wrong choice")
    elif n==2:
        print("""1. Area of square
2. Volume of cube""")
        m=int(input("State your choice of operation:-"))
        if m<3:
            a=float(input("Enter side of figure:-"))
            if m==1:
                print("Area of square:-",a**2)
            elif m==2:
                print("Volume of cube:-",a**3)
        else:
            print("No operation can be performed since you have chosen a Wrong choice")
    elif n==3:
        print("""1. Area of rectangle
2. Volume of cuboid""")
        m=int(input("State your choice of operation:-"))
        if m<3:
            l=float(input("Enter length of figure:-"))
            w=float(input("Enter width of figure:-"))
            if m==1:
                print("Area of rectangle:-",l*w)
            elif m==2:
                h=float(input("Enter height of figure:-"))
                print("Volume of cuboid:-",l*w*h)
        else:
            print("No operation can be performed since you have chosen a Wrong choice")
    elif n==4:
        print("""1. Area of triangle
2. Volume of cone formed by this triangle""")
        m=int(input("State your choice of operation:-"))
        if m<3:
            r=float(input("Enter base/radius of figure:-"))
            h=float(input("Enter height of figure:-"))
            if m==1:
                print("Area of triangle:-",0.5*r*h)
            elif m==2:
                print("""1. Revolve along height
2. Revolve along radius""")
                v=int(input("Choose the side to revolve:-"))
                if v<3:
                    if v==1:
                        print("Volume of Cone:-",(1/3)*(22/7)*r*r*h)
                    elif v==2:
                        print("Volume of Cone:-",(1/3)*(22/7)*h*h*r)
                else:
                    print("No operation can be performed since you have chosen a Wrong choice")
        else:
            print("No operation can be performed since you have chosen a Wrong choice")
else:
    print("No operation can be performed since you have chosen a Wrong choice")
