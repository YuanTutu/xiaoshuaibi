import numpy as np
import jieba
from wordcloud import WordCloud,ImageColorGenerator
import matplotlib.pyplot as plt
from imageio import imread
from PIL import Image


file_path = "jay.txt"

#读取txt
f = open(file_path,'r',encoding="UTF-8").read()
jieba_text = ' '.join(jieba.cut(f))
#print(jieba_text)


#尝试背景颜色图
#此处需要注意，并不是显示出来图片作为背景，而是提取图片的主颜色作为词云的背景颜色而已，所以下面换来换去并没有实际意义……
bg_pic = imread(r'sanjicaihua.jpg')
#帅比的
img = "sanjicaihua.jpg"
background_image = np.array(Image.open(img))


wordcloud = WordCloud(
    font_path='桦源黑体 Bold.ttf',
    background_color = "white",
    mask = background_image
    #mask=bg_pic
).generate(jieba_text)
#image_colors = ImageColorGenerator(bg_pic)
image_colors = ImageColorGenerator(background_image)

plt.imshow(wordcloud.recolor(color_func=image_colors),interpolation='bilinear')
plt.axis("off")
plt.show()