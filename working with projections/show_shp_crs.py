#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Showing  shapefile projection


# Begin with importing the OGR module as follows:
from osgeo import ogr

# Activate the OGR Shapefile driver:
shp_driver = ogr.GetDriverByName('Esri Shapefile')

# Open the Shapefile with OGR:
shp_dataset = shp_driver.Open(r'geodata/kenya_major_towns.shp')

# Access the layer information with GetLayer() :

shp_layer = shp_dataset.GetLayer()

# Now we can get the coordinate information using the GetSpatialRef() function:
shp_srs = shp_layer.GetSpatialRef()

# Finally, print the spatial reference system on screen:
print shp_srs


# function

def show_shp_crs(shp_path):
	shp_driver = ogr.GetDriverByName('Esri Shapefile')
	shp_dataset = shp_driver.Open(r'{}'.format(shp_path))
	shp_layer = shp_dataset.GetLayer()
	shp_srs = shp_layer.GetSpatialRef()
	print shp_srs
