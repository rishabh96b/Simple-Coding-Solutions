'''
Author: Rishabh(rishabhbohra10@gmail.com)
Problem: print a inverted flag
* * * * *
  * * * *
    * * *
      * *
        *
language: python 2.x

'''


n = int(raw_input())   #input number of lines from user

for i in range(0,n):   #for keeping track of lines
  for j in range(0,n): #for keeping track of stars and spaces
    if j>=i:
      print "*",
    else:
      print " ",
  print "\n"
  
  
#end of script
  
  
