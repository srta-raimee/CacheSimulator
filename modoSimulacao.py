import random
import numpy as np


def modSim():
  print("========= Modo Simulação Ativado ========")

  print("**** Solicitações User 1 - Aleatório *****")
  for _ in range(200):
    solicitarUserAleatorio()

  print("**** Solicitação User 2 - Probabilidade *****")
  for _ in range(200):
    solicitarUserChance()

  print("**** Solicitação User 3 - Poisson *****")
  for _ in range(200):
    solicitarUserPoisson()


def solicitarUserAleatorio():
  numeroArquivo = random.randint(1, 100)

  print(numeroArquivo)
  return numeroArquivo


def solicitarUserChance():
  maior_chance = [int(numero * 1.33) for numero in range(30, 41)]
  restantes = list(set(range(1, 101)) - set(maior_chance))
  numeroArquivo2 = random.choice(maior_chance + restantes)

  print(numeroArquivo2)
  return numeroArquivo2


def solicitarUserPoisson():
  lambd = 40  # lambda para a distribuição de Poisson
  numeroArquivo3 = np.random.poisson(lam=lambd, size=1)

  print(numeroArquivo3)
  return numeroArquivo3[0]

 