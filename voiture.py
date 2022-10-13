from PIL import Image
from skimage.transform import resize
import matplotlib.pyplot as plt

im=Image.open('voiture.png')
im.show()
im= plt.imread('voiture.png')
res= resize(im,(600,400))
