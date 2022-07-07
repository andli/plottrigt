import itertools
import matplotlib
import random
import matplotlib.pyplot as matplt

from .params import *

class GenerativePlot:

    def __init__(self, f1=None, f2=None):
        matplotlib.use("TkAgg")
        _set_params(self, f1, f2)

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
        if step is not None:
            self.step = step
        if seed is None:
            seed = random.randint(SEED_LOWER_BOUND, SEED_UPPER_BOUND)
        self.seed = seed

        self.data1 = []
        self.data2 = []
        range1 = list(float_range(self.start, self.stop, self.step))
        range2 = list(float_range(self.start, self.stop, self.step))
        range_prod = list(itertools.product(range1, range2))
        for point in range_prod:
            try:
                fill_point_data(self, point)
            except Exception as e:
                print(e.message())
        print(f"{len(range_prod)} points generated.")


    def plot(self, color=None, bgcolor=None, projection=None, linewidth=None):
        if color is not None:
            self.color = color
        if bgcolor is not None:
            self.bgcolor = bgcolor
        if projection is not None:
            self.projection = projection.value
        if linewidth is not None:
            self.linewidth = linewidth

        figure = matplt.figure()
        figure.set_size_inches(self.size[0], self.size[1]) #TODO: only in inches...
        ax = figure.add_subplot(111, facecolor=self.bgcolor, projection=self.projection)
        ax.scatter(
            self.data2,
            self.data1,
            c=self.color,
            alpha=self.alpha,
            s=self.spot_size,
            lw=self.linewidth)
        ax.set_axis_off()
        ax.patch.set_zorder(-1)
        ax.add_artist(ax.patch)
        self.figure = figure

    def show(self):
        matplt.interactive(False)
        matplt.show()
    
    def save_svg(self):
        matplt.savefig("test.svg", format="svg")

def _set_params(gp, f1, f2):
    gp.f1 = f1
    gp.f1_str = None
    gp.f2 = f2
    gp.f2_str = None
    gp.figure = None
    gp.seed = None
    gp.start = DEFAULT_START
    gp.stop = DEFAULT_STOP
    gp.step = DEFAULT_STEP
    gp.data1 = None
    gp.data2 = None
    gp.color = DEFAULT_COLOR
    gp.bgcolor = DEFAULT_BACKGROUND_COLOR
    gp.spot_size = DEFAULT_SPOT_SIZE
    gp.alpha = DEFAULT_ALPHA
    gp.depth = DEFAULT_DEPTH
    gp.size = DEFAULT_IMAGE_SIZE
    gp.projection = DEFAULT_PROJECTION
    gp.linewidth = DEFAULT_LINEWIDTH

def float_range(start, stop, step):
    while start < stop:
        yield float(start)
        start += step

def fill_point_data(g, point):
    random.seed(g.seed)
    try:
        data1_ = g.f1(point[0], point[1]).real
        data2_ = g.f2(point[0], point[1]).real
    except Exception as e:
        print(e)
        return False
    g.data1.append(data1_)
    g.data2.append(data2_)