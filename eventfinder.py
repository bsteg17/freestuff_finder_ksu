import urllib
import json
import re
import calendar
from datetime import date
import freefoodmethods

ksujsontextraw = urllib.urlopen("http://pulse.k-state.edu/calendar/api/v2/event/?format=jsonp&start=20141008&end=20141208&limit=100&callback=YUI.Env.JSONP.yui_3_13_0_2_1415475562180_16").read()

ksujsontextpart = ksujsontextraw.partition("(")
ksujsontexttrim = ksujsontextpart[2][:(len(ksujsontextpart[2]) - 1)]

ksujson = json.loads(ksujsontexttrim)

info = {}
calendar.setfirstweekday(calendar.SUNDAY)

for event in ksujson["objects"]:
	
	title = event["title"]
	info[title] = {"dateinfo":{}}

	#get free stuff info (ie what is being offered for free at event)
	
	found, freeitems = freefoodmethods.find_free_food(event["description"])
	if found:
		info[title]["free"] = freeitems
		if event["start_date"] == event["end_date"]:
	
			date = event["start_date"]
			datelist = event["start_date"].split("-")
			year = int(datelist[0])
			month = int(datelist[1])
			day = int(datelist[2])
			monthname = calendar.month_name[month]
			weekday = calendar.weekday(year, month, day)
			datedisplayed = calendar.day_name[weekday]+", "+monthname+" "+str(day)+", "+str(year)
			info[title]["dateinfo"]["datefancy"] = datedisplayed
			
			print info[title]["free"] 
			print "Date: " + info[title]["dateinfo"]["datefancy"]
			


		