mkdir dn_points

for file in kml_dn/*.shp; do
    output_file=dn_points/$(basename "$file" .shp)_points.shp
    ogr2ogr -f "ESRI Shapefile" "$output_file" "$file" -dialect sqlite -sql "SELECT ST_PointOnSurface(geometry) AS geometry, * FROM $(basename "$file" .shp)"
done
