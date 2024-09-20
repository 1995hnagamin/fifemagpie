from scipy.sparse import lil_matrix
import fifemagpie as fem

ndiv = 10
Th = fem.mesh2d.make_square_mesh(ndiv, ndiv)
print(Th)

def make_coeff_matrix(th):
    n = fem.mesh2d.nvtx(th)
    lil = lil_matrix((n, n), dtype=np)
    for vise in th.vises:
        qlat = fem.mesh2d.vise_to_qlat(vise)        
