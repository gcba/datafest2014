UPDATE departamentos_argentina_centroide SET lon=ST_X(ST_Centroid(the_geom)), lat=ST_Y(ST_Centroid(the_geom));