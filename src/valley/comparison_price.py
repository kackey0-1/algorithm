import requests
from bs4 import BeautifulSoup

def get_rakuen(keyword):
    url = f'https://search.rakuten.co.jp/search/mall/{keyword}?f=2&s=2'
    response = requests.get(url)
    # print(response.text)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)
    items = soup.select('.searchresultitem')
    item_number = 1
    price_list = []

    for item in items:
        title = item.select_one('.title').text.replace('\n', '')
        price = item.select_one('.important').text.replace('\n', '')
        price_list.append(price)
        print(item_number)
        print(title)
        print(price)
        item_number += 1
    
    selected_item_number = int(input("楽天:商品番号を選択してください\n"))
    selected_price = int(price_list[selected_item_number-1][:-1].replace(',', ''))
    print(selected_price)

if __name__ == '__main__':
    keyword = input("比較したい商品を入力してください:\n")
    get_rakuen(keyword)