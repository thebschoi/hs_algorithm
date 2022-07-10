'''
https://www.acmicpc.net/problem/1931
'''
n = int(input())
time_list = []
for i in range(n):
    start, end = map(int, input().split())
    time_list.append([start, end])
for i in time_list:
    print(i)