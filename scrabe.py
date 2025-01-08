from audioop import reverse

import requests
from bs4 import BeautifulSoup
import pprint
def combine_links(url):
    i=1
    mega_link=[]
    while i<3 and url:
        #res=requests.get('https://news.ycombinator.com/news?p='+str(i))
        res = requests.get(url + str(i))
        soup=BeautifulSoup(res.text,'html.parser')
        links=soup.select('.titleline')
        mega_link=mega_link+links
        i=i+1
    return mega_link


def combine_subtext(url):
    i=1
    mega_subtext=[]
    while i<3 and url:
        res=requests.get('https://news.ycombinator.com/news?p='+str(i))
        soup=BeautifulSoup(res.text,'html.parser')
        subtext=soup.select('.subtext')
        mega_subtext=mega_subtext+subtext
        i=i+1
    return mega_subtext


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'],reverse=True)

def create_custom_hacker_news(links,subtext):
    hn=[]
    for idx,item in enumerate(links):

        title=item.getText()
        href=item.find('a').get('href',None)
        vote=subtext[idx].select('.score')
        #print(item)

        if len(vote):
            points=int(vote[0].getText().replace(' points',''))
            if points>99:
                hn.append({'title':title,'link':href,'votes':points})

    return sort_stories_by_votes(hn)
#combine_links('https://news.ycombinator.com/news?p=')
list_news = create_custom_hacker_news(combine_links('https://news.ycombinator.com/news?p='),combine_subtext('https://news.ycombinator.com/news?p='))
pprint.pprint(list_news)
#print(list_news)
