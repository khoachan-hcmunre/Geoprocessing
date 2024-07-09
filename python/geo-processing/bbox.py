import geopandas as gpd
from shapely import Polygon, boundary, GeometryCollection, envelope
import os 

input_file = 'Data/vn_provinces.shp'
output_dir = 'Data/BBox'

os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, 'vn_province_bbox.shp')

try:
    gdf = gpd.read_file(input_file)
    merged_geom = gdf.unary_union
    bbox_geom = merged_geom.envelope
    bbox_gdf = gpd.GeoDataFrame(geometry=[bbox_geom], crs=gdf.crs)
    bbox_gdf.to_file(output_file, Driver = 'ESRI Shapefile', encoding = 'utf-8')
    print(f'Xuất dữ liệu thành công, lưu tại {output_dir}')

except Exception as e:
    print(f'Xuất dữ liệu không thành công, lỗi {e}')
