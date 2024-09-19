import numpy as np

def gauss4(weights, xs, ys, f):
    np.sum(np.array([w * f(x, y) for w, x, y in zip(weights, xs, ys)]))
