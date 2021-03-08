$fn=50;
inch = 25.4;

module roundedRect(size, radius)
{
        x = size[0];
        y = size[1];
        z = size[2];

        linear_extrude(height=z)
        hull()
        {
                // place 4 circles in the corners, with the given radius
                translate([(-x/2)+radius, (-y/2)+radius, 0])
                circle(r=radius);

                translate([(x/2)-radius, (-y/2)+radius, 0])
                circle(r=radius);

                translate([(-x/2) + radius, (y/2)-radius, 0])
                circle(r=radius);

                translate([(x/2)-radius, (y/2)-radius, 0])
                circle(r=radius);
        }

}

module counterSunk(position, radius)
{
union()
    {
     translate(position)
     union()
        {
     cylinder(3, radius, radius, 8, center=false);
     cylinder(3, 0, 3, center=false);
        }
    }
    
}

difference()
{
roundedRect([4.5*inch, 3.5*inch, 3], 5, center=false);

translate([-4*inch/2, -3*inch/2, 0])
cylinder(3, 0.13*inch, 0.13*inch, 8, center=false);
    
translate([-4*inch/2, 3*inch/2, 0])
cylinder(3, 0.13*inch, 0.13*inch, 8, center=false);
    
translate([4*inch/2, -3*inch/2, 0])
cylinder(3, 0.13*inch, 0.13*inch, 8, center=false);
    
translate([4*inch/2, 3*inch/2, 0])
cylinder(3, 0.13*inch, 0.13*inch, 8, center=false);

counterSunk([3*inch/2, 2*inch/2, 0], 0.056*inch);
counterSunk([-3*inch/2, 2*inch/2, 0], 0.056*inch);
counterSunk([3*inch/2, -2*inch/2, 0], 0.056*inch);
counterSunk([-3*inch/2, -2*inch/2, 0], 0.056*inch);



linear_extrude(height=5)
offset(r=3){
offset(r=-6){
union(){
square([4*inch,1.8*inch], center=true);
square([2.8*inch,3*inch], center=true);
}
}
}
}






