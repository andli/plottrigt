import random
import math
from plottrigt import GenerativePlot
from plottrigt import Projection

def f1(x,y):
    result = random.uniform(-1,1) * x**2  - math.sin(y**2) + abs(y-x)
    return result
def f2(x,y):
    result = random.uniform(-1,1) * y**3 - math.cos(x**2) + 2*x
    return result

gp = GenerativePlot(f1, f2)
gp.generate(seed=829730)
gp.plot(color="white", bgcolor="black", projection=Projection.POLAR)
#gp.save()
gp.show()