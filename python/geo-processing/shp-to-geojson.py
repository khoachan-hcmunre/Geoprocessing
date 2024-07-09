import geopandas as gpd

input = 'Data/vn_provinces.shp'
output = 'Data/vn_provinces.GeoJSON'

try:
    gpf = gpd.read_file(input)
    gpf.to_file(output, driver = 'GeoJSON')
    print(f'Chuyển đổi thành công, tệp lưu tại {output}')

except Exception as e:
    print(f'Chuyển đổi không thành công: {str(e)}')
    
