import numpy as np

def normalize_rownorms(Z):
    for i in range(len(Z)):
        Z[i] = Z[i] / np.sqrt(Z[i] @ Z[i])
    return Z

def decorrelate_weights(W):
    def inverse_sqrt(A):
        U, S, _ = np.linalg.svd(A, full_matrices=False)
        return U @ np.diag(1 / np.sqrt(S)) @ U.T

    return inverse_sqrt(W @ W.T) @ W

Z = np.ones((3, 3))
Z = np.array([[1.5, 2., 1], [2, 4, 3.4], [1, 7.4, 3]])

print(decorrelate_weights(Z))
