#!/usr/bin/env python3

# (C) Crown Copyright, Met Office. All rights reserved.
#
# This file is part of SciTools Commands and is released under the BSD 3-Clause license.
# See LICENSE in the root of the repository for full licensing details.

import sys
import iris


def stc_add(ifile, ofile, var='all', att_lim=None, verbose=False, index=None,
            show_coord='none', lim=None, p_lev=None, time_sel=None,
            nc_kwargs=None):
    """
    stc add: Add compatible fields from two or more files.

    Usage:

       stc add IFILE,IFILE2[,...,IFILEN] OFILE

    STC - SciTools Commands. Use "stc help" to list available commands
    """

    from stc_filter import stc_coordinate_filter
    from stc_load   import stc_load

    c0 = stc_load(ifile[0], var=var, att_lim=att_lim,
                  index=index, lim=lim, p_lev=p_lev, time_sel=time_sel)
    
    c1 = stc_load(ifile[1], var=var, att_lim=att_lim,
                  index=index, lim=lim, p_lev=p_lev, time_sel=time_sel)
    c3 = c0

    for k in range(0, len(c0)):
        c3[k] = c0[k] + c1[k]

    iris.save(c3, ofile[0], **nc_kwargs)


def stc_div(ifile, ofile, var='all', att_lim=None, verbose=False, index=None,
            show_coord='none', lim=None, p_lev=None, time_sel=None,
            nc_kwargs=None):

    """
    stc div: Divide fields from IFILE1 by fields from IFILE2.

    Usage:

      stc div IFILE1,IFILE2 OFILE

    STC - SciTools Commands. Use "stc help" to list available commands
    """

    from stc_filter import stc_coordinate_filter
    from stc_load   import stc_load


    c0 = stc_load(ifile[0], var=var, att_lim=att_lim,
                  index=index, lim=lim, p_lev=p_lev, time_sel=time_sel)
    
    c1 = stc_load(ifile[1], var=var, att_lim=att_lim,
                  index=index, lim=lim, p_lev=p_lev, time_sel=time_sel)

    c3 = c0

    for k in range(0, len(c0)):
        c3[k] = c0[k] / c1[k]

    iris.save(c3, ofile[0], **nc_kwargs)


def stc_sub(ifile, ofile, var='all', att_lim=None, verbose=False, index=None,
            show_coord='none', lim=None, p_lev=None, time_sel=None,
            nc_kwargs=None):

    """
    stc sub: Substract compatible fields from two or more files.

    Usage:

      stc sub IFILE,IFILE2[,...,IFILEN] OFILE

    STC - SciTools Commands. Use "stc help" to list available commands
    """

    from stc_filter import stc_coordinate_filter
    from stc_load   import stc_load
    

    c0 = stc_load(ifile[0], var=var, att_lim=att_lim,
                  index=index, lim=lim, p_lev=p_lev, time_sel=time_sel)
    
    c1 = stc_load(ifile[1], var=var, att_lim=att_lim,
                  index=index, lim=lim, p_lev=p_lev, time_sel=time_sel)

    try:
        iter(c0)
        iter(c1)
        c3 = c0
        for k in range(0, len(c0)):
            c3[k] = c0[k] - c1[k]
    except TypeError:
        c3 = c0 - c1

    iris.save(c3,ofile[0], **nc_kwargs)



def stc_rdiff(ifile, ofile, var='all', att_lim=None, verbose=False, index=None,
              show_coord='none', lim=None, p_lev=None, time_sel=None,
              nc_kwargs=None):

    """
    stc rdiff: Calculate relative difference from two files, i.e.
               ( IFILE1 - IFILE2 ) / IFILE1.

    Usage:

      stc rdiff IFILE1,IFILE2 OFILE

    STC - SciTools Commands. Use "stc help" to list available commands
    """

    from stc_filter import stc_coordinate_filter
    from stc_load   import stc_load
    
  #  iris.FUTURE.netcdf_no_unlimited = True

    c0 = stc_load(ifile[0], var=var, att_lim=att_lim,
                  index=index, lim=lim, p_lev=p_lev, time_sel=time_sel)
    
    c1 = stc_load(ifile[1], var=var, att_lim=att_lim,
                  index=index, lim=lim, p_lev=p_lev, time_sel=time_sel)

    c3 = c0

    for k in range(0, len(c0)):
        c3[k] = (c0[k] - c1[k]) / c0[k]

    iris.save(c3, ofile[0], **nc_kwargs)
