## [stc](https://github.com/MetOffice/stc/blob/main/doc/stc.md) cp 

**stc cp** copies, extracts, combines and converts data.

### Use

```
stc cp IFILE OFILE
stc cp IFILE,IFILE2 OFILE1,OFILE2
stc cp IFILE,IFILE2 OFILE
```

The format of OFILE is determined by the suffix (pp, nc or grib2).

```
stc cp fieldsfile   gribfile.grib
stc cp file1,file2  file12.nc
```

### Examples

Using your [example-data](https://github.com/MetOffice/stc/blob/main/doc/stc.md#example-data) you can concat two pp files and write the output to NetCDF

```
stc cp northward_sea_ice_velocity.1890.01.01.00.00.pp,northward_sea_ice_velocity.1890.02.01.00.00.pp vice_1890-01--02.nc
```

Use [filter options](https://github.com/MetOffice/stc/blob/main/doc/stc.md#filter-options) to select one variable from a pp file by name 'x_wind` and save the selected variable in GRIB2 format

```
stc cp wind_speed_lake_victoria.pp u.grib2 -var x_wind
```

or to select a varaible by its UM STASH code (`m01s00i033`) and store the field in NetCDF format  

```
stc cp uk_hires.pp surface_altitude.nc -stash m01s00i033
```
