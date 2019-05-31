from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time 
from selenium.webdriver.common.action_chains import ActionChains

# Configure filepaths
chrome_exe = "C:\\Program Files\\Python 3.5\\Scripts/chromedriver.exe"
chrome_options = Options()
chrome_options.add_extension('contacts.crx')

driver = webdriver.Chrome(executable_path=chrome_exe, chrome_options=chrome_options)
wait = ui.WebDriverWait(driver,10)
driver.get("https://web.whatsapp.com/")

form = '//form[@id="addContactFor"]/child::div[@id="addContactExternalForm"]/child::div[@ng-if="contact.addNewContact"]'

unams = "//form[@id='addContactForm']/child::div[2]/child::div/child::div/child::input[@placeholder='Name']"
mobile ='//form[@id="addContactForm"]/child::div[2]/child::div/child::div/child::input[@placeholder="Contact Number"]'
submit ='//form[@id="addContactForm"]/child::div[2]/child::div/child::div[8]/child::button[1]'


input("press something")

later = driver.find_element(By.XPATH,'//*[@id="coachMarks"]/div[2]/div[2]/div[2]')
later.click()
elem = driver.find_element(By.XPATH,'//img[@data-float-arrow="arrow-left"]')
elem.click()
wait = ui.WebDriverWait(driver,10)
addcontact = driver.find_element(By.XPATH,'//div[@title="Add new contact"]')
addcontact.click()
wait = ui.WebDriverWait(driver,10)

# modal = driver.switch_to.active_element
# print(modal)
time.sleep(2)

nameelem = driver.find_element(By.XPATH,unams)

mobelem = driver.find_element(By.XPATH,mobile)

subelem = driver.find_element(By.XPATH,submit)


nameelem.send_keys("jxack")
mobelem.send_keys("9863883838")


subelem.click()

time.sleep(5)

driver.find_element(By.XPATH,'//*[@id="addContactModal"]/div/div/div[1]/button/span').click()

time.sleep(1)

x = 5
print("loop has begun")
while(x>0):

	elem = driver.find_element(By.XPATH,'//img[@data-float-arrow="arrow-left"]')
	elem.click()
	time.sleep(2)
	addcontact = driver.find_element(By.XPATH,'//div[@title="Add new contact"]')
	addcontact.click()
	
	wait = ui.WebDriverWait(driver,10)

	# modal = driver.switch_to.active_element
	# print(modal)
	time.sleep(2)

	nameelem = driver.find_element(By.XPATH,unams)

	mobelem = driver.find_element(By.XPATH,mobile)

	subelem = driver.find_element(By.XPATH,submit)


	nameelem.send_keys("jxack"+str(x))
	mobelem.send_keys("986388383"+str(x))
	subelem.click()

	time.sleep(5)

	driver.find_element(By.XPATH,'//*[@id="addContactModal"]/div/div/div[1]/button/span').click()

	time.sleep(2)

	x = x - 1
