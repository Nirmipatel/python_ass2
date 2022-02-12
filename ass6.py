
'''AIM: You are given n words. Some words may repeat. For each word, output its number of occurrences.
 The output order should correspond with the input order of appearance of the word. See the sample
 input/output for clarification.'''
#Id:20ce095
#






import collections
N = int(input())
#create dictionary
d = collections.OrderedDict()

#taking N times input
for i in range(N):
    word = input()
    #find the count of word from existing word
    if word in d:
      d[word] +=1
    else:
      d[word] = 1

print(len(d))
#find the number of occranece of the word
for k,v in d.items():
   print(v,end = " ")





