import numpy as np
def LU(A):
    """
    对A进行LU分解，并求A的逆矩阵
    """
    m = A.shape[0]
    L = np.zeros((m, m))
    U = np.zeros((m, m))
    for i in range(m):
        L[i, i] = 1  # Set diagonal of L to 1
    for j in range(m):
        U[0, j] = A[0, j]
    for i in range(m):
        L[i, 0] = A[i, 0] / U[0, 0] 
    for k in range(1,m):
        for j in range(k, m):
            U[k, j] = A[k, j]  # Initialize U[k, j] directly
            for t in range(k):
                U[k, j] -= L[k, t] * U[t, j]
            
        for i in range(k+1, m):
            L[i, k] = A[i, k]
            for t in range(k):
                L[i, k] -= L[i, t] * U[t, k]
            L[i,k] /= U[k, k]
    U_inv = np.zeros((m, m))
    L_inv = np.zeros((m, m))
    for i in range(m):
        L_inv[i, i] = 1
        U_inv[i, i] = 1 / U[i, i]
    # 计算L的逆矩阵
    for j in range(m):
        for i in range(j+1, m):
            for t in range(j+1):
                L_inv[i, j] -= L[i, t] * L_inv[t, j]
    # print("L逆矩阵:\n", L_inv)
    # 计算U的逆矩阵
    for j in range(m):
        for i in range(j-1, -1, -1):
            for t in range(i+1, m):
                U_inv[i, j] -= U[i, t] * U_inv[t, j]
            U_inv[i, j] /= U[i, i]
    # print("U逆矩阵:\n", U_inv)
    # print("L矩阵:\n", L)
    # print("U矩阵:\n", U)
    # 计算A的逆矩阵
    A_inv = U_inv @ L_inv
    # print("逆矩阵:\n", A_inv)
    return A_inv

A = [[2, 1], [1, 2]]     # 理论逆矩阵: [[2/3, -1/3], [-1/3, 2/3]]
    

A = np.array(A)

LU(A)
