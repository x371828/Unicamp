import math
import numpy as np
from PIL import Image
import os
from collections import Counter
import matplotlib.pyplot as plt
from pathlib import Path


def calcula_vizinhos(array, lin, col):

    vizinhos = ""

    for i in range(8):

        inc_y = round(math.sin(i*math.pi/4))
        inc_x = round(math.cos(i*math.pi/4))

        if (lin - inc_y) in range(128) and (col + inc_x) in range(128):
            if array[lin, col] > array[lin - inc_y, col + inc_x]:
                vizinhos += "1"
            else:
                vizinhos += "0"
        else:
            if array[lin,col] == 0:
                vizinhos += "0"
            else:
                vizinhos += "1"

    return int(vizinhos, 2)


def gera_descritores(array):
    
    descritores_pre = []
    
    for lin in range(128):
        for col in range(128):
            descritores_pre.append(calcula_vizinhos(array, lin, col))
            
    hist = Counter(descritores_pre)
    descritores = np.array([hist[chave] for chave in sorted(list(hist.keys()))])
    
    return descritores
    

#Configura path da imagem, acessa e converte para array preto e branco
script_dir = Path(__file__).resolve().parent
img_path = script_dir.parent / "data" / "formated_data" / "Treino" / "c001_001.png"
img = Image.open(img_path).convert("L")
img_array = np.array(img)

print("PREIR")

# #Visualiza o histograma
# plt.hist(descritores, bins='auto')
# plt.show()