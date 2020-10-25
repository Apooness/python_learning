from math import sin,cos,tan,radians

msg = """Welcome TO Trigonometrics Functions
These Functions Are:
1- Sin 
2- Cos 
3- Tan
4- Cot 
"""
print(msg)
while True:
    choice = input("What is your choice(quit for 'q'): ")
    if choice == "q":
        print("Exiting the Program...")
        break
    elif choice == "1":
        degree = int(input("Degree for sine: "))
        radian = radians(degree)
        result = sin(radian)
        print(result)
    elif choice == "2":
        degree = int(input("Degree for cosine: "))
        radian = radians(degree)
        result = cos(radian)
        print(result)
    elif choice == "3":
        degree = int(input("Degree for tangent: "))
        radian = radians(degree)
        result = tan(radian)
        print(result)
    elif choice == "4":
        degree = int(input("Degree for cotangent: "))
        radian = radians(degree)
        result = tan(radian)
        print(1/result)
    else:
        print("Wrong Choice")