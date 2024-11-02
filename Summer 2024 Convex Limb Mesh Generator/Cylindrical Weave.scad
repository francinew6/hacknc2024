//Program to generate cylindrical weave pattern

diam=100; //mm
height=150; //mm
angle=45; //deg
weaveDiam=5; //mm
weaveGap=2; //mm
numWeave=24; //number of weaves crossing each other

angularResolution=1.5; //deg

$fn=12;




angResRad = angularResolution*3.1415/180;


function XCoord(r,theta) = r*cos(theta);
function YCoord(r,theta) = r*sin(theta);

module simpleWeave(){
    for (i=[0:numWeave]){
        rotate([0,0,i*360/numWeave])
        for (i=[0:(height/tan(angle))/angularResolution-1]){
            hull(){
                translate([XCoord((diam/2)+((weaveGap+weaveDiam)/2)*cos(180*(i*angularResolution/(360/(2*numWeave)))),i*angularResolution),YCoord((diam/2)+((weaveGap+weaveDiam)/2)*cos(180*(i*angularResolution/(360/(2*numWeave)))),i*angularResolution),i*tan(angle)*(diam/2)*angResRad]) sphere(d=weaveDiam);
                translate([XCoord((diam/2)+((weaveGap+weaveDiam)/2)*cos(180*((i+1)*angularResolution/(360/(2*numWeave)))),(i+1)*angularResolution),YCoord((diam/2)+((weaveGap+weaveDiam)/2)*cos(180*((i+1)*angularResolution/(360/(2*numWeave)))),(i+1)*angularResolution),(i+1)*tan(angle)*(diam/2)*angResRad]) sphere(d=weaveDiam);
                };
        };
        rotate([0,0,i*360/numWeave])
        for (i=[0:(height/tan(angle))/angularResolution-1]){
            hull(){
                translate([XCoord((diam/2)-((weaveGap+weaveDiam)/2)*cos(180*(-i*angularResolution/(360/(2*numWeave)))),-i*angularResolution),YCoord((diam/2)-((weaveGap+weaveDiam)/2)*cos(180*(-i*angularResolution/(360/(2*numWeave)))),-i*angularResolution),i*tan(angle)*(diam/2)*angResRad]) sphere(d=weaveDiam);
                translate([XCoord((diam/2)-((weaveGap+weaveDiam)/2)*cos(180*(-(i+1)*angularResolution/(360/(2*numWeave)))),-(i+1)*angularResolution),YCoord((diam/2)-((weaveGap+weaveDiam)/2)*cos(180*(-(i+1)*angularResolution/(360/(2*numWeave)))),-(i+1)*angularResolution),(i+1)*tan(angle)*(diam/2)*angResRad]) sphere(d=weaveDiam);
                };
        };
    };
};


simpleWeave();

