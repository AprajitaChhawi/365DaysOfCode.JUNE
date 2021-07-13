#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    sen=sentence.split(" ")
    sen=sen[::-1]
    s=''
    for i in sen:
        for j in i:
            if j.isupper():
                s=s+j.lower()
            if j.islower():
                s=s+j.upper()
        s=s+" "
    return s
    # Write your code here

if __name__ == '__main__':
    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)
    print(result)
