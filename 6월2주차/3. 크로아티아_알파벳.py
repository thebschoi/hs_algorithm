'''
https://www.acmicpc.net/problem/2941
'''
c_string = str(input())
c_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
idx = 0
ans = 0
while idx < len(c_string):
    if (c_string[idx:idx+2] in c_list):
        idx += 2
        ans += 1
    elif (c_string[idx:idx+3] in c_list):
        idx += 3
        ans += 1
    else:
        idx += 1
        ans += 1
print(ans)
