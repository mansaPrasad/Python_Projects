#  File: Geometry.py

#  Description: Object Oriented Programming of 3D geometric shapes

#  Student Name: Mansa Prasad

#  Student UT EID: mp38229

#  Partner Name: Joyce Adekunle

#  Partner UT EID: jma5293

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 02/09/21

#  Date Last Modified: 02/12/21

import math
import sys


class Point(object):
    # constructor with default values
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    # create a string representation of a Point
    # returns a string of the form (x, y, z)
    def __str__(self):
        return '(' + '{:.1f}'.format(self.x) + ', ' + '{:.1f}'.format(self.y) + ', ' + '{:.1f}'.format(self.z) + ')'

    # get distance to another Point object
    # other is a Point object
    # returns the distance as a floating point number
    def distance(self, other):
        return math.hypot(self.x - other.x, self.y - other.y, self.z - other.z)

    # test for equality between two points
    # other is a Point object
    # returns a Boolean
    def __eq__(self, other):
        tol = 1.0e-6
        return (abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol) and (abs(self.z - other.z) < tol)


class Sphere(object):

    # constructor with default values
    def __init__(self, x=0.0, y=0.0, z=0.0, radius=1.0):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.center = Point(x, y, z)
        self.box = []
        self.box.append(Point(self.x + self.radius, self.y + self.radius, self.z + self.radius))
        self.box.append(Point(self.x + self.radius, self.y - self.radius, self.z + self.radius))
        self.box.append(Point(self.x + self.radius, self.y + self.radius, self.z - self.radius))
        self.box.append(Point(self.x + self.radius, self.y - self.radius, self.z - self.radius))
        self.box.append(Point(self.x - self.radius, self.y + self.radius, self.z + self.radius))
        self.box.append(Point(self.x - self.radius, self.y - self.radius, self.z + self.radius))
        self.box.append(Point(self.x - self.radius, self.y + self.radius, self.z - self.radius))
        self.box.append(Point(self.x - self.radius, self.y - self.radius, self.z - self.radius))

    # returns string representation of a Sphere of the form:
    # Center: (x, y, z), Radius: value
    def __str__(self):
        return 'Center: ' + '(' + '{:.1f}'.format(self.x) + ', ' + '{:.1f}'.format(self.y) + ', ' + '{:.1f}'.format(self.z) + ')' + ', ' + 'Radius: ' + '{:.1f}'.format(
            self.radius)

    # compute surface area of Sphere
    # returns a floating point number
    def area(self):
        return 4 * math.pi * (self.radius ** 2)

    # compute volume of a Sphere
    # returns a floating point number
    def volume(self):
        return (4 / 3) * math.pi * (self.radius ** 3)

    # determines if a Point is strictly inside the Sphere
    # p is Point object
    # returns a Boolean
    def is_inside_point(self, p):
        if self.center.distance(p) < self.radius:
            return True
        else:
            return False

    # determine if another Sphere is strictly inside this Sphere
    # other is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, other):
        # find the distance between the two centers and compare it to the distance of the two radii
        difference = self.center.distance(other)
        return (difference + other.radius) < self.radius

    # determine if a Cube is strictly inside this Sphere
    # determine if the eight corners of the Cube are strictly
    # inside the Sphere
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):
        # dist of corner point from center of sphere must be less than the radius
        for i in a_cube.corner_pts:
            if not self.is_inside_point(i):
                return False
        return True

    # determine if a Cylinder is strictly inside this Sphere
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cyl(self, a_cyl):
        for i in a_cyl.prism_pts:
            if not self.is_inside_point(i):
                return False
        return True

    # determine if another Sphere intersects this Sphere
    # other is a Sphere object
    # two spheres intersect if they are not strictly inside
    # or not strictly outside each other
    # returns a Boolean
    def does_intersect_sphere(self, other):
        if self.is_inside_sphere(other):
            return False
        if other.is_inside_sphere(self):
            return False

        # distance is less than the sum of the two radii
        dist = self.center.distance(other.center)
        r = self.radius + other.radius
        if r > dist:
            return False
        else:
            return True

    # determine if a Cube intersects this Sphere
    # the Cube and Sphere intersect if they are not
    # strictly inside or not strictly outside the other
    # a_cube is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, a_cube):
        if self.is_inside_cube(a_cube):
            return False
        for i in a_cube.corner_pts:
            if not self.is_inside_point(i):
                return True

    # return the largest Cube object that is circumscribed
    # by this Sphere
    # all eight corners of the Cube are on the Sphere
    # returns a Cube object
    def circumscribe_cube(self):
        self.cube_side = (2 * self.radius) / math.sqrt(3)
        new_cube = Cube(self.x, self.y, self.z, self.cube_side)
        return new_cube


class Cube(object):
    # Cube is defined by its center (which is a Point object)
    # and side. The faces of the Cube are parallel to x-y, y-z,
    # and x-z planes.
    def __init__(self, x=0.0, y=0.0, z=0.0, side=1.0):
        self.x = x
        self.y = y
        self.z = z
        self.side = side
        self.center = Point(x, y, z)
        self.corner_pts = []
        self.corner_pts.append(Point(self.x + self.side / 2, self.y + self.side / 2, self.z + self.side / 2))
        self.corner_pts.append(Point(self.x - self.side / 2, self.y - self.side / 2, self.z - self.side / 2))
        self.corner_pts.append(Point(self.x + self.side / 2, self.y - self.side / 2, self.z + self.side / 2))
        self.corner_pts.append(Point(self.x + self.side / 2, self.y + self.side / 2, self.z - self.side / 2))
        self.corner_pts.append(Point(self.x + self.side / 2, self.y - self.side / 2, self.z - self.side / 2))
        self.corner_pts.append(Point(self.x - self.side / 2, self.y + self.side / 2, self.z - self.side / 2))
        self.corner_pts.append(Point(self.x - self.side / 2, self.y - self.side / 2, self.z + self.side / 2))
        self.corner_pts.append(Point(self.x - self.side / 2, self.y + self.side / 2, self.z + self.side / 2))

    # string representation of a Cube of the form:
    # Center: (x, y, z), Side: value
    def __str__(self):
        return 'Center: (' + '{:.1f}'.format(self.x) + ', ' + '{:.1f}'.format(self.y) + ', ' + '{:.1f}'.format(
            self.z) + '), Side: ' + '{:.1f}'.format(self.side)

    # compute the total surface area of Cube (all 6 sides)
    # returns a floating point number
    def area(self):
        return 6 * (self.side ** 2)

    # compute volume of a Cube
    # returns a floating point number
    def volume(self):
        return self.side ** 3

    # determines if a Point is strictly inside this Cube
    # p is a point object
    # returns a Boolean
    def is_inside_point(self, p):
        if self.center.distance(p) < self.side / 2:
            return True
        else:
            return False

    # determine if a Sphere is strictly inside this Cube
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        # radius compared to 1/2 cube side
        for i in a_sphere.box:
            if not self.is_inside_point(i):
                return False
        return True

    # determine if another Cube is strictly inside this Cube
    # other is a Cube object
    # returns a Boolean
    def is_inside_cube(self, other):
        for i in other.corner_pts:
            if not self.is_inside_point(i):
                return False
        return True

    # determine if a Cylinder is strictly inside this Cube
    # a_cyl is a Cylinder object
    # returns a Boolean
    def is_inside_cylinder(self, a_cyl):
        for i in a_cyl.prism_pts:
            if not self.is_inside_point(i):
                return False
        return True

        # determine if another Cube intersects this Cube

    # two Cube objects intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cube object
    # returns a Boolean
    def does_intersect_cube(self, other):
        if self.is_inside_cube(other):
            return False
        if other.is_inside_cube(self):
            return True

        # difference of the centers is less than half the 2 sides
        center_dist = self.center.distance(other.center)
        side_dist = self.side / 2 + other.side / 2
        if center_dist > side_dist:
            return False
        else:
            return True

    # determine the volume of intersection if this Cube
    # intersects with another Cube
    # other is a Cube object
    # returns a floating point number
    def intersection_volume(self, other):
        # see if the two volumes intersect
        new_vol = []
        if self.does_intersect_cube(other):
            pass

    # Do math
    # append to new_vol

    # all the corners function, and returns a list of those point objects
    # check to see if those points are in the other cube and other were appended to a new list
    # do this the other way too

    # return the largest Sphere object that is inscribed
    # by this Cube
    # Sphere object is inside the Cube and the faces of the
    # Cube are tangential planes of the Sphere
    # returns a Sphere object
    def inscribe_sphere(self):
        pass


class Cylinder(object):
    # Cylinder is defined by its center (which is a Point object),
    # radius and height. The main axis of the Cylinder is along the
    # z-axis and height is measured along this axis
    def __init__(self, x=0, y=0, z=0, radius=1, height=1):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.height = height
        self.center = Point(x, y, z)
        self.prism_pts = []
        self.prism_pts.append(Point(self.x + self.radius, self.y + self.radius, self.z + self.height / 2))
        self.prism_pts.append(Point(self.x + self.radius, self.y - self.radius, self.z + self.height / 2))
        self.prism_pts.append(Point(self.x + self.radius, self.y + self.radius, self.z - self.height / 2))
        self.prism_pts.append(Point(self.x + self.radius, self.y - self.radius, self.z - self.height / 2))
        self.prism_pts.append(Point(self.x - self.radius, self.y + self.radius, self.z + self.height / 2))
        self.prism_pts.append(Point(self.x - self.radius, self.y - self.radius, self.z + self.height / 2))
        self.prism_pts.append(Point(self.x - self.radius, self.y + self.radius, self.z - self.height / 2))
        self.prism_pts.append(Point(self.x - self.radius, self.y - self.radius, self.z - self.height / 2))

    # returns a string representation of a Cylinder of the form:
    # Center: (x, y, z), Radius: value, Height: value
    def __str__(self):
        return 'Center: (' + '{:.1f}'.format(self.x) + ', ' + '{:.1f}'.format(self.y) + ', ' + '{:.1f}'.format(
            self.z) + '), Radius: ' + '{:.1f}'.format(self.radius) + ', Height: ' + '{:.1f}'.format(self.height)

    # compute surface area of Cylinder
    # returns a floating point number
    def area(self):
        return 2 * math.pi * self.radius * self.height + 2 * math.pi * (self.radius ** 2)

    # compute volume of a Cylinder
    # returns a floating point number
    def volume(self):
        return math.pi * self.radius ** 2 * self.height

        # determine if a Point is strictly inside this Cylinder

    # p is a Point object
    # returns a Boolean
    def is_inside_point(self, p):
        if self.center.distance(p) < self.radius and self.center.distance(p) < self.height:
            return True
        else:
            return False

    # determine if a Sphere is strictly inside this Cylinder
    # a_sphere is a Sphere object
    # returns a Boolean
    def is_inside_sphere(self, a_sphere):
        cyl_center = Point(self.center.x, self.center.y, 0)
        sphere_center = Point(a_sphere.center.x, a_sphere.center.y, 0)
        return cyl_center.distance(sphere_center) + a_sphere.radius < self.radius and (
                    abs(self.center.z - a_sphere.center.z) + a_sphere.radius) < (self.height / 2)

    # determine if a Cube is strictly inside this Cylinder
    # determine if all eight corners of the Cube are inside
    # the Cylinder
    # a_cube is a Cube object
    # returns a Boolean
    def is_inside_cube(self, a_cube):
        for i in a_cube.corner_pts:
            if not self.is_inside_point(i):
                return False
        return True

        # determine if another Cylinder is strictly inside this Cylinder

    # other is Cylinder object
    # returns a Boolean
    def is_inside_cylinder(self, other):
        for i in other.prism_pts:
            if not self.is_inside_point(i):
                return False
        return True

        # determine if another Cylinder intersects this Cylinder

    # two Cylinder object intersect if they are not strictly
    # inside and not strictly outside each other
    # other is a Cylinder object
    # returns a Boolean
    def does_intersect_cylinder(self, other):
        pass


def main():
    # read data from standard input
    data = sys.stdin.readline().strip().split()

    # read the coordinates of the first Point
    # create a Point object
    p = Point(float(data[0]), float(data[1]), float(data[2]))

    # read the coordinates of the second Point q
    # create a Point object
    data1 = sys.stdin.readline().strip().split()
    q = Point(float(data1[0]), float(data1[1]), float(data1[2]))

    # read the coordinates of the center and radius of sphereA
    # create a Sphere object
    data2 = sys.stdin.readline().strip().split()
    sphereA = Sphere(float(data2[0]), float(data2[1]), float(data2[2]), float(data2[3]))

    # read the coordinates of the center and radius of sphereB
    # create a Sphere object
    data3 = sys.stdin.readline().strip().split()
    sphereB = Sphere(float(data3[0]), float(data3[1]), float(data3[2]), float(data3[3]))

    # read the coordinates of the center and side of cubeA
    # create a Cube object
    data4 = sys.stdin.readline().strip().split()
    cubeA = Cube(float(data4[0]), float(data4[1]), float(data4[2]), float(data4[3]))

    # read the coordinates of the center and side of cubeB
    # create a Cube object
    data5 = sys.stdin.readline().strip().split()
    cubeB = Cube(float(data5[0]), float(data5[1]), float(data5[2]), float(data5[3]))

    # read the coordinates of the center, radius and height of cylA

    # create a Cylinder object
    data6 = sys.stdin.readline().strip().split()
    cylA = Cylinder(float(data6[0]), float(data6[1]), float(data6[2]), float(data6[3]), float(data6[4]))

    # read the coordinates of the center, radius and height of cylB
    # create a Cylinder object
    data7 = sys.stdin.readline().strip().split()
    cylA = Cylinder(float(data7[0]), float(data7[1]), float(data7[2]), float(data7[3]), float(data7[4]))

    # print if the distance of p from the origin is greater
    # than the distance of q from the origin
    origin = Point(0, 0, 0)
    dist_p = p.distance(origin)
    dist_q = q.distance(origin)
    if dist_p > dist_q:
        print('Distance of Point p from the origin p is greater than the distance of Point q from the origin')
    else:
        print('Distance of Point p from the origin is not greater than the distance of Point q from the origin')

    # print if Point p is inside sphereA
    if sphereA.is_inside_point(p) == True:
        print('Point p is in sphereA')
    else:
        print('Point p is not in sphereA')

    # print if sphereB is inside sphereA
    if sphereA.is_inside_sphere(sphereB) == True:
        print('sphereB is inside sphereA')
    else:
        print('sphereB is not inside sphereA')

    # print if cubeA is inside sphereA
    if sphereA.is_inside_cube(cubeA) == True:
        print('cubeA is inside sphereA')
    else:
        print('cubeA is not inside sphereA')

    # print if cylA is inside sphereA
    if sphereA.is_inside_cyl(cylA) == True:
        print('cylA is inside sphereA')
    else:
        print('cylA is not inside sphereA')

    # print if sphereA intersects with sphereB
    if sphereA.does_intersect_sphere(sphereB) == True:
        print('sphereA does intersect sphereB')
    else:
        print('sphereA does not intersect sphereB')

    # print if cubeB intersects with sphereB
    if sphereB.does_intersect_cube(cubeB) == True:
        print('cubeB does intersect sphereB')
    else:
        print('cubeB does not intersect sphereB')

    # print if the volume of the largest Cube that is circumscribed
    # by sphereA is greater than the volume of cylA


    # print if Point p is inside cubeA
    if cubeA.is_inside_point(p) == True:
        print('Point p is inside sphereA')
    else:
        print('Point p is not inside sphereA')

    # print if sphereA is inside cubeA
    if cubeA.is_inside_sphere(sphereA) == True:
        print('sphereA is inside cubeA')
    else:
        print('sphereA is not inside cubeA')

    # print if cubeB is inside cubeA
    if cubeA.is_inside_cube(cubeB) == True:
        print('cubeB is inside cubeA')
    else:
        print('cubeB is not inside cubeA')

    # print if cylA is inside cubeA
    if cubeA.is_inside_cylinder(cylA) == True:
        print('cylA is inside cubeA')
    else:
        print('cylA is not inside cubeA')

    # print if cubeA intersects with cubeB
    if cubeA.does_intersect_cube(cubeB) == True:
        print('cubeA does intersect cubeB')
    else:
        print('cubeA does not intersect cubeB')

    # print if the intersection volume of cubeA and cubeB
    # is greater than the volume of sphereA
    cube_int = cubeA.intersection_volume(cubeB)
    if cube_int > volume(sphereA):
        print('Intersection volume of cubeA and cubeB is  greater than the volume of sphereA')
    else:
        print('Intersection volume of cubeA and cubeB is not greater than the volume of sphereA')

    # print if the surface area of the largest Sphere object inscribed
    # by cubeA is greater than the surface area of cylA
    sphere_cube = inscribe_sphere(cubeA)

    # print if Point p is inside cylA
    if cylA.is_inside_point(p) == True:
        print('Point p is inside sphereA')
    else:
        print('Point p is not inside sphereA')

    # print if sphereA is inside cylA
    if cylA.is_inside_sphere(sphereA) == True:
        print('sphereA is inside cylA')
    else:
        print('sphereA is not inside cylA')

    # print if cubeA is inside cylA
    if cylA.is_inside_cube(cubeA) == True:
        print('cubeA is inside cylA')
    else:
        print('cubeA is not inside cylA')

    # print if cylB is inside cylA
    if cylA.is_inside_cylinder(cylB) == True:
        print('cylB is inside cylA')
    else:
        print('cylB is not inside cylA')

    # print if cylB intersects with cylA
    if cylA.does_intersect_cylinder(cylB) == True:
        print('cylB does intersect cylA')
    else:
        print('cylB does not intersect cylA')

if __name__ == "__main__":
    main()
