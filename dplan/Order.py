class Order(object):
	def __init__(self):
		pass

	def setPointOrder(self, list_unique=[], list_order=[]):
		self.list_unique = list_unique
		self.list_order = list_order

	def getCoordinates(self, list_xy, index):
		for i, coordinates in enumerate(list_xy):
			x, y = coordinates
			if i == index-1:
				return x, y	

	def saveCsv(self, list_xy, filename):
		file_output = open('drone/'+filename,'w')
		file_output.write('latitude,longitude,altitude(m),heading(deg),curvesize(m),rotationdir,gimbalmode,gimbalpitchangle,actiontype1,actionparam1,actiontype2,actionparam2,actiontype3,actionparam3,actiontype4,actionparam4,actiontype5,actionparam5,actiontype6,actionparam6,actiontype7,actionparam7,actiontype8,actionparam8,actiontype9,actionparam9,actiontype10,actionparam10,actiontype11,actionparam11,actiontype12,actionparam12,actiontype13,actionparam13,actiontype14,actionparam14,actiontype15,actionparam15'+'\n')
		for i in xrange(0, len(list_xy)):
			x, y = list_xy[i]
			file_output.write(str(x)+','+str(y)+',30,0,0.2,0,0,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0,-1,0'+'\n')

	def start(self):
		list_arrange = []
		for i, order in enumerate(self.list_order):
			x, y = self.getCoordinates(self.list_unique, order)
			list_arrange.append(tuple((x, y)))

		self.saveCsv(list_arrange, 'litchi_order.csv')