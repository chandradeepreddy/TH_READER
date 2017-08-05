from bs4 import BeautifulSoup
import urllib2
import re
from datetime import date, timedelta
import warnings
import psycopg2


warnings.filterwarnings("ignore", category=UserWarning, module='bs4')




def TH_DayUrl_Generator():
	""" 
	This function takes in a date range and 
	give a list of hindu daily urls from 
	the hindu archives page ( print edition) like : 'http://www.thehindu.com/archive/print/2017/01/01/'.
	Returns a list
	"""
	print "Enter Start and End Date details in below format: \n\n***  YYYYMMDD  *** \n\n "
	Start_dt = raw_input("Enter the start date: ")
	end_dt = raw_input("Enter the end date: ")
	start_year = int(Start_dt[:4])
	start_month = int(Start_dt[4:6])
	start_day = int(Start_dt[6:8])
	end_year = int(end_dt[:4])
	end_month = int(end_dt[4:6])
	end_day = int(end_dt[6:8])

	DayUrls =[]
	Start_Date = date(start_year, start_month, start_day)  # start date
	End_Date = date(end_year, end_month, end_day)  # end date
	delta = (End_Date-Start_Date)

	for i in range(delta.days + 1):
		DayUrls.append('http://www.thehindu.com/archive/print/'+str((Start_Date + timedelta(days=i)).year)+'/'+str((Start_Date + timedelta(days=i)).strftime('%m'))+'/'+str((Start_Date + timedelta(days=i)).strftime('%d'))+'/')
	return DayUrls

def TH_Article_URL__Extractor(DayUrls_list):
	""" 
	This function takes in a daily hindu url list(generated above)
	and gives all artilce links from that day along with 
	the date. 
	Returns a list
	"""
	ArtUrls = {}
	for i in range(len(DayUrls_list)):
		soup = BeautifulSoup(urllib2.urlopen(DayUrls_list[i]))
		soup.prettify()
		AllUrls = soup.findAll('a', href=True)
		Articles = [AllUrls[url]['href'] for url in range(len(AllUrls)) if '.ece' in AllUrls[url]['href'] and '/todays-paper/' in AllUrls[url]['href'] ]
		
		for j in range(len(Articles)):
			print str(re.sub('[^0-9]','',DayUrls_list[i])) +' '+Articles[j]
			ArtUrls[Articles[j].encode('utf-8')] = str(re.sub('[^0-9]','',DayUrls_list[i]))
	
	return ArtUrls

def TH_Article_URL_DBInsert(ArtDict,pw):
	""" 
	This function takes in all the article url generated above and 
	inserts them in the table  TH.Article_urls. 
	Returns a list
	"""
	conn = psycopg2.connect(host="localhost",database="upsc", user="postgres", password=pw)
	cursor = conn.cursor()
	for item in ArtDict:
		url_dt = ArtDict[item]
		url = item
		query =  "INSERT INTO TH.Article_urls (url_id, url_dt, url) VALUES (nextval('TH.Article_urls_seq'), %s, %s);"
		data = (url_dt, url)
		cursor.execute(query, data)
		conn.commit()
