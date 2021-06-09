#  File: TestLinkedList.py

#  Description:

#  Student Name: Mansa Prasad

#  Student UT EID: mp38229

#  Partner Name: Joyce Adekunle

#  Partner UT EID: jma5293

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 04/06/21

#  Date Last Modified:
import sys


class Link(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    # create a linked list
    # you may add other attributes
    def __init__(self):
        self.first = None

    # get number of links
    def get_num_links(self):
        num = self.first
        ct = 0
        while num is not None:
            ct += 1
            num = num.next
        return ct

    # add an item at the beginning of the list
    def insert_first(self, data):
        new_link = Link(data)

        new_link.next = self.first
        self.first = new_link

    # add an item at the end of a list
    def insert_last(self, data):
        new_link = Link(data)

        current = self.first
        if current is None:
            self.first = new_link
            return

        while current.next is not None:
            current = current.next

        current.next = new_link

    # add an item in an ordered list in ascending order
    # assume that the list is already sorted
    def insert_in_order(self, data):
        new_link = Link(data)
        current = self.first
        if current is None:
            self.first = new_link
            return
        while current.next is not None:
            if current.next.data > new_link.data:
                new_link.next = current.next
                current.next = new_link
                return
            else:
                current = current.next
        current.next = new_link

    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        current = self.first
        if current is None:
            return None
        while current.data is not data:
            if current.next is None:
                return None
            else:
                current = current.next
        return current

    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        current = self.first
        if current is None:
            return None
        while current.data is not data:
            if current.next is None:
                return None
            else:
                current = current.next
        return current

    # Delete and return the first occurrence of a Link containing data
    # from an unordered list or None if not found
    def delete_link(self, data):
        previous = self.first
        current = self.first
        if current is None:
            return None
        while current.data != data:
            if current.next is None:
                return None
            else:
                previous = current
                current = current.next
        if current == self.first:
            self.first = self.first.next
        else:
            previous.next = current.next
        return current

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        current = self.first
        count = 0
        strng = []
        if current is None:
            return ''
        while current is not None:
            # count used to limit number of items per line to 10
            if count < 10:
                strng.append(str(current.data) + '  ')
                current = current.next
                count += 1
                continue
            # when items reach 10, new line is made and count is reset
            strng += '\n'
            count = 0
        return ''.join(strng)

    # Copy the contents of a list and return new list
    # do not change the original list
    def copy_list(self):
        new_lst = LinkedList()
        current = self.first

        if current is None:
            return None

        # adds to the new list one by one
        while current is not None:
            new_lst.insert_last(current.data)
            current = current.next

        return new_lst

    # Reverse the contents of a list and return new list
    # do not change the original list
    def reverse_list(self):
        new_lst = LinkedList()
        current = self.first
        previous = None
        while current is not None:
            # reverse the link
            next_node = current.next
            current.next = previous
            # moving to next node
            previous = current
            current = next_node
        # making head the last element in link
        self.first = previous

        # inserting items into the linked list and
        # returning a new list
        if current is None:
            return None
        while current is not None:
            new_lst.insert_last(current.data)
            current = current.next
        return new_lst

    # Sort the contents of a list in ascending order and return new list
    # do not change the original list
    def sort_list(self):
        new_lst = LinkedList()
        lst = []
        current = self.first

        if current is None:
            return None

        while current is not None:
            lst.append(current.data)
            current = current.next

        lst.sort()
        for i in lst:
            new_lst.insert_last(i)
        return new_lst

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        if self.sort_list():
            return True
        else:
            return False

    # Return True if a list is empty or False otherwise
    def is_empty(self):
        current = self.first
        if current is None:
            return True
        # else it returns false
        return current.next is None

    # Merge two sorted lists and return new list in ascending order
    # do not change the original lists
    def merge_list(self, other):
        new_lst = LinkedList()
        current = self.first
        o_current = other.first

        while current is not None and o_current is not None:
            if current.data < o_current.data:
                new_lst.insert_last(current.data)
                current = current.next
            else:
                new_lst.insert_last(o_current.data)
                o_current = o_current.next

        while current is not None:
            new_lst.insert_last(current.data)
            current = current.next

        while o_current is not None:
            new_lst.insert_last(o_current.data)
            o_current = o_current.next

        return new_lst

    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):
        current = self.first
        o_current = other.first
        if current is None and o_current is None:
            return True
        if current is None or o_current is None:
            return False
        while current is not None and o_current is not None:
            if current.data != o_current.data:
                return False
            current = current.next
            o_current = o_current.next
        return True

    # Return a new list, keeping only the first occurrence of an element
    # and removing all duplicates. Do not change the order of the elements.
    # do not change the original list
    def remove_duplicates(self):
        current = self.first
        previous = None
        dupl_lst = []
        while current is not None:
            # if data not already in list, add it to list
            if current.data not in dupl_lst:
                dupl_lst.append(current.data)
                previous = current
            else:
                # if duplicate is found, previous node is now current.next node
                # basically skips over the duplicate node
                previous.next = current.next
            current = current.next
        return dupl_lst


def main():
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    link1 = list(map(int, line))
    print(link1)

    line2 = sys.stdin.readline()
    line2 = line2.strip()
    line2 = line2.split()
    link2 = list(map(int, line2))
    print(link2)

    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    link = LinkedList()
    link.get_num_links()
    for i in link1:
        link.insert_in_order(i)

    linktwo = LinkedList()
    for i in link2:
        linktwo.insert_in_order(i)
    #    link.insert_first(1)

    #    link.insert_last(3)

    #    link.insert_in_order(6)

    #### returns address    print(link.find_unordered(14))

    #    link.find_ordered(20)
    #    link.delete_link(30)
    #    link.__str__()
    #    link.copy_list()
    ### returns None print(link.reverse_list())
    ### returns not in a list print(link.sort_list())
    #    print(link.is_empty())
    #    print(link.remove_duplicates())
    print(link.merge_list(linktwo))
    print(link.is_equal(linktwo))


# Test method insert_last()

# Test method insert_in_order()


# Test method get_num_links()

# Test method find_unordered()
# Consider two cases - data is there, data is not there

# Test method find_ordered()
# Consider two cases - data is there, data is not there

# Test method delete_link()
# Consider two cases - data is there, data is not there

# Test method copy_list()

# Test method reverse_list()

# Test method sort_list()

# Test method is_sorted()
# Consider two cases - list is sorted, list is not sorted

# Test method is_empty()

# Test method merge_list()

# Test method is_equal()
# Consider two cases - lists are equal, lists are not equal

# Test remove_duplicates()

if __name__ == "__main__":
    main()
