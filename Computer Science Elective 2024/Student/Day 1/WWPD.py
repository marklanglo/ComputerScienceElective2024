# Program Name	: What Would Python Do?
# Programmed By	: Mark Wiedeman
# For Use of By : Naveen Bahadur and Mark Wiedeman
# Date			: December 11 2023


#==========================================================
#
# What Would Python Do - Instructions
#
#==========================================================
#
# HOW TO RUN THIS:
#
# A) IN Thonny:
#
#     Simply press the green play button!
#
#
# B) IN Terminal:
#
# Firstly use cd to get to the folder holding this file
#
#       Example: "cd Desktop/Python\ Projects"
#
# In the terminal run the python REPL
# by running the command:
#
#       "python3"
#
# After starting the REPL
# to grab the functions
# run the command:
#
#       "from WWPD import *"
#
# Once this is done, you'll be able to run the functions
# in the command line itself.
#
#            Examples: GreaterThanTen(15)
#                      NumberSelector(12, 3, 19)
#                      FunkyNum(14)
#
#==========================================================

def GreaterThanTen(a):
    if a > 10:
        print(a)
    else:
        print(0)
        
# WWPD:
#       a = 5       Solution is 0
#       a = 12      Solution is 12
#       a = 8       Solution is 0
#       a = 15      Solution is 15


def NumberSelector(a, b, c):
    if (a + b) == 3:
        return a
    elif (c - b) >= 6:
        return c
    else:
        return b

# WWPD:
#       a = 1, b = 2, c = 3      Solution is 1
#       a = 3, b = 6, c = 18     Solution is 18
#       a = 3, b = 6, c = 7      Solution is 6
#       a = 1, b = 2, c = 18     Solution is 1

def FunkyNum(a):
    if a % 2 == 0:
        return "yes"
    else:
        return "no"

# WWPD:
#       a = 4        Solution is yes
#       a = 5        Solution is no
#       a = 18       Solution is yes
#       a = 17       Solution is no
