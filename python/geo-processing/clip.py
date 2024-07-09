import geopandas as gpd
from shapely.geometry import box 

input_file = 'Data/vn_provinces.shp'
mask = 'Data/Mask.shp'
output_file = 'Data/Clip.shp'
try:
    gdf = gpd.read_file(input_file)
    mdf = gpd.read_file(mask)
    mask_geom = mdf.geometry.unary_union
    clipped = gpd.overlay(gdf, mdf, how='intersection')
    df = clipped.to_file(output_file, Dirvier = ' ESRI Shapefile')
    print(f'Xuất dữ liệu thành công, tệp lưu tại {output_file}')
    
except Exception as e:
    print(f'Không thành công, lỗi {str(e)}')