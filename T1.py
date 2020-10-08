import classes
import random
from random import randint
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
	aux = []
	listasorted = []
	#necessita retornar as carteiras de maneira ordenada, com base nos dados de 2014 e 2015, pelo valor da media das empresas.  
	#da pra otimizar com hash o calculo medio.
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
			somatorioGanho = ganhoA + ganhoB + ganhoC + ganhoD + ganhoE + ganhoF + ganhoG + ganhoH + ganhoI + ganhoJ #somatorio do lucro medio,baseado nos dados. 
			aux.append(somatorioGanho)
		z = (reduce(lambda x, y: x + y, aux) / float(len(aux)))
		ganho.append(z)
		z=0
		aux *= 0
		somatorioGanho=0
	v = sorted(carteira,key=lambda k:CalculoFitness2(k))[::-1]
	#print CalculoFitness2(v[0])
	for item in v:
		indexv = carteira.index(item)
		listasorted.append(indexv)
	#return sorted(range(len(ganho)),key = lambda k: max(CalculoFitness(k))) [::-1]         #Retorna uma lista de indices, com o primeiro elemento correspondendo a carteira que possui um melhor valor medio bruto.
	return listasorted
def CalculoFitness2(filho):
	aux = []
	ganho = []
	for valor in filho:
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
		somatorioGanho = ganhoA + ganhoB + ganhoC + ganhoD + ganhoE + ganhoF + ganhoG + ganhoH + ganhoI + ganhoJ #somatorio do lucro medio,baseado nos dados.
	z = somatorioGanho / len(filho)
	somatorioGanho =0
	return z
		
def ComparaPop(index,carteira,filhos):
	for filho in filhos: 
		if CalculoFitness2(carteira[index[19]]) <= CalculoFitness2(filho):
			carteira.pop(index[19])
			carteira.append(filho)
	return carteira 
def Selecao(index):
	#selecao por torneio, com k=3.
	selecionados = []
	counter = 0
	while (counter<6):
		rng1=random.choice([i for i in range(0,19) if i not in selecionados])
		rng2=random.choice([i for i in range(0,19) if i not in selecionados])
		rng3=random.choice([i for i in range(0,19) if i not in selecionados])		
		for elemento in index:
			if rng1 == elemento:
				indexSelecionado = rng1
				break
			elif rng2 == elemento:
				indexSelecionado = rng2
				break
			elif rng3 == elemento:
				indexSelecionado = rng3
				break
		selecionados.append(indexSelecionado)
		counter = counter +1
		indexSelecionado = 0
	return selecionados
def Crossover(selecionados,carteira,index):
	# numero de filhos gerados por geracao = 2
	# numero de pais para crossover = 2 -> numero de selecionados precisa ser par. Percorrer lista de selecionados ate o final, de dois em dois.
	#print(selecionados,carteira)
	filhos = []
	aux = []
	while (len(selecionados)>0):
		filho1 = []
		filho2 = []
		aux = []
		pai1 = carteira[selecionados[0]]
		pai2 = carteira[selecionados[1]]
		for x in range (0,10):
			if x <= 4:
				filho1.append(pai1[x])
				filho2.append(pai2[x])
			else:
				filho1.append(pai2[x])
				filho2.append(pai1[x])
		filhos.append(filho1)
		filhos.append(filho2)
		selecionados.pop(0)
		selecionados.pop(0)
	return filhos
def Mutacao(filhos):
	#10% de chance de mutacao. Caso ocorra,ira alterar o valor dos genes dos filhos.
	#Mutara o individuo em dois genes, que deverao obedecer a regra da soma equivalente a um do individuo.Em outras palavras, serao dois novos valores com a mesma soma.
	probabilidade=randint(0,100)
	if probabilidade<=20:
		index = randint(0,2)
		rng1,rng2 = random.sample(range(0,10),2) 
		if index == 0:
			somapeso = filhos[0][rng1] + filhos[0][rng2]
			filhos[0][rng1] = round(random.uniform(0,filhos[0][rng1]),2)
			filhos[0][rng2] = round(somapeso - filhos[0][rng1],2)  
		elif index == 1:
			somapeso = filhos[1][rng1] + filhos[1][rng2]
			filhos[1][rng1] = round(random.uniform(0,filhos[1][rng1]),2)
			filhos[1][rng2] = round(somapeso - filhos[1][rng1],2)
		else:
			somapeso = filhos[2][rng1] + filhos[2][rng2]
			filhos[2][rng1] = round(random.uniform(0,filhos[2][rng1]),2)
			filhos[2][rng2] = round(somapeso - filhos[2][rng1],2)
	return filhos

def main():
	carteira = []
	indices = []
	selecionados = []
	respostaIgualRepetida=0
	numRep=0
	readInput()
	carteira = geraPopulacaoInicio()
	vantigo =  CalculoFitness2(carteira[0])
	print "fitness antigo da melhor solucao {} (que corresponde a carteira): {}".format(vantigo,carteira[0])  
	while(respostaIgualRepetida<=2 and numRep<10):
		respostaAntiga = CalculoFitness(carteira)
		selecionados = Selecao(respostaAntiga)
		filhos=Crossover(selecionados,carteira,respostaAntiga)
		filhosmuta=Mutacao(filhos)
		carteira=ComparaPop(respostaAntiga,carteira,filhosmuta)
		novaResposta = CalculoFitness(carteira)
		print(respostaAntiga,novaResposta)
		if (respostaAntiga==novaResposta):
			respostaIgualRepetida +=1
		else:
			respostaIgualRepetida==0
		numRep += 1
	vnovo =  CalculoFitness2(carteira[0])
	porcentagem = (((vnovo - vantigo) / vantigo) * 100)
	print "fitness novo da melhor solucao{},(que corresponde a carteira): {}".format(vnovo,carteira[0])
	print "melhora de {}%".format(porcentagem)
if __name__ == '__main__':
	main()