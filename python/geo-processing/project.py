from pyproj import Transformer
import geopandas as gpd

input_file = 'Data/vn_provinces.shp'
output_file = 'Data/vn_provinces_3857.shp'

transformer = Transformer.from_crs("epsg:4326", "epsg:3857")

gdf = gpd.read_file(input_file)
gdf = transformer.transform(gdf[gdf['geometry']])

gdf.to_file(output_file)


