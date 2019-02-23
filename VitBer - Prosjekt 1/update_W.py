import numpy as np

def Gfunc(u):
    return 4 * u **3 
def GderivativeFunc (u):
    return 12 * u **2

def update_W(W, Zcw):
    d = W.size() 
    N = W[0].size()
    S = W @ Zcw  
    G = Gfunc(S)
    Gderivative = GderivativeFunc(S)
    
    averageOfRowsInGDerivative = np.zeros(d)
    for i in range(d-1):
        averageOfRowsInGDerivative[i] = np.mean(W[i])
    diagonalMatrix = np.diag(averageOfRowsInGDerivative)  #Lager diagonal matrise med averageOfRows.. på diagonalen, resten 0.
   
    WPlus = 1 / N * G * np.transpose(Zcw) -  np.diag(averageOfRowsInGDerivative) @ W
    
    WPlusNormalized = np.zeros(shape = (d,d))
    for i in range(d-1):
        WPlusNormalized[i] = WPlus[i] / np.sum(WPlus)
    
    WKPlusOne = inverse_sqrt((WPlus @ np.transpose(Wplus))) @ np.transpose(WPlus) 

    return WKPlusOne 

    """Calculates W_k+1 from W_k.
    So the input is W=W_k (d x d) as well as the centered, whitened data Zcw (dxN known as tilde{x} in the note)
    Output is the new W (W_{k+1}).
    
    This function does the two iteration steps in the note: The optimisation step and the 
    orthogonalisation (decorrelation) step. The first step you need to code, the orthogonalisation is already
    provided by the function decorrelate_weights that needs to be called.
    You can use the kurtosis version, i.e. G(u)=4*(u**3) and its derivative. Don't include the while-loop in 
    this function
    """