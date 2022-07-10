'''
https://www.acmicpc.net/problem/11066
'''

t = int(input())
for i in range(t):
    k = int(input())
    k_list = list(map(int, input().split()))
    k_list.sort()
    print(k_list)
    ans_list = []
    ans = 0

    while len(k_list) > 1:
        print("!!!")
        k_list.sort()
        if len(k_list) % 2 == 0:
            for j in range(0, len(k_list), 2):
                k_list[j] = k_list[j] + k_list[j+1]
                ans += k_list[j] + k_list[j+1]
            print(k_list)
            for j in range(1, len(k_list)+1, 2):
                del k_list[j]
        else:
            for j in range(0, len(k_list)-1, 2):
                k_list[j] = k_list[j] + k_list[j+1]
                ans += k_list[j] + k_list[j+1]
            for j in range(1, len(k_list)-1, 2):
                del k_list[j]
            ans += k_list[-1]
        print("ans:", ans)
    


