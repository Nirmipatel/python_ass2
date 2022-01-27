#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given n scores. Store them in a list and find the score of the runner-up.
#https://github.com/Nirmipatel/python_ass2

runner_up=[]
n=int(input())

for i in range(0,n):
    item=int(input())
    runner_up.append(item)

print(runner_up)
runner_up.sort()
runner_up.reverse()
print(runner_up)
print(runner_up[2])