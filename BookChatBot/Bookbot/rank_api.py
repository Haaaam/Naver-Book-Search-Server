import requests
from bs4 import BeautifulSoup as bs



def MovieRank(date):
    keyword =date.replace('-','')
    url="https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date="+keyword
    html=requests.get(url)
    soup=bs(html.content,'html.parser')
    rank=soup.findAll("div",{"class":"tit3"})
    rank_lst=[]

    for i in rank:
        title=i.text.strip()
        rank_lst.append({"title":title})
    return rank_lst
