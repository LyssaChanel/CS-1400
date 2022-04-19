"""
Alyssa Smederovac Simmonds
CS 1400-002
Yondu Udonta.py
Design for 
Project 1
"""
print(int(10.98))


# Variables
initial_plunder = int(input("What is the plunder when the reavers enter the port?"))
crew_members = int(input("How many reavers are on the ship? (Including Yondu & Peter)"))

yondus_share = int()
peters_share = int()
rbf = int()
crew_share = int()

# Math

# Pseudocode
"""
input # of crew
input # of initial units
calculate Yondu's share
calculate Peter's share
calculate Crew's share
calculate RBF share
"""

"""
ask how many crew members there are
ask how much money they came into port with
take total amount of money and give each reaver 3 units to spend
take 13% of the remaining money and give it to yondu
take 11% of the remaining money after you give yondu his cut and give it to peter
divide the remainder evenly among the entire crew.
give the remainder to the rbf
print the results

"""

#Rubric
"""
(10 points) 20 reavers with 1000 units gives 54 shore leave, Yondu 158, Peter 126, each crew 36, and RBF 14.

(10 points) input some numbers you are not told

(10 points) If user enters anything other than positive integers for reavers and units,
print “Enter only positive integers for reavers and units.” and exit.

(10 points) If the number of reavers is less than 3, print “Not enough crew.” and exit.

(10 points) If the number of units is less than or equal to 3 times the number of reavers, print “Not enough units.” and exit.

(10 points) Code has a main function with conditional execution. All code is contained within a function.

(7 points) File has a module docstring with required information in it.

(6 points) Code follows PEP8 Python Style guide for code style

(7 points) The style checker (pylint with a custom configuration) emits no warnings.

"""