#Display the distance between two points

x1, y1 = eval(input("Enter x1 and y1 for Point 1: "))

x2, y2 = eval(input("Enter x2 and y2 for Point 2: "))

distance = ((x1 - x2) * (x1 - x2) + (y1- y2) *(y1 - y2)) ** 0.5

print("The distance between 2 points is: ", distance)