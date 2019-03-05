V0 = -50
w = 5
V = np.ones(1) * inf
for i in range(w):
    V = np.concatenate((V, np.zeros(n // (2*w + 1)), V0 * np.ones(n // (2*w + 1))))
    

V = np.concatenate((V, np.zeros(n // (2*w + 1) + n % (2*w + 1)), np.ones(1) * inf))

E, phi = solveTUSL(V, x, n)
l = 3
plotEigenfunc(phi**2, V, x, l)

for i in range(l):
    print(E[i] - V[1:-1][i])