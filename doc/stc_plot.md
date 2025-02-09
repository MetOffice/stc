## [stc](https://github.com/MetOffice/stc/blob/main/doc/stc.md) plot

**stc plot** plots 2d data slices. 

### Use

```
stc plot IFILE

stc plot IFILE [...] -clim CMIN CMAX

stc plot IFILE [...] -ncol NCOL

stc plot IFILE [...] -title 'YOUR TITLE'

stc plot IFILE [...] -cmap 'auto', 'RdYlBu_r' / 'terrain' / 'Accent' / ... See also http://goo.gl/51s91K

stc plot IFILE [...] -mask YOUR_PATH/qrparm.mask
```

`stc plot` handles 2d fields only, use appropriate [filter options](https://github.com/MetOffice/stc/blob/main/doc/stc.md#filter-options) like `-var`, `-pl` etc to trim your data to 2d.
