# Least Recently Used = LRU: os dados não acessados há muito tempo são excluídos primeiro

import random
import os
import modoSimulacao
import time

class Lru:
  def __init__(self):
    print("\n \n === Criando fila para algoritmo LRU === \n")
    # Criar uma lista vazia para armazenar strings
    self.textList = []
    self.pasta = 'arquivos_divididos'
    
    self.arquivos = os.listdir(self.pasta)
    self.textos = ['']
    for i in self.arquivos:
      self.textos.append(i)
      
    print("Inserindo 10 arquivos de texto aleatórios:")
    for _ in range(0,10):
        item = random.choice(self.textos)
        self.textList.append(item)
        print(f"Inserido: {item}")
    self.printQueue(self.textList)
  
  def printQueue(self,q):
      print("\n \n Fila: ", end='')
      for item in q:
          print(item, end=' ')
      print()
  
  def searchQueue(self,q, target):
      found = False
  
      for i, item in enumerate(q):
          if item == target:
              found = True
              # mover o item para o final da lista
              q.append(q.pop(i))
              break
  
      return found
  
  
  def readFile(self,textList, target, simulacao=False):
    if self.searchQueue(textList, target):
      print(f"========= {target} está na fila =========")
      txt = open(os.path.join(self.pasta, target), 'r')
      conteudo = txt.read()
      if not simulacao:
        print(conteudo)
      self.printQueue(textList)
      txt.close()
      return 1
  
    else:
      print(f"========= {target} não está na lista =========")
      if len(textList) >= 10:
          # remover o elemento mais antigo (primeiro da lista)
          item = textList.pop(0)
          print(f"Excluído: {item}")
      print(f"Adicionado: {target}")
      textList.append(target)
      txt = open(os.path.join(self.pasta, target), 'r')
      conteudo = txt.read()
      if not simulacao:
        print(conteudo)
      self.printQueue(textList)
      txt.close()
      return 0
  def simulacao(self):
    print("==============SIMULACAO User 1 - ALEATÓRIO ==================")
    elapsed1 = []  # guardar os tempos
    foundOrNot1 = [] # guardar infos de hit or miss
    for i in range(200):
      start_time1 = time.time()
      
      num = modoSimulacao.solicitarUserAleatorio()
      target = (f"arquivo_{num}.txt")
      foundOrNot1.append(self.readFile(self.textList, target, True))

      end_time1 = time.time()

      # calculando tempo
      elapsed_time1 = end_time1 - start_time1
      elapsed1.append(elapsed_time1)
    media_tempo1 = sum(elapsed1) / len(elapsed1)
      # encontrando arquivos miss e found
    miss1 = foundOrNot1.count(0)
    found1 = len(foundOrNot1) - miss1
      
    print("==============SIMULACAO User 2 - CHANCE ==================")
    elapsed2 = []
    foundOrNot2 = []
    for i in range(200):
      start_time2 = time.time()
      
      num = modoSimulacao.solicitarUserChance()
      target = (f"arquivo_{num}.txt")
      foundOrNot2.append(self.readFile(self.textList, target, True))

      end_time2 = time.time()

      elapsed_time2 = end_time2 - start_time2
      elapsed2.append(elapsed_time2)
    media_tempo2 = sum(elapsed2) / len(elapsed2)
    
    miss2 = foundOrNot2.count(0)
    found2 = len(foundOrNot2) - miss2
    
    print("==============SIMULACAO User 3 - POISSON ==================")
    elapsed3 = []
    foundOrNot3 = []
    for i in range(200):
      start_time3 = time.time()
      
      num = modoSimulacao.solicitarUserPoisson()
      target = (f"arquivo_{num}.txt")
      foundOrNot3.append(self.readFile(self.textList, target, True))

      end_time3 = time.time()
      elapsed_time3 = end_time3 - start_time3
      elapsed3.append(elapsed_time3)
    media_tempo3 = sum(elapsed3) / len(elapsed3)
      
    miss3 = foundOrNot3.count(0)
    found3 = len(foundOrNot3) - miss3
    media_tempo3 = sum(elapsed3) / len(elapsed3)


    # print(f"As médias de tempo cache hit and time:\n User 1: {media_tempo1}\n User 2: {media_tempo2}\n User 3:{media_tempo3}")
    
    # print(f"A quantidade de Cache Miss em cada user: \n User 1: {miss1} \n User 2: {miss2} \n User 3: {miss3}")
    
    # print(f"A quantidade de arquivos que já estavam no cache: \n User 1: {found1} \n User 2: {found2} \n User 3: {found3}")

    # Escrever informações no arquivo
    relatorio = open("relatorio.txt", "a+")
    relatorio.write(f"\n \n===== LRU ===== \n As médias de tempo cache hit and time:\n User 1: {media_tempo1}\n User 2: {media_tempo2}\n User 3:{media_tempo3} \n A quantidade de Cache Miss em cada user: \n User 1: {miss1} \n User 2: {miss2} \n User 3: {miss3} \n A quantidade de arquivos que já estavam no cache: \n User 1: {found1} \n User 2: {found2} \n User 3: {found3} ")
    relatorio.close()
    miss = [miss1,miss2,miss3]
    found = [found1, found2, found3]
    media_tempo = [media_tempo1, media_tempo2, media_tempo3]

    return miss, found, media_tempo
  
  def run(self,num):
    target = (f"arquivo_{num}.txt")
    self.readFile(self.textList, target)
              