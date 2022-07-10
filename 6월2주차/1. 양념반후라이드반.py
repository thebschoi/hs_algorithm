'''
https://www.acmicpc.net/problem/16917
'''
p_s, p_f, p_h, num_s, num_f = map(int, input().split())
ans1 = p_s*num_s + p_f*num_f
ans2 = 2*p_h*max(num_s, num_f)
'''
if (num_s > num_f):
    ans3 = 2 * p_h * num_f + p_s * (num_s-num_f)
else:
    ans3 = 2 * p_h * num_s + p_f * (num_f-num_s)
'''
ans3 = 2 * p_h * min(num_s, num_f) + p_s*max(0, num_s-num_f) + p_f*max(0, num_f-num_s)
ans = min(ans1, ans2, ans3)
print(ans)