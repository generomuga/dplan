class Flight(object):

	def __init__(self):
		pass

	def setCorners(self, **kwargs):
		"""Set four corners of the field (latitude and longitude)"""
		self.corner1 = kwargs['corner1']
		self.corner2 = kwargs['corner2']
		self.corner3 = kwargs['corner3']
		self.corner4 = kwargs['corner4']

	def setPartition(self, **kwargs):
		"""Set x for horizontal partition and y for vertical parition"""
		self.x_partition = kwargs['x']
		self.y_partition = kwargs['y']

	def calculateDistance(self):
		list_x = []
		list_y = []
		list_xy = []
		
		x_partition = x_partition
		y_partition = y_partition

		k1 = 0
		k2 = 0
		k3 = 0

		"""record coordinates of corner 1"""
		list_x.append(args[0][0])
		list_y.append(args[0][1])
		list_xy.append(tuple((args[0][0], args[0][1])))

		"""record coordinates of corner 3"""
		list_x.append(args[2][0])
		list_y.append(args[2][1])
		list_xy.append(tuple((args[2][0], args[2][1])))

		for i in xrange(0, x_partition):
			k1 = k1 + 1

			"""calculate equidistant between corner 1 and corner 2"""
			x = calculate_x(args[0][0], args[1][0], k1, x_partition)
			y = calculate_x(args[0][1], args[1][1], k1, x_partition)
			list_x.insert(k1,x)
			list_y.insert(k1,y)
			list_xy.insert(k1, tuple((x, y)))

			"""calculate equidistant between corner 3 and corner 4"""
			x = calculate_x(args[2][0], args[3][0], k1, x_partition)
			y = calculate_x(args[2][1], args[3][1], k1, x_partition)
			list_x.append(x)
			list_y.append(y)
			list_xy.append(tuple((x, y)))

		"""record coordinates of corner 1"""
		list_x.append(args[0][0])
		list_y.append(args[0][1])
		list_xy.append(tuple((args[0][0], args[0][1])))

		"""record coordinates of corner 2"""
		list_x.append(args[1][0])
		list_y.append(args[1][1])
		list_xy.append(tuple((args[1][0], args[1][1])))

		"""total number of elements of list x and y"""
		sum_elements = (len(list_x)+len(list_y))/2
		if not sum_elements % 2 == 0:
			raise "Error!: sum of elements cannot be float"
			exit()

		for i in xrange(0, y_partition):
			k2 = k2 + 1

			index = (k2+sum_elements)-2

			"""calculate equidistant between corner 1 and corner 4"""
			x = calculate_x(args[0][0], args[3][0], k2, y_partition)
			y = calculate_x(args[0][1], args[3][1], k2, y_partition)
			list_x.insert(index, x)
			list_y.insert(index, y)
			list_xy.insert(index, tuple((x, y)))

			"""calculate equidistant between corner 2 and corner 3"""
			x = calculate_x(args[1][0], args[2][0], k2, y_partition)
			y = calculate_x(args[1][1], args[2][1], k2, y_partition)
			list_x.append(x)
			list_y.append(y)
			list_xy.append(tuple((x, y)))

		"""get index of corner 1 to corner 2"""
		index_corner1 = list_x.index(args[0][0])
		index_corner2 = list_x.index(args[1][0])
		
		"""get index of corner 3 and corner 4"""
		index_corner3 = list_x.index(args[2][0])
		index_corner4 = list_x.index(args[3][0])

		for i in xrange(index_corner1+1, index_corner2):
			"""calulcate equidistant of mid points"""
			for a in xrange(0, y_partition):
				k3 = k3 + 1
			
				"""reset counter"""
				if k3 >= y_partition:
					k3 = 0

				x = calculate_x(list_x[i], list_x[index_corner4-i], k3, y_partition)
				y = calculate_y(list_y[i], list_y[index_corner4-i], k3, y_partition)
				list_x.append(x)
				list_y.append(y)
				list_xy.append(tuple((x, y)))

	def sayCorners(self):
		print self.corner1, self.corner2, self.corner3, self.corner4

instance = Flight()
instance.setCorners(corner1=(14.168087,121.255039), corner2=(14.168399,121.255377),
					corner3=(14.167741,121.256045), corner4=(14.167442,121.255707))

instance.setPartition(x=3, y=4)

