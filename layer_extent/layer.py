#!/usr/bin/python
import sys
from osgeo import ogr
def get_extent(fn,name=0):
	ds=ogr.Open(fn,0)
	if ds is None:
		sys.exit("Could Not  Open '{0}' File Or Path.Please Check And Try Again".format(fn))
	lyr=ds.GetLayer(name)
	extent=lyr.GetExtent()
	print(extent)
	del ds
