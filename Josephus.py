#  File: Josephus.py

#  Description: Solving Josephus's Problem using circular linked lists

#  Student Name: Mansa Prasad

#  Student UT EID: mp38229

#  Partner Name: Joyce Adekunle

#  Partner UT EID: jma5293

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 04/11/21

#  Date Last Modified: 04/12/21

import sys


class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None

    # Insert an element (value) in the list
    def insert(self, data):
        new_link = Link(data)
        # if linked list is empty, then first node
        # becomes only node in linked list
        if self.first is None:
            self.first = new_link
            new_link.next = new_link
        else:
            current = self.first
            # adds elements to list, while making the
            # last node loop over back to the first node
            while current.next is not self.first:
                current = current.next
            current.next = new_link
            new_link.next = self.first

    # Find the Link with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        current = self.first
        # if current node is data wanted
        # it returns that current node
        if current.data == data:
            return current
        # else it iterates and looks for the
        # data that is wanted
        while current.data is not data:
            if current.data == data:
                return current
            elif current.next == self.first:
                return None
            current = current.next

    # Delete a Link with a given data (value) and return the Link
    # or return None if the data is not there
    def delete(self, data):
        previous = self.first
        current = self.first
        # checks if list has any node
        if current is None:
            return None
        # check if list has a single node, and if it does
        # it is deleted
        if current.data == data and current.next == self.first:
            self.first.next = None
            self.first = None
            return current
        # add a while loop to find the current previous
        while current.next != self.first:
            previous = current
            current = current.next
        previous = current
        current = self.first
        # while current is not equal to data, it 'iterates' through the data resetting current
        while current.data != data:
            # checks if next is equal to first
            if current.next == self.first:
                return None
            else:
                previous = current
                current = current.next
        # if current is found in first node
        if current == self.first:
            self.first = self.first.next
            previous.next = self.first
        else:
            previous.next = current.next

        return current

    # Delete the nth Link starting from the Link start
    # Return the data of the deleted Link AND return the
    # next Link after the deleted Link in that order
    def delete_after(self, start, n):
        new_link = Link(start)
        # current node starts at start
        current = start
        # calling deleted function to delete current data
        # and return deleted data and next link in circular list
        if current is None:
            return None, None
        for i in range(n - 1):
            current = current.next
        new_link = current.next
        deleted_link = self.delete(current.data)
        if deleted_link is None:
            return None, None
        return deleted_link.data, new_link

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__(self):
        current = self.first
        strng = []
        if current is None:
            return '[]'
        # appending current and next data to strng
        strng.append(current.data)
        current = current.next
        while current != self.first:
            strng.append(current.data)
            current = current.next
        return str(strng)


def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int(line)

    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int(line)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int(line)

    # your code
    circle_lst = CircularList()
    # create a linked list from 1 to amount of soldiers
    for i in range(1, num_soldiers + 1):
        circle_lst.insert(i)

    start = circle_lst.find(start_count)
    for i in range(num_soldiers):
        deleted = circle_lst.delete_after(start, elim_num)
        print(deleted[0])
        start = deleted[1]


if __name__ == "__main__":
    main()