from email import header
import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}
try:
    response = requests.get(
        'https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt',
        headers=headers, timeout=5)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        title = soup.find(
            'span', {'class': 'lx-stream-post__header-text gs-u-align-middle'})

        if title:
            result = title.getText()
            print(result)
        else:
            print("Element Not Exist!!")

        result = title.getText()
    else:
        print("Status-Code Not 200!!")

except Exception as e:
    print(str(e))
