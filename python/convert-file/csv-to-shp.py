import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

csv_path = 'vn_provinces_pt.csv' 
shapefile_path = 'vn_provinces_pt.shp' 

try: 
    df = pd.read_csv(csv_path)
    geometry = [Point(xy) for xy in zip(df['lng'], df['lat'])] 
    gdf = gpd.GeoDataFrame(df, geometry=geometry, crs='EPSG:4326')
    gdf.to_file(shapefile_path)
    print(f'Exported data successfully, saved at {shapefile_path}')

except Exception as e:
    print(f'Data export failed, error {e}')