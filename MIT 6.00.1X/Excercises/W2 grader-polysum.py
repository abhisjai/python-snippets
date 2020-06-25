# Source: https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2020/courseware/
# Problem: Write a function called polysum that takes 2 arguments, n and s. 
# This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.
# A regular polygon has n number of sides. Each side has length s.
# The area of a regular polygon is: 0.25∗𝑛∗𝑠2𝑡𝑎𝑛(𝜋/𝑛)
# The perimeter of a polygon is: length of the boundary of the polygon
# @author: abhisjai1
# @date: 2020-06-20

from math import pi, tan

def polysum(n, s):
    ''' 
        input: takes 2 integers n and s  
        returns sum of area and square of the perimeter
    '''

    # Calculate are of a Polygon using a standard formula
    polygon_area = (0.25 * n * s**2) / tan(pi/n)
    
    # Calculate perimeter of polygon using a standard formula
    polygon_length = n * s

    # return the sum of area and square of the perimeter rounded up to 4 decimal places
    return round((polygon_area + polygon_length ** 2), 4)

# a simple test case for developed function
print(polysum(93, 44))