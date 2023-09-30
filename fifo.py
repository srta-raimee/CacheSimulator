#  FirstInFirstOut = primeiro a entrar, primeiro a sair da fila

import random
from queue import Queue
import os
import modoSimulacao
import time

class Fifo:

  def __init__(self):
    print("\n \n === Criando fila para algoritmo FIFO === \n")
    # Criar uma fila vazia para armazenar strings
    self.textQueue = Queue()
    self.pasta = 'arquivos_divididos'
    self.arquivos = os.listdir(self.pasta)
    self.textos = ['']

    for i in self.arquivos:
      self.textos.append(i)
    
    print("Inserindo 10 arquivos de texto aleatórios:")
    for _ in range(0, 10):
      item = random.choice(self.textos)
      self.textQueue.put(item)
      print(f"Inserido: {item}")
    self.printQueue(self.textQueue)


  def printQueue(self,q):
    tempQueue = Queue()
    print("\n \n Fila: ", end='')
    while not q.empty():
      item = q.get()
      print(item, end=' ')
      tempQueue.put(item)
    print()
  
    while not tempQueue.empty():
      q.put(tempQueue.get())
  
  
  def searchQueue(self, q, target):
    tempQueue = Queue()
    found = False
  
    while not q.empty():
      item = q.get()
      if item == target:
        found = True
      tempQueue.put(item)
  
    while not tempQueue.empty():
      q.put(tempQueue.get())
  
    return found
  
  
  def readFile(self,textQueue, target, simulacao = False): 
    if self.searchQueue(textQueue, target):
      print(f"========= {target} está na fila =========")
      txt = open(os.path.join(self.pasta, target), 'r')
      conteudo = txt.read()
      if not simulacao:
        print(conteudo)
      txt.close()
      return 1
    else:
      print(f"========= {target} não está na fila =========")
      for _ in range(1):
        item = textQueue.get()
        print(f"Excluído: {item}")
      print(f"Adicionado: {target}")
      self.textos.append(target)
      textQueue.put(target)
      txt = open(os.path.join(self.pasta, target), 'r')
      conteudo = txt.read()
      if not simulacao:
        print(conteudo)
      txt.close()
      return 0
      
  def simulacao(self):
    print("==============SIMULACAO User 1 - ALEATÓRIO ==================")
    foundOrNot1 = [] # guardar infos de hit or miss
    elapsed1 = []  # guardar os tempos
    for i in range(200):
      start_time1 = time.time()
      
      num = modoSimulacao.solicitarUserAleatorio()
      target = (f"arquivo_{num}.txt")
      foundOrNot1.append(self.readFile(self.textQueue, target, True))

      end_time1 = time.time()

      # calculando tempo
      elapsed_time1 = end_time1 - start_time1
      elapsed1.append(elapsed_time1)

    # encontrando arquivos miss e found
    miss1 = foundOrNot1.count(0)
    found1 = len(foundOrNot1) - miss1
    media_tempo1 = sum(elapsed1) / len(elapsed1)


    print("==============SIMULACAO User 2 - CHANCE ==================")
    elapsed2 = []
    foundOrNot2 = []
    for i in range(200):
      start_time2 = time.time()
      
      num = modoSimulacao.solicitarUserChance()
      target = (f"arquivo_{num}.txt")
      foundOrNot2.append(self.readFile(self.textQueue, target, True))

      end_time2 = time.time()

      elapsed_time2 = end_time2 - start_time2
      elapsed2.append(elapsed_time2)
    miss2 = foundOrNot2.count(0)
    found2 = len(foundOrNot2) - miss2
    media_tempo2 = sum(elapsed2) / len(elapsed2)

    
    print("==============SIMULACAO User 3 - POISSON ==================")
    elapsed3 = []
    foundOrNot3 = []
    for i in range(200):
      start_time3 = time.time()

      num = modoSimulacao.solicitarUserPoisson()
      target = (f"arquivo_{num}.txt")
      foundOrNot3.append(self.readFile(self.textQueue, target, True))
      end_time3 = time.time()
      
      elapsed_time3 = end_time3 - start_time3
      elapsed3.append(elapsed_time3)
      
    miss3 = foundOrNot3.count(0)
    found3 = len(foundOrNot3) - miss3
    media_tempo3 = sum(elapsed3) / len(elapsed3)


    # print(f"As médias de tempo cache hit and time:\n User 1: {media_tempo1}\n User 2: {media_tempo2}\n User 3:{media_tempo3}")
    
    # print(f"A quantidade de Cache Miss em cada user: \n User 1: {miss1} \n User 2: {miss2} \n User 3: {miss3}")
    
    # print(f"A quantidade de arquivos que já estavam no cache: \n User 1: {found1} \n User 2: {found2} \n User 3: {found3}")

    # Escrever informações no arquivo
    relatorio = open("relatorio.txt", "a+")
    relatorio.write(f"\n \n===== FIFO ===== \n As médias de tempo cache hit and time:\n User 1: {media_tempo1}\n User 2: {media_tempo2}\n User 3:{media_tempo3} \n A quantidade de Cache Miss em cada user: \n User 1: {miss1} \n User 2: {miss2} \n User 3: {miss3} \n A quantidade de arquivos que já estavam no cache: \n User 1: {found1} \n User 2: {found2} \n User 3: {found3} ")
    relatorio.close()
    miss = [miss1,miss2,miss3]
    found = [found1, found2, found3]
    media_tempo = [media_tempo1, media_tempo2, media_tempo3]

    return miss, found, media_tempo
    

  
  def run(self, num):
    # num = int(input("Digite o número do arquivo que quer visualizar: "))

    target = (f"arquivo_{num}.txt")
    self.readFile(self.textQueue, target)



    