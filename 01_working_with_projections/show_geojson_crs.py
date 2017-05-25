#!/usr/bin/env python
# -*- coding; utf-8 -*-

# show geojson file projection

import json

geojson_yes_crs = 'geodata/towns.geojson'
geojson_no_crs = 'geodata/towns_no_prj.geojson'

with open(geojson_no_crs) as my_geojson:
	data = json.load(my_geojson)

# check if crs is in the data python dictionary data
# if yes print the crs to screen
# else print NO to screen and print geojson data type

if 'crs' in data:
	print "the crs is : " + data['crs']['properties']['name']
else:
	print "++++++ no crs tag in file+++++"
	print "++++++ assume EPSG:4326 ++++++"
	if "type" in data:
		print "current GeoJSON data type is :" + data['type']


# show geojson projection function

def show_geojson_crs(geojson_file):
	with open(geojson_file) as my_geojson:
		data = json.load(my_geojson)
	if data:
		if 'crs' in data:
			print "the crs is : " + data['crs']['properties']['name']
		else:
			print "++++++ no crs tag in file+++++"
			print "++++++ assume EPSG:4326 ++++++"
			if "type" in data:
				print "current GeoJSON data type is :" + data['type']
	else:
		print "cant open file"


show_geojson_crs(geojson_yes_crs)


# Projection definitions

#  1. Esri Well-Known Text




