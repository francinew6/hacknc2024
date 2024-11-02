#!/usr/bin/env python
import sys
def inlinePrint(text):
    sys.stdout.write('\r')
    sys.stdout.write(text)
    sys.stdout.flush()
inlinePrint("Importing Subprocess")
import subprocess
inlinePrint("Importing VTK        ")
import vtk
inlinePrint("Importing numpy      ")
import numpy as np
inlinePrint("Importing time       ")
import time
inlinePrint("Importing solid2     ")
#import solid2 as pyscad
from solid2 import *
inlinePrint("Importing bezier   ")
import bezier
inlinePrint("Importing VTk Modules")
# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonDataModel import vtkPlane, vtkPolyLine, vtkCellArray, vtkPolyData
from vtkmodules.vtkCommonCore import vtkPoints
from vtkmodules.vtkFiltersCore import vtkCutter
from vtkmodules.vtkFiltersSources import vtkCubeSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)
inlinePrint("Imported vtk modules")
print("")




# Web Input
lengthSocket=100
lengthAmputation=150
lengthFullLimb=200
wristDiam=60
filename = "ReneeGardenerBaseScan" #example: TimArm.stl would be TimArm


# Defining variables
nominalDiam=75 #nominal diameter of limb in mm
skinOffset=0 #mm offset from skin for mesh

#Weave information
weaveAngle=45 #degree
weaveDiam=2.5 #mm
weaveWidth=6.5 #mm
weaveGap=0 #mm
weaveTransitionSpeed = 2 # larger values give sharper weave transitions
weaveNum=16 #number of weaves crossing each other
weaveStartAngle=0 #radians angle of initial weave
weaveEndType = "ring" # ring, plate, knots

#Center path information
centerPathDegree = 20 # level of fit of center path

# Rendering values
angularRes=90 #number of angular "pixels"
facetNum=4 #number of facets, $fn in openSCAD


#Calculated Variables
angleStepRad=2*np.pi/angularRes
stepZ=angleStepRad*(nominalDiam/2)/np.tan(weaveAngle*np.pi/180)
start_time = time.time()

# Translation functions from polar to cartesian coordinates and back
def cart2pol(x, y, z):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return(rho, phi, z)

def pol2cart(rho, phi, z):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return(x, y, z)

# determines strand offset for weave at given phi
def weaveOffAtPhi(weaveDiam, weaveGap, weaveNum, weaveStartAngle, phi):
    overlapAngleRad=2*np.pi/weaveNum
    # return ((weaveDiam+weaveGap)/2)*np.cos(2*np.pi/overlapAngleRad*(phi+weaveStartAngle))  ### Fully cosinal pattern - can be imitated with transition speed of 1
    return ((weaveDiam+weaveGap)/(2*np.tanh(weaveTransitionSpeed*np.cos(0))))*np.tanh(weaveTransitionSpeed*np.cos(2*np.pi/overlapAngleRad*(phi+weaveStartAngle)))

# determines radius at given phi given coords in one XY plane
def radAtPhi(coords, phi):
    ####### Important ##########
    # This equation is estimating radius - correct math needs to be performed later

    if phi<coords[0][1] and phi>coords[-1][1]:
        leftCoord = coords[0]
        rightCoord = coords[-1]
    else:
        adjCoords = coords[:,1]-phi
        leftCoord = coords[len(adjCoords[adjCoords<=0])-1]
        rightCoord = coords[-len(adjCoords[adjCoords>=0])]

    rad = (((phi-leftCoord[1])/(rightCoord[1]-leftCoord[1]))*(rightCoord[0]-leftCoord[0]))+leftCoord[0]
    return (rad)

# Creates spiral pattern with correct coordinates with input functions and values
def createPointPath(initPhi,coords,step,clock):
    currentPhi=initPhi
    #Outputs X,Y,Z coordinates
    pathOutput=np.zeros([len(coords),3])
    pathOutputPol=np.zeros([len(coords),3])
    if clock==True:
        for i,j in enumerate(coords):
            if currentPhi>np.pi:
                currentPhi=currentPhi-(2*np.pi)
            else:
                ...
            pathOutput[i,:] = pol2cart(radAtPhi(j, currentPhi)+weaveDiam+skinOffset+(weaveGap/2)+weaveOffAtPhi(weaveDiam, weaveGap, weaveNum, weaveStartAngle, currentPhi),currentPhi,j[0][2])
            pathOutputPol[i,:] = [radAtPhi(j, currentPhi)+weaveDiam+skinOffset+(weaveGap/2)+weaveOffAtPhi(weaveDiam, weaveGap, weaveNum, weaveStartAngle, currentPhi),currentPhi,j[0][2]]
            currentPhi+=step
    else:
        for i,j in enumerate(coords):
            if currentPhi<(-np.pi):
                currentPhi=(2*np.pi)+currentPhi
            pathOutput[i,:] = pol2cart(radAtPhi(j, currentPhi)+weaveDiam+skinOffset+(weaveGap/2)-weaveOffAtPhi(weaveDiam, weaveGap, weaveNum, weaveStartAngle, currentPhi),currentPhi,j[0][2])
            pathOutputPol[i,:] = [radAtPhi(j, currentPhi)+weaveDiam+skinOffset+(weaveGap/2)-weaveOffAtPhi(weaveDiam, weaveGap, weaveNum, weaveStartAngle, currentPhi),currentPhi,j[0][2]]
            currentPhi-=step
    return pathOutput, pathOutputPol

def plotArrayLine(array, ren, colors, color):
    centerLinePoints = vtkPoints()
    for i in array:
        centerLinePoints.InsertNextPoint(i)
    centerPolyLine = vtkPolyLine()
    centerPolyLine.GetPointIds().SetNumberOfIds(len(array))
    for i in range(len(array)):
        centerPolyLine.GetPointIds().SetId(i,i)
    cells=vtkCellArray()
    cells.InsertNextCell(centerPolyLine)
    centerPolyData = vtkPolyData()
    centerPolyData.SetPoints(centerLinePoints)
    centerPolyData.SetLines(cells)
    centerMapper = vtkPolyDataMapper()
    centerMapper.SetInputData(centerPolyData)
    centerActor = vtkActor()
    centerActor.SetMapper(centerMapper)
    centerActor.GetProperty().SetColor(colors.GetColor3d(color))
    centerActor.GetProperty().SetLineWidth(3)
    ren.AddActor(centerActor)

# Function to read an STL file and find min and max Z values
def find_min_max_z(stl_file):
    # Create a reader for the STL file
    reader = vtk.vtkSTLReader()
    reader.SetFileName(stl_file)
    reader.Update()

    # Get the output polydata from the reader
    polydata = reader.GetOutput()

    # Get the points from the polydata
    points = polydata.GetPoints()

    # Initialize min and max Z values
    min_z = float('inf')
    max_z = float('-inf')

    # Iterate over all points to find min and max Z values
    for i in range(points.GetNumberOfPoints()):
        z = points.GetPoint(i)[2]  # Get the Z value
        if z < min_z:
            min_z = z
        if z > max_z:
            max_z = z

    return min_z, max_z


############################ OpenSCAD Interaction ##################################

#initialize OpenSCAD File
set_global_fn(facetNum)


def main():
    ### Getting bounds
    minZ,maxZ = find_min_max_z(f"{filename}.stl")
    # Set Z values for analysis
    initialZ=maxZ-lengthSocket
    finalZ=maxZ

    colors = vtkNamedColors()

    # Create a cube
    cube = vtk.vtkSTLReader()
    cube.SetFileName(f"{filename}.stl")
    cubeMapper = vtkPolyDataMapper()
    cubeMapper.SetInputConnection(cube.GetOutputPort())

    # create cube actor
    cubeActor = vtkActor()
    cubeActor.GetProperty().SetColor(colors.GetColor3d('Aquamarine'))
    cubeActor.GetProperty().SetOpacity(0.5)
    cubeActor.SetMapper(cubeMapper)

    # create renderers and add actors of plane and cube
    ren = vtkRenderer()
    ren.AddActor(cubeActor)
    ren.SetBackground(colors.GetColor3d('Silver'))


    # Create array for ring definitions
    outlineArray = []
    outlineArrayCart = []
    centerLine = []

    ############################## Slice, Render, and Analyze slices #################################
    for i in np.arange(initialZ,finalZ,stepZ):
        #######  Slice and Render ##########
        # create a plane to cut,here it cuts in the XY direction (xz normal=(1,0,0);XY =(0,0,1),YZ =(0,1,0)
        plane = vtkPlane()
        plane.SetOrigin(0, 0, i)
        plane.SetNormal(0, 0, 1)

        # create cutter
        cutter = vtkCutter()
        cutter.SetCutFunction(plane)
        cutter.SetInputConnection(cube.GetOutputPort())
        cutter.Update()
        cutterMapper = vtkPolyDataMapper()
        cutterMapper.SetInputConnection(cutter.GetOutputPort())

        # create plane actor
        planeActor = vtkActor()
        planeActor.GetProperty().SetColor(colors.GetColor3d('yellow'))
        planeActor.GetProperty().SetLineWidth(1)
        planeActor.GetProperty().SetAmbient(1.0)
        planeActor.GetProperty().SetDiffuse(0.0)
        planeActor.SetMapper(cutterMapper)
        ren.AddActor(planeActor)
        #######################################

        ########### Analyze slices ###############
        #Get cutter points
        out=cutter.GetOutput()
        points=out.GetPoints()

        # Check plane exists
        try:
            NumPts=points.GetNumberOfPoints()
        except:
            inlinePrint(f"Z: {i} Not Valid")
            print(f"Halting slicing at Z = {i-stepZ}, proceed as usual")
            break

        # Define arrays of layer points
        outlinePts=np.zeros([NumPts,3])
        outlinePtsCart=np.zeros([NumPts,3])
        outlineAnalysis=np.zeros([NumPts,3])

        for n in range(0,NumPts,1):
            # writes each coordinate as (r, phi, z)
            coord=np.round(points.GetPoint(n),5)
            outlinePts[n,:]=np.round(cart2pol(coord[0],coord[1],coord[2]),5)
            outlinePtsCart[n,:]=coord
            outlineAnalysis[n,:]=coord # Append for centerline analysis
        outlineArray.append(outlinePts[outlinePts[:,1].argsort()])
        outlineArrayCart.append(outlinePtsCart)
        # Add centerline point
        centerPoint = outlineAnalysis.mean(axis=0)
        centerLine.append(centerPoint)
    ################# End of slicing loop #########################



    # Make final outline arrays
    outlineArray= np.asarray(outlineArray, dtype=object)
    outlineArrayCart=np.asarray(outlineArrayCart,dtype=object)

    # Make smooth centerline
    centerLine = np.asarray(centerLine)
    centerLineFitPoints = []
    # centerLineFitPoints = np.array([centerLine[0],centerLine[int(centerPathSlice1*len(centerLine))],centerLine[int(centerPathSlice2*len(centerLine))],centerLine[int(centerPathSlice3*len(centerLine))],centerLine[int(centerPathSlice4*len(centerLine))],centerLine[-1]])
    for i in np.linspace(0,len(centerLine)-1,centerPathDegree+1):
        centerLineFitPoints.append(centerLine[int(i)])
    centerLineFitPoints = np.asarray(centerLineFitPoints)

    nodes = np.array([centerLineFitPoints[:,0],centerLineFitPoints[:,1],centerLineFitPoints[:,2]])
    curve = bezier.Curve(nodes, degree=centerPathDegree)

    # Define points evenly spaced in time
    tFine = np.linspace(0,1,len(centerLine))
    pointsFine = curve.evaluate_multi(tFine)
    pointsFine.shape

    # Define evenly spaced z layers that match to z layers sliced
    t_zregular = np.interp(centerLine[:,2], pointsFine[2], tFine)
    points_zregular = curve.evaluate_multi(t_zregular)

    # Create center line at given z values
    centerLineSmooth = np.zeros([len(points_zregular[0]),3])
    for i in range(len(centerLineSmooth)):
        centerLineSmooth[i,:]=[points_zregular[0,i],points_zregular[1,i],points_zregular[2,i]]
    centerLineRough = centerLine
    centerLine = centerLineSmooth

    plotArrayLine(centerLine, ren, colors, "red")
    plotArrayLine(centerLineRough, ren, colors, "blue")
    plotArrayLine(centerLineFitPoints, ren, colors, "purple")




    # Add renderer to renderwindow and render
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetSize(1200, 1000)
    renWin.SetWindowName('Cutter')

    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Set camera position
    camera = ren.GetActiveCamera()
    camera.SetPosition(10, 10, 10)
    camera.SetFocalPoint(centerLine[int(len(centerLine)/2)])
    camera.SetViewUp(0, 0, 0)
    camera.SetDistance(40)
    camera.SetClippingRange(0.2019, 165.753)

    # exit = False
    # while exit==False:
    #     #Render
    #renWin.Render()
    #iren.Start()


    # inputHandler = MyInteractorStyle()

    # Check if slice looks good
    proceed = "y" #input("Ready to proceed? (y/n) ")



    if proceed=="y" or proceed=="Y":

        outlineArrayCartSmooth = []
        outlineArrayPolSmooth = []

        for i, planePts in enumerate(outlineArrayCart):
            outlinePtsCartAdj = np.zeros([len(planePts),3])
            outlinePtsPolAdj = np.zeros([len(planePts),3])
            for j, point in enumerate(planePts):
                outlinePtsCartAdj[j,:]=[point[0]-centerLineSmooth[i,0],point[1]-centerLineSmooth[i,1],point[2]]
                outlinePtsPolAdj[j,:]=cart2pol(outlinePtsCartAdj[j,0],outlinePtsCartAdj[j,1],outlinePtsCartAdj[j,2])
            outlineArrayCartSmooth.append(outlinePtsCartAdj)
            outlineArrayPolSmooth.append(outlinePtsPolAdj[outlinePtsPolAdj[:,1].argsort()])

        # Reassign base arrays to new smoothed versions
        outlineArray = np.asarray(outlineArrayPolSmooth, dtype=object)
        outlineArrayCart = np.asarray(outlineArrayCartSmooth, dtype=object)


        # Create array to store weave values
        weaveArray = []
        weaveArrayAnti = []
        weaveArrayPol = []
        weaveArrayAntiPol = []

        # Generate Mesh profile
        meshProf = hull()(translate(([0,-(weaveWidth-weaveDiam)/2,0]))(sphere(d=weaveDiam)),translate(([0,(weaveWidth-weaveDiam)/2,0]))(sphere(d=weaveDiam)))

        # Generate Mesh
        model = union()
        for w,i in enumerate(np.linspace(-np.pi,np.pi,weaveNum, endpoint=False)):
            pathCurr, pathCurrPol = createPointPath(i,outlineArray,angleStepRad,True)
            for j in range(len(pathCurr)-1):
                model+=hull()(translate((pathCurr[j][0]+centerLine[j][0],pathCurr[j][1]+centerLine[j][1],pathCurr[j][2]))(rotate(([0,0,pathCurrPol[j][1]*180/np.pi]))(meshProf)),translate((pathCurr[j+1][0]+centerLine[j+1][0],pathCurr[j+1][1]+centerLine[j+1][1],pathCurr[j+1][2]))(rotate(([0,0,pathCurrPol[j+1][1]*180/np.pi]))(meshProf)))
            pathCurrAnti, pathCurrAntiPol = createPointPath(i,outlineArray,angleStepRad,False)
            for j in range(len(pathCurrAnti)-1):
                model+=hull()(translate((pathCurrAnti[j][0]+centerLine[j][0],pathCurrAnti[j][1]+centerLine[j][1],pathCurrAnti[j][2]))(rotate(([0,0,pathCurrAntiPol[j][1]*180/np.pi]))(meshProf)),translate((pathCurrAnti[j+1][0]+centerLine[j+1][0],pathCurrAnti[j+1][1]+centerLine[j+1][1],pathCurrAnti[j+1][2]))(rotate(([0,0,pathCurrAntiPol[j+1][1]*180/np.pi]))(meshProf)))
            weaveArray.append(pathCurr)
            weaveArrayAnti.append(pathCurrAnti)
            weaveArrayPol.append(pathCurrPol)
            weaveArrayAntiPol.append(pathCurrAntiPol)
            sys.stdout.write('\r')
            sys.stdout.write(f"Weave: {w+1} / {weaveNum}  Time: {np.round((time.time()-start_time),3)} s")
            sys.stdout.flush()
        weaveArray = np.asarray(weaveArray, dtype=object)
        weaveArrayAnti = np.asarray(weaveArrayAnti, dtype=object)
        weaveArrayPol = np.asarray(weaveArrayPol, dtype=object)
        weaveArrayAntiPol = np.asarray(weaveArrayAntiPol, dtype=object)




        # Export OpenSCAD to file
        scad_render_to_file(model, f"{filename}.scad")
        print(f"\nThank you! Total time (including inputs) = {np.round((time.time()-start_time),2)}")
        print(f"File is exported at {filename}.scad")

        # Compile to STL using OpenSCAD
        try:
            result = subprocess.run(
                ["openscad", "--enable","all", "-o", f"{filename}_output.stl", f"{filename}.scad"],
                check=True,
                capture_output=True,
                text=True
            )
            print("OpenSCAD Output:", result.stdout)
            print("OpenSCAD Errors:", result.stderr)
        except subprocess.CalledProcessError as e:
            print("An error occurred:", e)
            print("Return code:", e.returncode)
            print("Output:", e.output)
            print("Error output:", e.stderr)
    else:
        print("Sorry :) Goodbye")


if __name__ == '__main__':
    main()
