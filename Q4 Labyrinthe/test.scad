cellsize = 10;
wallheight = 10;
wallthickness = 1;
length = 13; 
width = 13;

    translate([-0.5,-0.5,-1])
    cube([length * cellsize +1, width * cellsize + 1, 1]); 
    translate([65,0,5]){
       cube([130,1,10],center = true);}
       
    translate([0,65,5]){rotate([0,0,90]){
       cube([130,1,10],center = true);}
   }
   
   
   translate([65,130,5]){
       cube([130,1,10],center = true);}
       
    translate([130,65,5]){rotate([0,0,90]){
       cube([130,1,10],center = true);}
       }
    

