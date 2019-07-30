# RedFox-Tools
Number Points Sequentially

This tool is designed to number points sequentially within each forest stand polygon feature. 

This tool adds a field called "point_ID" to the input featureclass which will contain the sequential numbering. 

Please make a copy of your featureclass if you do not wish to make changes to the source featureclass.

This tool assumes the forest Stand ID has already been assigned to each point (e.g. via Spatial Join). 

Instructions: 

1) Select the featureclass or shapefile in which you would like to create sequentially numbered points within each polygon feature. 

2) Select the forest stand field (e.g. "STAND_ID") 

