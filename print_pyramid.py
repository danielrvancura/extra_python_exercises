# Implement a program that prints out a half-pyramid of a specified height.

# Example: pyramid(6)
# input: (6) number of levels high
# output:
     #
    ##
   ###
  ####
 #####
######


# Challenge
# Implement a program that prints out a full-pyramid of a specified height.

# Example: pyramid(6)
# input: (6) number of levels high
# output:
     # #
    ## ##
   ### ###
  #### ####
 ##### #####
###### ######


# *** your code here ***
x=1
y=8
while x<=8:
 print((y*' ')+x*'@ ')
 y=y-1
 x=x+1
