import math

# Functions for area and volume of shapes

def circle_area(radius):
    area = math.pi * radius * radius
    return area

def square_area(a):
    area=a*a
    return area

def rectangle_area(a,b):
    area=a*b
    return area

def triangle_area(a,b):
    area=a*b/2
    return area

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius * radius
    return volume

def cylinder_volume(radius, height):
    volume = math.pi * radius *radius*height
    return volume

def cone_volume(radius, height):
    volume = (1/3) * math.pi * radius *radius *height
    return volume

def cube_surface_area(side):
    surface_area = 6 * side *side
    return surface_area

def cube_volume(side):
    volume = side *side*side
    return volume

def rectangular_prism_surface_area(length, width, height):
    surface_area = 2 * (length * width + length * height + width * height)
    return surface_area

def cubiod_volume(length, width, height):
    volume = length * width * height
    return volume


x=input("Enter area for calculating area and enter volume for calculating volume ")
if x=="area":
  print("1.square,2.rectangle,3.circle.4.triangle,5.cube")
  ref=input("enter reference number of shape: ")
  if ref=="1":
    s=float(input("enter square side: "))
    print(square_area(s))
  elif ref=="2":
    l,b=float(input("enter length of rectangle: ")),float(input("enter breadth: "))
    print(rectangle_area(l,b))
  elif ref=="3":
    r=float(input("enter radius of circle: "))
    print(circle_area(r))
  elif ref=="4":
    base,h=float(input("enter base length of triangle: ")),float(input("enter height: "))
    print(triangle_area(b,h))
  elif ref=="5":
    side=float(input("enter side of cube: "))
    print(cube_surface_area(side))
  else:
    print("invalid choice, please enter valid reference number")
    

elif x=="volume":
   print("1.cube,2.cubiod,3.sphere,4.cone,5.cylinder")
   ref=input("enter reference number of the shape: ")
   if ref=="1":
    side=float(input("enter side of cube: "))
    print(cube_volume(side))
   elif ref=="2":
    length,width,height=float(input("enter length of cubiod: ")),float(input("enter width: ")),float(input("enter height: "))
    print(cubiod_volume(length, width, height))
   elif ref=="3":
    radius=float(input("enter radius of sphere: "))
    print(sphere_volume(radius))
   elif ref=="4":
    rad,hei=float(input("enter radius of cone: ")),float(input("enter height of cone: "))
    print(cone_volume(rad, hei))
   elif ref=="5":
    r,h=float(input("enter radius of cylinder: ")),float(input("enter height of cylinder: "))
    print(cylinder_volume(r,h))
   else:
    print("invalid choice, Please enter valid reference number")
    
else:
  print("invalid choice")