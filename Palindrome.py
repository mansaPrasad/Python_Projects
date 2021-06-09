#  File: Palindrome.py

#  Description:

#  Student Name: Mansa Prasad

#  Student UT EID: mp38229

#  Partner Name: Joyce Adekunle

#  Partner UT EID: jma5293

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 02/03/21

#  Date Last Modified: 02/08/21

import sys


# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a string that is the smallest palindrome that can be
#         made by adding characters to the start of the input string
def smallest_palindrome(str):
    if str == str[::-1]:
        return str
    else:
        start = str[0]
        r = str[::-1]
        end = len(str) - 1 - r.find(start)
        if end == len(str):
            substring = str[1:]
            return substring[::-1] + str
        else:
            palin = str[0:end + 1]
            for i in range(str.count(start)):
                if palin == palin[::-1]:
                    substring_2 = str[end + 1:]
                    return substring_2[::-1] + str
                else:
                    r = palin[::-1]
                    find_index = r[1:].find(start)
                    end = end - 1 - find_index
                    palin = str[0:end + 1]


def main():
    # read the data
    # print the smallest palindromic string that can be made for each input
    for i in sys.stdin:
        k = smallest_palindrome(i.strip())
        print(k)


if __name__ == "__main__":
    main()
