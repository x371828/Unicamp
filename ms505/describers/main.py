import math
import numpy as np

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