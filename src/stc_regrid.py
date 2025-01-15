#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys
import iris


def stc_regrid(ifile, ofile,
               target_grid='n2004', target_lat=None, target_lon=None,
               var='all', att_lim=None, index=None, lim=None,
               p_lev=None, time_sel=None, nc_kwargs=None):
    """
    stc regrid: Regrid to data to a target grid (default lon lat)

      stc regrid IFILE OFILE

      stc regrid [...] -tgrid FILE_WITH_TARGET_GRID
                              default: lsm for n2004 from $UMDIR

      stc regrid [...] -tlon  LON_MIN LON_MAX
                              longitute limits for target grid

      stc regrid [...] -tlat  LAT_MIN LAT_MAX
                              latitude limits for target grid

    STC - SciTools Commands. Use "stc help" to list available commands
    """

    # load data

    from stc_filter import stc_coordinate_filter
    from stc_load   import stc_load
    
    iris.FUTURE.netcdf_no_unlimited = True

    c = stc_load(ifile, var=var, att_lim=att_lim, index=index, lim=lim,
                 p_lev=p_lev, time_sel=time_sel)

    # load target grid from file

    cs_target = iris.Constraint()

    if target_lat != [None, None]:
        cs_target = cs_target & iris.Constraint(latitude =
                                                lambda lat: target_lat[0] <= lat <= target_lat[1])
    if target_lon != [None, None]:
        cs_target = cs_target & iris.Constraint(longitude =
                                                lambda lon: target_lon[0] <= lon <= target_lon[1])

    if not isinstance(target_grid, basestring):
        target_grid = target_grid[0]

    if os.path.isfile(target_grid):
        grid_file = target_grid
    else:
        s = str(os.environ.get('UMDIR') + '/ancil/atmos/' + target_grid + '/land_sea_mask/igbp/v1/')
        if os.path.isfile(s + 'qrparm.mask'):
            grid_file = s + 'qrparm.mask'
        elif os.path.isfile(s + 'qrparm.coastdist'):
            grid_file = s + 'qrparm.coastdist'
        elif os.path.isfile(s + 'qrparm.landfrac'):
            grid_file = s + 'qrparm.landfrac'
        else:
            raise RuntimeError("File with target grid not found")

    c_target = iris.load_cube(grid_file, cs_target)

    # interpolate and save

    scheme = iris.analysis.Linear(extrapolation_mode='mask')

    if is_iter(c):
        c_regrid = c
        k = 0
        for my_cube in c:
            c_regrid[k] = my_cube.regrid(c_target, scheme)
            k += 1
    else:
        c_regrid = c.regrid(c_target, scheme)

    iris.save(c_regrid, ofile[0], **nc_kwargs)


def is_iter(x):
    try:
        iter(x)
        return True
    except:
        return False
