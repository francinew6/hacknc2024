#!/usr/bin/env python
import sys
import os
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




#Defining variables
lengthSocket=120
lengthAmputation=260
lengthFullLimb=275
wristDiam=35
filename = "OllieScanOriented" #example: TimArm.stl would be TimArm


skinOffset=1 #mm offset from skin for mesh
minimumSocketThickness=2.5 #mm

#Center path information
centerPathDegree = 20 # level of fit of center path

# Rendering values
angularRes=90 #number of angular voxels
verticalRes=100 #number of vertical voxels
facetNum=4 #number of facets, $fn in openSCAD

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

def sparceCoords(coords,angularRes):
    #Outputs X,Y,Z coordinates - not corrected for centerline
    solidWrapOutput=np.zeros([len(coords),angularRes,3])
    for i,l in enumerate(coords):
        for j,p in enumerate(np.linspace(-np.pi,np.pi, angularRes, endpoint=False)):
            solidWrapOutput[i,j,:]=pol2cart(radAtPhi(l,p)+skinOffset+minimumSocketThickness,p,l[0][2])
    return(solidWrapOutput)

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

def largestAnglePoints(points,coords):
    # takes polar points and polar coords in form (r,phi,z)
    largestAnglePointOutput=np.zeros([len(points),3])
    angleArray=np.zeros([len(points)])
    for i in range(len(points)):
        rPoint,phiPoint,zPoint=points[i]
        for j in range(len(coords)):
            coordLevel=coords[j]
            coords_sorted = coordLevel[coordLevel[:, 1].argsort()]
            rCoord=radAtPhi(coords_sorted,phiPoint)
            zCoord=coords[j,0,2]

            #print(coords[:,i,:][j])
            angleAtPoint=np.arccos((rCoord-rPoint)/(zCoord-zPoint))
            if angleAtPoint>angleArray[i]:
                angleArray[i]=angleAtPoint
                largestAnglePointOutput[i]=rCoord,phiPoint,zCoord
        #largestAnglePointOutput[i]= np.argmax(angleArray)
    print(largestAnglePointOutput)
    return largestAnglePointOutput


############################ OpenSCAD Interaction ##################################

#initialize OpenSCAD File
set_global_fn(facetNum)


def main(uploaded_filename, socket_length, amputation_length, limb_length, wrist_diameter):
    lengthSocket = socket_length
    lengthAmputation = amputation_length
    lengthFullLimb = limb_length
    wristDiam = wrist_diameter
    filename = uploaded_filename
    
    #Calculated Variables
    if (lengthFullLimb-lengthAmputation)>30:
        wristSpacing=lengthFullLimb-lengthAmputation
    else:
        wristSpacing=35
    
    # Getting bounds
    minZ,maxZ = find_min_max_z(f"{filename}")
    print(minZ)
    print(maxZ)
    # Set Z values for analysis
    initialZ=maxZ-lengthSocket
    finalZ=maxZ
    stepZ=(finalZ-initialZ)/verticalRes

    colors = vtkNamedColors()

    # Create a cube
    cube = vtk.vtkSTLReader()
    cube.SetFileName(f"{filename}")
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


    # renWin.Render()
    # iren.Start()


    # inputHandler = MyInteractorStyle()

    # Check if slice looks good
    proceed = "y" #input("Ready to proceed? (y/n) ")



    if proceed=="y" or proceed=="Y":
        #### Smooth outline Arrays ####
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


        ############### Generate Solid Inner Sleeve #################
        sparceOuter = sparceCoords(outlineArray,angularRes)
        model = union()
        # Add all layers:
        for i in range(0,len(sparceOuter)-1):
            layerModel=union()
            layerModel2=union()
            for j,x in enumerate(sparceOuter[i]):
                layerModel+=hull()(
                    translate((x[0]+centerLine[i][0],x[1]+centerLine[i][1],x[2]))(sphere(d=minimumSocketThickness)),
                    translate((sparceOuter[i][(j+1)%len(sparceOuter[i])][0]+centerLine[i][0],sparceOuter[i][(j+1)%len(sparceOuter[i])][1]+centerLine[i][1],sparceOuter[i][(j+1)%len(sparceOuter[i])][2]))(sphere(d=minimumSocketThickness)),
                    translate((sparceOuter[i+1][(j+1)%len(sparceOuter[i+1])][0]+centerLine[i+1][0],sparceOuter[i+1][(j+1)%len(sparceOuter[i+1])][1]+centerLine[i+1][1],sparceOuter[i+1][(j+1)%len(sparceOuter[i+1])][2]))(sphere(d=minimumSocketThickness)))
                layerModel2+=hull()(
                    translate((x[0]+centerLine[i][0],x[1]+centerLine[i][1],x[2]))(sphere(d=minimumSocketThickness)),
                    translate((sparceOuter[i+1][j][0]+centerLine[i+1][0],sparceOuter[i+1][j][1]+centerLine[i+1][1],sparceOuter[i+1][j][2]))(sphere(d=minimumSocketThickness)),
                    translate((sparceOuter[i+1][(j+1)%len(sparceOuter[i+1])][0]+centerLine[i+1][0],sparceOuter[i+1][(j+1)%len(sparceOuter[i+1])][1]+centerLine[i+1][1],sparceOuter[i+1][(j+1)%len(sparceOuter[i+1])][2]))(sphere(d=minimumSocketThickness)))
                sys.stdout.write('\r')
                sys.stdout.write(f"Weave: {i+1} / {len(sparceOuter)}  Time: {np.round((time.time()-start_time),3)} s")
                sys.stdout.flush()
            model+=layerModel
            model+=layerModel2
        # Add last layer (solid)
        layerModel=union()
        for j,x in enumerate(sparceOuter[-1]):
            layerModel+=hull()(
                translate((x[0]+centerLine[-1][0],x[1]+centerLine[-1][1],x[2]))(sphere(d=minimumSocketThickness)),
                translate((sparceOuter[-1][(j+1)%len(sparceOuter[i])][0]+centerLine[-1][0],sparceOuter[-1][(j+1)%len(sparceOuter[-1])][1]+centerLine[-1][1],sparceOuter[-1][(j+1)%len(sparceOuter[-1])][2]))(sphere(d=minimumSocketThickness)),
                translate((centerLine[-1][0],centerLine[-1][1],x[2]))(sphere(d=minimumSocketThickness)))
        model+=layerModel


        ##### Wrist unit ########
        wristUnit=union()
        wristUnitRingPoints=np.zeros([angularRes,3])
        for i,a in enumerate(np.linspace(-np.pi,np.pi,angularRes,endpoint=False)):
            wristUnitRingPoints[i,:]=[wristDiam/2,a,maxZ+wristSpacing]

        sparceOuterCorrected=np.zeros([len(sparceOuter),len(sparceOuter[0]),len(sparceOuter[0][0])])
        sparceOuterCorrectedPol=np.zeros([len(sparceOuter),len(sparceOuter[0]),len(sparceOuter[0][0])])
        for i in range(len(sparceOuter)):
            for j in range(len(sparceOuter[i])):
                sparceOuterCorrected[i,j,:]=(sparceOuter[i][j][0]+centerLine[i][0],sparceOuter[i][j][1]+centerLine[i][1],sparceOuter[i][j][2])
                sparceOuterCorrectedPol[i,j,:]=cart2pol(sparceOuter[i][j][0]+centerLine[i][0],sparceOuter[i][j][1]+centerLine[i][1],sparceOuter[i][j][2])

        largeAnglePointIndex = largestAnglePoints(wristUnitRingPoints,sparceOuterCorrectedPol)
        for i,w in enumerate(wristUnitRingPoints):
            cartCoord = pol2cart(wristUnitRingPoints[i,0],wristUnitRingPoints[i,1],wristUnitRingPoints[i,2])
            cartCoord2 = pol2cart(largeAnglePointIndex[i,0],largeAnglePointIndex[i,1],largeAnglePointIndex[i,2])
            cartCoord3 = pol2cart(largeAnglePointIndex[(i+1)%len(wristUnitRingPoints),0],largeAnglePointIndex[(i+1)%len(wristUnitRingPoints),1],largeAnglePointIndex[(i+1)%len(wristUnitRingPoints),2])
            cartCoord4 = pol2cart(wristUnitRingPoints[(i+1)%len(wristUnitRingPoints),0],wristUnitRingPoints[(i+1)%len(wristUnitRingPoints),1],wristUnitRingPoints[(i+1)%len(wristUnitRingPoints),2])
            wristUnit+=hull()(
                    translate(centerLine[-1][0]+cartCoord[0],centerLine[-1][1]+cartCoord[1],cartCoord[2])(cylinder(d=minimumSocketThickness,h=1, _fn=64)),
                    translate(cartCoord2)(sphere(d=minimumSocketThickness)),
                    translate(cartCoord3)(sphere(d=minimumSocketThickness))
                )
            wristUnit+=hull()(
                    translate(centerLine[-1][0]+cartCoord[0],centerLine[-1][1]+cartCoord[1],cartCoord[2])(cylinder(d=minimumSocketThickness,h=1, _fn=64)),
                    translate(cartCoord3)(sphere(d=minimumSocketThickness)),
                    translate(centerLine[-1][0]+cartCoord4[0],centerLine[-1][1]+cartCoord4[1],cartCoord4[2])(cylinder(d=minimumSocketThickness,h=1, _fn=64))
                )
        wristUnit+=translate(centerLine[-1][0],centerLine[-1][1],maxZ+1)(cylinder(h=wristSpacing,d=wristDiam,_fn=64))


        model+=wristUnit


        cuttingTool=import_stl("cuttingTool.stl")
        model-=translate(centerLine[-1][0],centerLine[-1][1],maxZ+wristSpacing+1)(cuttingTool)




        # Export OpenSCAD to file
        scad_render_to_file(model, "result.scad")
        print(f"\nOpenSCAD is exported at result.scad")
        print("Exporting STL file using OpenSCAD backend...")

        # Compile to STL using OpenSCAD
        try:
            result = subprocess.run(
                ["openscad", "--backend","Manifold", "-o", "static/result.stl", "result.scad"],
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
        print(f"Thank you! Total time (including inputs) = {np.round((time.time()-start_time),2)}")
        print(f"STL is exported at {filename}")

    else:
        print("Sorry :) Goodbye")


if __name__ == '__main__':
    main()
