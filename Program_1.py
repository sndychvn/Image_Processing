from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


i = Image.open('images/numbers/y0.5.png')
plt.imshow(i)
plt.show()
iar = np.array(i)

print(iar)

plt.imshow(iar)
plt.show()
