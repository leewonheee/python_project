from bs4 import BeautifulSoup
import requests
import pandas as pd

res = requests.get('http://www.daum.net/')
#mArticle > div.cmain_tmp > div.section_media > div.hot_issue.issue_mini > div.hotissue_mini > ol > li
soup = BeautifulSoup(res.text, 'html.parser')
list = []
for a in soup.select('#mArticle > div.cmain_tmp > div.section_media > div.hot_issue.issue_mini > div.hotissue_mini > ol > li'):
    rank = a.div.div.span.span.text
    keyword = a.div.div.a.text
    list.append([rank, keyword])
df2 = pd.read_csv('daum_real_time_keyword.xlsx', na_values=['-'], encoding='cp949')
print(df2)

list2 = []
for i in range(0,10):
    list2.append([df2['rank'][i],df2['keyword'][i]])
print(list2)
#
# #웹페이지 크롤링
#
# #데이터 입력시키는 법
# df = pd.DataFrame(list, columns=['rank', 'keyword'])
# df.to_csv('daum_real_time_keyword.xls', index=False, encoding='cp949')

