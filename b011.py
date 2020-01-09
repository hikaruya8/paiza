import numpy as np
n, m = map(int, input().split())
binder_matrix = np.arange(2*n).reshape(2,n)
binder_matrix[1] = np.flip(binder_matrix[1])
binder_matrix += m

print(binder_matrix)