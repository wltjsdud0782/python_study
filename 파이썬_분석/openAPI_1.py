# library 임포트
import requests
import pandas
import bs4

# API로 데이터 불러오기
url = 'http://apis.data.go.kr/3210000/SeochoIaqSvc/getSeochoIaqRtData'
params ={'serviceKey' : 'Pq8dvT+tIR3dsc7IfeeEl/KGNryvWt3WWuHU8Gw4VxNsT97/66aRRKa/AtNeCLpHqwzPr2hiwbS3Z5JO48djqg=='
        , 'numOfRows' : '10'
        , 'pageNo' : '1' }

response = requests.get(url, params=params)

# 가져온 데이터(문자열)를 beautifulSoup 형태로 변환
bs_data = bs4.BeautifulSoup(response.text, 'lxml-xml')

# item 태그의 모든 내용만 가져오기
items = bs_data.findAll('item')

# items 안의 내용을 통해 dictionary 데이터 구성
dataTime_list = []
for item in items :
    print(item.find('dataTime').text)
    dataTime_list.append(item.find('dataTime').text)

# api 로 가져온 데이터를 모두 저장 할 dictionary
dic_data = {}
dic_data['dataTime'] = dataTime_list

# dictionary 데이터를 DataFrame 으로 변환
df = pandas.DataFrame(dic_data)
df.to_excel('api_test.xlsx')
print(df)