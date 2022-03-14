import requests
from bs4 import BeautifulSoup


url = "http://chart.capital.com.tw/Chart/TWII/TAIEX11.aspx?fbclid=IwAR0zV9w6j1dWIme9lemKBMxSJrZV94sx9moZ3LSyWKGn-WljNlTa3ldaEJ8"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

overboughts = {}

for table in soup.table.find_all('table'):
    for tr in table.find_all('tr')[1: :]:
        # 日期
        date = tr.contents[1].string
        # 八大行庫買賣超金額
        overbought = tr.contents[3].string
        # tx: 台指期
        tx = tr.contents[5].string

        overboughts[date] = {
            'tx': tx,
            'overbought': overbought 
        }


for key in overboughts:
    print(key, ": ", overboughts[key])
