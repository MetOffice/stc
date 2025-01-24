## [stc](https://github.com/MetOffice/stc/blob/main/doc/stc.md) plot - plot 2d data slices

### Use

```
stc plot IFILE

stc plot IFILE [...] -clim CMIN CMAX

stc plot IFILE [...] -ncol NCOL

stc plot IFILE [...] -title 'YOUR TITLE'

stc plot IFILE [...] -cmap 'auto', 'RdYlBu_r' / 'terrain' / 'Accent' / ... See also http://goo.gl/51s91K

stc plot IFILE [...] -mask YOUR_PATH/qrparm.mask
```

Handle 2d fields only, use appropriate [filter options](https://github.com/MetOffice/stc/blob/main/doc/stc.md#filter-options) like `-var`, `-pl` etc. Use `stc help` for details on available options.
