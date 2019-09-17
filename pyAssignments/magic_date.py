#!/usr/bin/env python3

"""
David McGinn
Program 1 - 9/11/19
This program determines whether a certain date is magic
(month * day = year)
"""

import sys, os

"""
    Accepts:
        int m - month
        int d - day
        int y - year
    Returns:
        tuple - (boolean, errormsg)
    ensures date is an actual, possible date(sort of)    
"""
def verify(m,d,y):
    if m > 12 or m < 1:
        return (False,"invalid: month must be 1-12")
    elif d > 31 or d <1:
        return (False,"invalid: day must be 1-31")
    elif y > 99 or y < 0:
        return (False,"invalid: year must be 00-99")
    return (True, ";^)")

"""
    Accepts: 
        int m - month
        int d - day
        int y - year
    Returns:
        none
    Determines wether the date is magic by
    comparing m * d to y, printing the result
"""
def is_Magic(m,d,y):
    mult = m*d
    if mult is y:
        print (str(m) + "/" + str(d) + "/" + str(y) + " is magic because ")
        print (str(m) + " * " + str(d) + " = " + str(y))
    else:
        print (str(m) + "/" + str(d) + "/" + str(y) + " is not magic because ")
        print (str(m) + " * " + str(d) + " != " + str(y))

"""
    Entry point function
"""
if __name__ == "__main__":
    
    is_Valid = (False, -1)
    
    #loop until valid entry
    while(not is_Valid[0]):
        date = input("input date (mm/dd/yy)\n")
    
        date_List = date.split('/')
    
        m = int(date_List[0])
        d = int(date_List[1])
        y = int(date_List[2])

        is_Valid = verify(m,d,y)
        
        if is_Valid[0]:
            is_Magic(m,d,y)

    



