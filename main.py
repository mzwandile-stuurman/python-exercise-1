""" Code to calculate circle specifics
    using the radius """
# The radius from a user
radius = eval(input("please enter the radius of a circle: "))
_pi = 3.14
area = (radius**2)*_pi # the formula for area
print("area of the circle is:", area)

diameter = 2*radius # Diameter of the circle

print("the diameter of this circle is:", diameter)

circumfurance = 2*(_pi*radius)

print("the circumfurance of this circle is:", circumfurance)

