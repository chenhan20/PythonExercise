import requests
import pandas as pd
from bs4 import BeautifulSoup

res = requests.get("http://isin.twse.com.tw/isin/C_public.jsp?strMode=2")

# print("hi stock")

# print(res.status_code)

# print(pd)

# scores = pd.Series({'小明':90, '小華':80, '小李':70})
# #Series簡單的創建方法，直接給一個dictionary
# #新增資料的方法，有點像是陣列
# scores['小強'] = 55

# print(scores.describe())
# print("--------------------------------")
# print(scores)

df = pd.read_html(res.text)[0]
df
# print(df)