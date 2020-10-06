class Empresa():
	EmpresaA = []
	EmpresaB = []
	EmpresaC = []
	EmpresaD = []
	EmpresaE = []
	EmpresaF = []
	EmpresaG = []
	EmpresaH = []
	EmpresaI = []
	EmpresaJ = []
	EmpresaK = []
	def __init__(self):
		#self.nome=[]
		self.data = None
		self.maxi = 0
		self.min = None
		self.med = None
	def __str__(self):
		return "data = {} , Maximo = {} , Minimo = {} , Media = {}".format(self.data,self.maxi,self.min,self.med)
	def __repr__(self):
		return ("data = {}, Maximo = {} , Minimo = {} , Media = {}").format(self.data,self.maxi,self.min,self.med)
#class Simulador():
	#def __init__(self):
		#self.saldo = None
	#def GetSaldo(self):
		#return self.saldo
	#def __str__(self):
		#return "saldo{}".format(self.indice)
#class Agente(Simulador):
	#def__init__(self):
#class AG(Agente):



		