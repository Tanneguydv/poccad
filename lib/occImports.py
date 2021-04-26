from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox , BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakeSphere
from OCC.Core.BRepOffsetAPI import  BRepOffsetAPI_MakePipeShell
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeVertex,  BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire
from OCC.Core.Geom import Geom_BezierCurve , Geom_RectangularTrimmedSurface ,Geom_Circle
from OCC.Core.Law import Law_Linear
from OCC.Core.TColgp import TColgp_Array1OfPnt , TColgp_Array1OfPnt2d
from OCC.Core.gp import gp_Circ, gp_Pnt, gp_ZOX , gp_Pln, gp_XOY, gp_Ax3, gp_YOZ, gp_Elips, gp_Ax2, gp_Dir, gp_XYZ , gp_Pnt2d
from OCC.Core.IntAna import IntAna_IntConicQuad
from OCC.Core.Precision import precision_Angular, precision_Confusion
from OCC.Core.GC import GC_MakePlane, GC_MakeEllipse
from OCC.Core.GeomAPI import GeomAPI_ProjectPointOnCurve
from OCC.Core.BRepBndLib import brepbndlib_AddOBB
from OCC.Core.Bnd import Bnd_OBB
from OCC.Core.Geom2dAPI import Geom2dAPI_PointsToBSpline
from OCC.Core.Geom2d import Geom2d_OffsetCurve
from OCC.Core.Bnd import Bnd_Box
from OCC.Core.BRepBndLib import brepbndlib_Add
from OCC.Core.BRepMesh import BRepMesh_IncrementalMesh
from OCC.Extend.DataExchange import read_stl_file, read_step_file
from OCC.Core.gp import gp_Vec, gp_Trsf
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCC.Core.Graphic3d import Graphic3d_NOM_STEEL
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut
