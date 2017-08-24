#Python program to reverse a string

#taking input from user
string1 = list(input()) #converting the string to a list of characters.

#initializing the starting index
i=0

#initializing end index
j= len(string1)-1

while(i<j):
  string1[i],string1[j] = string1[j],string1[i]  #python way of swapping 2 elements
  i+=1
  j-=1
  
 #printing the string again by converting list into string
print(''.join(string1))
