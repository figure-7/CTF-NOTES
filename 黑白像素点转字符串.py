#使用：.\hb黑白像素块10.py 2239f085-4e8c-425b-9e8e-793c982c42f5.png
#author:CHTXRT
from PIL import Image
import sys

img = Image.open('2239f085-4e8c-425b-9e8e-793c982c42f5.png')
res = ''
temp = ''
n = 0
for x in range(320):
    for y in range(320):
        n+=1
        if(img.getpixel((x,y))==(255,255,255)):
            temp += '0'
        else:
            temp += '1'
        if(n==8):
            n = 0
            res += chr(int(temp,2))
            temp = ''
img.close()
print(res)
