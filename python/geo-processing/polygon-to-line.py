import geopandas as gpd
import os
from shapely.geometry import LineString, MultiPolygon, Polygon

input_file = 'Data/vn_provinces.shp'
output_dir = 'Data/Merg/Polyline'
output_file = os.path.join(output_dir, 'polylines.shp')

os.makedirs(output_dir, exist_ok=True)

try:
    # Read the polygon shapefile
    gdf = gpd.read_file(input_file)
    
    # Function to convert a polygon to a polyline
    def polygon_to_polyline(geom):
        if geom.geom_type == 'Polygon':
            return LineString(list(geom.exterior.coords))
        elif geom.geom_type == 'MultiPolygon':
            lines = []
            for part in geom:
                lines.append(LineString(list(part.exterior.coords)))
            return lines
        else:
            return geom
        
    gdf['geometry'] = gdf['geometry'].apply(polygon_to_polyline)
    output_file = os.path.join(output_dir, 'vn_provinces_ln.shp')
    gdf.to_file(output_file, encoding = 'utf-8')
    print(f'Xuất dữ liệu thành công, tệp được lưu tại{output_dir}{output_file}')

except Exception as e:
    print(f'Xuất dữ liệu không thành công, lỗi {e}')


