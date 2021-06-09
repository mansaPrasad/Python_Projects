#  File: Intervals.py

#  Description: Converting a list of intervals into tuples
#				then merging the overlapping intervals and ordering 
#				based on interval size.

#  Student Name: Mansa Prasad

#  Student UT EID: mp38229

#  Partner Name: Joyce Adekunle

#  Partner UT EID: jma5293

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 02/03/2021

#  Date Last Modified: 02/05/2021

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval

import sys


def merge_tuples(tuples_list):
    # Created a sorted variable and a list to store the tuples
    sort = sorted(tuples_list, key=lambda tuple: tuple[0])
    lst = []

    # Used a for loop to index and iterate the list of tuples and merge
    # overlapping values.
    for i in sort:
        if not lst:
            lst.append(i)
        else:
            n = lst[-1]
            if i[0] <= n[1]:
                j = max(n[1], i[1])
                lst[-1] = (n[0], j)
            else:
                lst.append(i)
    return lst


# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval

def sort_by_interval_size(tuples_list):
    # Variable that sorts the tuples according to their size
    sort = sorted(tuples_list, key=lambda tuple: abs(tuple[0] - tuple[1]))
    return sort


def main():
    # open file intervals.in and read the data and create a list of tuples
    l = int(sys.stdin.readline())

    new_lst = []
    for k in range(l):
        a, b = map(int, sys.stdin.readline().split())
        new_lst.append((a, b))

    # merge the list of tuples
    merg = merge_tuples(new_lst)
    print(merg)

    # sort the list of tuples according to the size of the interval
    srt = sort_by_interval_size(merg)
    print(srt)


if __name__ == "__main__":
    main()
