from gettext import gettext
import requests
from bs4 import BeautifulSoup

for page in range(1, 4):
    response = requests.get(
        f'https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt/page/{page}')

    soup = BeautifulSoup(response.text, 'lxml')

    titles = soup.find_all(
        'span', {'class': 'lx-stream-post__header-text gs-u-align-middle'})

    title_list = []
    for title in titles:
        title_list.append(title.getText())

    urls = soup.find_all(
        'a', {'class': 'qa-heading-link lx-stream-post__header-link'})
    tag_list = []
    for url in urls:
        sub_response = requests.get('https://www.bbc.com' + url.get('href'))
        sub_soup = BeautifulSoup(sub_response.text, 'lxml')
        tags = sub_soup.find_all('li', {'class': 'bbc-1msyfg1 e1hq59l0'})
        for tag in tags:
            tag_list.append(tag.getText())

    print(f'第{page}頁')
    print(title_list)
    print(tag_list)
