
from bs4 import BeautifulSoup
import requests

response = requests.get("http://www.nepalstock.com/")

# print(response.text)

bs = BeautifulSoup(response.text, "html.parser")

h1s = bs.select("#market-watch .panel-body td")

print("Todays Total Turnover in Sharemarket is Rs.", h1s[2].text)


# for a in h1s:
#     print(a)
