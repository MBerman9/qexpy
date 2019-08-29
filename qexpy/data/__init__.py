"""This package contains the data structures and operations for experimental values"""

from .data import MeasuredValue as Measurement
from .datasets import ExperimentalValueArray as MeasurementArray, XYDataSet
from .data import get_covariance, set_covariance, get_correlation, set_correlation
from .operations import sqrt, exp, sin, sind, cos, cosd, tan, tand, sec, secd, cot, cotd, \
    csc, cscd, asin, acos, atan, log, log10, pi, e
