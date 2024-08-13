from math import sqrt

def power(base, exponent):
    if(exponent == 0):
        return 1
    else:
        return base*power(base, exponent-1)
    
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    distance = sqrt(power(x2-x1, 2) + power(y2-y1, 2))
    
    if(distance < 0):
        distance = -1 * distance

    return distance


point1X = float(input("First point' x value: "))
point1Y = float(input("First point' y value: "))

point2X = float(input("Second point' x value: "))
point2Y = float(input("Second point' y value: "))

point3X = float(input("Third point' x value: "))
point3Y = float(input("Third point' y value: "))

points = [
            (point1X, point1Y),
            (point2X, point2Y),
            (point3X, point2Y)
          ]


distances = []

for i in points:
    for j in points:
        if(i == j):
            continue
        distances.append(euclideanDistance(i, j))
        
print(f"minimum distance is {min(distances)}")