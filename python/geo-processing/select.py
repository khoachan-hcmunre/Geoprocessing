import geopandas as gpd 
import os

input_file = 'Data/vn_provinces.shp'
output_dir = 'Data/Provinces'

os.makedirs(output_dir, exist_ok= True)
prov_codes = ['01','79','48','92']

try:
    gdf = gpd.read_file(input_file)
    gdf_select = gdf.to_crs(epsg=4326)

    for prov_code in prov_codes:
        gdf_select = gdf[gdf['prov_code']== prov_code]
        gdf_select['DienTich'] = gdf_select.geometry.area
        output_files = os.path.join(output_dir, f'{prov_code}.shp')
        df = gdf_select.to_file(output_files, driver = 'ESRI Shapefile', encoding = 'utf-8')
        print(f'Xuất thành công tệp {output_files}')

except Exception as e:
    print(f'Xuất tệp không thành công {str(e)}')