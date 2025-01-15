#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import iris
import warnings


def stc_load(ifile, var='all', att_lim=None, index=None, lim=None,
             p_lev=None, time_sel=None, eqatt=False):

    from stc_filter import stc_coordinate_filter

    cs = stc_coordinate_filter(var, lim, p_lev, att_lim, time_sel)

    # Supress warning to filter "STASH code m??s??i?? was not found"
    warnings.filterwarnings("ignore", category=UserWarning)

    try:
        from iris.experimental.ugrid.load import PARSE_UGRID_ON_LOAD
        ugrid_available = True
    except ImportError:
        ugrid_available = False

    try:
        if ugrid_available:
            c = iris.load_cube(ifile, cs)
        else:
            c = iris.load(ifile, cs)
    except:
        c = iris.load(ifile, cs)

    if index != None:
        c = c[index]

    if eqatt:
        if is_iter(c):
            try:
                from iris.experimental.equalise_cubes import equalise_attributes
                equalise_attributes(c)
                c = c.concatenate_cube()
            except:
                print("STC WARNING: equalising did not work")
                pass
        
    return c


def is_iter(x):
    try:
        iter(x)
        return True
    except:
        return False
