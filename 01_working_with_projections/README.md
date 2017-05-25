# Working with Projections

## Discovering the Projection of a Shapefile / Geojson 

Code to show how to discover the projection of a shapefile or geojson dataset

We ended up with two functions

        show_shp_crs()
        show_geojson_crs()

where both of them take the path to the file as a parameter

## Projection definitions

### Esri Well-Known Text 
e.g 

    GEOGCS["GCS_WGS_1984",
    DATUM["WGS_1984",
    SPHEROID["WGS_84",6378137.0,298.257223563]],
    PRIMEM["Greenwich",0.0],
    UNIT["Degree",0.0174532925199433],
    AUTHORITY["EPSG","4326"]]

### OGC Well-Known-Text
e.g

      GEOGCS["WGS 84",DATUM["WGS_1984",
      SPHEROID["WGS84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],
      AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],
      UNIT["d egree",0.01745329251994328,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]] 

### Proj4 Format

        +proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs

