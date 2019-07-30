# RedFox-Tools

## numberPoints

This tool is designed to number points sequentially within each forest stand polygon feature. 

The tool adds a field called "point_ID" to the input featureclass which will contain the sequential numbering. 

**Please make a copy of your featureclass if you do not wish to make changes to the source featureclass.**

This tool assumes the forest Stand ID has already been assigned to each point (e.g. via Spatial Join). 

## Instructions: 
1) Download and unzip "number_points.zip" from the repository

2) In ArcGIS, open the script tool "numberPoints" located within the "RedFoxTools" toolbox

3) Select the featureclass or shapefile in which you would like to create sequentially numbered points within each polygon feature. 

4) Select the forest stand field (e.g. "STAND_ID") 

