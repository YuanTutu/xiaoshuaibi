import requests
import re
from fontTools.ttLib import TTFont
import os
import xml.dom.minidom as xmldom
base_font = TTFont("fonts/e48d781ccb675ee3cfd897187ae246a82284.woff")
# 转换成xml格式
base_font.saveXML("fonts/e48d781ccb675ee3cfd897187ae246a82284.xml")
