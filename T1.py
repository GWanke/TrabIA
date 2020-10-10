import classes
import random
from random import randint
import itertools
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
	with open("COTAHIST_A2014.TXT", "r") as k, open("COTAHIST_A2015.TXT", "r") as f:
		for line in k:
			listaux = list(line) 
			if (line[27:39] == "METAL LEVE  "):          #1
				e=readData(listaux)
				classes.Empresa().EmpresaA.append(e)     
			elif (line[27:39] == "WEG         "):        #2
				e=readData(listaux)		 
				classes.Empresa().EmpresaB.append(e)     
			elif (line[27:39] == "NATURA      "):        #3
				e=readData(listaux)
				classes.Empresa().EmpresaC.append(e)
			elif (line[27:39] == "SABESP      "):        #4
				e=readData(listaux)
				classes.Empresa().EmpresaD.append(e)
			elif (line[27:39] == "SID NACIONAL"):  
				e=readData(listaux)
				classes.Empresa().EmpresaE.append(e)
			elif (line[27:39] == "PFIZER      "):        #6
				e=readData(listaux)
				classes.Empresa().EmpresaF.append(e)
			elif (line[27:39] == "LOJAS RENNER"):        #7
				e=readData(listaux)
				classes.Empresa().EmpresaG.append(e)
			elif (line[27:39] == "CIELO       "):        #8
				e=readData(listaux)
				classes.Empresa().EmpresaH.append(e)
			elif (line[27:39] == "TELEF BRASIL"):        #9
				e=readData(listaux)
				classes.Empresa().EmpresaI.append(e)
			elif (line[27:39] == "GRENDENE    "):        #10
				e=readData(listaux)
				classes.Empresa().EmpresaJ.append(e)
			listaux *= 0
		for line in f:
			listaux = list(line) 
			if (line[27:39] == "METAL LEVE  "):          #1
				e=readData(listaux)
				classes.Empresa().EmpresaA.append(e)     
			elif (line[27:39] == "WEG         "):        #2
				e=readData(listaux)		 
				classes.Empresa().EmpresaB.append(e)     
			elif (line[27:39] == "NATURA      "):        #3
				e=readData(listaux)
				classes.Empresa().EmpresaC.append(e)
			elif (line[27:39] == "SABESP      "):        #4
				e=readData(listaux)
				classes.Empresa().EmpresaD.append(e)
			elif (line[27:39] == "SID NACIONAL"):  
				e=readData(listaux)
				classes.Empresa().EmpresaE.append(e)
			elif (line[27:39] == "PFIZER      "):        #6
				e=readData(listaux)
				classes.Empresa().EmpresaF.append(e)
			elif (line[27:39] == "LOJAS RENNER"):        #7
				e=readData(listaux)
				classes.Empresa().EmpresaG.append(e)
			elif (line[27:39] == "CIELO       "):        #8
				e=readData(listaux)
				classes.Empresa().EmpresaH.append(e)
			elif (line[27:39] == "TELEF BRASIL"):        #9
				e=readData(listaux)
				classes.Empresa().EmpresaI.append(e)
			elif (line[27:39] == "GRENDENE    "):        #10
				e=readData(listaux)
				classes.Empresa().EmpresaJ.append(e)
			listaux *= 0			
	k.close()
	f.close()
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
		aux = [(compraA),(compraB),(compraC),(compraD),(compraE),(compraF),(compraG),(compraH),(compraI),(compraJ),]
		carteira.append(aux)
	return carteira
def hash():
	dici = {}
	soma=0
	for x in range(len(classes.Empresa().EmpresaA)):
		soma = soma + classes.Empresa().EmpresaA[x].med
	dici[1]  = soma / len(classes.Empresa().EmpresaA)
	soma =0
	for x in range(len(classes.Empresa().EmpresaB)):
		soma = soma + classes.Empresa().EmpresaB[x].med
	dici[2]  = soma / len(classes.Empresa().EmpresaB)
	soma =0
	for x in range(len(classes.Empresa().EmpresaC)):
		soma = soma + classes.Empresa().EmpresaC[x].med
	dici[3]  = soma / len(classes.Empresa().EmpresaC)
	soma =0
	for x in range(len(classes.Empresa().EmpresaD)):
		soma = soma + classes.Empresa().EmpresaD[x].med
	dici[4]  = soma / len(classes.Empresa().EmpresaD)
	soma =0
	for x in range(len(classes.Empresa().EmpresaE)):
		soma = soma + classes.Empresa().EmpresaE[x].med
	dici[5]  = soma / len(classes.Empresa().EmpresaE)
	soma =0
	for x in range(len(classes.Empresa().EmpresaF)):
		soma = soma + classes.Empresa().EmpresaF[x].med
	dici[6]  = soma / len(classes.Empresa().EmpresaF)
	soma =0
	for x in range(len(classes.Empresa().EmpresaG)):
		soma = soma + classes.Empresa().EmpresaG[x].med
	dici[7]  = soma / len(classes.Empresa().EmpresaG)
	soma =0
	for x in range(len(classes.Empresa().EmpresaH)):
		soma = soma + classes.Empresa().EmpresaH[x].med
	dici[8]  = soma / len(classes.Empresa().EmpresaH)
	soma =0
	for x in range(len(classes.Empresa().EmpresaI)):
		soma = soma + classes.Empresa().EmpresaI[x].med
	dici[9]  = soma / len(classes.Empresa().EmpresaI)
	soma =0
	for x in range(len(classes.Empresa().EmpresaJ)):
		soma = soma + classes.Empresa().EmpresaJ[x].med
	dici[10]  = soma / len(classes.Empresa().EmpresaJ)
	soma =0
	return dici
def CalculoMedia(opc,dici):
	return dici[opc]	


def CalculoFitness(carteira,dici):
	listasorted = []
	v = sorted(carteira,key=lambda k:CalculoFitness2(k,dici))[::-1]
	for item in v:
		indexv = carteira.index(item)
		listasorted.append(indexv)
	return listasorted
def CalculoFitness2(filho,dici):
	aux = []
	ganho = []
	for valor in filho:
		ganhoA = valor * CalculoMedia(1,dici)
		ganhoB = valor * CalculoMedia(2,dici)
		ganhoC = valor * CalculoMedia(3,dici)
		ganhoD = valor * CalculoMedia(4,dici)
		ganhoE = valor * CalculoMedia(5,dici)
		ganhoF = valor * CalculoMedia(6,dici)
		ganhoG = valor * CalculoMedia(7,dici)
		ganhoH = valor * CalculoMedia(8,dici)
		ganhoI = valor * CalculoMedia(9,dici)
		ganhoJ = valor * CalculoMedia(10,dici)
		somatorioGanho = ganhoA + ganhoB + ganhoC + ganhoD + ganhoE + ganhoF + ganhoG + ganhoH + ganhoI + ganhoJ #somatorio do lucro medio,baseado nos dados.
	z = somatorioGanho / len(filho)
	somatorioGanho =0
	return z
		
def ComparaPop(index,carteira,filhos,dici):
	for filho in filhos: 
		if CalculoFitness2(carteira[index[len(index)-1]],dici) <= CalculoFitness2(filho,dici) and filho not in carteira:
			carteira.pop(index[len(index)-1])
			carteira.append(filho)
	return carteira 
def Selecao(index):
	#selecao por torneio, com k=3.
	selecionados = []
	aux = []
	rngl = []
	indexSelecionado = -1
	excluidos = []
	pop = int(len(index) * 0.3)
	if pop %2 != 0:
		pop =pop +1
	while (len(selecionados)<pop): 
		for _ in range(0,3):
			rng=random.choice([i for i in range(0,len(index)-1) if i not in selecionados and i not in rngl])
			rngl.append(rng)		
		for posicao,item in enumerate(index):
			for aleatorio in rngl:
				if aleatorio == item:
					aux.append(posicao)
		indexSelecionado=min(aux)
		if indexSelecionado not in selecionados:
			selecionados.append(indexSelecionado)
		aux *=0
		rngl *= 0
	return selecionados
def Crossover(selecionados,carteira):
	# numero de filhos gerados por geracao = 2
	# numero de pais para crossover = 2 -> numero de selecionados precisa ser par. Percorrer lista de selecionados ate o final, de dois em dois.
	# Corte na pos random.
	filhos = []
	while (len(selecionados)>0):
		filho1 = []
		filho2 = []
		ac1=0
		ac2=0
		fator1=0
		fator2=0
		soma=0
		pai1 = carteira[selecionados[0]]
		pai2 = carteira[selecionados[1]]
		rng = randint(0,9)
		for x in range (0,10):
			if x<rng:
				ac1 += pai1[x]
				ac2 += pai2[x]
			else:
				ac1 += pai2[x]
				ac2 += pai1[x]
		fator1 = round(1.0/ac1,4)
		fator2 = round(1.0/ac2,4)
		for i in range (0,10):
			if i<rng:
				filho1.append(pai1[i]*fator1)
				filho2.append(pai2[i]*fator2)
			else:
				filho1.append(pai2[i]*fator1)
				filho2.append(pai1[i]*fator2)
		filhos.append(filho1)
		filhos.append(filho2)
		selecionados.pop(0)
		selecionados.pop(0)
	return filhos
def Mutacao(filhos):
	#10% de chance de mutacao. Caso ocorra,ira alterar o valor dos genes dos filhos.
	#Mutara o individuo em dois genes, que deverao obedecer a regra da soma equivalente a um do individuo.Em outras palavras, serao dois novos valores com a mesma soma.
	probabilidade=randint(0,100)
	tamfilhos=len(filhos)-1
	if probabilidade<0:
		index = randint(0,tamfilhos)
		rng1,rng2 = random.sample(range(0,10),2)
		somapeso = filhos[index][rng1] + filhos[index][rng2]
		filhos[index][rng1] = random.uniform(0,filhos[index][rng1])
		filhos[index][rng2] = somapeso - filhos[index][rng1]
	return filhos
def genetico():
	carteira = []
	respostaIgualRepetida=0
	numRep=0
	soma=0
	med=0
	valor=0
	readInput()
	dici=hash()
	carteira = geraPopulacaoInicio()
	while(respostaIgualRepetida<50 and numRep<10000):
		indices = []
		selecionados = []
		filhos = []
		filhosmuta = []
		respostaAntiga = CalculoFitness(carteira,dici) 
		selecionados = Selecao(respostaAntiga)
		filhos=Crossover(selecionados,carteira)
		filhosmuta=Mutacao(filhos)
		carteira=ComparaPop(respostaAntiga,carteira,filhosmuta,dici)
		novaResposta = CalculoFitness(carteira,dici)
		if (CalculoFitness2(carteira[respostaAntiga[0]],dici)==CalculoFitness2(carteira[novaResposta[0]],dici)):
			respostaIgualRepetida +=1
		else:
			respostaIgualRepetida=0
		numRep += 1
	return carteira[novaResposta[0]],CalculoFitness2(carteira[novaResposta[0]],dici)
	soma=0
	med=0

def main():
	carteira = []
	sol = 0
	carteira,sol = genetico()
if __name__ == '__main__':
	main()