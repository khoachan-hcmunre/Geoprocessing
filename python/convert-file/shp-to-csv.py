import geopandas as gpd

input_file = 'vn_vietnam.shp' 
output_file = 'vietnam.csv'
try: 
    gdf = gpd.read_file(input_file)
    gdf.to_csv(output_file, index=False)
    print(f'Exported data successfully, saved at {output_file}')
    
except Exception as e:
    print(f'Data export failed, error {e}')