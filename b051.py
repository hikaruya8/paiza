import numpy as np
import math

n = int(input())
listA=[] #appendのために宣言が必要
while len(listA)<n:
    try:
        listA.append(list(map(int,input().split())))

    except:
        break;
        #または、quit(),os.exit()をして止める。

init_matrix = np.array(listA)
# print("最初の魔法陣:\n{}".format(init_matrix))

# sum_list = np.concatenate([matrix_yoko_sum, matrix_tate_sum, matrix_taikaku_sum])
# print(sum_list)

for im in init_matrix:
    if np.any(im==0):
        continue
    else:
        tate_sum = np.sum(im)
        break

if tate_sum is not None:
    result_sum = tate_sum

elif tate_sum is None:
    for im in init_matrix.T:
        if np.any(im==0):
            continue
        else:
            yoko_sum = np.sum(im)
            break

        if yoko_sum is not None:
            result_sum = yoko_sum

else:
    result_sum = np.sum(np.diag(init_matrix))

# print(result_sum)

# index_list = []
# for im in init_matrix:
#     index_0 = [i for i, x in enumerate(im) if x==0]
#     index_list.append(index_0)
# print(index_list)

# for i, im in enumerate(init_matrix):
#     if (np.count_nonzero(im==0)) == 1:
#         init_matrix[i] = np.where(im==0, result_sum-np.sum(im), im)
#     elif (np.count_nonzero(im==0)) == 0:
#         continue
#     else:
#         continue

if np.any(init_matrix==0):
    result_matrix = init_matrix.T
    for i, im in enumerate(result_matrix):
        if (np.count_nonzero(im==0)) == 1:
            result_matrix[i] = np.where(im==0, result_sum-np.sum(im), im)
            # import pdb;pdb.set_trace()
        elif (np.count_nonzero(im==0)) == 0:
            continue
        else:
            continue

    for im in result_matrix.T:
        print(*im)

else:
    for im in init_matrix:
        print(*im)


