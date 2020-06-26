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
    item_number = 0
    price_list = []

    for item in items:
        title = item.select_one('.title').text.replace('\n', '')
        price = item.select_one('.important').text.replace('\n', '').replace(',', '').replace('円', '')
        price_list.append(price)
        print(item_number)
        print(title)
        print(price)
        item_number += 1
    
    selected_item_number = int(input("楽天:商品番号を選択してください\n"))
    selected_price = int(price_list[selected_item_number])
    # print(selected_price)
    return selected_price

def get_yahoo(keyword):
    url = f'https://shopping.yahoo.co.jp/search?p={keyword}&X=2&ship=on'
    response = requests.get(url)
    # print(response.text)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    items = soup.select('.LoopList__item')
    item_number = 0
    price_list = []

    for item in items:
        title = item.select_one('._2EW-04-9Eayr').text.replace('\n', '')
        price = item.select_one('._3-CgJZLU91dR').text.replace('\n', '').replace(',', '').replace('円', '')
        price_list.append(price)
        print(item_number)
        print(title)
        print(price)
        item_number += 1
    
    selected_item_number = int(input("Yahoo:商品番号を選択してください\n"))
    selected_price = int(price_list[selected_item_number])
    # print(selected_price)
    return selected_price



if __name__ == '__main__':
    keyword = input("比較したい商品を入力してください:\n")
    rakuten_price = int(get_rakuen(keyword))
    print(rakuten_price)

    yahoo_price = int(get_yahoo(keyword))
    print(yahoo_price)

    print(f'楽天: {rakuten_price}円\nYahoo: {yahoo_price}円')
    if yahoo_price > rakuten_price:
        print("Yahoo Product is Cheaper.")
    elif yahoo_price < rakuten_price:
        print("Rakuten Product is Cheaper.")
    else:
        print("Same Price.")
    # Pythonチュートリアル

