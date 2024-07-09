polygon_shapefile="kml_dn/dn_buffer.shp"
input_folder="dn_points"
output_folder="intersection"
mkdir -p $output_folder

for point_shapefile in $input_folder/*.shp; do

    output_file="$output_folder/$(basename $point_shapefile)"


    if [ -e "$output_file" ]; then
        echo "Tệp $output_file đã tồn tại. Bỏ qua."
    else

    ogr2ogr -f "ESRI Shapefile" -clipsrc $polygon_shapefile $output_file $point_shapefile

        if [ $? -eq 0 ]; then
            echo "Đã xử lý $point_shapefile"
        else
            echo "Lỗi xử lý $point_shapefile"
        fi
    fi
done