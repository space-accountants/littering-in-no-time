import pandas as pd
import geopandas as gpd

from functions.handler_gpx import gpx_to_traj

GPX_NAME = 'data/Schoonwandelen_714_items.gpx'
XLS_NAME = 'data/200-records-van-cert-76.xlsx'

# import movement data
traj = gpx_to_traj(GPX_NAME)

# import picks
picks = pd.read_excel(XLS_NAME, header=0, index_col=0)
picks = gpd.GeoDataFrame(picks,
                         geometry=gpd.points_from_xy(picks.lon, picks.lat),
                         crs="EPSG:4326")
