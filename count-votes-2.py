#importing library collections for counting items
import collections
#creat a list to save inputs(candidates)
list1=[]
votes=int(input())
#bring iterable for set range
for i in range(0,votes):
    candidates=input()
#add input items to list1
    list1.append(candidates)
#sort list of strings
    list1.sort()
#use counter from collections library
    list2=collections.Counter(list1)
#turn list2 to dictionary
    d=dict(list2)
#use below code to control all items in dictionary 
for key in d:
#use below code to print keys and values in each lines
    print(key,d[key])



