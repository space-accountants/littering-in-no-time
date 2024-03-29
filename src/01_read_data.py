from functions.handler_gpx import gpx_to_traj

GPX_NAME = 'data/Schoonwandelen_714_items.gpx'
XLS_NAME = 'data/200-records-van-cert-76.xlsx'

traj = gpx_to_traj(GPX_NAME)