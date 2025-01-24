#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (C) Crown Copyright, Met Office. All rights reserved.
#
# This file is part of SciTools Commands and is released under the BSD 3-Clause license.
# See LICENSE in the root of the repository for full licensing details.

import sys
import iris


def stc_cp(ifile, ofile, var='all', att_lim=None, index=None, lim=None,
           p_lev=None, time_sel=None, nc_kwargs=None, eqatt=False):
    """
    stc cp (convert, copy): Copy, extract, combine and convert data.

    Usage:

       stc cp IFILE OFILE
       stc cp IFILE,IFILE2 OFILE1,OFILE2
       stc cp IFILE,IFILE2 OFILE

       The format of OFILE is determined by the suffix (pp, nc or grib).

    Examples

      stc cp fieldsfile   gribfile.grib
      stc cp file1,file2  file12.nc

    STC - SciTools Commands. Use "stc help" to list available commands
    """

    from stc_filter import stc_coordinate_filter
    from stc_load import stc_load

    print(" " + str(ifile) + "  => " + str(ofile))

    if len(ofile) == 1:
        c = stc_load(ifile, var=var, att_lim=att_lim, index=index, lim=lim,
                     p_lev=p_lev, time_sel=time_sel, eqatt=eqatt)
        try:
            iris.save(c, ofile[0], **nc_kwargs)
        except Exception as e:
            raise Exception(e)

    elif len(ofile) == len(ifile):
        for k in range(len(ifile)):
            c = stc_load(ifile[k], var=var, att_lim=att_lim, index=index,
                         lim=lim, p_lev=p_lev, time_sel=time_sel)
            iris.save(c, ofile[k], **nc_kwargs)
