# Write a Python script to check whether a given key already exists in a dictionary.
#Nirmi Patel(20CE095)
#creating a dictionary
'''dict={1:'A',2:'B',3:'C',4:'D'}
print("dictionry is :",dict)
check=1
#checking a key is in the dictionary
if check in dict.keys():
    print(check, "is in the dictonary")
else:
    print(check,"is not in dictionary")
print("20CE095")'''

#Write a Python script to merge two Python dictionaries.
#Nirmi Patel(20CE095)

#creating a dictionary
import collections

'''d1={'A':"anad",'B':"baroda",'C':"chennai",'D':"delhi"}
d2={1:"one",2:"two",3:"Three",4:"Four"}
print("d1 is ",d1)
print("d2 is ",d2)
#merging of two dictionary in d1 which print none
print("after the merge :",d1.update(d2))
#this print the merge of the dictionary
print("after merge in the d1 :",d1)
print("after merge in the d1 :",d2)'''

# Write a Python program to sum all the items in a dictionary.
#Nirmi Patel(20cE095)
'''#creating a function to do sum
def returnSum(dict1):
    sum = 0
    for i in dict1.values():
        sum = sum + i

    return sum
#creating a dictionry
dict1={'a':1,'b':2,'c':3,'d':4}
print("dict1 is ",dict1)
#prirnting summation of all element of the dictionry
print("sum of all element in the dictionry",returnSum(dict1))'''

#Write a Python script to add a key to a dictionary.
#Nirmi Patel(20CE095)
'''Dictionary = dict()
Dictionary[0]=10
Dictionary[1]=20
Dictionary[2]=30
print(Dictionary)
Result : {0: 10, 1: 20, 2: 30}'''

#Write a Python script to concatenate following dictionaries to create a new one.
#Nirmi Patel(20CE095)

'''dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)'''
