holeDiam = 3.4; //mm
holeSpacing = 2.8; //mm
spacingError = 1; //mm


holeDepth = 500; //mm
patternSizeX = 500; //mm
patternSizeY = 500; //mm

patternDiam = 175; //mm
patternHeight = 500; //mm


module hexagonPattern(){
    holeDiamScale = holeDiam*2/sqrt(3);
    for (i=[0:patternSizeX/(sqrt(3)*(holeDiam+holeSpacing))]){
        for (j=[0:patternSizeY/((holeDiam+holeSpacing))]){
            translate([i*sqrt(3)*(holeDiam+holeSpacing),j*(holeDiam+holeSpacing),0]) 
            linear_extrude(holeDepth)
            circle(d=holeDiamScale,$fn=6);
        }
    }
    for (i=[0:patternSizeX/(sqrt(3)*(holeDiam+holeSpacing))]){
        for (j=[0:patternSizeY/((holeDiam+holeSpacing))]){
            translate([((sqrt(3)*(holeDiam+holeSpacing))/2)+i*sqrt(3)*(holeDiam+holeSpacing),(holeDiam+holeSpacing)/2+j*(holeDiam+holeSpacing),0]) 
            linear_extrude(holeDepth)
            circle(d=holeDiamScale,$fn=6);
        }
    }
};

module semiCylHexPattern(){
    holeDiamScale = holeDiam*2/sqrt(3);
    angularSpacingRad = 2*(holeSpacing+holeDiamScale)/patternDiam;
    angularSpacingDeg = 180*angularSpacingRad/3.1415;
    for (j=[0:patternHeight/(holeDiamScale+holeSpacing)]){
        translate([0,0,j*(holeDiamScale+holeSpacing)]) rotate([0,0,(j%2)*angularSpacingDeg/2])
        for (i=[0:180/angularSpacingDeg]){
            rotate([0,0,i*angularSpacingDeg]) rotate([0,90,0]) linear_extrude(1.5*patternDiam, center=true) circle(d=holeDiamScale,$fn=6);
        };
    };
};

difference(){
    translate([-30,-100,50]) rotate([-32,13,0]) import("/Users/jacobrose/Downloads/TimBaumanShoulderSocket.stl");

    difference(){
        semiCylHexPattern();
        translate([0,0,-3]) cylinder(h=2*patternHeight,d=patternDiam/2);
    };
 };