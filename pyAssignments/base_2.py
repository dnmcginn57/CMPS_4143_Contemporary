#! usr/bin/env python3

"""
David McGinn
CMPS-4143
9-18-19
This program reads in an interger value and prints a binary representation

Please note: shell redirection was used to direct standard out to output.txt
"""

import sys,os

"""
    Accepts:
        int quo: quotent
    Returns
        string "0" or string "0" or "1" concatenated with a recursive call
        recursively concatenates to form a binary number
"""
def to_Binary(q):
    #adds an extra 0 but needed to represent actual 0 if it's passed in
    if (q == 0):
        return "0"
    else:
        quo = int(q/2)
        rem = q%2
        if(rem==1):
            return "1" + to_Binary(quo)
        else:
            return "0" + to_Binary(quo)    



if __name__ == "__main__":
    num = 0
    bi_Num = ""
    num = int(input("Enter a base 10 Number:\n"))
    while(num!=-1):
        bi_Num = to_Binary(num)
        #cheeky string comprehension trick to reverse bi_Num
        print(num, "=", bi_Num[::-1])
        num = int(input("Enter a base 10 Number:\n"))
    