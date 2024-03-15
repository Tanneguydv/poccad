import sys
import numpy as np
from math import cos, pi

from OCC.Core.BRep import BRep_Builder
from OCC.Core.BRepFilletAPI import BRepFilletAPI_MakeFillet
from OCC.Core.TopoDS import TopoDS_Shell, topods
from OCC.Core.TopLoc import TopLoc_Location
from OCC.Display.SimpleGui import init_display
from OCC.Core.gp import gp_Ax2, gp_Pnt, gp_Dir, gp_Pnt2d, gp_Ax1, gp_Trsf
from OCC.Core.LocOpe import LocOpe_FindEdges
from OCC.Extend.TopologyUtils import TopologyExplorer
from OCCUtils.Construct import make_box

display, start_display, add_menu, add_function_to_menu = init_display()

box1 = make_box(gp_Pnt(0, 0, 0), 20, 20, 20)
box1_faces = list(TopologyExplorer(box1).faces())

# Make Shell by only two faces
box1_shell = TopoDS_Shell()
bild = BRep_Builder()
bild.MakeShell(box1_shell)
for shp in [box1_faces[0], box1_faces[2]]:
    bild.Add(box1_shell, shp)

# Find Edge that the two faces share
find_edge = LocOpe_FindEdges(box1_faces[0], box1_faces[2])
find_edge.InitIterator()
fillet_edge = find_edge.EdgeTo()

# Create Fillet of R5 on shared Edge.
fillet = BRepFilletAPI_MakeFillet(box1_shell, 0)
fillet.Add(5, fillet_edge)
fillet.Build()
if fillet.IsDone():
    display.DisplayShape(fillet.Shape())
else:
    print("fillet is not done")
display.DisplayShape(box1_shell, transparency=0.7)

box2_ = make_box(gp_Pnt(40, 0, 0), 20, 20, 20)


# Rotate 45 degree
box2_trsf = gp_Trsf()
box2_trsf.SetRotation(gp_Ax1(gp_Pnt(40, 0, 0), gp_Dir(0, 0, 1)), np.deg2rad(45))
box2_faces = list(TopologyExplorer(box2_).faces())
face = box2_faces[0].Moved(TopLoc_Location(box2_trsf))

faces = box2_faces.copy()
face2 = faces[2]

from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Copy
# Créez une copie de la face
copied_face_builder = BRepBuilderAPI_Copy(face2)
copied_face = topods.Face(copied_face_builder.Shape())


copied_face_builder0 = BRepBuilderAPI_Copy(face)
copied_face0 = topods.Face(copied_face_builder0.Shape())

import ctypes

print(id(copied_face))
print(id(box2_faces[2]))

# Make Shell by only two faces
box2_shell = TopoDS_Shell()
bild = BRep_Builder()
bild.MakeShell(box2_shell)
for shp in [copied_face0, copied_face]:
    bild.Add(box2_shell, shp)


# box2_shell.Move(TopLoc_Location(box2_trsf))
box2_shell_faces = list(TopologyExplorer(box2_shell).faces())


# Find Edge that the two faces share
find_edge = LocOpe_FindEdges(box2_shell_faces[0], box2_shell_faces[1])
find_edge.InitIterator()
fillet_edge = find_edge.EdgeTo()

# Create Fillet of R5 on shared Edge.
fillet = BRepFilletAPI_MakeFillet(box2_shell, 0)
fillet.Add(2, fillet_edge)
# fillet.Build() 
if fillet.IsDone():
    display.DisplayShape(fillet.Shape())
else:
    print("fillet is not done")

display.DisplayShape(box2_shell, transparency=0.7)

display.FitAll()
start_display()