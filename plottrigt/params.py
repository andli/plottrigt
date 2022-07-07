# -*- coding: utf-8 -*-
"""Plottrigt params."""
import math
from enum import Enum

PLOTTRIGT_VERSION = "0.1"  # pragma: no cover

DEFAULT_START = -1 * math.pi
DEFAULT_STOP = math.pi
DEFAULT_STEP = 0.01
DEFAULT_LINEWIDTH = 0.8
DEFAULT_IMAGE_SIZE = (10, 10)
DEFAULT_PROJECTION = "rectilinear"
SEED_LOWER_BOUND = 0
SEED_UPPER_BOUND = 2**20

class Projection(Enum):
    DEFAULT = DEFAULT_PROJECTION
    POLAR = "polar"
    AITOFF = "aitoff"
    HAMMER = "hammer"
    LAMBERT = "lambert"
    MOLLWEIDE = "mollweide"
    RECTILINEAR = "rectilinear"
    RANDOM = "random"

RANDOM_COEF_LIST = [
    "random.uniform(-1,1)",
    "random.gauss(0,1)",
    "random.betavariate(1,1)",
    "random.gammavariate(1,1)",
    "random.lognormvariate(0,1)"]

ELEMENTS_LIST = [
    "{0}*math.atan({1})",
    "{0}*math.asinh({1})",
    "{0}*math.acosh(abs({1})+1)",
    "{0}*math.erf({1})",
    "{0}*math.sqrt(abs({1}))",
    "{0}*math.log(abs({1})+1)",
    "{0}*math.tanh({1})",
    "{0}*math.cos({1})",
    "{0}*math.sin({1})",
    "{0}*{1}",
    "{0}*abs({1})",
    "{0}*math.ceil({1})",
    "{0}*math.floor({1})"]

ARGUMENTS_LIST = [
    "x*y",
    "x",
    "y",
    "y-x",
    "x-y",
    "x+y",
    "x**3",
    "y**3",
    "x**2",
    "y**2",
    "(x**2)*y",
    "(y**2)*x",
    "(x**2)*(y**3)",
    "(x**3)*(y**2)",
    "x*(y**3)",
    "y*(x**3)"]

OPERATORS_LIST = ["+", "-", "*", "/"]
