import numpy as np
from scipy.sparse import dok_matrix
import fifemagpie as fem

ndiv = 10
Th = fem.mesh2d.make_square_mesh(ndiv, ndiv)


def N(xi, et):
    return np.array(
        [
            (1 - xi) * (1 - et) / 4,
            (1 + xi) * (1 - et) / 4,
            (1 + xi) * (1 + et) / 4,
            (1 - xi) * (1 + et) / 4,
        ]
    )


def dNdxiet(xi, et):
    return np.array(
        [
            [-(1 - et) / 4, +(1 - et) / 4, +(1 + et) / 4, -(1 + et) / 4],
            [-(1 - xi) / 4, -(1 + xi) / 4, +(1 + xi) / 4, +(1 - xi) / 4],
        ]
    )


# [dx/dxi dx/det; dy/dxt dy/det]
def dxydxiet(qlat, xi, et):
    dx = dNdxiet(xi, et).dot(qlat.xs)
    dy = dNdxiet(xi, et).dot(qlat.ys)
    return np.array([dx, dy])


def make_coeff_matrix(th):
    n = fem.mesh2d.nvtx(th)
    dok = dok_matrix((n, n), dtype=np.float64)
    for vise in th.vises:
        qlat = fem.mesh2d.vise_to_qlat(th, vise)
        for i in range(4):
            for j in range(4):
                dok[vise[i], vise[j]] += 1
    return dok.tocsr()


# print(make_coeff_matrix(Th))
