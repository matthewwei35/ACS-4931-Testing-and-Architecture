# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.

import math

# Calculate the distance between the two circle
def calculate_distance_btwn_two_circle(xc1, yc1, xc2, yc2):
  return math.sqrt((xc1-xc2)**2 + (yc1 - yc2)**2)

distance = calculate_distance_btwn_two_circle(4, 4.25, 53, -5.35)
print('distance:', distance)

# calcualte the length of vector AB vector which is a vector between A and B points.
def calculate_length_ab_vector(xa, ya, xb, yb):
  return math.sqrt((xa-xb)*(xa-xb) + (ya-yb)*(ya-yb))

length = calculate_length_ab_vector(-36, 97, .34, .91)
print('length:', length)
