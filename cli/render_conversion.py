import numpy as np
from PIL import Image, ImageDraw, ImageFont
from conversions import find_conversion_path
import requests
from io import BytesIO
import cv2

def get_img(compound):
    response = requests.get("https://opsin.ch.cam.ac.uk/opsin/" + compound + ".png")
    return Image.open(BytesIO(response.content))

def test(imgs):
    widths, heights = zip(*(i.size for i in imgs))

    total_width = 15+sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height), (255,255,255))

    x_offset = 15
    for im in imgs:
        new_im.paste(im, (x_offset,max_height//2 - im.height//2))
        x_offset += im.size[0]

    new_im.show()

print("Convert")
from_c = input("from: ")
to_c = input("to: ")
res = find_conversion_path(from_c, to_c)
print("Converting...")
imgs = []
res = res + [(res[-1][-1],0,0)]
for x in res:
    reac, reag, prod = x
    l = reac
    imgs.append(get_img(l))
    if l==to_c:
        break
    w, h = 110, 50
    im = Image.new('RGB', (w,h), (255,255,255))

    na = np.array(im)

    na = cv2.arrowedLine(na, (15,h//2), (w-15, h//2), (255,0,0), 1)

    arr_img = Image.fromarray(na)
    I1 = ImageDraw.Draw(arr_img)
    size = 9
    reactant = reag
    myFont = ImageFont.truetype('arial.ttf', size)

    r = reactant.split(" / ")
    if "(" in r[-1]:
        r = [*r[:-1], r[-1].split("(")[0], "("+r[-1].split("(")[1]]

    for i, text in enumerate(r):
        n = 2*(len(r)//2) + 2
        size += 2
        ypos = h//2 - (size*n)//2 + i*size
        I1.text((15+((w-30)//2-len(text)*2), ypos), text, font=myFont, fill=(255, 0, 0))

    imgs.append(arr_img)
    
test(imgs)


