
 # stc - SciTools Commands

 Collection of command line utilities build on top of the SciTools
 library, http://scitools.org.uk, to work with FF, PP, NetCDF and GRIB
 files from the UNIX command line.

 ## AVAILABLE SUBCOMMANDS

```
   add                  Add fields from two files
   cp (convert, copy)   Copy, extract, combine and convert data
   div                  Divide fields from two files
   help                 Print help
   ls (info)            List information from file
   plot                 Plot 2d data slices
   rdiff                Calculate relative difference between to files
   regrid               Regrid fields from file
   split_precip         Split accumulated precipitation in time intervals
   sub                  Subtract fields from two files
   stc help SUBCOMMAND  Print detailed help
```

##  FILTER OPTIONS

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

   The above options are available for all subcommands to filter the input
   data at the begin of the operation requested by the command.

 ## OTHER OPTIONS

```
   stc [...]
    -nc_format NETCDF3_CLASSIC|NETCDF3_64BIT|NETCDF4_CLASSIC|NETCDF4(default)
    -nc_zlib   Turn on gzip compression while saving NetCDF
    --version  Print version information (based on svn info, st and diff)
```
