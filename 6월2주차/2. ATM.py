'''
https://www.acmicpc.net/problem/11399
'''
n = int(input())
time_list = list(map(int, input().split()))
time_list.sort()
ans = 0
for i in range(n):
    ans += time_list[i]*(n-i)
print(ans)
