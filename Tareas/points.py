from math import sqrt
def distance_between(x1, y1, x2, y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def where_in_circle(distance, radius):
    if (distance > radius):
        return('OUTSIDE')
    elif (distance < radius):
        return('INSIDE')
    else:
        return('PERIMETER')

def quadrant(center_x, center_y, point_x, point_y):
    if (center_x == point_x) and (center_y == point_y):
        return('CENTER')
    elif (center_x == point_x) or (center_y == point_y):
        return('AXIS')
    elif (center_x < point_x) and (center_y < point_y):
        return('Q1')
    elif (center_x > point_x) and (center_y < point_y):
        return('Q2')
    elif (center_x > point_x) and (center_y > point_y):
        return('Q3')
    else:
        return('Q4')

center_x = float(input())
center_y = float(input())
radius = abs(float(input()))
point_x = float(input())
point_y = float(input())

if radius == 0:
    print('ERROR')
else:
    distance = distance_between(center_x, center_y, point_x, point_y)
    label = where_in_circle(distance, radius)
    location = quadrant(center_x, center_y, point_x, point_y)
    print(distance)
    print(label)
    print(location)