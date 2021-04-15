# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 23:10:44 2019

@author: Melina
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.cm import get_cmap
from matplotlib.colors import from_levels_and_colors
from cartopy import crs
from cartopy.feature import NaturalEarthFeature, COLORS
from netCDF4 import Dataset
from wrf import (getvar, to_np, get_cartopy, latlon_coords, vertcross,
                 cartopy_xlim, cartopy_ylim, interpline, CoordPair)

wrf_file = Dataset("wrfout_d01_2019-07-10_00_00_00") #wrf elec

# Get the WRF variables
ht = getvar(wrf_file, "z", timeidx=None)
dbz = getvar(wrf_file, "dbz", timeidx=None)
max_dbz = getvar(wrf_file, "mdbz", timeidx=None)
#CDC = 1.0e9 * getvar( wrf_file, "SCW", timeidx=None ) #=cloud_droplets_charge 
#RC = 1.0e9 * getvar( wrf_file, "SCR", timeidx=None ) #=rain_charge 
#CIC = 1.0e9 * getvar( wrf_file, "SCI", timeidx=None ) #=cloud_ice_charge 
#GC = 1.0e9 * getvar( wrf_file, "SCH", timeidx=None ) #=graupel_charge 
#HC = 1.0e9 * getvar( wrf_file, "SCHL", timeidx=None ) #=hail_charge 
NC = 1.0e9 * getvar( wrf_file, "SCTOT", timeidx=None ) #=net_charge
#SCS = 1.0e9 * getvar( wrf_file, "SCS", timeidx=None ) #=snow_charge
#QGRAUP=1000*getvar(wrf_file, "QGRAUP", timeidx=None) # en g/kg
#QHAIL=1000*getvar(wrf_file, "QHAIL", timeidx=None) # en g/kg
#QICE=1000*(getvar(wrf_file, "QICE", timeidx=None)+getvar(wrf_file, "QSNOW", timeidx=None)) # en g/kg
#


