import classes
import random
from random import randint
#def Selecao():
#def Mutacao():
#def Genetico():
#def Agente():
#def Simulador():
def readData(linha):
	e = classes.Empresa()
	e.data = str(''.join(map(str,linha[3:10])))
	e.abertura = int(''.join(map(str,linha[57:69])))
	e.maxi  = int(''.join(map(str,linha[70:82])))
	e.min = int(''.join(map(str,linha[83:95])))
	e.med = int(''.join(map(str,linha[96:108])))
	return e
def readInput():
	with open("teste.TXT", "r") as k:
		for line in k:
			listaux = list(line) 
			if (line[27:39] == "FII XP GAIA "):          #1
				e=readData(listaux)
				classes.Empresa().EmpresaA.append(e)     
			elif (line[27:39] == "FIP XP OMEGA"):        #2
				e=readData(listaux)		 
				classes.Empresa().EmpresaB.append(e)     
			elif (line[27:39] == "CAIXAETFXBOV"):        #3
				e=readData(listaux)
				classes.Empresa().EmpresaC.append(e)
			elif (line[27:39] == "FII GAVEA   "):        #4
				e=readData(listaux)
				classes.Empresa().EmpresaD.append(e)
			elif (line[27:39] == "EZTEC       "):  
				e=readData(listaux)
				classes.Empresa().EmpresaE.append(e)
			elif (line[27:39] == "GUARARAPES  "):        #6
				e=readData(listaux)
				classes.Empresa().EmpresaF.append(e)
			elif (line[27:39] == "GGBRE       "):        #7
				e=readData(listaux)
				classes.Empresa().EmpresaG.append(e)
			elif (line[27:39] == "GERDAU      "):        #8
				e=readData(listaux)
				classes.Empresa().EmpresaH.append(e)
			elif (line[27:39] == "FLEURY      "):        #9
				e=readData(listaux)
				classes.Empresa().EmpresaI.append(e)
			elif (line[27:39] == "EMAE        "):        #10
				e=readData(listaux)
				classes.Empresa().EmpresaJ.append(e)
			listaux *= 0
	k.close()
def geraPopulacaoInicio():
	aux = []
	carteira = []
	popMax = 20
	for pop in range (popMax):
		rngA = randint(0,100) 
		rngB = randint(0,100)
		rngC = randint(0,100)
		rngD = randint(0,100)
		rngE = randint(0,100)
		rngF = randint(0,100)
		rngG = randint(0,100)
		rngH = randint(0,100)
		rngI = randint(0,100)
		rngJ = randint(0,100)
		fator = 1.0 / (rngA + rngB + rngC + rngD + rngE + rngF + rngG + rngH + rngI + rngJ) ##normaliza a rng
		compraA = rngA * fator 
		compraB = rngB * fator
		compraC = rngC * fator
		compraD = rngD * fator
		compraE = rngE * fator
		compraF = rngF * fator
		compraG = rngG * fator
		compraH = rngH * fator
		compraI = rngI * fator
		compraJ = rngJ * fator
		somatorio = compraA + compraB + compraC + compraD + compraE + compraF + compraG + compraH + compraI + compraJ
		aux = [round(compraA,2),round(compraB,2),round(compraC,2),round(compraD,2),round(compraE,2),round(compraF,2),round(compraG,2),round(compraH,2),round(compraI,2),round(compraJ,2)]
		carteira.append(aux)
	return carteira
def CalculoMedia(opc):
	soma = 0
	med = 0
	if opc ==1 :
		for x in range(len(classes.Empresa().EmpresaA)):
			soma = soma + classes.Empresa().EmpresaA[x].med
		med = soma / len(classes.Empresa().EmpresaA)
	elif opc ==2 :
		for x in range(len(classes.Empresa().EmpresaB)):
			soma = soma + classes.Empresa().EmpresaB[x].med
		med = soma / len(classes.Empresa().EmpresaB)
	elif opc ==3 :
		for x in range(len(classes.Empresa().EmpresaC)):
			soma = soma + classes.Empresa().EmpresaC[x].med
		med = soma / len(classes.Empresa().EmpresaC)
	elif opc ==4 :
		for x in range(len(classes.Empresa().EmpresaD)):
			soma = soma + classes.Empresa().EmpresaD[x].med
		med = soma / len(classes.Empresa().EmpresaD)
	elif opc ==5 :
		for x in range(len(classes.Empresa().EmpresaE)):
			soma = soma + classes.Empresa().EmpresaE[x].med
		med = soma / len(classes.Empresa().EmpresaE)
	elif opc ==6 :
		for x in range(len(classes.Empresa().EmpresaF)):
			soma = soma + classes.Empresa().EmpresaF[x].med
		med = soma / len(classes.Empresa().EmpresaF)
	elif opc ==7 :
		for x in range(len(classes.Empresa().EmpresaG)):
			soma = soma + classes.Empresa().EmpresaG[x].med
		med = soma / len(classes.Empresa().EmpresaG)
	elif opc ==8 :
		for x in range(len(classes.Empresa().EmpresaH)):
			soma = soma + classes.Empresa().EmpresaH[x].med
		med = soma / len(classes.Empresa().EmpresaH)
	elif opc ==9 :
		for x in range(len(classes.Empresa().EmpresaI)):
			soma = soma + classes.Empresa().EmpresaI[x].med
		med = soma / len(classes.Empresa().EmpresaI)
	elif opc ==10 :
		for x in range(len(classes.Empresa().EmpresaJ)):
			soma = soma + classes.Empresa().EmpresaJ[x].med
		med = soma / len(classes.Empresa().EmpresaJ)
	return med

def CalculoFitness(carteira):
	ganho = []
	#print(carteira)
	for empresa in carteira:
		for valor in empresa:
			ganhoA = valor * CalculoMedia(1)
			ganhoB = valor * CalculoMedia(2)
			ganhoC = valor * CalculoMedia(3)
			ganhoD = valor * CalculoMedia(4)
			ganhoE = valor * CalculoMedia(5)
			ganhoF = valor * CalculoMedia(6)
			ganhoG = valor * CalculoMedia(7)
			ganhoH = valor * CalculoMedia(8)
			ganhoI = valor * CalculoMedia(9)
			ganhoJ = valor * CalculoMedia(10)
		somatorioGanho = ganhoA + ganhoB + ganhoC + ganhoD + ganhoE + ganhoF + ganhoG + ganhoH + ganhoI + ganhoJ  
		porcentual = somatorioGanho / 1000 # percentual baseado em 100.000 de saldo.
		ganho.append(round(porcentual))
		print(ganho,somatorioGanho)
	somatorioGanho=0
	#print(ganho.somatorioGanho)

def main():
	carteira = []
	readInput()
	carteira = geraPopulacaoInicio()
	CalculoFitness(carteira)
if __name__ == '__main__':
	main()