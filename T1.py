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
			listaux = list(line)
			e.data = str(''.join(map(str,listaux[3:10])))
			e.maxi  = str(''.join(map(str,listaux[70:82])))
			e.min = str(''.join(map(str,listaux[83:95])))
			e.med = str(''.join(map(str,listaux[96:108]))) 
			if (line[27:39] == "FII XP GAIA "):          #1
				classes.Empresa().EmpresaA.append(e)     
			elif (line[27:39] == "FIP XP OMEGA"):		 #2
				classes.Empresa().EmpresaB.append(e)     
			elif (line[27:39] == "CAIXAETFXBOV"):        #3
				classes.Empresa().EmpresaC.append(e)
			elif (line[27:39] == "FII GAVEA   "):        #4
				classes.Empresa().EmpresaD.append(e)
			elif (line[27:39] == "EZTEC       "):        #5
				classes.Empresa().EmpresaE.append(e)
			elif (line[27:39] == "GUARARAPES  "):        #6
				classes.Empresa().EmpresaF.append(e)
			elif (line[27:39] == "GGBRE       "):        #7
				classes.Empresa().EmpresaG.append(e)
			elif (line[27:39] == "GERDAU      "):        #8
				classes.Empresa().EmpresaH.append(e)
			elif (line[27:39] == "FLEURY      "):        #9
				classes.Empresa().EmpresaI.append(e)
			elif (line[27:39] == "EMAE        "):        #10
				classes.Empresa().EmpresaJ.append(e)
			listaux *= 0
	k.close()
readInput()
print len((classes.Empresa().EmpresaA))
print len((classes.Empresa().EmpresaB))
print len((classes.Empresa().EmpresaC))
print len((classes.Empresa().EmpresaD))
print len((classes.Empresa().EmpresaE))
print len((classes.Empresa().EmpresaF))
print len((classes.Empresa().EmpresaG))
print len((classes.Empresa().EmpresaH))
print len((classes.Empresa().EmpresaI))
print len((classes.Empresa().EmpresaJ))
#for i in classes.Empresa():
#for maxi in classes.Empresa():
	#print(maxi)
#def main():
#if __name__ == '__main__':
#	main()