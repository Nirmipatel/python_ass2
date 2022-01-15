
# Defination:Write a Python program to add member(s) in a set and clear a set
#Name:Nirmi Patel (20CE095)
# creating set
'''set1=set({1,2,3,4,5,6,7,8})
print("set :")
# printing the set
print(set1)
#adding element inside the set
for i in range(9,11):
    set1.add(i)
print("After add the element inside the set :")
print(set1)
#clearing the set
set1.clear()
print("After the clearing set")
print(set1)

print("20CE095")'''


#Write a Python program to remove an item from a set if it is present in the set.
#Name:Nirmi Patel (20CE095)
#creating a set
'''student={"Nirmi","Shloka","sajeda","Arva","Disha","Princi"}
print(student)
#remove elemnt from set if it is present
if "Nirmi" in student :
    student.remove("Nirmi")
    print(student)
else:
    print("NO such element")'''


#Write a Python program to create an intersection, Union, difference of sets.
#Name:Nirmi Patel (20CE095)
#creating a set
'''alpha={'A','B','C','D','E','F'}
bita={'G','H','I','J','k,''L','A','B'}
#printing a set
print("alpha is :",alpha)
print("Bita is :",bita)

# unioun of two set using | operator
gamma=alpha|bita
print("after union set is :",gamma )

#intersection using & operator
delta=alpha&bita
print("After intesection set is :",delta)

#difference using diff operator
diff=alpha-bita
print("after differnece :",diff)'''

#Write a Python program to find maximum and the minimum value in a set.
#Name:Nirmi Patel (20CE095)
#create a set
'''values={'A','B','C','D'}
#print the maximum abd minimum values from the set using max() and min() function
print("maximum value from the set is :",max(values))
print("minimum value from the set is :",min(values))

#print the maximum and minimum values from the set using max() and min() function
number={90,110,9750,869,110,11,0,1}
print("\nMinimum value from the set is :",min(number))
print("maximum values from the set is :",max(number))'''

# Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
#20CE095
#creating tuple
'''from collections import Counter
tup=1,2,3,4,11,23,11,11,11,11
#creating a list
list=['a','b','c','c','c','c']
#creating a dictionary
dict={1:"Nirmi",2:"Nirmi",3:"Nirmi",4:"shloka"};


#for findind most commom element creating a function
def most_frequent(list):
    occurence_count = Counter(list)
    return occurence_count.most_common(1)[0][0]
#most frequrnt elemet
count_list=most_frequent(list)
#printinting most frequent element
print("frequent element in list is :",count_list)
#prrint count of most common element
print("count of frequent element is :",list.count(count_list))

#most commom element in tuple
count_tup=most_frequent(tup)
#printing most commom element
print("frequent elemt in tuple is :",count_tup)
#printing count of most commom element
print("count of commom element",tup.count(count_tup))

#most commom element in dictionary
count_dict=most_frequent(dict)
print("frequent element in dictionary is :",count_dict)'''



