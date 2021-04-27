#---------------------
#SHAPES
#---------------------

def make_box(arg):
    if arg == 'imp':
        return 'from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox\n\
box = BRepPrimAPI_MakeBox(30, 60, 60).Shape()\n\
display.DisplayShape(box)\n'
    else :
        return 'box = BRepPrimAPI_MakeBox(30, 60, 60).Shape()\n\
display.DisplayShape(box)\n'

def make_sphere(arg):
    if arg == 'imp':
        return  'from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeSphere\n\
from math import atan, cos, sin, pi\n\
sphere_radius = 30.0\n\
sphere_angle = atan(2)\n\
sphere_origin = i.gp_Ax2(i.gp_Pnt(0, 0, 0), i.gp_Dir(0, 0, 1))\n\
sphere = i.BRepPrimAPI_MakeSphere(sphere_origin, sphere_radius, -sphere_angle, sphere_angle).Shape()\n\
display.DisplayShape(sphere)\n'

    else:
        return  'sphere_radius = 30.0\n\
sphere_angle = atan(2)\n\
sphere_origin = i.gp_Ax2(i.gp_Pnt(0, 0, 0), i.gp_Dir(0, 0, 1))\n\
sphere = i.BRepPrimAPI_MakeSphere(sphere_origin, sphere_radius, -sphere_angle, sphere_angle).Shape()\n\
display.DisplayShape(sphere)\n'

def make_point(arg):
    if arg == 'imp':
        return 'from OCC.Core.gp import gp_Pnt\n\
point = gp_Pnt(0, 0, 0)\n\
display.DisplayShape(point)\n'
    else:
        return 'point = gp_Pnt(0, 0, 0)\n\
display.DisplayShape(point)\n'

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

def bool_cut(arg):
    if arg == 'imp':
        return 'from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut\n\
from OCC.Core.Graphic3d import Graphic3d_NOM_STEEL\n\
result = BRepAlgoAPI_Cut(basis, cutter).Shape()\n\
display.DisplayShape(result, update=True, material=Graphic3d_NOM_STEEL)\n'
    else :
        return 'result = BRepAlgoAPI_Cut(basis, cutter).Shape()\n\
display.DisplayShape(result, update=True, material=Graphic3d_NOM_STEEL)\n'

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