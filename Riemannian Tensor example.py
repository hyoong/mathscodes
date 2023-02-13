import sympy as sp, numpy as np

def Riemann_tensor(g):
    n = g.shape[0]
    R = sp.zeros(n, n, n, n)
    x, y = sp.symbols('x y')
    g_sym = sp.Matrix(g)
    g_inv = g_sym.inv()
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    R[i, j, k, l] = sp.diff(sp.diff(g_inv[i, k], x), y) * g_inv[j, l]
                    + sp.diff(sp.diff(g_inv[i, l], x), y) * g_inv[j, k]
                    - sp.diff(sp.diff(g_inv[i, j], x), y) * g_inv[k, l]
    return R

g = np.array([[1, 0], [0, 1]])
R = Riemann_tensor(g)
