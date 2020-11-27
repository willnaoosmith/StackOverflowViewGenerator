from selenium.webdriver.firefox.options import Options
import time, requests, json, sys
from selenium import webdriver

UserLoginList = [json.loads(credential) for credential in sys.argv[1].split('|')]
UserID = sys.argv[2]

url = "https://api.stackexchange.com/2.2/users/" + UserID + "/questions?order=desc&sort=activity&site=stackoverflow"
search = requests.get(url=url, headers={'Cache-Control': 'no-cache', 'Content-Type': 'application/json'}).json() 
LinkList = [question['link'] for question in search['items']]

def generateViews(browser):
	for link in LinkList:
		browser.get(link)
		time.sleep(2)

def Login(browser, user, password):
	browser.get(r'https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f')
	time.sleep(2)

	browser.find_element_by_id('email').send_keys(user)
	browser.find_element_by_name('password').send_keys(password)
	time.sleep(1)

	browser.find_element_by_name('submit-button').click()
	time.sleep(2)

try:

	options = Options()
	options.add_argument("--headless")
	browser = webdriver.Firefox(options=options)

	generateViews(browser)

	for credential in UserLoginList:

		Login(browser, credential['User'], credential['Password'])

		generateViews(browser)

		browser.get("https://stackoverflow.com/users/logout")
		browser.find_element_by_xpath("//*[@class='grid--cell s-btn s-btn__primary']").click()

except Exception as error:
	browser.close()

finally:
	browser.close()
