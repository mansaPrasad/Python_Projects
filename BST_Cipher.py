#  File: BST_Cipher.py

#  Description: Using Binary Search Trees to encrypt and decrypt strings

#  Student Name: Mansa Prasad

#  Student UT EID: mp38229

#  Partner Name: Joyce Adekunle

#  Partner UT EID: jma5293

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 04/20/2021

#  Date Last Modified: 04/20/2021
import sys


class Node(object):
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None


class Tree(object):
    # the init() function creates the binary search tree with the
    # encryption string. If the encryption string contains any
    # character other than the characters 'a' through 'z' or the
    # space character drop that character.
    def __init__(self, encrypt_str):
        self.root = None
        # adding and checking whether i is in the alphabet
        # as well as a space and inserting it into the binary tree
        for i in encrypt_str:
            if i.isalpha() or i == ' ':
                self.insert(i)

    # the insert() function adds a node containing a character in
    # the binary search tree. If the character already exists, it
    # does not add that character. There are no duplicate characters
    # in the binary search tree.

    def insert(self, ch):
        # code adapted from notes and altered
        newNode = Node(ch)
        if self.root == None:
            self.root = newNode
        else:
            current = self.root
            parent = self.root
            # while current node is not empty
            while current != None:
                parent = current
                # if less than current.data, current becomes less child
                if ch < current.data:
                    current = current.lChild
                # if more than current.data, current becomes right child
                elif ch > current.data:
                    current = current.rChild
                # if found, current data is returned
                elif ch == current.data:
                    return
            if ch < parent.data:
                parent.lChild = newNode
            else:
                parent.rChild = newNode

    # the search() function will search for a character in the binary
    # search tree and return a string containing a series of lefts
    # (<) and rights (>) needed to reach that character. It will
    # return a blank string if the character does not exist in the tree.
    # It will return * if the character is the root of the tree.
    def search(self, ch):
        strng = ''
        current = self.root
        if current == None:
            return ''
        # the root of the tree is '*'
        if ch == self.root.data:
            return '*'
        while current != None:
            # if ascii value is left it adds '<' to strng
            # else if right it adds '>'
            if ch < current.data:
                strng += '<'
                current = current.lChild
            elif ch > current.data:
                strng += '>'
                current = current.rChild
            elif ch == current.data:
                return strng
        return ''

    # the traverse() function will take string composed of a series of
    # lefts (<) and rights (>) and return the corresponding
    # character in the binary search tree. It will return an empty string
    # if the input parameter does not lead to a valid character in the tree.
    def traverse(self, st):
        current = self.root
        if current == None:
            return ''
        if st == '*':
            return current.data
        else:
            for i in st:
                # to make sure we're still within the tree
                if current == None:
                    return ''
                elif i == '<':
                    current = current.lChild
                elif i == '>':
                    current = current.rChild
            # if at right/left parent node, and there's
            # none right/left, empty string is returned
            if current == None:
                return ''
            return current.data

    # the encrypt() function will take a string as input parameter, convert
    # it to lower case, and return the encrypted string. It will ignore
    # all digits, punctuation marks, and special characters.
    def encrypt(self, st):
        e_string = ''
        # turning string to lower case
        strng = st.lower()
        # iterates through BST and search is called in order to return *, <, or >
        for i in strng:
            if i.isalpha() or i == ' ':
                e_string += self.search(i) + '!'
        # takes off last '!'
        return e_string[:-1]

    # the decrypt() function will take a string as input parameter, and
    # return the decrypted string.
    def decrypt(self, st):
        d_string = ''
        # string split by the '!'
        lst = st.split('!')
        # iterates through encrypted string, where traverse returns the character
        for i in lst:
            d_string += self.traverse(i)
        return d_string


def main():
    # read encrypt string
    line = sys.stdin.readline()
    encrypt_str = line.strip()

    # create a Tree object
    the_tree = Tree(encrypt_str)

    # read string to be encrypted
    line = sys.stdin.readline()
    str_to_encode = line.strip()

    # print the encryption
    print(the_tree.encrypt(str_to_encode))

    # read the string to be decrypted
    line = sys.stdin.readline()
    str_to_decode = line.strip()

    # print the decryption
    print(the_tree.decrypt(str_to_decode))


if __name__ == "__main__":
    main()
