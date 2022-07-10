'''
https://www.acmicpc.net/problem/2644
'''
# 입력받기
n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
rel_list = []
for i in range(m):
    x, y = map(int, input().split())
    rel_list.append([x, y])

# 촌수마스터 dict
rel_mst_dict = {}
for i in range(1, n+1):
    rel_mst_dict[str(i)] = []

for i in rel_list:
   rel_mst_dict[str(i[0])].append(i[1])

for i in rel_mst_dict:
    print(i, rel_mst_dict[i])