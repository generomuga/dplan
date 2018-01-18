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

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Horizontal partition (x) and vertical partition (y)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In this example x = 4 and y = 3

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![grid](https://user-images.githubusercontent.com/11206290/35096465-48f8539e-fc87-11e7-9337-4265b4d68343.png)

<b>NOTE:</b> Create <b>drone</b> folder in your root directory for the output

### Implementation of API

#### Import dplan library 
from dplan import Flight <br>
from dplan import Order <br>

#### Initialize flight 
flight = Flight()

#### Set four corners of the field
flight.setCorners(corner1 = (14.168092, 121.255055),
				  corner2 = (14.168402, 121.255369),
				  corner3 = (14.167741, 121.256036),
				  corner4 = (14.167434, 121.255701))
          
#### Set partition of x and y
flight.setPartition(x=4, y=3) <br>
unique_coordinates = fl.calculateDistance()
          
### Result 
To view the flight plan result, import the <b>litchi.csv</b> from the </b>drone</b> folder to https://flylitchi.com/hub

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![folder](https://user-images.githubusercontent.com/11206290/35097591-bb2ac4e8-fc8b-11e7-915c-9d71b1f407c4.png) &nbsp;&nbsp;![litchi](https://user-images.githubusercontent.com/11206290/35097596-bebeb72c-fc8b-11e7-863d-545213892d8f.png) &nbsp;&nbsp;![import](https://user-images.githubusercontent.com/11206290/35097669-18067946-fc8c-11e7-8b8e-940b834a310b.png)

### Default flight plan result

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![result 2](https://user-images.githubusercontent.com/11206290/35098286-849d7508-fc8e-11e7-9e09-31f95b10e775.png)

### Customize flight plan

### Initialize order
order = Order()

#### Select point numbers in which order you prefer 
This a sample order of points <br><br>

list_order = [14,9,4,1,2,6,11,16,18,13,8,3,5,10,15,19,20,17,12,7] <br>
order.setPointOrder(unique_coordinates, list_order)<br>
order.start() <br>



order.setPointOrder(unique_coordinates, [20,19,17,15,11,13,16,18,14,12,9,7,3,5,8,10,6,4,2,1]) <br>
order.start() <br>
