import numpy as np

def matrix_transpose(A):
    A = np.asarray(A)
    n, m = A.shape
    temp = np.zeros((m , n), dtype = A.dtype)
    for i in range(m):
        for j in range(n):
            temp[i][j] = A[j][i]

    return temp