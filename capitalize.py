#Q You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
#For example, neeraj kumar should be capitalised correctly as Neeraj Kumar.



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    pre_wordList = s.split(" ")
    post_wordList = list()
    for i in pre_wordList:
        if i != "":
            post_wordList.append(''.join([j for j in i][0].upper())+''.join([j for j in i][1:]))
        else:
            post_wordList.append(i)
        
    return ' '.join(post_wordList)
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
