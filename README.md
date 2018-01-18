# Drone Flight Plan Generator for FLYLITCHI

Website: https://flylitchi.com/hub <br>

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
