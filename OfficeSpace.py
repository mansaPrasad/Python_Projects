#  File: OfficeSpace.py

#  Description: Identifying employee requested office spaces within a buildings parameter

#  Student Name: Mansa Prasad

#  Student UT EID: mp38229

#  Partner Name: Joyce Adekunle

#  Partner UT EID: jma5293

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 02/11/21

#  Date Last Modified: 02/24/21


import sys
import math


# Self made function to find total area of a space with two int values.
def total_space(tot):

    width = int(tot[0])
    height = int(tot[1])
    tot_area = width * height
    return tot_area


# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area(rect):

    x = int(rect[2]) - int(rect[0])
    y = int(rect[3]) - int(rect[1])
    tot_area = x * y
    return tot_area


# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap(rect1, rect2):

    # setting up the overlapping points
    bx = max(rect1[0], rect2[0])
    by = max(rect1[1], rect2[1])
    tx = min(rect1[2], rect2[2])
    ty = min(rect1[3], rect2[3])

    # if statement to see if the rectangles are truly overlapping
    if bx > tx or by > ty:
        return 0, 0, 0, 0
    else:
        return bx, by, tx, ty


# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated
#         space in the office
def unallocated_space(bldg):

    unallocated = 0

    for j in range(len(bldg)):
        for i in range(len(bldg[j])):
            if bldg[j][i] == 0:
                unallocated += 1
    return unallocated


# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested
#         space in the office
def contested_space(bldg):

    contested = 0

    for j in range(len(bldg)):
        for i in range(len(bldg[j])):
            if bldg[j][i] > 1:
                contested += 1
    return contested


# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested
#         space in the office that the employee gets
def uncontested_space(bldg, rect):

    uncontested = 0
    # assigning variables to x, y points
    x1 = rect[0]
    y1 = rect[1]
    x2 = rect[2]
    y2 = rect[3]

    # counting the uncontested space of that requested space
    for i in range(x1, x2):
        for j in range(y1, y2):
            if bldg[i][j] == 1:
                uncontested += 1
    return uncontested


# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space(office, cubicles):

    # using the points we would find the height and the width to be the range in the 2d list
    width = int(office[2])
    height = int(office[3])
    bldg_space = [[0 for i in range(height)] for j in range(width)]

    # iterating through the 2D list to add 1 for each requested space
    for index in range(len(cubicles)):
        x1 = cubicles[index][0]
        y1 = cubicles[index][1]
        x2 = cubicles[index][2]
        y2 = cubicles[index][3]
        for i in range(x1, x2):
            for j in range(y1, y2):
                bldg_space[i][j] += 1
    return bldg_space


def main():
    # read the data
    # get the total office space
    data = sys.stdin.readline().split()
    total = total_space(data)
    print('Total', total)

    emp_num = int(sys.stdin.readline())

    # cubicles is list of tuples for all employee requests
    # create for loop to add each request
    office = (0, 0, int(data[0]), int(data[1]))
    cubicles = []
    name_lst = []
    for line in sys.stdin:
        r = line.split()
        name_lst.append(r[0])
        cubicles.append((int(r[1]), int(r[2]), int(r[3]), int(r[4])))

    request = request_space(office, cubicles)

    # compute the total unallocated space
    un = unallocated_space(request)
    print('Unallocated', un)

    # compute the total contested space
    c = contested_space(request)
    print('Contested', c)

    # list of each employee and their office space
    # use a for loop for each element of name_lst
    for i in range(len(name_lst)):
        unc = uncontested_space(request, cubicles[i])
        print(name_lst[i], unc)


if __name__ == "__main__":
    main()
