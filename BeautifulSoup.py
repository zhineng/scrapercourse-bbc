import requests
from bs4 import BeautifulSoup
"""
response = requests.get(
    "https://travel.ettoday.net/category/%E6%A1%83%E5%9C%92/")
soup = BeautifulSoup(response.text, 'html.parser')
#soup = BeautifulSoup(response.text, 'lxml')
# print(soup.prettify())
result = soup.find("h3")
result1 = soup.find_all('h3', itemprop="headline")
result2 = soup.find("div", itemprop="itemListElement")
tiltes = soup.find_all("p", class_="summary")
result3 = soup.find('h3', itemprop="headline")
previous_node = result3.find_previous_sibling('a')
# print(result2.select("a"))
# print(result1)
# print(result.select_one("a"))
"""
"""
print(previous_node)
tiltes1 = soup.find_all("h3", itemprop="headline")
# for title in tiltes1:
#    print(title.select_one("a"))

for title in tiltes1:
    print(title.select_one("a").get("href"))
for title in tiltes1:
    print(title.select_one("a").getText())

# print(tiltes1)
"""
"""

urls = soup.find_all('a', {'class': 'pic'})
# print(urls)
key_word = []
for url in urls:
    sub_response = requests.get(url.get('href'))
    sub_soup = BeautifulSoup(sub_response.text, 'lxml')
    tags = sub_soup.find_all('div', {'class': 'tag'})
    for tag in tags:
        key_word.append(tag.getText())
        # key_word.append(tag.find_all('a').get())
print(key_word)
"""

for page in range(1, 4):
    response = requests.get(
        f"https://travel.ettoday.net/category/%E6%A1%83%E5%9C%92/?&page={page}")
    soup = BeautifulSoup(response.text, 'html.parser')
    urls = soup.find_all('a', {'class': 'pic'})
    # print(urls)
    key_word = []
    for url in urls:
        sub_response = requests.get(url.get('href'))
        sub_soup = BeautifulSoup(sub_response.text, 'lxml')
        tags = sub_soup.find_all('div', {'class': 'tag'})
        for tag in tags:
        key_word.append(tag.getText())
    print(f"Page{page}")
    print(key_word)
