from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("your_photo.jpg")

plt.imshow(img)
plt.axis("off")
plt.show()
