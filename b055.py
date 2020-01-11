import numpy as np
import math


n, x = map(int,input().split())

listA=[] #appendのために宣言が必要
while len(listA)<n:
    try:
        listA.append(list(map(int,input().split())))

    except:
        break;
        #または、quit(),os.exit()をして止める。

unchin_list = np.array(listA)
# print(unchin_list)

hatsunori_ryokin = np.zeros(n, dtype=int)
for i,z in enumerate(hatsunori_ryokin):
    hatsunori_ryokin[i] = unchin_list[i][1]

hatsunori_kyori = np.zeros(n, dtype=int)
for i,z in enumerate(hatsunori_kyori):
    hatsunori_kyori[i] = unchin_list[i][0]

kasan_kyori = np.zeros(n, dtype=int)
for i,z in enumerate(kasan_kyori):
    kasan_kyori[i] = unchin_list[i][2]

kasan_ryokin = np.zeros(n, dtype=int)
for i,z in enumerate(kasan_ryokin):
    kasan_ryokin[i] = unchin_list[i][3]

# for i, ul in enumerate(unchin_list):
#     for u in ul:
#         if zissai_unchin<x:
#             [i] += u
#             break

# print('初乗り距離:{}'.format(hatsunori_kyori))
# print('初乗り料金:{}'.format(hatsunori_ryokin))
# print('加算距離:{}'.format(kasan_kyori))
# print('加算料金:{}'.format(kasan_ryokin))

result_ryokin = np.zeros(n, dtype=int)
result_kyori = np.zeros(n, dtype=int)

#最安値を求める
for i, (hk, hr, kk, kr) in enumerate(zip(hatsunori_kyori, hatsunori_ryokin, kasan_kyori, kasan_ryokin)):
    result_ryokin[i] = hr
    result_kyori[i] = hk
    # if result_kyori[i]>x:
    #     continue
    # elif result_kyori[i]<=x:

    while result_kyori[i]<=x:
        result_ryokin[i] += kr
        result_kyori[i] += kk
    # import pdb;pdb.set_trace()

# print(result_ryokin.max())
print("{} {}".format(result_ryokin.min(), result_ryokin.max()))




