
import requests

url = 'http://apis.data.go.kr/B552895/LocalGovPriceInfoService/getItemPriceResearchSearch'
params ={'serviceKey' : 'kPvWkLn8zX/rcSryaV88GKZw89YENVfrgvH06AuvYSrXsHOx6r705chjRSn/+jrdwYpeOPms5YcVRuYID5eWkA==', 'numOfRows' : '3', 'pageNo' : '1', '_returnType' : 'xml', 'examin_de' : '20200504' }

response = requests.get(url, params=params)
print(response.content)