
from lru import Lru
from lfu import Lfu
from fifo import Fifo
import separaArquivos as sa
import random

print("Arquivos sendo divididos...")
sa.sepArquivos()
fifo = Fifo()
lfu = Lfu()
lru = Lru()


algoritmos_cache = ["fifo","lfu","lru"]
algoritmo_ativo = algoritmos_cache[random.randint(0,2)]

while True:
    if algoritmo_ativo == "fifo":
        print("\n \n ======== FIFO ========")

    if algoritmo_ativo == "lfu":
        print("\n \n ======== LFU ========")

    if algoritmo_ativo == "lru":
        print("\n \n ======== LRU ========")
        
    num = int(input("Digite o número do arquivo que quer visualizar: "))
    if num == 0:
        break
    
    if num == -1:
        fifo_miss, fifo_found, fifo_media_tempo = fifo.simulacao()
        lfu_miss, lfu_found, lfu_media_tempo = lfu.simulacao()
        lru_miss, lru_found, lru_media_tempo = lru.simulacao()
        FifoMissMediaTempo = sum(fifo_media_tempo)/len(fifo_media_tempo)
        LfuMissMediaTempo = sum(lfu_media_tempo)/len(lfu_media_tempo)
        LruMissMediaTempo = sum(lru_media_tempo)/len(lru_media_tempo)
        if min(FifoMissMediaTempo,LfuMissMediaTempo,LruMissMediaTempo) == fifo_media_tempo:
            algoritmo_ativo = "fifo"
        elif min(FifoMissMediaTempo,LfuMissMediaTempo,LruMissMediaTempo)== lfu_media_tempo:
            algoritmo_ativo = "lfu"
        elif min(FifoMissMediaTempo,LfuMissMediaTempo,LruMissMediaTempo) == lru_media_tempo:
            algoritmo_ativo = "lru"
        print("O melhor algoritmo foi:", algoritmo_ativo)
    elif algoritmo_ativo == "fifo":
        fifo.run(num)

    elif algoritmo_ativo == "lfu":
        lfu.run(num)

    elif algoritmo_ativo == "lru":
        lru.run(num)

    

    


