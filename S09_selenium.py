from selenium import webdriver

driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromePro.exe')
driver.get("https://www/baidu.com")

input = driver.find_element_by_css_selector('#kw')
input.send_keys("苍老师照片")

button = driver.find_elements_by_css_selector('#su')
button.click()