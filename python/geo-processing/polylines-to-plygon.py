import geopandas as gpd
from shapely.geometry import LineString, Polygon, MultiPolygon
import os

input_file = 'Data/vn_provinces.shp'
output_dir = 'Data/Merg/Polygon'

os.makedirs(output_dir, exist_ok=True)

try:
    gdf = gpd.read_file(input_file)
    
    def polyline_to_polygon(geom):
        if geom.geom_type == 'LineString':
            return Polygon(list(geom.coords))  
        elif geom.geom_type == 'MultiLineString':
            polygons = [Polygon(list(part.coords)) for part in geom]
            return MultiPolygon(polygons)  
        return geom  

    gdf['geometry'] = gdf['geometry'].apply(polyline_to_polygon)  
    
    output_file = os.path.join(output_dir, 'vn_provinces_pg.shp')
    gdf.to_file(output_file, encoding='utf-8')
    print(f'Xuất dữ liệu thành công, lưu tại {output_file}')

except Exception as e:
    print(f'Xuất dữ liệu không thành công, lỗi {e}')
