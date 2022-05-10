from gettext import gettext
import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt")

# print(response.text.find('亞馬遜將為美國員工報銷墮胎和其它治療的差旅費'))

soup = BeautifulSoup(response.text, 'lxml')
# tilte = soup.find(
#    'span', {'class': 'lx-stream-post__header-text gs-u-align-middle'})
# print(tilte.getText())

tiltes = soup.find_all(
    'span', {'class': 'lx-stream-post__header-text gs-u-align-middle'})
# print(tiltes)

title_list = []
for title in tiltes:
    title_list.append(title.getText())
# print(title_list)


urls = soup.find_all(
    'a', {'class': 'qa-heading-link lx-stream-post__header-link'})
tags_list = []
for url in urls:
    #print('https://www.bbc.com' + url.get('href'))
    sub_response = requests.get('https://www.bbc.com' + url.get('href'))
    sub_soup = BeautifulSoup(sub_response.text, 'lxml')
    tags = sub_soup.find_all('li', {'class': 'bbc-1msyfg1 e1hq59l0'})
    for tag in tags:
        tags_list.append(tag.find('a').getText())

print(tags_list)
