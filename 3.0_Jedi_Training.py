# Sign your name:Zachary Blum
# In all the short programs below, do a good job communicating with your end user!


# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
name = input("what is your name")
print("Hello", name)
# 2. Write a program where a user enters a base and height and you print the area of a triangle.
bass = float(input("What is the bass of the triangle"))
height = float(input("what is the height of the triangle"))
area = bass*height/2
print("The area of the triangle is", area)
# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
radius = float(input("what is the radius of the circle"))
circumference = radius**2*3.14
print("The circumfrance of the circle is", circumference)
# 4. Ask a user for an integer and then print the square root.
integer = int(input("what is the integer"))
sq= integer**0.5
print("the square root is", sq)
# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma.
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
mass = float(input("What is the mass"))
acceleration = float(input("What is the acceleration"))
Force = mass*acceleration
print("May the force of",Force, "be with you")
print("get it")


