from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import xlwt

firefox_options = webdriver.ChromeOptions()
firefox_options.set_headless()
driver = webdriver.Firefox(firefox_options=firefox_options)
driver.get("https://www.bilibili.com")
driver.close()
