## stc - SciTools Commands

**[stc](https://github.com/MetOffice/stc)** allows simple file manipulation and listing with the following syntax:

```
stc COMMAND IFILE1[,IFILE2,...] [OFILE1[,OFILE2,...]] [-OPTION1 ARG1] [-OPTION2 ARG2]
```

### Subcommands

The follwing commands are avalble:

```
   add                  Add fields from two files
   cp                   Copy, extract, combine and convert data
   div                  Divide fields from two files
   help                 Print help
   ls                   List information from file
   plot                 Plot 2d data slices
   rdiff                Calculate relative difference between to files
   regrid               Regrid fields from file
   split_precip         Split accumulated precipitation in time intervals
   sub                  Subtract fields from two files
   stc help SUBCOMMAND  Print detailed help
```

See [cp](https://github.com/MetOffice/stc/blob/main/doc/stc_cp.md), [div](https://github.com/MetOffice/stc/blob/main/doc/stc_div.md), [ls](https://github.com/MetOffice/stc/blob/main/doc/stc_ls.md), [plot](https://github.com/MetOffice/stc/blob/main/doc/stc_plot.md), [rdiff](https://github.com/MetOffice/stc/blob/main/doc/stc_rdiff.md), [regrid](https://github.com/MetOffice/stc/blob/main/doc/stc_regrid.md), [split_precip](https://github.com/MetOffice/stc/blob/main/doc/stc_split_precip.md), and [sub](https://github.com/MetOffice/stc/blob/main/doc/stc_sub.md) for details. 

### Filter options

Filter options allow to operated on subsets of the input data. The availble filter options are:

```
   stc [...]
    -fcp   FCP_MIN FCP_MAX            Filter by forecast period
    -lat   LAT_MIN LAT_MAX            Filter by latitude
    -lh    L_HEIGTH_MIN L_HEIGTH_MAX  Filter by level heigth
    -lon   LON_MIN LON_MAX            Filter by longitude
    -ml    ML_MIN  ML_MAX             Filter by model level
    -pl    P_MIN   P_MAX              Filter by pressure level limits
    -plev  P_LEV1[,P_LEV2,...]        Filter by pressure level list
    -sl    SL_MIN  SL_MAX             Filter by soil level
    -stash m??s??i???,[m??s??i???]    Filter by STASH code
    -um_version x.y                   Filter by UM version x.y
    -var   VAR_NAME[,VAR_NAME2,...]   Filter by variable name
```

### Other options
```
   stc [...]
    -nc_format NETCDF3_CLASSIC|NETCDF3_64BIT|NETCDF4_CLASSIC|NETCDF4(default)
    -nc_zlib   Turn on gzip compression while saving NetCDF
    --version  Print version information (based on svn info, st and diff)
```

### Example data

To learn how to use stc you can download example data from [iris-sample-data](https://github.com/SciTools/iris-sample-data) with `git clone https://github.com/SciTools/iris-sample-data.git` and experiment with the examples given in the documentation for the individual commands.
