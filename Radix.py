#  File: Radix.py

#  Description: Sorting unique combinations of lower case letters and numbers
#               through a use of a queue

#  Student Name: Mansa Prasad

#  Student UT EID: mp38229

#  Partner Name: Joyce Adekunle

#  Partner UT EID: jma5293

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 04/05/21

#  Date Last Modified: 04/06/21

import sys


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue if empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))


# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort(a):
    dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18,
            'j': 19, 'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28,
            't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 35
            }
    # lst 0 - 9 are numbers, and 10 - 35 are letters
    # adding queues to a list
    queue_lst = []
    for i in range(0, 37):
        queue_lst.append(Queue())

    # to find the longest string in the list 'a'
    longest = 0
    for i in a:
        strng = len(i)
        if strng >= longest:
            longest = strng

    for i in range(longest - 1, -1, -1):
        for strng in a:
            # if the string is less that the longest string in the list,
            # then a 0 is added to the queue
            if i >= len(strng):
                queue_lst[0].enqueue(strng)
                continue
            # sorting ascii value of string and
            # adding them to queue
            digit = dict[strng[i]]
            queue_lst[digit].enqueue(strng)

        # in order to dequeue values in list
        a = []
        for k in queue_lst:
            while not k.is_empty():
                a.append(k.dequeue())
    return a


def main():
    # read the number of words in file
    line = sys.stdin.readline()
    line = line.strip()
    num_words = int(line)

    # create a word list
    word_list = []
    for i in range(num_words):
        line = sys.stdin.readline()
        word = line.strip()
        word_list.append(word)

    '''
    # print word_list
    print (word_list)
    '''

    # use radix sort to sort the word_list
    sorted_list = radix_sort(word_list)

    # print the sorted_list
    print(sorted_list)


if __name__ == "__main__":
    main()