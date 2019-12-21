import requests
import pandas as pd

res = requests.get("http://isin.twse.com.tw/isin/C_public.jsp?strMode=2")

# print("hi stock")

# print(res.text)


df = pd.read_html(res.text)[0]
df