"""

print("안녕 PyPet~")
'''
name = "플루토"
age = 5
weight = 5
photo = "(=^0.0^=)~~~"

print("My Pet Name: " + name)
print(photo)
'''

## 딕셔너리
cat = {
    "name":"플루토",
    "age":5,
    "hungry":True,
    "weight":5,
    "photo":"(=^0.0^=)~~~"
}

mouse = {
    "name":"찍찍이",
    "age":3,
    "hungry":True,
    "weight":1.5,
    "photo":"<:3)~~~~~"
}

pets = [cat, mouse]

def feed(pet):
    if pet["hungry"] == True :
        pet["hungry"] = False
        pet["weight"] = pet["weight"] + 1
    else:
        print(pet["name"] + "는 이미 배가 불러요~")

for pet in pets:
    print(pet)
    feed(pet)
    print(pet)


'''
print(cat)
print(mouse)
feed(cat)
print(cat)
feed(cat)
print(cat)
cat["hungry"] = True
feed(cat)
print(cat)
feed(mouse)
print(mouse)
'''

"""
#import glob
#import os.path

"""
#이미지 불러오기
from PIL import Image

img = Image.open("C:\Workspaces\Python\minion.jpg")
print(type(img))
img.show()
"""

"""
#이미지 속성확인
from PIL import Image

img = Image.open("C:\Workspaces\Python\minion.jpg")

print(f'이미지 파일 이름 : {img.filename}')
print(f'이미지 파일형식(format) : {img.format}')
print(f'이미지 용량(size) : {img.size}')
print(f'이미지 색상모드 : {img.mode}')
print(f'이미지 width : {img.width}')
print(f'이미지 height : {img.height}')
"""

"""
## 이미지 크기변경(Resize)
from PIL import Image

img = Image.open("C:\Workspaces\Python\minion.jpg")

resize_img = img.resize((800, 800))
resize_img.save("C:\Workspaces\Python\minion_800x800.jpg")
"""

"""
## 이미지 크기변경(Resize)
from PIL import Image

img = Image.open("C:\Workspaces\Python\minion_800x800.jpg")
(width, height) = (img.width // 2, img.height // 2)
resize_img = img.resize((width, height))
resize_img.save("C:\Workspaces\Python\minion_400x400.jpg")
"""

"""
## 이미지 자르기(Crop)
from PIL import Image

img = Image.open("C:\Workspaces\Python\minion.jpg")
cropped_img = img.crop((100, 100, 200, 200))
cropped_img.show()
"""

"""
## 이미지 회전(Rotate)
from PIL import Image

img = Image.open("C:\Workspaces\Python\minion.jpg")
img.rotate(45).show()
"""

"""
## 이미지 회전(Rotate)
from PIL import Image

img = Image.open("C:\Workspaces\Python\minion.jpg")
img.show()

flip_img = img.transpose(Image.FLIP_LEFT_RIGHT)
flip_img.show()

flip_img2 = img.transpose(Image.FLIP_TOP_BOTTOM)
flip_img2.show()
"""

"""
## 이미지 회전(Rotate)
from PIL import Image

img = Image.open("C:\Workspaces\Python\minion.jpg")
img.show()

flip_img = img.transpose(Image.ROTATE_90)
flip_img.show()

flip_img2 = img.transpose(Image.ROTATE_180)
flip_img2.show()

flip_img3 = img.transpose(Image.ROTATE_270)
flip_img3.show()
"""

"""
## 이미지 필터링(BLUR)
from PIL import Image
from PIL import ImageFilter

img = Image.open("C:\Workspaces\Python\minion.jpg")
blur_img = img.filter(ImageFilter.BLUR)
blur_img2 = img.filter(ImageFilter.BoxBlur(10))
blur_img3 = img.filter(ImageFilter.GaussianBlur(10))

img.show()
blur_img.show()
blur_img2.show()
blur_img3.show()
"""

"""
## 이미지 필터링(ALL)
from PIL import Image
from PIL import ImageFilter

img = Image.open("C:\Workspaces\Python\minion.jpg")
filter_list = [ ImageFilter.BLUR, ImageFilter.CONTOUR, ImageFilter.DETAIL,
                ImageFilter.EDGE_ENHANCE, ImageFilter.EDGE_ENHANCE_MORE, ImageFilter.EMBOSS,
                ImageFilter.FIND_EDGES, ImageFilter.SHARPEN, ImageFilter.SMOOTH, ImageFilter.SMOOTH_MORE]
for i in range(len(filter_list)):
    filter_img = img.filter(filter_list[i])
    #filter_img.show()
    filter_img.save("C:\Workspaces\Python\minion-filter{}.jpg".format(i))
"""

"""
## 이미지 합치기
from PIL import Image

img = Image.open("C:\Workspaces\Python\minion.jpg")
img2 = Image.open("C:\Workspaces\Python\minion-filter5.jpg")
img3 = Image.open("C:\Workspaces\Python\minion-filter6.jpg")

print(img.size)
print(img2.size)
print(img3.size)
new_img = Image.new("RGB", (830, 800), 100000)
new_img.paste(img, (10, 10))
new_img.paste(img2, (img.width+10, 10))
new_img.paste(img3, (10, img.height+10))
new_img.show()
"""

"""
## 이미지 저장
from PIL import Image

img = Image.open("C:\Workspaces\Python\minion.jpg")
rotate_img = img.rotate(45)
new_img = rotate_img.save("C:\Workspaces\Python\minion-R45.png")
print(type(new_img))
"""

"""
## 이미지 썸네일
from PIL import Image

size = 40, 40
img = Image.open("C:\Workspaces\Python\minion.jpg")
img.thumbnail(size)

img.save("C:\Workspaces\Python\minion_40x40.jpg")
thumbnail_img = Image.open("C:\Workspaces\Python\minion_40x40.jpg")
thumbnail_img.show()
"""

"""
## 현재 디렉토리의 모든 JPEG 이미지에 대해 썸네일 만들기
import glob
import os
from PIL import Image

size = (128, 128)
count = 0
for infile in glob.glob("C:\Workspaces\Python\m*.jpg"):
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save(file+".thumbnail", "JPEG")
    count += 1
print("썸네일로 생성한 이미지 갯수 : ", count)
"""

"""
## 이미지를 바이트배열로 변환
from PIL import Image
import io

img = Image.open("C:\Workspaces\Python\minion.jpg")
bytearr = io.BytesIO()
img.save(bytearr, format="JPEG")
print(bytearr.getvalue())
"""

"""
## 이미지를 바이트배열로 변환
from PIL import Image
import io

def image_to_byte_array(image):
    bytearr = io.BytesIO()
    image.save(bytearr, format=image.format)
    imgbytearr = bytearr.getvalue()
    return imgbytearr

img = Image.open("C:\Workspaces\Python\minion.jpg")
print(image_to_byte_array(img))
"""
"""
## 이미지를 넘파이 배열로 변환
from PIL import Image
import numpy as np

img = Image.open("C:\Workspaces\Python\minion.jpg")
numpy_img = np.array(img)
print(type(numpy_img))
print(numpy_img)
"""

"""
## 넘파이 배열을 이미지로  변환
from PIL import Image
import numpy as np

img = Image.open("C:\Workspaces\Python\minion.jpg")
#numpy_array = np.array(img, dtype"uint8")
numpy_array = np.array(img)
print(numpy_array)

image2 = Image.fromarray(numpy_array, "RGB")
image2.show()
"""

"""
## 이미지를 픽셀 값으로 변환
from PIL import Image
import numpy as np

img = Image.open("C:\Workspaces\Python\minion.jpg")
pixel_list = list(img.getdata())
print(pixel_list)
np.savetxt("pixel_type_data.txt", pixel_list, fmt='%d', delimiter="")
"""

"""
## 이미지의 특정 픽셀의 RGB 색상 구하기
from PIL import Image
img = Image.open("C:\Workspaces\Python\minion.jpg")

rgb_img = img.convert("RGB")

tuple_item = rgb_img.getpixel((1, 100))
print(tuple_item)

r, g, b = tuple_item
print(r)
print(g)
print(b)
"""

"""
import sympy
x = sympy.symbols("x")
f = sympy.Eq(x**2, 1)
print(sympy.solve(f))
"""

"""
import sympy as sp

x, y = sym.symbols("x y")
y = x**2
sp.plot(y, (x, -3, 3), ylim=(-10, 10))
"""


def is_factor(a, b):
    if b % a == 0:
        return True
    else:
        return False

print(is_factor(4, 1024))
