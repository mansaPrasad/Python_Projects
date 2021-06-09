#  File: Hull.py

#  Description: Inputting a set of points on a x-y plane which returns a list of point objects
#               that define the outer most vertices of the convex hull in a clockwise order.

#  Student Name: Mansa Prasad

#  Student UT EID: mp38229

#  Partner Name: Joyce Adekunle

#  Partner UT EID: jma5293

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 02/26/21

#  Date Last Modified: 02/28/21

import math
import sys


class Point(object):
    # constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get the distance to another Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # string representation of a Point
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # equality tests of two Points
    def __eq__(self, other):
        tol = 1.0e-8
        return (abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol)

    def __ne__(self, other):
        tol = 1.0e-8
        return (abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol)

    def __lt__(self, other):
        tol = 1.0e-8
        if abs(self.x - other.x) < tol:
            if abs(self.y - other.y) < tol:
                return False
            else:
                return self.y < other.y
        return self.x < other.x

    def __le__(self, other):
        tol = 1.0e-8
        if abs(self.x - other.x) < tol:
            if abs(self.y - other.y) < tol:
                return True
            else:
                return self.y <= other.y
        return self.x <= other.x

    def __gt__(self, other):
        tol = 1.0e-8
        if abs(self.x - other.x) < tol:
            if abs(self.y - other.y) < tol:
                return False
            else:
                return self.y > other.y
        return self.x > other.x

    def __ge__(self, other):
        tol = 1.0e-8
        if abs(self.x - other.x) < tol:
            if abs(self.y - other.y) < tol:
                return True
            else:
                return self.y >= other.y
        return self.x >= other.x


# order in the det helper function matters

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det(p, q, r):
    orient = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    return orient


# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull(sorted_points):
    upper_hull = []
    lower_hull = []

    upper_hull.append(sorted_points[0])
    upper_hull.append(sorted_points[1])

    for i in range(2, len(sorted_points)):
        upper_hull.append(sorted_points[i])
        while len(upper_hull) >= 3 and det(upper_hull[-1], upper_hull[-2], upper_hull[-3]) >= 0:
            # remove the middle value
            upper_hull.pop(-2)

    lower_hull.append(sorted_points[-1])
    lower_hull.append(sorted_points[-2])

    # go counter clockwise
    for i in range(len(sorted_points) - 3, -1, -1):
        lower_hull.append(sorted_points[i])
        while len(lower_hull) >= 3 and det(lower_hull[-1], lower_hull[-2], lower_hull[-3]) >= 0:
            # remove the middle value
            lower_hull.pop(-2)
    lower_hull.pop(0)
    lower_hull.pop(-1)

    # merge the two lists into convex hull
    for x in lower_hull:
        upper_hull.append(x)

    return upper_hull


# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly(convex_poly):
    # one for loop because it's n by 2
    det = 0
    for i in range(len(convex_poly)):
        # using the coordinate vertices to compute the determinant
        if len(convex_poly) - 1 > i:
            det += convex_poly[i].x * convex_poly[i + 1].y - convex_poly[i].y * convex_poly[i + 1].x
        # finding out of range coordinates of x_n and y_n
        else:
            det += convex_poly[-1].x * convex_poly[0].y - convex_poly[-1].y * convex_poly[0].x
    area = 1 / 2 * abs(det)
    return area


def main():
    # create an empty list of Point objects
    points_list = []

    # read number of points
    line = sys.stdin.readline()
    line = line.strip()
    num_points = int(line)

    # read data from standard input
    for i in range(num_points):
        line = sys.stdin.readline()
        line = line.strip()
        line = line.split()
        x = int(line[0])
        y = int(line[1])
        points_list.append(Point(x, y))

    # sort the list according to x-coordinates
    sorted_points = sorted(points_list)
    new_list = convex_hull(sorted_points)

    # get the convex hull
    print('Convex Hull')

    # print your results to standard output

    # print the convex hull
    for i in new_list:
        print(i)

    # get the area of the convex hull
    # print the area of the convex hull
    tot_area = area_poly(new_list)
    print("\nArea of Convex Hull =", tot_area)


if __name__ == "__main__":
    main()
