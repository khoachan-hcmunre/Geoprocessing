import geopandas as gpd

input = 'Data/vn_provinces.shp'
output = 'Data/vn_provinces.csv'

try:
    gdf = gpd.read_file(input)
    df = gdf.drop(columns = ['geometry', 'region'])
    df.to_csv(output, index = False)
    print(f'Chuyển đổi thành công, tệp lưu tại {output}')

except Exception as e:
    print(f'Chuyển đổi không thành công {str(e)}')
    