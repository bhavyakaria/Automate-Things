import requests
from bs4 import BeautifulSoup

r = requests.get("http://myanimelist.net/topanime.php")

soup = BeautifulSoup(r.content, "html5lib")

g_data = soup.find_all("tr",{"class": "ranking-list"})

x=1
for item in g_data:
    if x < 10: 
        print(item.contents[1].find_all("span",{"class":"lightLink top-anime-rank-text rank1"})[0].text)
    else:
        print(item.contents[1].find_all("span",{"class":"lightLink top-anime-rank-text rank2"})[0].text)
    
    print(item.contents[3].find_all("a",{"class":"hoverinfo_trigger fl-l fs14 fw-b"})[0].text)
    print(item.contents[5].text)
    x+=1
