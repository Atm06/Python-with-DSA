"""
Q2. Given three angles of a triangle, determine whether it is an acute,
obtuse, or right-angled triangle.
"""

# given three angles:

angle1_value = 60
angle2_value = 60
angle3_value = 60

if angle1_value < 90 and angle2_value < 90 and angle3_value < 90:
    print("Acute")
elif angle1_value > 90 or angle2_value > 90 or angle3_value > 90:
    print("Obtuse")
elif angle1_value == 90 or angle2_value == 90 or angle3_value == 90:
    print("Equilateral")
else:
    print("Invalid")
