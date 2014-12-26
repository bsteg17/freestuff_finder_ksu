import urllib
from selenium import webdriver
from bs4 import BeautifulSoup
import freefoodmethods

def find_food_from_page(url, html_container):
	#Path to the chromedriver is definitely working fine.
	path_to_chromedriver = 'C:\Users\Ben\Desktop\Coding\FreeFoodFinder\chromedriver.exe'
	browser = webdriver.Chrome(executable_path = path_to_chromedriver)

	browser.implicitly_wait(10)
	browser.get(url)

	#KSU Home Events Page
	#content = browser.find_elements_by_css_selector(".ksu-el-events")

	#KSU Vet College Events Page
	content = browser.find_elements_by_css_selector(html_container)

	if isinstance(content, list):
		if len(content) > 0:
			html = content[0].get_attribute("innerHTML")
			html = html.encode('utf-8')
		else:
			return [], []
	else:
		html = content.get_attribute("innerHTML")
		html = html.encode('utf-8')
	
	soup = BeautifulSoup(html)

	paragraphs = soup.find_all('p')

	descriptions = []
	for p in paragraphs:
		descriptions.append(str(p).replace("<p>","").replace("</p>",""))

	freethings = []
	for desc in descriptions:
		freestuff = freefoodmethods.find_free_food(desc)
		if freestuff[0]:
			for freething in freestuff[1]:
				freethings.append(freething)
	
	browser.quit()
	return descriptions, freethings
'''
if isinstance(content, list):
	for element in content:
		html = element.get_attribute("innerHTML")
		html = html.encode('utf-8')
		print len(html)
else:
	html = content.get_attribute("innerHTML")
	html = html.encode('utf-8')
	print len(html)
'''
	



