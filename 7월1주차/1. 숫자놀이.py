'''
https://www.acmicpc.net/problem/1755
'''

m, n = map(int, input().split())
num_dict = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
reversed_dict = dict(map(reversed, num_dict.items()))
ans_list = []

#사전 리스트 만들기
for i in range(m, n+1):
    # 한자리 숫자인 경우
    if len(str(i)) == 1:
        ans_list.append([num_dict[str(i)]])
    else:
        ans_list.append([num_dict[str(i)[0]]])
        ans_list[len(ans_list)-1].append(num_dict[str(i)[1]])

# 사전 순으로 정렬
ans_list.sort()

for idx, i in enumerate(ans_list):
    # 10개씩 출력하기
    if (idx+1) % 10 == 0:
        endwith = '\n'
    else:
        endwith = ' '
    # 한자리 숫자인 경우
    if len(i) == 1:
        print(reversed_dict[i[0]], end=endwith)
    else:
        print(reversed_dict[i[0]]+reversed_dict[i[1]], end=endwith)