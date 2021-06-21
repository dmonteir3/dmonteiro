import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
#import shapefile as shp
import geopandas as gpd

data = gpd.read_file('/home/monteiro/STAGEIENM3/data_S2M/massifs_shapefiles/massifs_alpes_2154.shp')

data = data.to_crs(epsg=4326)
data.crs = '+proj=utm +zone=32 +ellps=GRS80 +units=m +no_defs'
data.to_file('/home/monteiro/STAGEIENM3/data_S2M/massifs_shapefiles/massifs_alpes_4326.shp')

