import geopandas as gpd 

input = 'Data/vn_provinces.shp'
output = 'Data/hanoi1.GeoJSON'

try:
    gdf = gpd.read_file(input)
    gdf_select = gdf[gdf['prov_code'].isin(['01', '79'])].copy()
    gdf_select.loc[:, 'DienTich'] = gdf_select.geometry.area
    df = gdf_select.to_file(output, driver = 'GeoJSON')
    print(f'Xuất thành công, {output}')

except Exception as e:
    print(f'Xuất tệp không thành công, lỗi {str(e)}')
