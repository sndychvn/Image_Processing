from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


i = Image.open('D:/Downloads/sample1.jpg')
iar = np.array(i)

print(iar)

plt.imshow(iar)
plt.show()