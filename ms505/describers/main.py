import math
import numpy as np
from PIL import Image
import os
from collections import Counter
import matplotlib.pyplot as plt
from pathlib import Path

script_dir = Path(__file__).resolve().parent
img_path = script_dir.parent / "data" / "formated_data" / "Treino" / "c001_001.png"

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

#Gera descritor de imagem qualquer
img = Image.open(img_path).convert("L")
img_array = np.array(img)

descritores = []

for lin in range(128):
    for col in range(128):
        descritores.append(calcula_vizinhos(img_array, lin, col))

#Cria histograma (dict) da imagem
hist = Counter(descritores)
print(hist)

#Ordena o histograma e transforma em lista
list = np.array([hist[chave] for chave in sorted(list(hist.keys()))])

#Visualiza o histograma
plt.hist(descritores, bins='auto')
plt.show()