""" This module loads the entire VTK library into its namespace.  It
also allows one to use specific packages inside the vtk directory.."""

from __future__ import absolute_import

# --------------------------------------
from .vtkCommonCore import *
try:
  from .vtkWebCore import *
except ImportError:
  pass
from .vtkCommonMath import *
from .vtkCommonTransforms import *
from .vtkCommonDataModel import *
from .vtkCommonExecutionModel import *
from .vtkIOCore import *
from .vtkImagingCore import *
from .vtkIOImage import *
from .vtkIOXMLParser import *
from .vtkIOXML import *
from .vtkCommonMisc import *
from .vtkFiltersCore import *
from .vtkRenderingCore import *
from .vtkRenderingContext2D import *
from .vtkRenderingFreeType import *
try:
  from .vtkRenderingSceneGraph import *
except ImportError:
  pass
try:
  from .vtkRenderingVtkJS import *
except ImportError:
  pass
from .vtkIOExport import *
try:
  from .vtkWebGLExporter import *
except ImportError:
  pass
from .vtkInteractionStyle import *
from .vtkFiltersGeneral import *
from .vtkFiltersSources import *
from .vtkInteractionWidgets import *
from .vtkViewsCore import *
from .vtkViewsInfovis import *
try:
  from .vtkCommonColor import *
except ImportError:
  pass
from .vtkViewsContext2D import *
from .vtkTestingRendering import *
from .vtkRenderingLabel import *
try:
  from .vtkRenderingQt import *
except ImportError:
  pass
from .vtkPythonContext2D import *
from .vtkImagingMath import *
try:
  from .vtkRenderingHyperTreeGrid import *
except ImportError:
  pass
from .vtkRenderingUI import *
from .vtkRenderingOpenGL2 import *
from .vtkRenderingVolume import *
from .vtkRenderingVolumeOpenGL2 import *
try:
  from .vtkRenderingMatplotlib import *
except ImportError:
  pass
from .vtkRenderingLOD import *
from .vtkRenderingLICOpenGL2 import *
from .vtkRenderingImage import *
from .vtkRenderingContextOpenGL2 import *
from .vtkIOLegacy import *
try:
  from .vtkIOXdmf2 import *
except ImportError:
  pass
from .vtkIOVeraOut import *
from .vtkIOTecplotTable import *
from .vtkIOSegY import *
try:
  from .vtkIOXdmf3 import *
except ImportError:
  pass
from .vtkIOParallelXML import *
from .vtkIOPLY import *
from .vtkIOMovie import *
from .vtkIOOggTheora import *
from .vtkIONetCDF import *
from .vtkIOMotionFX import *
from .vtkIOGeometry import *
from .vtkIOParallel import *
from .vtkIOMINC import *
from .vtkIOLSDyna import *
from .vtkIOInfovis import *
from .vtkIOImport import *
from .vtkParallelCore import *
from .vtkIOIOSS import *
from .vtkIOVideo import *
try:
  from .vtkIOFFMPEG import *
except ImportError:
  pass
from .vtkIOExportPDF import *
try:
  from .vtkRenderingGL2PSOpenGL2 import *
except ImportError:
  pass
from .vtkIOExportGL2PS import *
from .vtkIOExodus import *
from .vtkIOEnSight import *
from .vtkIOCityGML import *
from .vtkIOChemistry import *
from .vtkIOCesium3DTiles import *
from .vtkIOCONVERGECFD import *
from .vtkIOHDF import *
from .vtkIOCGNSReader import *
from .vtkIOAsynchronous import *
from .vtkIOAMR import *
from .vtkInteractionImage import *
from .vtkImagingStencil import *
from .vtkImagingStatistics import *
from .vtkImagingGeneral import *
from .vtkImagingMorphological import *
from .vtkImagingFourier import *
from .vtkIOSQL import *
from .vtkImagingSources import *
from .vtkInfovisCore import *
from .vtkGeovisCore import *
from .vtkInfovisLayout import *
from .vtkRenderingAnnotation import *
from .vtkImagingHybrid import *
from .vtkImagingColor import *
from .vtkFiltersTopology import *
from .vtkFiltersSelection import *
from .vtkFiltersSMP import *
from .vtkFiltersPython import *
from .vtkFiltersProgrammable import *
from .vtkFiltersModeling import *
from .vtkFiltersPoints import *
from .vtkFiltersVerdict import *
from .vtkFiltersStatistics import *
from .vtkFiltersImaging import *
from .vtkFiltersExtraction import *
from .vtkFiltersGeometry import *
from .vtkFiltersHybrid import *
from .vtkFiltersTexture import *
from .vtkFiltersParallel import *
from .vtkFiltersParallelImaging import *
from .vtkCommonSystem import *
try:
  from .vtkFiltersParallelDIY2 import *
except ImportError:
  pass
from .vtkFiltersGeneric import *
from .vtkCommonComputationalGeometry import *
from .vtkFiltersFlowPaths import *
from .vtkFiltersAMR import *
from .vtkDomainsChemistry import *
from .vtkDomainsChemistryOpenGL2 import *
from .vtkFiltersHyperTree import *
from .vtkCommonPython import *
from .vtkChartsCore import *


# useful macro for getting type names
from .util.vtkConstants import vtkImageScalarTypeNameMacro

# import convenience decorators
from .util.misc import calldata_type

# import the vtkVariant helpers
from .util.vtkVariant import *
