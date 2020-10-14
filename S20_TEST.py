try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
#如果不关联这个exe就不能用
pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'
#1/2/4/7/14/
#灰度处理
captcha = Image.open(".\\pic\\4.jpg")
# result = captcha.convert('L')
# result.show()
#二值化
def convert_img(img,threshold):
    img = img.convert("L")  # 处理灰度
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            if pixels[x, y] > threshold:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
    return img

img=convert_img(captcha,150)

data = img.getdata()
w,h = img.size
count = 0
for x in range(1,h-1):
    for y in range(1, h - 1):
        # 找出各个像素方向
        mid_pixel = data[w * y + x]
        if mid_pixel == 0:
            top_pixel = data[w * (y - 1) + x]
            left_pixel = data[w * y + (x - 1)]
            down_pixel = data[w * (y + 1) + x]
            right_pixel = data[w * y + (x + 1)]

            if top_pixel == 0:
                count += 1
            if left_pixel == 0:
                count += 1
            if down_pixel == 0:
                count += 1
            if right_pixel == 0:
                count += 1
            if count > 4:
                img.putpixel((x, y), 0)

result = pytesseract.image_to_string(img)
print(result)