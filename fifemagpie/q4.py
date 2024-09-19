# Bilinear quadrilateral elements (Q4)

import numpy as np
import mesh2d


def func_to_q4(mesh, func):
    n = mesh2d.nvtx(mesh)
    return np.array([func(mesh.xs[i], mesh.ys[i]) for i in range(n)])


def _eval_at_qlat(mesh, k, fel, x, y):
    vise = mesh.vises[k]
    qlat = mesh2d.vise_to_qlat(mesh, vise)
