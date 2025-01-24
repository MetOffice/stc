**[stc](https://github.com/MetOffice/stc/blob/main/doc/stc.md) ls**: List information about file content.

### Use
```
stc ls IFILE[,IFILE2,...]
stc ls IFILE -ind index
stc ls IFILE -v
stc ls IFILE -coord [time|level|height|model_level_number|
                     grid_latitude|grid_longitude|altitude]
```
### Example 

Go to your [example-data](https://github.com/MetOffice/stc/blob/main/doc/stc.md#example-data) and try `stc ls uk_hires.pp` which will give the listing

```
0: air_potential_temperature / (K)     (time: 3; model_level_number: 7; grid_latitude: 204; grid_longitude: 187)
1: surface_altitude / (m)              (grid_latitude: 204; grid_longitude: 187)
```

[Filter](https://github.com/MetOffice/stc/blob/main/doc/stc.md#filter-options) for the first data set ([cube](https://scitools-iris.readthedocs.io/en/stable/userguide/iris_cubes.html#)) and show more details with `stc ls uk_hires.pp -var air_potential_temperature -v`:

```
0: air_potential_temperature / (K)     (time: 3; model_level_number: 7; grid_latitude: 204; grid_longitude: 187)
    Dimension coordinates:
        time                             x                      -                 -                    -
        model_level_number               -                      x                 -                    -
        grid_latitude                    -                      -                 x                    -
        grid_longitude                   -                      -                 -                    x
    Auxiliary coordinates:
        forecast_period                  x                      -                 -                    -
        level_height                     -                      x                 -                    -
        sigma                            -                      x                 -                    -
        surface_altitude                 -                      -                 x                    x
    Derived coordinates:
        altitude                         -                      x                 x                    x
    Scalar coordinates:
        forecast_reference_time     2009-11-19 04:00:00
    Attributes:
        STASH                       m01s00i004
        source                      'Data from Met Office Unified Model'
        um_version                  '7.3'
```
