"""
requestsを使用して、https://diveintocode.jp/のページからすべてのリンクを取得するコードを作成してください。
"""

import requests
page = requests.get('https://diveintocode.jp/')
text = page.text

def get_link(text):
    href_number = text.find("href=")
    if href_number == -1:
        return None,0
    start_number = text.find('"', href_number)
    end_number = text.find('"', start_number + 1)
    url = text[start_number + 1:end_number]
    return url, end_number

while True:
    url, end_position = get_link(text)
    if url == None:
        break
    print(url, end_position)
    text = text[end_position:]
