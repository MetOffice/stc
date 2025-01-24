## [stc](https://github.com/MetOffice/stc/blob/main/doc/stc.md) regrid - regrid to data to a target grid (default lon lat)

### Use

```
stc regrid IFILE OFILE

stc regrid [...] -tgrid FILE_WITH_TARGET_GRID
                        default: lsm for n2004 from $UMDIR

stc regrid [...] -tlon  LON_MIN LON_MAX
                        longitute limits for target grid

stc regrid [...] -tlat  LAT_MIN LAT_MAX
                        latitude limits for target grid
```
