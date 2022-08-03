from PIL import Image
import os

file_list = os.listdir('princess_img')
for file in file_list:
    img = Image.open(f'princess_img/{file}')
    if img.getbands() != ('P',):
        img = img.convert('P',)
        
    img_resize = img.resize((5, 5))
    img_resize = img_resize.resize((256, 256))
    name = file.replace('.png', '')
    img_resize.save(f'princess_img_25/{name}_25.png')
    
    
