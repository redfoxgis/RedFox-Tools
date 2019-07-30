# Copyright:   (c) RedFox GIS & Remote Sensing 2019
# created 7-29-2019
#-------------------------------------------------------------------------------

import arcpy

fc = arcpy.GetParameterAsText(0)
stand_ID_field = arcpy.GetParameterAsText(1)

def add_field(fc, field_name):
    """
    Add point_ID field
    """
    if 'point_ID' not in [f.name for f in arcpy.ListFields(fc)]:
        arcpy.AddField_management(fc, field_name, "SHORT")

def add_count(fc, field):
    """
    Adds sequential numbers to points within each polygon
    """
    for item in {row[0] for row in arcpy.da.SearchCursor(fc,field)}: # Get unique list of STAND ID's
        with arcpy.da.UpdateCursor(fc, (field, "point_ID")) as cursor:
            count = 1
            for row in cursor:
                if row[0] == item:
                    row[1] = count
                    count += 1
                cursor.updateRow(row)

if __name__ == '__main__':
    add_field(fc, "point_ID")
    add_count(fc, stand_ID_field)

    print "Processing complete"

