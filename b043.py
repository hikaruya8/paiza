import numpy as np
import math

h, w = map(int,input().split())
h0, w0 = map(int,input().split())

listA=[] #appendのために宣言が必要
while len(listA)<h:
    try:
        listA.append(list(map(str,input().split())))

    except:
        break;
        #または、quit(),os.exit()をして止める。

init_matrix = []
for l in listA:
    for a in l:
        init_matrix.append(list(a))

init_matrix = np.array(init_matrix)
matrix = init_matrix

h0 = h0-1
w0 = w0-1
nezumi_init = [h0, w0]
print(init_matrix)
print(nezumi_init)

hugou_houkou = [[1,0], [0,1], [0,-1],[-1,0]]
syomin_houkou = [[-1,0], [0,-1], [1,0],[0,1]]
i_hugou = 4
i_syomin = 4

while True:
    if matrix[h0][w0]=='*':
        matrix[h0][w0]='.'
        i_hugou+=1
        i_hugou = i_hugou + i_hugou%4

    else:
        matrix[h0][w0]='*'