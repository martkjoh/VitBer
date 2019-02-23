import numpy as np

test = np.array([[1.1, 2,5], [3, 4,8],[6,5,9]])
test1 = np.array([[1.1, 2,4], [3, 4,1],[6,2,9]])


#forstår ikke hva mus er 
def centerRows(Z):
    for row in Z:
        row -= np.mean(row)
    return Z

def whitenRows(Z):
    C = np.cov(Z)
    U, S, _ = np.linalg.svd(C, full_matrices=False)
    T  = U @ np.diag(1 / np.sqrt(S)) @ U.T
    Z_wr = T @ Z
    return Z_wr,T
    
def measure_of_convergence(W1, W2):
    max = -10000008
    for i in range(len(W1)):
        innerProduct = np.absolute(np.dot(W1[i],W2[i].T))
        if (1-innerProduct) > max:
            max = 1-innerProduct       
    return max

print(measure_of_convergence(test,test1))
