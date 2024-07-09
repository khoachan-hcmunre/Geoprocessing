import geopandas as gpd 
from shapely import Point, Polygon, buffer, BufferCapStyle, BufferJoinStyle
import os

input_file = 'Data/Points/HaiDuong_pt.shp'
output_dir = 'Data/Buffer'

os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, 'Buffer_Point.shp')
try: 
    gdf = gpd.read_file(input_file)
    gdf['geometry'] = gdf['geometry'].buffer(2, cap_style=1) 
    gdf.to_file(output_file, Driver = 'ESRI Shapfile', encoding = 'utf-8')
    print(f'Xuất dữ liệu thành công, lưu tại {output_dir}')
except Exception as e:
    print(f'Xuất dữ liệu không thành công, lỗi {str(e)}')