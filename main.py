import random

ben = [3, 3, 2, 4, 2, 3, 5, 2]
weight = [5, 4, 7, 8, 4, 4, 6, 8]

def gerarCromossomo(tamanho):
  cromossomo = []
  i = 0
  while i < tamanho:
    gene = random.randint(0, 1)
    cromossomo.append(gene)
    i = i + 1
  return cromossomo

def gerarFuncaoFitness(cromossomoGerado, tamanho):
  i = 0
  beneficio = 0
  peso = 0
  while i < tamanho:
    gene = cromossomo[i]
    if gene == 1:
      beneficio = beneficio + ben[i]
      peso = peso + weight[i]
    i = i + 1
  if peso > 25:
    beneficio = -1
  return beneficio

tamanho = 8
cromossomoGerado = gerarCromossomo(tamanho)
beneficio = -1

while beneficio < 13:
  cromossomo = gerarCromossomo(tamanho)
  beneficio = gerarFuncaoFitness(cromossomo, tamanho)
  print(cromossomo)
  print(beneficio)