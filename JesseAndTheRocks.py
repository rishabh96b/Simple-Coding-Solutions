'''
@Author: Rishabh(rishabhbohra10@gmail.com)
Link of problem: https://www.hackerrank.com/contests/codeagon-2016/challenges/jesse-and-the-rocks/copy-from/1302990078
language: python 2
'''

n, strengthJesse = raw_input().split(" ")
rocks = map(int, raw_input().split())

	
skip = 0    #to count number of skips
count =0    #to count the crushed rocks

for rock in rocks:
	if skip==2:  # check if atleast one ock is skipped or not
		break
	if (int(strengthJesse) >= rock):
		count+=1   # crush the rock and count it
	else:
		skip+=1
		continue

print count
	
