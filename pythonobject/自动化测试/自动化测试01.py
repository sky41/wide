from selenium import webdriver

option = webdriver.ChromeOptions()
option.binary_location = r'C:\Users\sky14\AppData\Local\Chromium\Application\Chromium.exe'

driver = webdriver.Chrome(r'D:\anaconda\chromedriver.exe')
driver.get("https://www.baidu.com")
