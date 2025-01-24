## [stc](https://github.com/MetOffice/stc/blob/main/doc/stc.md) cp 

**stc cp** copies, extracts, combines and converts data.

### Use

```
stc cp IFILE OFILE
stc cp IFILE,IFILE2 OFILE1,OFILE2
stc cp IFILE,IFILE2 OFILE
```

The format of OFILE is determined by the suffix (pp, nc or grib).

### Examples

```
stc cp fieldsfile   gribfile.grib
stc cp file1,file2  file12.nc
```
