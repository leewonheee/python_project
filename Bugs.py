from bs4 import BeautifulSoup
import requests
import pandas as pd

res = requests.get('https://music.bugs.co.kr/chart')
soup = BeautifulSoup(res.text, 'html.parser')
list = []
#CHARTrealtime > table > tbody > tr:nth-child(1) > td:nth-child(4) > div > strong
for tr in soup.select('#CHARTrealtime > table > tbody >tr'):
    rank = tr.select('td')
    rank = rank[1].find('strong').get_text()
    title = tr.th.p.a.text
    list.append([rank, title])

print(list)

df = pd.DataFrame(list, columns=['rank', 'title'])
df.to_csv('Bugs.xlsx', index=False, encoding='cp949')

