#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (C) Crown Copyright, Met Office. All rights reserved.
#
# This file is part of SciTools Commands and is released under the BSD 3-Clause license.
# See LICENSE in the root of the repository for full licensing details.

import sys
import iris


def stc_split_precip(ifile, ofile, var='all', att_lim=None, verbose=False,
                     index=None, lim=None, p_lev=None, time_sel=None,
                     nc_kwargs=None):
    """
    stc split_precip: Split accumulated precipitation in time intervals

    Usage:

       stc split_precip IFILE,IFILE2[,...,IFILEN] OFILE

    STC - SciTools Commands. Use "stc help" to list available commands
    """

    from stc_filter import stc_coordinate_filter
    from stc_load   import stc_load

    iris.FUTURE.netcdf_no_unlimited = True

    if var[0] not in ['all', 'precipitation_amount']:
        raise Exception('STC_SPLIT_PRECIP is only intended for ' +
                        'precipitation_amount. Please check your input ' +
                        'arguments of the -var option.')

    if att_lim.stash and att_lim.stash not in ['m01s05i226']:
        raise Exception('STC_SPLIT_PRECIP is only intended for STASH ' +
                        'm01s05i226. Please check your input ' +
                        'arguments of the -stash option.')

    if len(ofile) == 1:

        c0 = stc_load(ifile, var=var, att_lim=att_lim, index=index, lim=lim,
                      p_lev=p_lev, time_sel=time_sel)
        
        c1 = c0.copy()

        # Use implicit assumption that first dimension is forecast_period
        nt = c1.data.shape[0]
        for i in range(1, nt):
            c1.data[i, :, :] = c0.data[i, :, :] - c0.data[i-1, :, :]

        if ofile[0][-6:] == '.grib2':
            # Remove bounds due to GRIB API problem with
            # negative lengthOfTimeRange
            c1.coord('time').bounds = None

        iris.save(c1, ofile[0], **nc_kwargs)

    else:
        raise Exception('Not implemented for multiple output files yet.')
