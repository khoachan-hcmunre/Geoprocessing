import geopandas as gpd
from shapely import GeometryCollection, Polygon
import os

input_file = 'Data/vn_provinces.shp'
output_dir = 'Data/Merg'
output_file = os.path.join(output_dir, 'HCM_LA.shp')
try:
    gdf = gpd.read_file(input_file)
    HCM = gdf[gdf['name'] =='Hồ Chí Minh']
    LA = gdf[gdf['name'] =='Long An']
    merged_geom = HCM.unary_union | LA.unary_union
    merged_gdf = gpd.GeoDataFrame(geometry=[merged_geom], crs=gdf.crs)
    merged_gdf.to_file(output_file, Driver = 'ESRI Shapefile', encoding = 'utf-8')
    print(f'Xuất dữ liệu thành công, tệp lưu tại {output_dir}')
except Exception as e:
    print(f'Xuất dữ liệu không thành công, lỗi {str(e)}')