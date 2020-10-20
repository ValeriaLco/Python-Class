# car_averague_speed.py

# This programs shows the average speed given by the travelled distance and the time it
# took to travel such distance.

# Written by Valeria Lucio Rangel
# a01411381@itesm.mx

# Date: August 16th 2019
# Last revision: August 16th 2019

#I ask the user for the travelled distance and the time it took to travel that distance
distance = float(input('Give me the distance travelled: '))
time = float(input('How much time did it took you to travel it? '))

# I compute the average speed dividing distance by time
speed = distance / time

# I show the user the average speed computed using their values
print('Your speed average was', speed, 'km/h')