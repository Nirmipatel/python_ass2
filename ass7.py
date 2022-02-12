'''Lapindrome is defined as a string which when split in the middle, gives two halves having the same
characters and same frequency of each character. If there are odd number of characters in the string,
we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, since the
two halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are
a few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves contain the same
characters but their frequencies do not match. Your task is simple. Given a string, you need to tell
if it is a lapindrome. '''
#20CE095 Nirmipatel
#
#take input for test cases
T = int(input())
for i in range(T):
    #take input string
    s=input()
    s1,s2='',''
    #split string which has even length
    if(len(s)%2==0):
     s1=s[:len(s)//2]
     s2=s[len(s)//2:]
    else:
    #split string which has odd length
     s1=s[:len(s)//2]
     s2=s[len(s)//2+1:]
    #convert string into list for sorting the string
    l1=list(s1)
    l2=list(s2)
    l1.sort()
    l2.sort()
    #convert list into string
    s1=str(l1)
    s2=str(l2)
    if(s1==s2):
     print('YES')
    else:
     print('NO')