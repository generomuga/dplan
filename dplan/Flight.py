class Flight(object):

	def __init__(self):
		pass

	def setCorners(self, **kwargs):
		self.corner1 = kwargs['corner1']
		self.corner2 = kwargs['corner2']
		self.corner3 = kwargs['corner3']
		self.corner4 = kwargs['corner4']

	def setPartition(self, **kwargs):
		self.x_partition = kwargs['x']
		self.y_partition = kwargs['y']

	def sayCorners(self):
		print self.corner1, self.corner2, self.corner3, self.corner4

instance = Flight()
instance.setCorners(corner1=(14.168087,121.255039), corner2=(14.168399,121.255377),
					corner3=(14.167741,121.256045), corner4=(14.167442,121.255707))

instance.sayCorners()
