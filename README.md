# Drone Flight Plan Generator for FLYLITCHI

### Website: https://flylitchi.com/hub <br>

### How to get the coordinates of the field?

1) Go to https://flylitchi.com/hub and search for your target location.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![searchloc](https://user-images.githubusercontent.com/11206290/35094779-49996776-fc81-11e7-9fd8-58c0b42da73a.png)

2) Click the map to generate a point and extract the coordinates from the panel.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![clickpoint](https://user-images.githubusercontent.com/11206290/35095296-eb475ac8-fc82-11e7-82b4-5e487dc3dba2.png) &nbsp;&nbsp;![getcoordinates](https://user-images.githubusercontent.com/11206290/35095469-88463588-fc83-11e7-8c18-3bac2fe029ac.png)

### Input requirement for the drone flight plan

Four corners of the field (latitude and longitude)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;corner 1 = 14.168092, 121.255055 <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;corner 2 = 14.168402, 121.255369 <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;corner 3 = 14.167741, 121.256036 <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;corner 4 = 14.167434, 121.255701 <br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![cornersfield](https://user-images.githubusercontent.com/11206290/35095787-c8142c64-fc84-11e7-878a-c2cea96d57d5.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Horizontal partition (x) = 3
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Vertical partition (y) = 4

<b> Sample source code </b> <br>

from dplan import Flight <br>
from dplan import Order <br>

"""Initiate flight plan"""<br>
fl = Flight() <br>
fl.setCorners(corner1=(14.168087,121.255039), corner2=(14.168399,121.255377), corner3=(14.167741,121.256045), corner4=(14.167442,121.255707)) <br>
fl.setPartition(x=3, y=4) <br>
unique_coordinates = fl.calculateDistance()

"""Initiate order of points"""<br>
order = Order() <br>
order.setPointOrder(unique_coordinates, [20,19,17,15,11,13,16,18,14,12,9,7,3,5,8,10,6,4,2,1]) <br>
order.start() <br>
