from PIL import Image
import numpy as np
import os

folder = "Treino"

for filename in os.listdir(folder):
    if filename.endswith((".png", ".jpg", ".jpeg")):  # filter image files
        filepath = os.path.join(folder, filename)

        img = Image.open(filepath).convert("L")
        img_array = np.array(img)
        print(img_array.shape)


