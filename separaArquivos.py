import os
import time

def sepArquivos():
  min_palavras = 1000
  
  max_arquivos = 100
  
  with open('livro.txt', 'r') as f:
      conteudo = f.read()
  
  num_palavras = len(conteudo.split())
  
  num_arquivos = min(max_arquivos, int(num_palavras / min_palavras) + 1)
  
  palavras_por_arquivo = int(num_palavras / num_arquivos)

  diretorio = 'arquivos_divididos'
  
  if not os.path.isdir(diretorio):
      os.makedirs(diretorio)
  else:
    print("Arquivos já foram divididos anteriormente! Vamos continuando...")
    time.sleep(2)
  
  for i in range(num_arquivos):
      nome_arquivo = f'arquivos_divididos/arquivo_{i+1}.txt'
      with open(nome_arquivo, 'w') as f:
          f.write(' '.join(conteudo.split()[i*palavras_por_arquivo:(i+1)*palavras_por_arquivo]))
  