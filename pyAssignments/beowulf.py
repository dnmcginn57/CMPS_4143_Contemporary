#!usr/bin/env python3

#David McGinn
#10.9.19
#Contemporary Programming
import re
import sys,os

with open("beowulf_Poem.txt") as f:

    print("""
David McGinn
This program replaces all the occurrences of certain words in the Beowulf
Poem with other, more modern words.
    """)

    s=f.read()
    s2 = str(re.findall('BEOWULF\.(.*?)ADDENDA\.',s,re.DOTALL))
    s2 = s2.replace("\\n","\n") #must be done with replace since re
    s2 = s2.replace("\\","")    #automatically escapes its special characters
    
    bairn = len(re.findall("bairn",s2,flags=re.IGNORECASE))
    bight = len(re.findall("bight",s2,flags=re.IGNORECASE))
    floats = len(re.findall("float",s2,flags=re.IGNORECASE))
    carle = len(re.findall("carle",s2,flags=re.IGNORECASE))

    #better translation in context since both child, progeny and son are also
    #in the poem. Heirs could work as well
    s2 = re.sub("bairn","descendant", s2, flags=re.IGNORECASE)
    s2 = re.sub("bight","bay", s2, flags=re.IGNORECASE)
    s2 = re.sub("float","ship", s2, flags=re.IGNORECASE)
    #more accurate translation of this word than "Househero"
    s2 = re.sub("housecarle","bodyguard", s2, flags=re.IGNORECASE)
    #plurals
    s2 = re.sub("carles","heroes", s2, flags=re.IGNORECASE)
    #base
    s2 = re.sub("carle","hero", s2, flags=re.IGNORECASE)

    #proof all occurences were replaced
    post_Bairn = bairn - len(re.findall("bairn",s2,flags=re.IGNORECASE))
    post_Bight = bight - len(re.findall("bight",s2,flags=re.IGNORECASE))
    post_Floats = floats - len(re.findall("float",s2,flags=re.IGNORECASE))
    post_Carle = carle - len(re.findall("carle",s2,flags=re.IGNORECASE))

    print("bairn was replaced:\t" + str(post_Bairn), "times")
    print("bight was replaced:\t" + str(post_Bight), "times")
    print("float was replaced:\t" + str(post_Floats), "times")
    print("carle was replaced:\t" + str(post_Carle), "times")

    print(s2)