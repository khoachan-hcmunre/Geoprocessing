import geopandas as gpd 
from shapely import points, polygons
import os

input_file = 'data/tramsac_pt.shp'
admin = 'data/vn_wards_full.shp'
output_dir = 'data/join'

os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, 'tramsac_pt.shp')

try: 
    gdf = gpd.read_file(input_file)
    adf = gpd.read_file(admin)
    filter = adf[['prov_code','dist_code','ward_code','prov_name','dist_name','ward_fname','geometry']]
    df = gdf.sjoin(filter, how="left", predicate='intersects')
    df = df.drop(columns=['index_right'])
    df.to_file(output_file, encoding = 'utf-8')
    print(f'Exported data successfully, saved at {output_file}')

except Exception as e:
    print(f'Data export failed, error {e}')