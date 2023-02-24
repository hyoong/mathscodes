import numpy as np
from scipy.misc import derivative


def Riemann_tensor(g):
    n = g.shape[0]
    R = np.zeros((n, n, n, n))
    g_inv = np.linalg.inv(g)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):

                    def f(x):
                        return g_inv[i, k] * g_inv[j, l] * x

                    R[i, j, k, l] = derivative(f, 0, dx=1e-6)
    return R


g = np.array([[1, 0], [0, -1]])
R = Riemann_tensor(g)
print(R)
