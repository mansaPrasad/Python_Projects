#  File: Cipher.py

#  Description: Allowing a character string to be encrypted using a matrix
#				and rotating it by 90 degrees then decrypting a string 
# 				through the same process.

#  Student Name: Mansa Prasad

#  Student UT EID: mp38229

#  Partner Name: Joyce Adekunle

#  Partner UT EID: jma5293

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 02/06/21

#  Date Last Modified: 02/08/21


import math
import sys


# Input: strng is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string

def encrypt(strng):
    # defining the variables
    l = len(strng)
    k = math.ceil(math.sqrt(l))
    m = k ** 2
    asterisk = '*'

    # adding the * to the string 
    while len(strng) < m:
        strng = strng + asterisk

    # creating the matrix 
    arr = []
    for i in range(k):
        row = []
        for j in range(k):
            row.append('')
        arr.append(row)
    index = 0
    for i in range(k):
        for j in range(k):
            arr[i][j] = strng[index]
            index += 1

    # rotating the matrix clockwise
    rotated = []
    for i in range(k):
        r = []
        for j in range(k):
            r.append('')
        rotated.append(r)
    for i in range(k):
        for j in range(k):
            rotated[i][j] = arr[k - 1 - j][i]

    # Getting the matrix back into a string and removing the asterisks
    encoded = ''
    for i in range(k):
        for j in range(k):
            new = rotated[i][j]
            if new != '*':
                encoded += new
    return encoded


# Input: strng is a string of 100 or less of upper case, lower case,
#        and digits
# Output: function returns an encrypted string

def decrypt(strng):
    # defining the variables
    l = len(strng)
    k = math.ceil(math.sqrt(l))
    m = k ** 2
    asterisk = '*'

    # adding the *
    while len(strng) < m:
        strng = strng + asterisk

    # creating the matrix
    arr = []
    for i in range(k):
        row = []
        for j in range(k):
            row.append('')
        arr.append(row)
    index = 0
    for i in range(k):
        for j in range(k):
            arr[i][j] = strng[index]
            index += 1

    # rotating the matrix counter-clockwise
    rotated = []
    for i in range(k):
        r = []
        for j in range(k):
            r.append('')
        rotated.append(r)
    for i in range(k):
        for j in range(k):
            rotated[i][j] = arr[j][k - 1 - i]

    # converting the matrix into a string, and removing astrisks if needed
    decoded = ''
    for i in range(k):
        for j in range(k):
            new = rotated[i][j]
            if new != '*':
                decoded += new
    return decoded


def main():
    # read the two strings P and Q from standard input
    p = sys.stdin.readline().strip()
    q = sys.stdin.readline().strip()

    # encrypt the string P
    encryp = encrypt(p)

    # decrypt the string Q
    decryp = decrypt(q)

    # print the encrypted string of P and the
    print(encryp)
    # decrypted string of Q to standard out
    print(decryp)


if __name__ == "__main__":
    main()
