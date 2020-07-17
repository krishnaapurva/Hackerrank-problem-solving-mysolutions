#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    dic = { 1:'one',2:'two', 3:'three', 4:'four', 5:'five',
            6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
            11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen',
         15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen',
         19:'nineteen', 20:'twenty', 21:'twenty one', 22:'twenty two', 
         23:'twenty three', 24:'twenty four', 25:'twenty five', 26:'twenty six',
         27:'twenty seven', 28:'twenty eight', 29:'twenty nine'}
    if(m==00):
        return(dic[h] + " o' clock")
    elif(m==15):
        return("quarter past "+dic[h])
    elif(m<30):
        if(m==1):
            return(dic[m] + " minute past "+dic[h])
        else:
            return(dic[m] + " minutes past "+dic[h])
    elif(m==30):
        return("half past "+ dic[h])
    elif(m==45):
        return("quarter to "+dic[h+1])
    else:
        x = 60-m
        if(x==1):
            return(dic[x]+" minute to "+ dic[h+1])
        else:    
            return(dic[x]+" minutes to "+ dic[h+1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
