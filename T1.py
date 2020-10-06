import classes
#def CalculoFitness():
#def geraPopulacaoInicio():
#def Selecao():
#def Mutacao():
#def Genetico():
#def Agente():
#def Simulador():
def readInput():
		#linha=1
	with open("teste.TXT", "r") as k:
		for line in k:
			#for i in line.split():
				#print(i)
			#listaux = list(line)
			e=classes.Empresa() 
			if (line[27:39] == "FII XP GAIA "):
				listaux = list(line)
				e.data = str(''.join(map(str,listaux[3:10])))
				e.maxi  = int(''.join(map(str,listaux[70:82])))
				e.min = int(''.join(map(str,listaux[83:95])))
				e.med = int(''.join(map(str,listaux[96:108])))
				listaux *= 0
				print (e.data)


	k.close()
readInput()
#for maxi in classes.Empresa():
	#print(maxi)
#def main():
#if __name__ == '__main__':
#	main()