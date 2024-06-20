from rembg import remove
from PIL import Image

sample = Image.open('dog.png')

output = remove(sample)

output.save('out.png')
