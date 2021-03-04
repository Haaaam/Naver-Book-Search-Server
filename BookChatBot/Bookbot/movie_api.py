import os
import sys
import urllib.request

def NaverMovie(moviename):
    client_id = "27Ajj0rHmLFO5d5Mxfsb"
    client_pw = "tO8tLDsUr5"
    movie = urllib.parse.quote(moviename)
    url = f"https://openapi.naver.com/v1/search/movie.json?query={movie}" # json 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_pw)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if rescode==200:
        response_body = response.read()
        return response_body.decode('utf-8')
    else:
        return None
