import geopandas as gpd

input = 'Data/vn_provinces.GeoJSON'
output = 'Data/vn_provinces1.shp'

try:
    gdf = gpd.read_file(input)
    gdf.to_file(output, driver = 'Shapefile')
    print(f'Chyển đổi thành công, tệp lưu tại{output}')

except Exception as e:
    print(f'Xuất tệp không thành công {str(e)}')
