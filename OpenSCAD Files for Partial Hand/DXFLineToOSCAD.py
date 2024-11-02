#Program to create points from dxf
import numpy as np

arrayNames=['startX','startY','endX','endY']
key=['10','20','11','21']
thickPercentage=.1

def readDXFLine(filename):
    returnarr=[]
    evenarr=[]
    oddarr=[]
    for i,line in enumerate(open(filename, 'r')):
        if i%2==0:
            evenarr.append(line[:-1])
        else:
            oddarr.append(line[:-1])
    tableOfCont=np.array(evenarr)
    content=np.array(oddarr)
    for k in key:
        returnarr.append(content[tableOfCont==k])
    return returnarr

def pointsToOpenPoints(points):
    outputstr=''
    for p in points:
        outputstr+=f"{str(np.round(float(p),2))}, "
    return outputstr[:-2]

def printToLine(rawInCol):
    for i,name in enumerate(arrayNames):
        print(f"{name}=[{pointsToOpenPoints(rawInCol[i])}];")

def printBounds(rawCols,widthPerc):
    x_vals=[]
    y_vals=[]
    for i,column in enumerate(rawCols):
        for j,value in enumerate(column):
            if i%2==1:
                y_vals.append(np.round(float(value),2))
            else:
                x_vals.append(np.round(float(value),2))
    x_width=np.max(x_vals)-np.min(x_vals)
    y_width=np.max(y_vals)-np.min(y_vals)
    x_min = np.round(np.min(x_vals)-abs(widthPerc*x_width),2)
    y_min = np.round(np.min(y_vals)-abs(widthPerc*y_width),2)
    x_max = np.round(np.max(x_vals)+abs(widthPerc*y_width),2)
    y_max = np.round(np.max(y_vals)+abs(widthPerc*x_width),2)
    print(f"bot_left=[{x_min},{y_min}];")
    print(f"top_right=[{x_max},{y_max}];")

def rawToPoints(rawCols):
    returnPoints=[]
    startX=rawCols[0]
    startY=rawCols[1]
    endX=rawCols[2]
    endY=rawCols[3]
    for i in range(len(startX)):
        returnPoints.append([startX[i],startY[i]])
    returnPoints.append([endX[-1],endY[-1]])
    print(returnPoints)
    return returnPoints

def raw2DPointsToOpen(rawPoints):
    output=[]
    for p in rawPoints:
        output.append([np.round(float(p[0]),2),np.round(float(p[1]),2)])
    print(output)
    return(output)


dxfFile = input('Input the relative file location of the DXF: ')

rawInCol = readDXFLine(dxfFile)

#printToLine(rawInCol)
#printBounds(rawInCol,thickPercentage)

raw2DPointsToOpen(rawToPoints(rawInCol))
