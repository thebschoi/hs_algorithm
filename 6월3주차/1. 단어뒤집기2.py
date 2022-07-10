'''
https://www.acmicpc.net/problem/17413
'''
s_string = str(input())
stack_list = []
idx = 0
# tag 내부인지 판별하기 위한 flag
flag = 0

for i in range(len(s_string)):
    if s_string[i] == '<':
        if i > idx:
            stack_list.append(''.join(reversed(s_string[idx:i])))
        idx = i
        flag = 1
    elif s_string[i] == '>' and flag == 1:
        stack_list.append(s_string[idx:i+1])
        idx = i+1
        flag = 0
    elif s_string[i] == ' ' and flag == 0:
        stack_list.append(''.join(reversed(s_string[idx:i])))
        stack_list.append(s_string[i])
        idx = i+1
    # tag로 끝나지 않는 경우
    elif (i+1 == len(s_string)) and s_string[i] != '>':
        stack_list.append(''.join(reversed(s_string[idx:])))
print(''.join(stack_list))