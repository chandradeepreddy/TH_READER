from TH_Repository import *

#this line generates a list of Hindu daily urls like : 'http://www.thehindu.com/archive/print/2017/01/01/'
dayUrls= TH_DayUrl_Generator()

#this line takes in Database password
PWD = raw_input( "Please Enter Database Password: ")

#this line extracts  article urls (ending in .ece) from each day's url generated above
articl_dict = TH_Article_URL__Extractor(dayUrls)

#this line inserts the article urls got in above step into database without any filteration
TH_Article_URL_DBInsert(articl_dict, PWD)
