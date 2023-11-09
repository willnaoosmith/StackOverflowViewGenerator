from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import requests, json, sys, os
from time import sleep

UserLoginList = [json.loads(credential) for credential in sys.argv[1].split('|')]
UserID = sys.argv[2]

url = "https://api.stackexchange.com/2.2/users/" + UserID + "/questions?order=desc&sort=activity&site=stackoverflow"
search = requests.get(url=url, headers={'Cache-Control': 'no-cache', 'Content-Type': 'application/json'}).json() 
LinkList = [question['link'] for question in search['items'] if question['view_count'] <= int(10000)]

def generateViews(browser):
	for link in LinkList:
		browser.get(link)
		sleep(2)

def Login(browser, user, password):
	browser.get(r'https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f')
	sleep(2)

	browser.find_element(By.ID, 'email').send_keys(user)
	browser.find_element(By.NAME, 'password').send_keys(password)
	sleep(1)

	browser.find_element(By.NAME, 'submit-button').click()
	sleep(2)

try:
	options = Options()
	options.add_argument("--headless")
	service = Service(log_path=os.devnull)
	browser = webdriver.Firefox(options=options, service=service)
	
	generateViews(browser)

	for credential in UserLoginList:

		Login(browser, credential['User'], credential['Password'])

		generateViews(browser)

		browser.get("https://stackoverflow.com/users/logout")
		browser.find_element(By.XPATH, "//*[@class='flex--item s-btn s-btn__filled']").click()

except Exception as error:
	print(error)	

finally:
	try:
		browser.quit()

	except:
		pass
