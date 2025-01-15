#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import iris


def stc_ls(ifile, var='all', att_lim=None, verbose=False, index=None,
           show_coord='none', lim=None, p_lev=None, time_sel=None, eqatt=None):
    """
   stc ls (info): List information about file content.

    Usage:

      stc ls IFILE[,IFILE2,...]

      stc ls IFILE -ind index
          Select variable index

      stc ls IFILE -v
          Use verbose mode

      stc ls IFILE -coord [time|level|height|model_level_number|
                           grid_latitude|grid_longitude|altitude]

    stc - SciTools Commands. Use "stc help" to list available commands
    """

    from stc_filter import stc_coordinate_filter
    from stc_load   import stc_load

    c = stc_load(ifile, var=var, att_lim=att_lim, index=index, lim=lim,
                     p_lev=p_lev, time_sel=time_sel, eqatt=eqatt)
    
    if is_iter(c):
        k = 0
        for my_cube in c:
            print_cube(k, my_cube, verbose, show_coord)
            k += 1
    else:
        print_cube(0, c, verbose, show_coord)


def is_iter(x):
    try:
        iter(x)
        return True
    except:
        return False


def print_cube(k, c, verbose, show_coord):

    if verbose:
        print(str(k) + ": " + str(c))
    else:
        print(str(k) + ": " + str(c).splitlines()[0])

    if show_coord[0] in ['time']:
        coord = c.coord(show_coord[0])
        for my_coord in coord:
            print(my_coord)
    elif show_coord[0] in ['grid_longitude',
                           'grid_latitude',
                           'latitude',
                           'longitude',
                           'model_level_number',
                           'pressure']:
        coord = c.coord(show_coord[0])
        for my_coord in coord:
            print(str(my_coord.points))
    elif show_coord[0] in ['forecast_period',
                           'forecast_reference_time',
                           'heigth',
                           'level_heigth']:
        coord = c.coord(show_coord[0])
        for my_coord in coord:
            print(str(my_coord.points) + " " + str(my_coord.bounds))
    elif show_coord == 'none':
        pass
    else:
        raise Exception('Coordinate lookup not implemented for ' +
                        show_coord[0])

    if show_coord[0] in ['time', 'level_heigth', 'heigth']:
        print('---')
