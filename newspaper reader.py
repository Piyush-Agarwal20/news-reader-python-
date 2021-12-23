from pickle import APPEND
import requests
import json


def speeak(str):  
    from win32com.client import Dispatch

    speak=Dispatch('SAPI.Spvoice')

    speak.speak(str)

speeak('news for today')
url="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=6f766959fea14227b592e3ec5b5deefe"
news=requests.get(url).text
news=json.loads(news)
arts=news['articles']



arts3=[]
for i in range(len(arts)):
    arts1=arts[i]
    arts2=arts1['title']
    arts3.append(arts2)

for i,i1 in enumerate(arts3):
    print(i+1,i1)
    speeak(str(i1))
    if i <=18:
        speeak('next')
    else:
        speeak('over')