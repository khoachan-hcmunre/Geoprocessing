import geopandas as gpd 
from shapely import Polygon, Point, MultiPolygon, centroid
import os

input_file = 'Data/vn_provinces.shp'
output_dir = 'Data/Centroid'

os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, 'vn_provinces_pt.shp')

try:
    gdf = gpd.read_file(input_file)
    gdf['geometry'] = centroid(gdf['geometry'])
    gdf[['prov_code','geometry', 'name']].to_file(output_file, Driver = 'ESRI Shapefile', encoding = 'utf-8')
    print(f'Xuất dữ liệu thành công, tệp lưu tại {output_dir}')
except Exception as e:
    print(f'Xuất dữ liệu không thành công, lỗi {str(e)}')