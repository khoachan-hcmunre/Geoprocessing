import geopandas as gpd 
import os

input_file = 'Data/Clip.shp'
output_dir = 'Merg'

os.makedirs(output_dir, exist_ok= True)

try: 
    gdf = gpd.read_file(input_file)
    merged = gdf.dissolve(by='region', aggfunc='first')
    output_file = os.path.join(output_dir, 'Merg1.shp')
    merged.to_file(output_file)
    print(f'Xuất dữ liệu thành công, {output_file}')

except Exception as e:
    print(f'Không thành công, lỗi {str(e)}')