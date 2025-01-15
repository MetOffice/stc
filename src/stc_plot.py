#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (C) Crown Copyright, Met Office. All rights reserved.
#
# This file is part of SciTools Commands and is released under the BSD 3-Clause license.
# See LICENSE in the root of the repository for full licensing details.

import sys
import numpy as np


def stc_plot(ifile, ofile, var='all', att_lim=None, index=None, lim=None,
             p_lev=None, ncol=25, clim=None, cmap='auto', title=None,
             maskfile=None, time_sel=None):
    """
    stc plot: Plot 2d data slices.

    Usage:

      stc plot IFILE

      stc plot IFILE [...] -clim CMIN CMAX

      stc plot IFILE [...] -ncol NCOL

      stc plot IFILE [...] -title 'YOUR TITLE'

      stc plot IFILE [...] -cmap 'auto', 'RdYlBu_r' / 'terrain' /
                            'Accent' / ... See also http://goo.gl/51s91K

      stc plot IFILE [...] -mask YOUR_PATH/qrparm.mask

      Handle 2d fields only, use appropriate filter options like -var,
      -pl etc. Use "stc help" for details on available options.

    stc - SciTools Commands. Use "stc help" to list available commands
    """

    import time

    try:
        import matplotlib.pyplot as plt
    except:
        # Avoid problems with missing X server
        import matplotlib
        matplotlib.use('agg')
        import matplotlib.pyplot as plt

    import iris
    import iris.plot as iplt
    import iris.quickplot as qplt

    from stc_filter import stc_coordinate_filter
    from stc_filter import stc_single_filter
    from stc_load   import stc_load

    c = stc_load(ifile, var=var, att_lim=att_lim, index=index, lim=lim,
                 p_lev=p_lev, time_sel=time_sel)

    if is_iter(c):
        raise RuntimeError("""
        At the moment 'stc plot' is only implemented for one variable.
        Please use
           stc info """ + str(ifile)[2:-2] + """
        to check for available varibales and plot with
           stc plot """ + str(ifile)[2:-2] + """ -var VAR_NAME""")

    if maskfile != None:
        constrain = stc_single_filter('all', lim, p_lev, time_sel)
        mask = iris.load_cube(maskfile, constrain)        
        if c.shape != mask.shape:
            raise RuntimeError("Shape from mask and data do not match")
        eps = np.spacing(1)
        c.data = np.ma.masked_where(mask.data < eps, c.data)

    if var == "surface_altitude" and cmap == 'auto':
        # cmap = "terrain"
        # cmap = "gist_earth"
        cdict = {'blue':  [(0.0 , 0.4 , 0.4) , (0.5, 0.6, 0.6),
                           (0.75, 0.33, 0.33), (1.0, 1.0, 1.0)],
                 'alpha': [(0.0 , 1.0 , 1.0) , (0.5, 1.0, 1.0),
                           (0.75, 1.0 , 1.0 ), (1.0, 1.0, 1.0)],
                 'green': [(0.0 , 0.8 , 0.8) , (0.5, 1.0, 1.0),
                           (0.75, 0.36, 0.36), (1.0, 1.0, 1.0)],
                 'red':   [(0.0 , 0.0 , 0.0) , (0.5, 1.0, 1.0),
                           (0.75, 0.5 , 0.5) , (1.0, 1.0, 1.0)]}
        cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap',
                                                         cdict, 256)

    fig = plt.figure()

    if cmap == 'auto':
        iplt.contourf(c, ncol)
    else:
        iplt.contourf(c, ncol, cmap=cmap)

    if clim != None:
        plt.clim(clim[0], clim[1])

    if title != None:
        title = str(title)
        title = title[2:-2]
        plt.title(title)
    else:
        plt.title(ifile)

    cbar = plt.colorbar()

    ofile = str(ofile)
    ofile = ofile[2:-2]
    if len(ofile) == 0:
        iplt.show()
    else:
        if ofile[-4:] in ['.png', '.pdf']:
            fig.savefig(ofile)
        else:
            raise RuntimeError("No support for output file format")


def is_iter(x):
    try:
        iter(x)
        return True
    except:
        return False
