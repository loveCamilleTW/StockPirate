import requests
from bs4 import BeautifulSoup


url = "https://www.twse.com.tw/zh/holidaySchedule/holidaySchedule"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find_all("tr > td")
print(table)
# print(soup.prettify())  #輸出排版後的HTML內容