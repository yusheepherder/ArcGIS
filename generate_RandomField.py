#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      silva
#
# Created:     27-01-2017
# Copyright:   (c) silva 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#initial setting
import arcpy
arcpy.env.workspace=r'C:\data\workspace.gdb'

#target feature & field
tar="polygon"
fld="r_value"

#code block
code_block="""def getRand():
    return arcgis.rand("INTEGER")"""

#generate Field and get random value
arcpy.AddField_management(tar,fld,"LONG")
arcpy.CalculateField_management(tar,fld,"getRand()",'PYTHON',code_block)