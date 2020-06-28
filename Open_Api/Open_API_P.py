#from urllib2 import Request, urlopen
import r
from urllib import urlencode, quote_plus

url = 'http://apis.data.go.kr/1192000/OceansBeachSeawaterService/getOceansBeachSeawaterInfo'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '08un1SDWwxvMxkCQwzES6WAgo9UiKywjZFnSVsV9wCudGxhUgtye%2FS0%2B1OG9CMiCk08Yncq1MwO%2B20FIBoO3eg%3D%3D',\
                                quote_plus('ServiceKey') : '-', quote_plus('pageNo') : '1',\
                                quote_plus('numOfRows') : '10', quote_plus('SIDO_NM') : '충남',\
                                quote_plus('RES_YEAR') : '2016', quote_plus('resultType') : 'xml' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)