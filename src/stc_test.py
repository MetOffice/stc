#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (C) Crown Copyright, Met Office. All rights reserved.
#
# This file is part of SciTools Commands and is released under the BSD 3-Clause license.
# See LICENSE in the root of the repository for full licensing details.

import sys
import iris

def stc_test( ifile, var='all', att_lim=None, verbose=False, index=None, show_coord='none',
              lim=None, p_lev=None, time_sel=None, nc_kwargs=None):
    """
    stc test: Dummy function for debugging and fast prototyping

      Use for initial tests only. Implement general things properly!

    STC - SciTools Commands. Use "stc help" to list available commands
    """
    from stc_filter import stc_coordinate_filter
    from stc_load import stc_load
    
    iris.FUTURE.netcdf_no_unlimited = True

    c = stc_load(ifile, var=var, att_lim=att_lim, index=index, lim=lim,
                 p_lev=p_lev, time_sel=time_sel)

    print(c)
