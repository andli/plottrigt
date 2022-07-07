import itertools
import matplotlib
import random
import matplotlib.pyplot as matplt

from .params import *

class GenerativePlot:

    def __init__(self, f1=None, f2=None):
        self._set_params(self, f1, f2)

        #if self.f1 is None:
        #    if self.f1_str is None:
        #        self.f1_str = random_equation_gen()
        #    self.f1 = eval("lambda x,y:" + self.f1_str)
        #if self.f2 is None:
        #    if self.f2_str is None:
        #        self.f2_str = random_equation_gen()
        #    self.f2 = eval("lambda x,y:" + self.f2_str)

    def generate(
            self,
            seed=None,
            start=None,
            step=None,
            stop=None):

        if g.seed is None:
            seed = random.randint(SEED_LOWER_BOUND, SEED_UPPER_BOUND)

        self.data1 = []
        self.data2 = []
        range1 = list(float_range(self.start, self.stop, self.step))
        range2 = list(float_range(self.start, self.stop, self.step))
        range_prod = list(itertools.product(range1, range2))
        for point in range_prod:
            try:
                fill_data(self, point)
            except Exception as e:
                print(e.message())


    def plot(self, size=None, projection=None, linewidth=None):
        fig = matplt.figure()
        fig.set_size_inches(self.size[0], self.size[1])
        ax = fig.add_subplot(111, projection=self.projection)
        ax.scatter(
            self.data2,
            self.data1,
            alpha=self.alpha,
            c=self.color,
            s=self.spot_size,
            lw=self.linewidth)
        ax.set_axis_off()
        ax.patch.set_zorder(-1)
        ax.add_artist(ax.patch)
        self.fig = fig

    def show():
        matplt.show()

    def _set_params(gp, f1, f2):
        gp.f1 = f1
        gp.f1_str = None
        gp.f2 = f2
        gp.f2_str = None
        gp.fig = None
        gp.seed = None
        gp.start = DEFAULT_START
        gp.step = DEFAULT_STEP
        gp.stop = DEFAULT_STOP
        gp.data1 = None
        gp.data2 = None
        gp.size = DEFAULT_IMAGE_SIZE
        gp.projection = DEFAULT_PROJECTION
        gp.linewidth = DEFAULT_LINEWIDTH

def float_range(start, stop, step):
    while start < stop:
        yield float(start)
        start += step

def fill_data(g, point):
    """
    Fill data with functions in given points.

    :param g: generative image instance
    :type g: GenerativeImage
    :param point: given point
    :type point: tuple
    :return: false if some exception occurred
    """
    random.seed(g.seed)
    try:
        data1_ = g.function1(point[0], point[1]).real
        data2_ = g.function2(point[0], point[1]).real
    except Exception:
        return False
    g.data1.append(data1_)
    g.data2.append(data2_)