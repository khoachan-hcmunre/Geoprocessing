import geopandas as gpd
from shapely.geometry import Point

input_file = 'polygon.shp'
output_file = 'point.shp'

try:
    gdf_polygons = gpd.read_file(input_file)
    gdf_points = gpd.GeoDataFrame(columns=gdf_polygons.columns, crs=gdf_polygons.crs)
    for index, row in gdf_polygons.iterrows():
        polygon_geometry = row['geometry']
        point_geometry = Point(polygon_geometry.centroid)
    gdf_points = gdf_points._append({'geometry': point_geometry, **row.drop('geometry')}, ignore_index=True)
    gdf_points.to_file(output_file, driver='ESRI Shapefile')
    print(f'Exported data successfully, saved at {output_file}')
    
except Exception as e:
    print(f'Data export failed, error {e}')