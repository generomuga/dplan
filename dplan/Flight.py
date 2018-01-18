from fractions import *
import numpy as np

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

	def calculateX(self, x1, x2, k, partition):
		k = Fraction(k, partition)
		return ((x2 - x1) * k) + x1

	def calculateY(self, y1, y2, k, partition):
		k = Fraction(k, partition)
		return ((y2 - y1) * k) + y1

	def getUniqueCoordinates(self, list_xy):
		return np.unique(list_xy, axis=0)

	def saveCsv(self, list_xy, filename):
		file_output = open('drone/'+filename,'w')
		file_output.write('latitude,longitude,altitude(m),heading(deg),curvesize(m),rotationdir,gimbalmode,gimbalpitchangle,actiontype1,actionparam1,actiontype2,actionparam2,actiontype3,actionparam3,actiontype4,actionparam4,actiontype5,actionparam5,actiontype6,actionparam6,actiontype7,actionparam7,actiontype8,actionparam8,actiontype9,actionparam9,actiontype10,actionparam10,actiontype11,actionparam11,actiontype12,actionparam12,actiontype13,actionparam13,actiontype14,actionparam14,actiontype15,actionparam15'+'\n')
		for i in xrange(0, len(list_xy)):
			x, y = list_xy[i]
			file_output.write(str(x)+','+str(y)+',30,0,0.2,0,0,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0'+'\n')

	def calculateDistance(self):
		list_x = []
		list_y = []
		list_xy = []
		
		x_partition = self.x_partition
		y_partition = self.y_partition

		k1 = 0
		k2 = 0
		k3 = 0

		"""record coordinates of corner 1"""
		list_x.append(self.corner1[0])
		list_y.append(self.corner1[1])
		list_xy.append(tuple((self.corner1[0], self.corner1[1])))

		"""record coordinates of corner 3"""
		list_x.append(self.corner3[0])
		list_y.append(self.corner3[1])
		list_xy.append(tuple((self.corner3[0], self.corner3[1])))

		for i in xrange(0, x_partition):
			k1 = k1 + 1

			"""calculate equidistant between corner 1 and corner 2"""
			x = self.calculateX(self.corner1[0], self.corner2[0], k1, x_partition)
			y = self.calculateX(self.corner1[1], self.corner2[1], k1, x_partition)
			list_x.insert(k1,x)
			list_y.insert(k1,y)
			list_xy.insert(k1, tuple((x, y)))

			"""calculate equidistant between corner 3 and corner 4"""
			x = self.calculateX(self.corner3[0], self.corner4[0], k1, x_partition)
			y = self.calculateX(self.corner3[1], self.corner4[1], k1, x_partition)
			list_x.append(x)
			list_y.append(y)
			list_xy.append(tuple((x, y)))

		"""record coordinates of corner 1"""
		list_x.append(self.corner1[0])
		list_y.append(self.corner1[1])
		list_xy.append(tuple((self.corner1[0], self.corner1[1])))

		"""record coordinates of corner 2"""
		list_x.append(self.corner2[0])
		list_y.append(self.corner2[1])
		list_xy.append(tuple((self.corner2[0], self.corner2[1])))

		"""total number of elements of list x and y"""
		sum_elements = (len(list_x)+len(list_y))/2
		if not sum_elements % 2 == 0:
			raise "Error!: sum of elements cannot be float"
			exit()

		for i in xrange(0, y_partition):
			k2 = k2 + 1

			index = (k2+sum_elements)-2

			"""calculate equidistant between corner 1 and corner 4"""
			x = self.calculateX(self.corner1[0], self.corner4[0], k2, y_partition)
			y = self.calculateX(self.corner1[1], self.corner4[1], k2, y_partition)
			list_x.insert(index, x)
			list_y.insert(index, y)
			list_xy.insert(index, tuple((x, y)))

			"""calculate equidistant between corner 2 and corner 3"""
			x = self.calculateX(self.corner2[0], self.corner3[0], k2, y_partition)
			y = self.calculateX(self.corner2[1], self.corner3[1], k2, y_partition)
			list_x.append(x)
			list_y.append(y)
			list_xy.append(tuple((x, y)))

		"""get index of corner 1 to corner 2"""
		index_corner1 = list_x.index(self.corner1[0])
		index_corner2 = list_x.index(self.corner2[0])
		
		"""get index of corner 3 and corner 4"""
		index_corner3 = list_x.index(self.corner3[0])
		index_corner4 = list_x.index(self.corner4[0])

		for i in xrange(index_corner1+1, index_corner2):
			"""calulcate equidistant of mid points"""
			for a in xrange(0, y_partition):
				k3 = k3 + 1
			
				"""reset counter"""
				if k3 >= y_partition:
					k3 = 0

				x = self.calculateX(list_x[i], list_x[index_corner4-i], k3, y_partition)
				y = self.calculateY(list_y[i], list_y[index_corner4-i], k3, y_partition)
				list_x.append(x)
				list_y.append(y)
				list_xy.append(tuple((x, y)))

		unique_coordinates = self.getUniqueCoordinates(list_xy)
		self.saveCsv(unique_coordinates, 'litchi.csv')

		return unique_coordinates
		"""if len(self.list_order) > 0:
			list_arrange = []
			for i, order in enumerate(self.list_order):
				x, y = self.getCoordinates(unique_coordinates, order)
				list_arrange.append(tuple((x, y)))

			self.saveCsv(list_arrange, 'litchi_order.csv')"""
	
	def sayCorners(self):
		print self.corner1, self.corner2, self.corner3, self.corner4

#instance = Flight()
#instance.setCorners(corner1=(14.168087,121.255039), corner2=(14.168399,121.255377),
#					corner3=(14.167741,121.256045), corner4=(14.167442,121.255707))

#instance.setPartition(x=3, y=4)
#instance.sayCorners()
#instance.setPointOrder([1,2,3,4])
#print instance.calculateDistance()


