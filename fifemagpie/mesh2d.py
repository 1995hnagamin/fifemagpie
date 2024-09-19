import numpy as np
from collections import namedtuple

Mesh2d = namedtuple("Mesh2d", ("xs", "ys", "vises"))


def nvtx(mesh):
    return mesh.xs.size


def make_square_mesh(nex, ney):
    xs = np.linspace(0, 1, nex + 1)
    ys = np.linspace(0, 1, ney + 1)

    xx, yy = np.meshgrid(xs, ys)
    xx = xx.reshape(((nex + 1) * (ney + 1),))
    yy = yy.reshape(((nex + 1) * (ney + 1),))

    # vertex index sequence list
    vises = np.zeros((nex * ney, 4), dtype=int)
    for iy in range(ney):
        for ix in range(nex):
            k = nex * iy + ix
            lowleft = (nex + 1) * iy + ix
            vises[k] = [lowleft, lowleft + 1, lowleft + nex + 2, lowleft + nex + 1]

    return Mesh2d(xx, yy, vises)


# Quadrilateral
Qlat = namedtuple("Qlat", ("xs", "ys"))


def vise_to_qlat(mesh, vise):
    xs = mesh.xs.take(vise)
    ys = mesh.ys.take(vise)
    return Qlat(xs, ys)
