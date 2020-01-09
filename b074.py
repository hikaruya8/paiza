import numpy as np
import math
n, m = map(int,input().split())
a = list(map(int,input().split()))
q = int(input())
se=[]
while len(se)<q:
    se.append(list(map(int,input().split())))
a_num = np.array(a)
for s in se:
#     print(s)
    k_mean = np.mean(a_num[s[0]-1:s[1]])
#     k_mean = sum(a_num[s[0]-1:s[1]])/s[1]-s[0]+1
#     print(k_mean)
    if k_mean < m:
        a_num[s[0]-1:s[1]] += math.ceil(m - k_mean)
#         print(a_num)
print(*a_num.tolist())