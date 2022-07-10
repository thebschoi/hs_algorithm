'''
https://www.acmicpc.net/problem/10773
'''
k = int(input())
stack_list = []
for i in range(k):
    n = int(input())
    if n == 0:
        stack_list.pop()
    else:
        stack_list.append(n)
print(sum(stack_list))