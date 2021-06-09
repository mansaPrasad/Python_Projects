#  File: Reducible.py

#  Description: Finding the largest possible word that can collapse on itself

#  Student Name: Mansa Prasad

#  Student UT EID: mp38229

#  Partner Name: Joyce Adekunle

#  Partner UT EID: jma5293

#  Course Name: CS 313E

#  Unique Number: 52230

#  Date Created: 03/30/21

#  Date Last Modified: 03/31/21

import sys


# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime(n):
    if n == 1:
        return False

    limit = int(n ** 0.5) + 1
    div = 2
    while div < limit:
        if n % div == 0:
            return False
        div += 1
    return True


# Input: takes as input a string in lower case and the size
#        of the hash table
# Output: returns the index the string will hash into
def hash_word(s, size):
    hash_idx = 0
    for j in range(len(s)):
        letter = ord(s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx


# Input: takes as input a string in lower case and the constant
#        for double hashing
# Output: returns the step size for that string
def step_size(s, const):

    # incorporating double hashing
    hash_idx = 0
    for stng in range(len(s)):
        letter = ord(s[stng]) - 96
        hash_idx = (hash_idx * 26 + letter) % const
    s_size = const - hash_idx % const
    return s_size


# Input: takes as input a string and a hash table
# Output: no output; the function enters the string in the hash table,
#         it resolves collisions by double hashing
def insert_word(s, hash_table):

    # adds string from hash table to an empty slot in index
    idx = hash_word(s, len(hash_table))
    if hash_table[idx] == '':
        hash_table[idx] = s

    # finds next empty slot using the step size function
    else:
        step = step_size(s, 11)
        while hash_table[idx] != '':
            idx = (idx + step) % len(hash_table)
        hash_table[idx] = s


# Input: takes as input a string and a hash table
# Output: returns True if the string is in the hash table
#         and False otherwise
def find_word(s, hash_table):

    # if word is in hash table, it's true
    idx = hash_word(s, len(hash_table))
    if hash_table[idx] == s:
        return True

    # Checking for collisions, if string not found in index
    # the search continues to find an empty slot
    else:
        step = step_size(s, 11)
        while hash_table[idx] != s:
            if hash_table[idx] == '':
                return False
            idx = (idx + step) % len(hash_table)
        return True


# Input: string s, a hash table, and a hash_memo
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo
#         and returns True and False otherwise
def is_reducible(s, hash_table, hash_memo):

    # the only possible 1 letter words that are acceptable
    if len(s) == 1:
        return s == 'a' or s == 'i' or s == 'o'

    # find if s is not in the hash table, then it will return false
    if not find_word(s, hash_table):
        return False

    # these are the three base cases
    # check if the work is in the list
    if find_word(s, hash_memo):
        return True

    # find reduced word with recursion, must be added to hash memo if reducible
    for idx in range(len(s)):
        new_s = s[:idx] + s[idx + 1:]
        if is_reducible(new_s, hash_table, hash_memo):
            insert_word(new_s, hash_memo)
            return True
    return False


# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words(string_list):

    lst = []
    size_word = 0

    # Iterating through the string list to find longest word
    for strg in string_list:
        if len(strg) > size_word:
            size_word = len(strg)
            lst = [strg]
        elif len(strg) == size_word:
            lst.append(strg)
    return lst


def main():
    # create an empty word_list
    word_lst = []

    # open the file words.txt
    # read words from words.txt and append to word_list
    for line in sys.stdin:
        line = line.strip()
        word_lst.append(line)

    # find length of word_list
    lngth = len(word_lst)

    # determine prime number N that is greater than twice
    # the length of the word_list
    prime_n = lngth * 2
    while not is_prime(prime_n):
        prime_n += 1

    # create an empty hash_list
    hash_list = []

    # populate the hash_list with N blank strings
    for strg in range(prime_n):
        hash_list.append('')

    # hash each word in word_list into hash_list
    # for collisions use double hashing
    for word in word_lst:
        insert_word(word, hash_list)

    # create an empty hash_memo of size M
    # we do not know a priori how many words will be reducible
    # let us assume it is 10 percent (fairly safe) of the words
    # then M is a prime number that is slightly greater than
    # 0.2 * size of word_list
    hash_memo = []
    prime_m = int(lngth * 0.2)
    while not is_prime(prime_m):
        prime_m += 1

    # populate the hash_memo with M blank strings
    for strg in range(prime_m):
        hash_memo.append('')

    # create an empty list reducible_words
    reducible_words = []

    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    # as you recursively remove one letter at a time check
    # first if the sub-word exists in the hash_memo. if it does
    # then the word is reducible and you do not have to test
    # any further. add the word to the hash_memo.
    for word in word_lst:
        redu = is_reducible(word, hash_list, hash_memo)
        if redu is True:
            reducible_words.append(word)

    # find the largest reducible words in reducible_words
    long_list = get_longest_words(reducible_words)

    # print the reducible words in alphabetical order
    # one word per line
    long_list.sort()
    for word in long_list:
        print(word)


if __name__ == "__main__":
    main()
