import urllib
from ghost import Ghost
from BeautifulSoup import BeautifulSoup

ghost = Ghost(wait_timeout=10)
page, resources = ghost.open("http://www.k-state.edu/calendar/")
result, resources = ghost.evaluate("document.getElementsByClassName('ksu-el-events')")
print result