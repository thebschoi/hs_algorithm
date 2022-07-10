'''
https://www.acmicpc.net/problem/1120
'''
a, b = map(str, input().split())

if a in b:
    print(0)
else:
    gap = len(b) - len(a) + 1
    ans_list = []
    for i in range(gap):
        s_str = b[i:i+len(a)]
        tmp_ans = 0
        for j in range(len(a)):
            if a[j] != s_str[j]:
                tmp_ans += 1
        ans_list.append(tmp_ans)
    print(min(ans_list))