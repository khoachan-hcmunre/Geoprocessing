import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

input_file = 'vn_provinces_pt.csv'
output_file = 'vn_provinces_pt.geojson'

try: 
    df = pd.read_csv(input_file)
    geometry = [Point(xy) for xy in zip(df['lng'], df['lat'])]
    gdf = gpd.GeoDataFrame(df, geometry=geometry, crs='EPSG:4326')
    gdf.to_file(output_file, driver='GeoJSON')
    print(f'Exported data successfully, saved at {output_file}')

except Exception as e:
    print(f'Data export failed, error {e}')