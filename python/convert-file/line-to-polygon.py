import geopandas as gpd
from shapely.geometry import Polygon

input_file = 'vietnam_ln.shp'
output_file = 'vietnam_pg.shp'

try:
    gdf_lines = gpd.read_file(input_file)
    gdf_polygons = gpd.GeoDataFrame(columns=['geometry'], crs=gdf_lines.crs)
    for index, row in gdf_lines.iterrows():
        line_geometry = row['geometry']
        if line_geometry.geom_type == 'LineString':
            polygon_geometry = Polygon(line_geometry.convex_hull.exterior.coords)
            gdf_polygons = gdf_polygons._append({'geometry': polygon_geometry}, ignore_index=True)
    gdf_polygons.to_file(output_file, driver='ESRI Shapefile')
    print(f'Exported data successfully, saved at {output_file}')
    
except Exception as e:
    print(f'Data export failed, error {e}')