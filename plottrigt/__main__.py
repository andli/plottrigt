# -*- coding: utf-8 -*-
"""Plottrigt main entry."""

from plottrigt.genplot import GenerativePlot
from .params import PLOTTRIGT_VERSION, Projection

def f1(x,y):
    result = random.uniform(-1,1) * x**2  - math.sin(y**2) + abs(y-x)
    return result

def f2(x,y):
    result = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
    return result

if __name__ == "__main__":

    gp = GenerativePlot(f1,f2)
    gp.generate(seed=829730)
    gp.plot(projection=Projection.POLAR)
    gp.show()

