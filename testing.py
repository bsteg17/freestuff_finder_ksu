import SeleniumFood

urls = [('http://www.vet.k-state.edu/events/','.ksu-el-container'),('http://www.k-state.edu/calendar/','.ksu-el-events'),('http://www.k-state.edu/openhouse/events/engineering.html','.ksu-main-content')]

for url in urls:
	descs, things = SeleniumFood.find_food_from_page(url[0], url[1])

	print url
	print len(descs)
	print len(things)