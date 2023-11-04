import os
import glob
from PIL import Image

# dst_dir = 'public\images\construction-management\section1'
# os.makedirs(dst_dir, exist_ok=True)

files = glob.glob('public\images\construction-management\section1/*.jpg')

for f in files:
    img = Image.open(f)
    img_resize = img.resize((img.width // 2, img.height // 2))
    

    img_resize.save(f)

