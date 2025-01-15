#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import iris


def stc_coordinate_filter(name, lim, p_lev, att_lim, time_sel):

    cs = [None] * len(name)
    for k in range(len(name)):
        cs[k] = stc_single_filter(name[k], lim, p_lev, time_sel)

        if att_lim.stash != None:
            stash = att_lim.stash.split(',')
            cs[k] = cs[k] & iris.AttributeConstraint(STASH =
                                                     lambda s: s in stash)

        if att_lim.um_version != None:
            version = att_lim.um_version[0]
            cs[k] = cs[k] & iris.AttributeConstraint(um_version =
                                                     lambda um: um == version)

    return cs


def stc_single_filter(name, lim, p_lev, time_sel):

    from iris.time import PartialDateTime as pdt

    cs = iris.Constraint()

    if name != 'all':
        cs = cs & iris.Constraint(name = name)

    if lim.pl != [None, None]:
        cs = cs & iris.Constraint(pressure =
                                  lambda p: lim.pl[0] <=  p <= lim.pl[1])

    if lim.fcp != [None, None]:
        cs = cs & iris.Constraint(forecast_period =
                                  lambda fcp: lim.fcp[0] <= fcp <= lim.fcp[1])

    if lim.ml != [None, None]:
        cs = cs & iris.Constraint(model_level_number =
                                  lambda ml: lim.ml[0] <= ml <= lim.ml[1])

    if lim.lh != [None, None]:
        cs = cs & iris.Constraint(level_heigth =
                                  lambda lh: lim.lh[0] <= lh <= lim.lh[1])

    if lim.lat != [None, None]:
        cs = cs & iris.Constraint(latitude =
                                  lambda lat: lim.lat[0] <= lat <= lim.lat[1])

    if lim.lon != [None, None]:
        cs = cs & iris.Constraint(longitude =
                                  lambda lon: lim.lon[0] <= lon <= lim.lon[1])

    if lim.sl != [None, None]:
        cs = cs & iris.Constraint(soil_model_level_number =
                                  lambda sml: lim.sl[0] <= sml <= lim.sl[1])

    if p_lev != None:
        p_lev = [int(x) for x in p_lev.split(',')]
        cs = cs & iris.Constraint(pressure =
                                  lambda p: p in p_lev)
        
    if time_sel.YYYY != [None]:
        years = [pdt(year=int(time_sel.YYYY[i])) for i in range(len(time_sel.YYYY))]
        cs =  cs & iris.Constraint(time = lambda t: t in years)
            
    if time_sel.MM != [None]:
        months = [pdt(month=int(time_sel.MM[i])) for i in range(len(time_sel.MM))]
        cs =  cs & iris.Constraint(time = lambda t: t in months)
        
    if time_sel.DD != [None]:
        days = [pdt(day=int(time_sel.DD[i])) for i in range(len(time_sel.DD))]
        cs = cs & iris.Constraint(time = lambda t: t in days)
        
    if time_sel.hh != [None]:
        hours = [pdt(hour=int(time_sel.hh[i])) for i in range(len(time_sel.hh))]
        cs = cs & iris.Constraint(time = lambda t: t in hours)

    if time_sel.mm != [None]:
        minutes = [pdt(minute=int(time_sel.mm[i])) for i in range(len(time_sel.mm))]
        cs = cs & iris.Constraint(time = lambda t: t in minutes)
 
    if time_sel.ss != [None]:
        seconds = [pdt(second=int(time_sel.ss[i])) for i in range(len(time_sel.ss))]
        cs = cs & iris.Constraint(time = lambda t: t in seconds)

    if time_sel.sss != [None]:
        microseconds = [pdt(microsecond=int(time_sel.sss[i])) for i in range(len(time_sel.sss))]
        cs = cs & iris.Constraint(time = lambda t: t in microseconds)     
        
    return cs
