import pandas as pd
import geopandas as gpd

from movingpandas import Trajectory
from shapely import Point

from .handler_xml import get_root_of_table

def gpx_to_traj(gpx_name: str) -> Trajectory:
    root = get_root_of_table(gpx_name)

    gpx = []
    trk_id = 0
    for elem in root:
        if not elem.tag.endswith('trk'):
            continue
        seg = None
        for trk in elem:
            if not trk.tag.endswith('trkseg'):
                continue
            trk_id += 1
            for pnt in trk:
                gpx.append(
                    {
                        'track_id': trk_id,
                        'time': pnt[1].text,
                        'geometry': Point(float(pnt.get('lon')),
                                          float(pnt.get('lat'))),
                    }
                )
        df = pd.DataFrame(gpx)
        df['t'] = pd.to_datetime(df.time,
                                 format='%Y-%m-%dT%H:%M:%SZ')
        df = df.drop(columns='time')
        gdf = gpd.GeoDataFrame(df,
                               geometry=df.geometry,
                               crs='epsg:4326')
        gdf = gdf.set_index('t')
        return Trajectory(gdf, 1)