'''
https://www.acmicpc.net/problem/9375
'''
n = int(input())
ans_list = []
for i in range(n):
    m = int(input())
    c_dict = {}
    for j in range(m):
        c_name, c_type = map(str, input().split())
        if c_type in c_dict:
            (c_dict[c_type]).append(c_name)
        else:
            c_dict[c_type] = [c_name]
    c_mul = 1
    for val in c_dict.values():
        c_mul *= len(val)+1     
    ans_list.append(c_mul - 1)
for i in ans_list:
    print(i)
