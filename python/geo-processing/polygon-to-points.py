import geopandas as gpd
from shapely.geometry import polygon, point, MultiPolygon
import os

input_file = 'Data/HaiDuong.shp'
output_dir = 'Data/Points'

os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, 'HaiDuong_pt.shp')

try:
    gdf = gpd.read_file(input_file)
    def Polygon_To_Point(geom):
        if geom.geom_type == 'Polygon':
            return geom.representative_point()
        elif geom.geom_type == 'MultiPolygon':
            points = [poly.representative_point() for poly in geom]
            return points
        else:
            return geom
    gdf['geometry'] = gdf['geometry'].apply(Polygon_To_Point)
    df = gdf.to_file(output_file, Driver = 'ESRI Shapefile', encoding = 'utf-8')
    print(f'Xuất dữ liệu thành công, tệp lưu tại {output_dir}')
except Exception as e:
    print(f'Xuất dữ liệu không thành công, lỗi {str(e)} ')