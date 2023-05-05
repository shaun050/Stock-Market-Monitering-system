object= input("enter the object:")
if object=="square":
    side= int(input("enter side of square:"))
    area_of_square= side*side
    print("Area of square:",area_of_square)

elif object=="rectangle":
    length= int(input("enter length of rectangle:"))
    height= int(input("enter height of rectangle:"))
    area_of_rectangle= length*height
    print("Area of rectangle:",area_of_rectangle)
elif object=="triangle":
    base= int(input("enter base of rectangle:"))
    height_of_triangle= int(input("enter height of rectangle:"))
    area_of_triangle= (base*height_of_triangle)/2
    print("Area of triangle:",area_of_triangle)
else:
    print("Invalid object entered.")