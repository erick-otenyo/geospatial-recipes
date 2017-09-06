# Discover GIS file/layer extents from command line
Most of the time when building a web map application, I found myself in need to
know the extent of a shapefile or a Geojson file. I had to open a desktop GIS
software like QGIS or ArcGIS, just to know the extents and then close, which
usually took time. Just for a very simple task.

## Solution
Make a small script for only knowing the spatial extents of a supplied GIS file,
(supported by OGR) and make it accessible from anywhere on my Computer system.

The script requires atleast the filepath to the geojson or shapefile to be read for extents


## Dependencies
I assume you  already  have OGR installed in your Linux machine

## Usage
Download this folder and on its root, make the extent python file executable by
running :

    chmod +x extent

Notice I omitted the .py extension when naming the file.There is no problem, as
long as you are on a unix machine.

Then make the script in your PATH so you can run it from anywhere. I put the
folder in my home directory and added it to my Path

    sudo nano .bashrc

add this line to the end of the file

    export PATH=/my/directory/with/layer_extent:$PATH

Now if you can run the script from anywhere in your computer e.g :

    extent /path/to/buildings.geojson

And just like that, you will have the extents printed without touching QGIS or
ArcGIS
