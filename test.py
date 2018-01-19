from dplan import Flight
from dplan import Order

"""Initiate flight plan"""
flight = Flight()

"""Set four corners"""
flight.setCorners(corner1 = (14.168092, 121.255055),
				  corner2 = (14.168402, 121.255369),
				  corner3 = (14.167741, 121.256036),
				  corner4 = (14.167434, 121.255701))

flight.setPartition(x=4, y=3)
unique_coordinates = flight.calculateDistance()

"""Initiate order of points"""
order = Order()

list_order = [14,9,4,1,2,6,11,16,18,13,8,3,5,10,15,19,20,17,12,7]
order.setPointOrder(unique_coordinates, list_order)
order.start()
