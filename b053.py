import numpy as np
import math

listA=[] #appendのために宣言が必要
while True:
    try:
        listA.append(list(map(int,input().split())))

    except:
        break;
        #または、quit(),os.exit()をして止める。

gyo = listA[0][0]
retsu = listA[0][1]

gyounosa = listA[2][0]-listA[1][0]
retsunosa = listA[1][1]-listA[1][0]

hyo = np.zeros((gyo, retsu), dtype=int)

print(gyounosa)
print(retsunosa)
print(hyo)

hyo[0][0] += listA[1][0]
# hyo[0][1] += listA[1][1]
# hyo[1][0] += listA[2][0]
# hyo[1][1] += listA[2][1]

print(hyo)

for i, h in enumerate(hyo):
    if i>0:
        h[0] = hyo[i-1][0]+gyounosa

print(hyo)

for i, h in enumerate(hyo[0]):
    if i>0:
        hyo[0][i] = hyo[0][i-1] + retsunosa

hyooo = hyo.tolist()
for h in hyooo:
    print(*h)
# for i, h in enumerate(hyo):
#     for i, l in enumerate(h):


