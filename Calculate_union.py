#! /bin/python3.7
import sys
if len(sys.argv)<3:
	print ('Usage: idlist1.txt idlist2.txt')
	sys.exit()
else:
	input1=sys.argv[1]
	input2=sys.argv[2]

user_input = input("Enter Choice (1,2,3,4)")
idlist1 = open(input1 , "r") 
idlist2 = open(input2 , 'r')
list1 = {}
for line in idlist1:
	k=line.strip().split('\t')[0]
	list1[k.strip()] = ""
idlist1.close()

list2 = {}
for line1 in idlist2:
	k=line1.strip().split('\t')[0]
	list2[k.strip()] = ""

idlist2.close()
tempUnion={**list1 , **list2}

if user_input == "1":
# Union
	tempUnion= {**list1 , **list2}
	print(tempUnion)
elif user_input == "2": 
	intersection = list1.keys() & list2.keys()
	print(intersection)
elif user_input == "3":
	unique_list1 = list1.keys() & tempUnion.keys()
	print(unique_list1)
else:
	unique_list2 = list2.keys() & tempUnion.keys()
	print(unique_list2)
	