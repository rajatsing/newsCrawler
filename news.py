import requests
from bs4 import *
def LatestNews(topic):
    url="https://timesofindia.indiatimes.com/"+topic
    print("Searching.....")
    data=requests.get(url)
    data=BeautifulSoup(data.text,'html.parser')
    newsdata1=data.findAll('span',{'class':'w_tle'})
    j=1
    print("Get yourself updated with latest news of"+topic+":-") 
    for i in newsdata1:
                                data=i.string
                                if not data:
                                    continue
                                print(data)
                                j=j+1
                                if(j==10):
                                        break                 

def start():
    topic=input("Enter to get latest news of sports,city,business,India:  ")
    LatestNews(topic)
    more=input("Want to serach more?: "+"  y/n:")
    if(more=="y"):
         start()
    else:
            print("byee")


start()
