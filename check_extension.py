from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

op = Options()

# op.add_extension('C:/Users/User/Desktop/ZeuZ/test/Momentum.crx')
op.add_extension('C:/Users/User/Desktop/ZeuZ/test/Metamask.crx')

# driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe", options=op)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=op)

driver.get("https://www.google.com/")

parent = driver.window_handles[0]
chld = driver.window_handles[1]
driver.switch_to.window(parent)
driver.close()
driver.switch_to.window(chld)

driver.get("https://facebook.com/")
user_input = input("type something on the console")
