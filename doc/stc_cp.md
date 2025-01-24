## [stc](https://github.com/MetOffice/stc/blob/main/doc/stc.md) cp 

**stc cp** copies, extracts, combines and converts data.

### Use

```
stc cp IFILE OFILE
stc cp IFILE,IFILE2 OFILE1,OFILE2
stc cp IFILE,IFILE2 OFILE
```

The format of OFILE is determined by the suffix (pp, nc or grib).

```
stc cp fieldsfile   gribfile.grib
stc cp file1,file2  file12.nc
```

### Examples

Using your [example-data](https://github.com/MetOffice/stc/blob/main/doc/stc.md#example-data) you can concat two pp files and write the output to NetCDF

```
stc cp UM/northward_sea_ice_velocity.1890.01.01.00.00.pp,UM/northward_sea_ice_velocity.1890.02.01.00.00.pp vice_1890-01--02.nc
```

