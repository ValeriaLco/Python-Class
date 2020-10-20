# quadrant.py

# This programs tells you the the quadrant your angle is located given certain amount of degrees or if the angle
# degree falls on an axis.

# Written by Valeria Lucio
# a01411381@itesm.mx

# Date: August 24th 2019
# Last revision: August 24th 2019

# I first ask the user for the degrees.
angle = int(input())

#Then the program verfies that the number of degrees is within the Cartesian plane.
if angle < 0 or angle > 360:
    print('OUT OF BOUNDS')
# If the number is valid, the program determines its position.
else:
    if (angle > 0) and (angle < 90):
        print('QUADRANT 1')
    if (angle > 90) and (angle < 180):
        print('QUADRANT 2')
    if (angle > 180) and (angle < 270):
        print('QUADRANT 3')
    if (angle > 270) and (angle < 360):
        print('QUADRANT 4')
        
    else:
        if (angle == 0) or (angle == 90) or (angle == 180) or (angle == 270) or (angle == 360):
            print('AXIS')