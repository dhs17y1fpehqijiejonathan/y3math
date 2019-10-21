#Finding Equation of Perpendicular Bisector of Line connecting two points

x_coordinate_of_A = float('''insert x coordinate of first point''')
y_coordinate_of_A = float('''insert y coordinate of first point''')

x_coordinate_of_B = float('''insert x coordinate of second point''')
y_coordinate_of_B = float('''insert y coordinate of first point''')

Gradient_AB = (y_coordinate_of_A-y_coordinate_of_B)/(x_coordinate_of_A-x_coordinate_of_B)
Gradient_Perpendicular = ('''insert product of any two perpendicular lines'''/Gradient_AB)

#Note: Perpendicular bisector will pass through midpoint of AB
x_coordinate_of_Midpoint = (x_coordinate_of_A + x_coordinate_of_B)/2
y_coordinate_of_Midpoint = (y_coordinate_of_A + y_coordinate_of_B)/2

#Note: This line substitutes y= y of midpoint, x= x of midpoint and m=Gradient_perpendicular into y=mx+c, then makes y-intercept the subject
c = y_coordinate_of_Midpoint-Gradient_Perpendicular*x_coordinate_of_Midpoint

print("The equation is y =",Gradient_Perpendicular,"x +",c)
