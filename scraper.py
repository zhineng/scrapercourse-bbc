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
print(title_list)
