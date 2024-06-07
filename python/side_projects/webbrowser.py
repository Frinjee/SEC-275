from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''

prof_path = 'C:\\Users\\Jen\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\hs3d3z0n.default'
path = 'C:\\Webdriver\\geckodriver.exe'
options = Options()
options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
options.set_preference('profile', prof_path)
service = Service(path)

driver = webdriver.Firefox(service=service, options=options)
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

src = driver.find_element("xpath", '//*[@id="box3"]')
dest_elem = driver.find_element("xpath", '//*[@id="box103"]')

actions = ActionChains(driver)
actions.drag_and_drop(src, dest_elem).perform()
