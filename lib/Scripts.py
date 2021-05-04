#---------------------
#SHAPES
#---------------------
class Shape():
    def make_box(name, point, settings):
        method = str(name)+' = BRepPrimAPI_MakeBox('+str(point)+','+str(settings)+').Shape()\n\
'+str(name)+'_Shape = display.DisplayShape('+str(name)+')\n'
        return method

    def make_cylinder(name, axis, settings):
        method = str(name) + ' = BRepPrimAPI_MakeCylinder(' + str(axis) + ',' + str(settings) + ').Shape()\n\
' + str(name) + '_Shape = display.DisplayShape(' + str(name) + ')\n'
        return method

def make_sphere(arg):
    if arg == 'imp':
        return  'from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeSphere\n\
from OCC.Core.gp import gp_Ax2 , gp_Dir , gp_Pnt\n\
from math import atan, cos, sin, pi\n\
sphere_radius = 30.0\n\
sphere_angle = atan(2)\n\
sphere_origin = gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1))\n\
sphere = BRepPrimAPI_MakeSphere(sphere_origin, sphere_radius, -sphere_angle, sphere_angle).Shape()\n\
display.DisplayShape(sphere)\n'

    else:
        return  'sphere_radius = 30.0\n\
sphere_angle = atan(2)\n\
sphere_origin = gp_Ax2(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1))\n\
sphere = BRepPrimAPI_MakeSphere(sphere_origin, sphere_radius, -sphere_angle, sphere_angle).Shape()\n\
display.DisplayShape(sphere)\n'

#---------------------
#CONSTRUCTION
#---------------------

class Construction():
    def draw_point(name, settings):
        method = str(name) + ' = gp_Pnt(' + str(settings) + ')\n\
' + str(name) + '_Point = display.DisplayShape(' + str(name) + ')\n'
        return method

    def draw_axis(name, point, dir):
        method = str(name) + ' = gp_Ax2('+str(point)+', gp_Dir('+str(dir)+'))\n'
        return method

#---------------------
#TRANSFORMATION
#---------------------

def translate(arg):
    if arg == 'imp':
        return 'from OCC.Core.gp import gp_Vec, gp_Trsf\n\
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform\n\
trns = gp_Trsf()\n\
trns.SetTranslation(gp_Vec(-30, -30, -30))\n\
translated = BRepBuilderAPI_Transform(reference, trns).Shape()\n\
display.DisplayShape(translated)\n'
    else:
        return 'trns = gp_Trsf()\n\
trns.SetTranslation(gp_Vec(-30, -30, -30))\n\
translated = BRepBuilderAPI_Transform(reference, trns).Shape()\n\
display.DisplayShape(translated)\n'

#---------------------
#BOOLEAN
#---------------------

class Boolean():

    def bool_cut(name, basis, cutter):
        method = str(name)+' = BRepAlgoAPI_Cut('+str(basis)+','+ str(cutter)+').Shape()\n\
'+str(name)+'_Shape =display.DisplayShape('+str(name)+', update=True, material=Graphic3d_NOM_STEEL)\n'
        return method


#---------------------
#EXPORT
#---------------------

def export_step(arg):
    if arg == 'imp':
        return 'from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs\n\
step_writer = STEPControl_Writer()\n\
step_writer.Transfer(a_shape, STEPControl_AsIs)\n\
status = step_writer.Write("filename.step")\n'
    else :
        return 'step_writer = STEPControl_Writer()\n\
step_writer.Transfer(a_shape, STEPControl_AsIs)\n\
status = step_writer.Write("filename.step")\n'