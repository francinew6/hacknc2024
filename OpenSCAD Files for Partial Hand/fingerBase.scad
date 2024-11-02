//////////////////////////////////////////////////////////
///////////// Combination program for every part /////////
//////////////////////////////////////////////////////////
$fn=128;

/////////////////// Parameters //////////////////////

//- Inside finger width
innerWidth=7.8;
//-Outside width
outerWidth=14.6;
//- Radius of pin hole
innerRadius=5.4/2;
//- Height of base of finger
outerRadius=8;
//- Length of part
distalLength=49;
//- How tall the pad of finger is from the print bed
distalTipHeight=19.5;
//- Clearance around joint width
jointWidthClearance=.3;
//- Clearance around radius of joint
jointRadiusClearance=1;
//- Rubber width
rubberClearance=3;
//- Rubber Length
lengthOfElastic=18;
//- Angle of fingertip (degrees)
fingertipAngle=35; //degrees
//- Length of pin head (long side)
pinHeadLength=6.5;
//- Width of pin
pinWidth=4.5;
//- Depth of pin head 
pinHeadDepth=1.6;
//- Depth of clip hole
pinClipDepth=2;
//- Diameter of clip
pinClipDiam=6;
//- Diameter of pin
pinDiam=5;
//-Clearance around pin
pinClear=.25;
//- Vertcal scale factor for base of skin to attach to fingertip
skinScale = .9;
//- Width of proximal finger "skin" at base
skinWidth=16.6;
//- Height of proximal finger "skin" at base
skinHeight=20;
//- Length of proximal section between peg holes
length=27;
//- Radius of path for string
stringPathRadius=1;
//- Taper of proximal skin
proximalSkinTaper=.85;
//- Finger base channel fillet
fingerBaseFillet = 1;

module proximalSkin(skinWidth,skinHeight,skinLength,taper=.85){ 
    //Section to define and make the "skin"
    rotate([-90,0,0]) 
    linear_extrude(skinLength,center=true,scale=taper) 
    polygon(points = [[0.017102*skinWidth,-1.0*skinHeight],[-0.144914*skinWidth,-0.988835*skinHeight],[-0.243024*skinWidth,-0.979763*skinHeight],[-0.319532*skinWidth,-0.962317*skinHeight],[-0.377138*skinWidth,-0.936497*skinHeight],[-0.415842*skinWidth,-0.90649*skinHeight],[-0.458146*skinWidth,-0.857641*skinHeight],[-0.480648*skinWidth,-0.791347*skinHeight],[-0.49505*skinWidth,-0.71947*skinHeight],[-0.50045*skinWidth,-0.605722*skinHeight],[-0.493249*skinWidth,-0.483601*skinHeight],[-0.477948*skinWidth,-0.329379*skinHeight],[-0.448245*skinWidth,-0.199581*skinHeight],[-0.409541*skinWidth,-0.090021*skinHeight],[-0.368137*skinWidth,-0.034194*skinHeight],[-0.327633*skinWidth,0.0*skinHeight],[0.351935*skinWidth,0.0*skinHeight],[0.39964*skinWidth,-0.034194*skinHeight],[0.437444*skinWidth,-0.09351*skinHeight],[0.457246*skinWidth,-0.160502*skinHeight],[0.480648*skinWidth,-0.237264*skinHeight],[0.489649*skinWidth,-0.332868*skinHeight],[0.49685*skinWidth,-0.457083*skinHeight],[0.49955*skinWidth,-0.579204*skinHeight],[0.487849*skinWidth,-0.701326*skinHeight],[0.467147*skinWidth,-0.826936*skinHeight],[0.452745*skinWidth,-0.86462*skinHeight],[0.427543*skinWidth,-0.900907*skinHeight],[0.387939*skinWidth,-0.933008*skinHeight],[0.337534*skinWidth,-0.956734*skinHeight],[0.281728*skinWidth,-0.972784*skinHeight],[0.209721*skinWidth,-0.985345*skinHeight],[0.142214*skinWidth,-0.990928*skinHeight]], paths = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,0]]);
}
module proximalMiddleFingers(length,outerRadius,innerRadius,fingerWidth,taper){
    //creates middle connector
    translate([0,0,outerRadius]) rotate([0,90,0]) 
    difference(){
        union(){
            linear_extrude(fingerWidth,center=true) hull(){
              translate([0,-length/2,0]) circle(outerRadius);
              translate([(1-taper)*outerRadius,length/2,0]) circle(taper*outerRadius);};
          };
        
    }
};

module proximalSkinCutObjects(skinWidth,skinHeight,skinLength,length,outerRadius,clearance,frontPegYOffset, frontPegLength, backPegYOffset, backPegLength, backPegHeight,rubberClearance){
    //creates objects to subtract from skin
    //Cut out circles around holes
    translate([0,0,outerRadius]) rotate([0,90,0]) 
    union(){
        linear_extrude(skinWidth+1,center=true) translate([0,-length/2,0]) circle(outerRadius+clearance);
        linear_extrude(skinWidth+1,center=true) translate([0,length/2,0]) circle(outerRadius+clearance);
    };
    //Cut off front
    translate([-(skinWidth+1)/2,frontPegYOffset-frontPegLength/2-2*clearance,0]) cube([skinWidth+1,skinWidth+1,skinHeight]);
    //Cut off back lower corner
    translate([0,-length/2,outerRadius/2]) cube([skinWidth+1,2*outerRadius,outerRadius],center=true);
    //Cut around back peg
    peg(rubberClearance+1.3*backPegLength,.5*innerWidth+rubberClearance,skinHeight,ypos=backPegYOffset,zpos=2*outerRadius+skinHeight/2,angle=-5);
    };

module proximalAllCutObjects(skinWidth,skinHeight,skinLength,length,outerRadius,clearance,frontPegYOffset, frontPegLength, backPegYOffset, backPegLength, backPegHeight,rubberClearance){
    //Circles through fingers
    translate([0,0,outerRadius]) rotate([0,90,0]) union(){
    linear_extrude(innerWidth+1,center=true) translate([0,-length/2,0]) circle(innerRadius);
    linear_extrude(innerWidth+1,center=true) translate([0,length/2,0]) circle(innerRadius);
    };
    //Fishing line run
    translate([0,0,2*stringPathRadius]) rotate([90,0,0]) cylinder(length+2*outerRadius,r=stringPathRadius,center=true);
    difference(){
        translate([0,0,stringPathRadius]) cube([2*stringPathRadius,length+2*outerRadius,2*stringPathRadius],center=true);
        translate([0,0,stringPathRadius]) cube([2*stringPathRadius,.5*length,2*stringPathRadius],center=true);
    }; 
    translate([0,-length/2-outerRadius,2*stringPathRadius]) cube([2*stringPathRadius,outerRadius,length],center=true);
};

module peg(length,width,height,xpos=0,ypos=0,zpos=0,angle=0,lipheight=.1,lipwidth=.5,radius=.5){
    translate([xpos,ypos,zpos])
    rotate([angle,0,0])
    union(){
    minkowski() {
        cube([width-2*radius+2*lipwidth,length-2*radius+2*lipwidth,lipheight],center=true);
        sphere(radius);};
    translate([0,0,-height/2])
    linear_extrude(height,center=true)
    minkowski(){
        square([width-2*radius,length-2*radius],center=true);
        circle(radius);
    }
    };
}


module drawProximal(skinWidth,skinHeight,length,outerRadius,
    innerRadius,fingerWidth,clearance,rubberClearance,lengthOfElastic,taper=.85) {
        //Creates proximal finger joint at origin from paramaters listed
    frontPegYOffset=length/2;
    frontPegLength=lengthOfElastic/2;
    backPegYOffset=-.7*(length/2);
    backPegZOffset=2*outerRadius+(2/3)*outerRadius;
    backPegLength=.8*lengthOfElastic/2;
    backPegHeight=(2/3)*outerRadius;
    skinLength=length*.75;
    difference(){
        union() {
            difference(){
            proximalSkin(skinWidth,skinHeight,skinLength,taper=taper);
            proximalSkinCutObjects(skinWidth,skinHeight,skinLength,length,outerRadius,clearance,frontPegYOffset,frontPegLength,backPegYOffset, backPegLength, backPegHeight, rubberClearance);
        };
            //Front peg:
            peg(frontPegLength,.5*fingerWidth,(2/3)*outerRadius,ypos=frontPegYOffset,zpos=1.7*outerRadius+(2/3)*outerRadius-2,angle=-15);
            //Back peg
            peg(backPegLength,.5*fingerWidth,backPegHeight,ypos=backPegYOffset,zpos=2*outerRadius+.65*backPegHeight,angle=-5);
            //MiddleFingers
            proximalMiddleFingers(length,outerRadius,innerRadius,fingerWidth,taper);
        };
        proximalAllCutObjects(skinWidth,skinHeight,skinLength,length,outerRadius,clearance,frontPegYOffset,frontPegLength,backPegYOffset, backPegLength, backPegHeight, rubberClearance);
        
};
};


/////////// Distal modules //////////////


module skinExtrude(outerWidth,outerRadius,distalLength,linscale=1){
    skinWidth=outerWidth;
    skinHeight=2*outerRadius;
    rotate([-90,0,0])
    linear_extrude(distalLength,scale=linscale)
    polygon(points = [[0.36789*skinWidth,-1.0*skinHeight],[-0.368807*skinWidth,-1.0*skinHeight],[-0.394495*skinWidth,-0.976013*skinHeight],[-0.422018*skinWidth,-0.923077*skinHeight],[-0.444037*skinWidth,-0.867659*skinHeight],[-0.466055*skinWidth,-0.797353*skinHeight],[-0.478899*skinWidth,-0.712986*skinHeight],[-0.490826*skinWidth,-0.590571*skinHeight],[-0.494495*skinWidth,-0.477254*skinHeight],[-0.5*skinWidth,-0.331679*skinHeight],[-0.499083*skinWidth,-0.229115*skinHeight],[-0.495413*skinWidth,-0.144748*skinHeight],[-0.488991*skinWidth,-0.093466*skinHeight],[-0.480734*skinWidth,-0.055418*skinHeight],[-0.468807*skinWidth,-0.01737*skinHeight],[-0.457798*skinWidth,0.0*skinHeight],[0.453211*skinWidth,0.0*skinHeight],[0.470642*skinWidth,-0.023987*skinHeight],[0.481651*skinWidth,-0.045492*skinHeight],[0.489908*skinWidth,-0.086849*skinHeight],[0.494495*skinWidth,-0.138958*skinHeight],[0.498165*skinWidth,-0.198511*skinHeight],[0.499083*skinWidth,-0.26799*skinHeight],[0.499083*skinWidth,-0.3689*skinHeight],[0.5*skinWidth,-0.457403*skinHeight],[0.498165*skinWidth,-0.519438*skinHeight],[0.494495*skinWidth,-0.597188*skinHeight],[0.488073*skinWidth,-0.677419*skinHeight],[0.474312*skinWidth,-0.761787*skinHeight],[0.465138*skinWidth,-0.82134*skinHeight],[0.455963*skinWidth,-0.859388*skinHeight],[0.443119*skinWidth,-0.892473*skinHeight],[0.424771*skinWidth,-0.927213*skinHeight],[0.407339*skinWidth,-0.961125*skinHeight],[0.4*skinWidth,-0.975186*skinHeight],[0.392661*skinWidth,-0.985939*skinHeight],[0.380734*skinWidth,-0.993383*skinHeight]], paths = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,0]]);
};


module distalPositive(outerWidth,outerRadius,distalTipHeight,fingertipAngle,distalLength,skinScale){
    
    xScaleFront = .9;
    yScaleFront = .9;
    zScaleFront = .65;
    xScaleMiddle = .8;
    yScaleMiddle = 1.1;
    zScaleMiddle = .45;
    yScaleBack = 1.5;
    
    yTransFront = distalLength-(yScaleFront*outerWidth)/1.85;
    zTransMiddle = distalTipHeight-(zScaleMiddle*outerWidth)/2;
    zTransFront = zTransMiddle-(zScaleFront*outerWidth)/5;
    yTransMiddle = distalLength-(yScaleMiddle*outerWidth)/2-(yScaleMiddle*outerWidth)/10;
    yTransBack = distalLength-(yScaleBack*outerWidth)/2-zTransFront/tan(fingertipAngle)-((yScaleBack-yScaleFront)*outerWidth)/2;
    //Fingertip creation
    difference(){
        //positive
        hull(){
            //front
            translate([0,yTransFront,zTransFront])
            scale([xScaleFront,yScaleFront,zScaleFront]) 
            sphere(d=outerWidth);
            //middle
            translate([0,yTransMiddle,zTransMiddle])
            scale([xScaleMiddle,yScaleMiddle,zScaleMiddle])
            sphere(d=outerWidth);
            //back
            translate([0,yTransBack,0])
            scale([1,yScaleBack,1])
            sphere(d=outerWidth);
        };
        //cut off bottom
        translate([0,yTransBack,-outerWidth/2]) 
        cube([outerWidth,5*yScaleBack*outerWidth,outerWidth],center=true);
        //round off bottom
        difference(){
            scale([1.5,1,1.5]) skinExtrude(outerWidth,outerRadius,distalLength);
            scale([1,1.1,1]) skinExtrude(outerWidth,outerRadius,distalLength);
            translate([0,distalLength/2,distalTipHeight]) cube([outerWidth,distalLength,distalTipHeight],center=true);
        };
        //cut off back if it goes too far
        translate([0,-distalLength/2,outerRadius]) cube([outerWidth,distalLength,outerRadius*2],center=true);
    };
    
    //Skin attach
    difference(){
        skinExtrude(outerWidth,outerRadius,distalLength,[1,skinScale]);
        translate([0,yTransBack,0]) rotate([fingertipAngle-90,0,0]) translate([-outerWidth/2,0,0]) cube([outerWidth,10*outerWidth,10*zTransMiddle/sin(fingertipAngle)]);
    };
};


module distalAddObjects(innerWidth,outerWidth,innerRadius,outerRadius,distalLength,distalTipHeight,jointWidthClearance,jointRadiusClearance,rubberClearance,lengthOfElastic,fingertipAngle,pinHeadLength,pinHeadDepth,pinClipDepth,pinDiam,skinScale,pegLipHeight=.55){
    
    difference(){
        translate([0,2*outerRadius+lengthOfElastic/4,pegLipHeight]) rotate([180,0,0]) peg(length=lengthOfElastic/2,width=innerWidth/2,height=(2/3)*outerRadius);
        translate([0,outerRadius,outerRadius]) rotate([0,90,0]) cylinder(h=innerWidth+jointWidthClearance,r=outerRadius+jointRadiusClearance,center=true);
    };
    
    //String tie point
    radiusTiePoint=1.5;
    distanceTiePoint=2*outerRadius+lengthOfElastic/4;
    fractionLengthTie=(distanceTiePoint/distalLength);
    heightTiePoint=(1-fractionLengthTie+fractionLengthTie*skinScale)*2*outerRadius-.75*radiusTiePoint;
    translate([0,distanceTiePoint,heightTiePoint]) scale([1,1,.75]) rotate([0,90,0]) cylinder(r=radiusTiePoint,h=innerWidth+2*jointWidthClearance,center=true);
};

module distalCutObjects(innerWidth,outerWidth,innerRadius,outerRadius,distalLength,distalTipHeight,jointWidthClearance,jointRadiusClearance,rubberClearance,lengthOfElastic,fingertipAngle,pinHeadLength,pinWidth,pinHeadDepth,pinClipDepth,pinDiam,pinClear,pegLipHeight=.55){
    
    //Middle cut out for proximal fingers to fit inside
    difference(){
        translate([0,outerRadius/2,outerRadius]) cube([outerWidth,outerRadius,2*outerRadius],center=true);
        translate([0,outerRadius,outerRadius]) rotate([0,90,0]) cylinder(h=outerWidth,r=outerRadius,center=true);
        translate([0,outerRadius/1.4,outerRadius/2]) cube([outerWidth,outerRadius,outerRadius],center=true);
    };
    translate([0,outerRadius,outerRadius]) rotate([0,90,0]) cylinder(h=innerWidth+jointWidthClearance,r=outerRadius+jointRadiusClearance,center=true);
    cube([innerWidth+jointWidthClearance,outerRadius+jointRadiusClearance,outerRadius+jointRadiusClearance],center=true);
    
    
    //Hole for rubber band
    filletSize=2.5;
    minkowski(){
        rotate([0,0,90]) cube([2*(2*outerRadius+lengthOfElastic/2+rubberClearance-filletSize),innerWidth+jointWidthClearance-2*filletSize,(2/3)*outerRadius-2*filletSize],center=true);
        sphere(r=filletSize);
       };
       
       
    //Hole for string
    filletSizeString=2;
    minkowski(){
        translate([0,0,2*outerRadius]) rotate([0,0,90]) cube([2*(2*outerRadius+lengthOfElastic/2-filletSizeString),innerWidth+jointWidthClearance-2*filletSizeString,1.25*outerRadius-2*filletSizeString],center=true);
        sphere(r=filletSizeString);
       };
       
    //Peg hole
    intersection(){
        translate([0,outerRadius,outerRadius]) rotate([0,90,0]) cylinder(h=outerWidth,d=pinDiam+2*pinClear,center=true);
        translate([0,outerRadius,outerRadius]) cube([outerWidth,pinDiam+2*pinClear,pinWidth+2*pinClear],center=true);
    };
    translate([(outerWidth-pinHeadDepth)/2,outerRadius,outerRadius]) cube([pinHeadDepth+2*pinClear,pinHeadLength+2*pinClear,pinWidth+2*pinClear],center=true);
    translate([-(outerWidth-pinClipDepth)/2,outerRadius,outerRadius]) rotate([0,90,0]) cylinder(h=pinClipDepth,d=pinClipDiam+2*pinClear,center=true);
};

    


module renderDistal(innerWidth,outerWidth,innerRadius,outerRadius,distalLength,distalTipHeight,jointWidthClearance,jointRadiusClearance,rubberClearance,lengthOfElastic,fingertipAngle,pinHeadLength,pinWidth,pinHeadDepth,pinClipDepth,pinDiam,pinClear,skinScale,pegLipHeight=.55){
    
    difference(){
    distalPositive(outerWidth,outerRadius,distalTipHeight,fingertipAngle,distalLength,skinScale);
    distalCutObjects(innerWidth,outerWidth,innerRadius,outerRadius,distalLength,distalTipHeight,jointWidthClearance,jointRadiusClearance,rubberClearance,lengthOfElastic,fingertipAngle,pinHeadLength,pinWidth,pinHeadDepth,pinClipDepth,pinDiam,pinClear);
    };
    distalAddObjects(innerWidth,outerWidth,innerRadius,outerRadius,distalLength,distalTipHeight,jointWidthClearance,jointRadiusClearance,rubberClearance,lengthOfElastic,fingertipAngle,pinHeadLength,pinHeadDepth,pinClipDepth,pinDiam,skinScale,pegLipHeight=.55);
};












module baseModel(){
translate([-70,-30,0]) import("/Users/jacobrose/Library/CloudStorage/OneDrive-Personal/UNC/Helping Hands/Parametric Hand/Left Hand Final v7.obj");
}


fingerBaseWidth = 3;


module fingerBaseCutTool(){
    union(){
        minkowski(){
            union(){
                rotate([0,90,0]) cylinder(h=innerWidth+2*jointWidthClearance-2*fingerBaseFillet,r=outerRadius-fingerBaseFillet, center=true);
                translate([0,0,3.5*outerRadius]) cube([innerWidth+2*jointWidthClearance-2*fingerBaseFillet,3*(outerRadius-fingerBaseFillet),8*outerRadius], center=true);
                translate([0,-1.5*(outerRadius-fingerBaseFillet),3.5*outerRadius]) cylinder(h=8*outerRadius,r=stringPathRadius,center=true);
            }
            sphere(r=fingerBaseFillet);
        }
        rotate([0,90,0]) cylinder(h=skinWidth,r=pinDiam/2+pinClear,center=true);
        translate([0,outerRadius-(3/4*outerRadius),-(outerRadius+jointRadiusClearance)/2]) cube([innerWidth+2*jointWidthClearance,2*outerRadius,outerRadius+jointRadiusClearance], center=true);
        difference(){
            union(){
                rotate([0,90,0]) cylinder(h=skinWidth,r=outerRadius+jointRadiusClearance, center=true);
                translate([0,outerRadius,(outerRadius+jointRadiusClearance)]) cube([skinWidth,2*(outerRadius+jointRadiusClearance),4*(outerRadius+jointRadiusClearance)],center=true);
            }
            rotate([0,90,0]) cylinder(h=skinWidth,r=outerRadius, center=true);
            translate([0,-(outerRadius+jointRadiusClearance)/2,0]) cube([skinWidth,(outerRadius+jointRadiusClearance),2*(outerRadius+jointRadiusClearance)], center=true);
            rotate([-20,0,0]) translate([0,-2*(outerRadius+jointRadiusClearance)/2,0]) cube([skinWidth,2*(outerRadius+jointRadiusClearance),10*(outerRadius+jointRadiusClearance)], center=true);    
        }
        
    }
}

module fingerBasePositive() {
    basePegLength = 15;
    basePegHeight = 3;
    basePegYOffset = -basePegLength/2;
    basePegZPos = outerRadius+basePegHeight;
    basePegAngle = -25;
    difference(){
        translate([0,-outerRadius/2,basePegLength/2+outerRadius]) cube([innerWidth+2*jointWidthClearance,outerRadius,basePegLength], center=true);
        rotate([basePegAngle,0,0]) translate([0,-outerRadius/2,basePegLength/2+outerRadius]) cube([innerWidth+2*jointWidthClearance,6*outerRadius,basePegLength], center=true);
    }
    intersection(){
        translate([0,-outerRadius/2,basePegLength/2+outerRadius]) cube([innerWidth+2*jointWidthClearance,outerRadius,basePegLength], center=true);
        rotate([basePegAngle,0,0]) peg(basePegLength,.5*innerWidth,basePegHeight,ypos=basePegYOffset,zpos=basePegZPos,angle=0);
    }
    
}

//ingerBaseCutTool();
fingerBasePositive();

difference(){
    translate([0,0,outerRadius/4]) cube([skinWidth,4*outerRadius,2.5*outerRadius], center=true);
    fingerBaseCutTool();
}


translate([0,length,0]) rotate([5,180,0])  translate([0,-outerRadius,-outerRadius]) renderDistal(innerWidth,outerWidth,innerRadius,outerRadius,distalLength,distalTipHeight,jointWidthClearance,jointRadiusClearance,rubberClearance,lengthOfElastic,fingertipAngle,pinHeadLength,pinWidth,pinHeadDepth,pinClipDepth,pinDiam,pinClear,skinScale,pegLipHeight=.55);


translate([0,length/2,-outerRadius]) drawProximal(skinWidth,skinHeight,length,outerRadius,innerRadius,innerWidth,jointRadiusClearance,rubberClearance,lengthOfElastic,proximalSkinTaper);

//baseModel();
