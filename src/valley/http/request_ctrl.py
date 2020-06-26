"""
urllib.request

REST
HTTPメソッドクライアントが行いたい処理をサーバーに伝える
GET    データ参照
POST   データ登録
PUT    データ更新
DELETE データ削除
"""
import urllib.request
import json

payload = {'key1': 'value1', 'key2': 'value2'}
url = ' http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
print(url)

# Get
with urllib.request.urlopen(url) as f:
    b = f.read()
    print(b)
    print(type(b))

    p = json.loads(b.decode('utf-8'))
    print(p)
    print(type(p))

# Post
payload = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(
    'http://httpbin.org/post', data=payload, method='POST')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

# Put
req = urllib.request.Request(
    'http://httpbin.org/put', data=payload, method='PUT')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

# Delete
req = urllib.request.Request(
    'http://httpbin.org/delete', data=payload, method='DELETE')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

"""
3rd Party Libraries
requests
"""
import requests
payload = {'key1': 'value1', 'key2': 'value2'}

get = requests.get('http://httpbin.org/get', params=payload, timeout=1)
#print(get.status_code)
#print(get.text)
print(get.json())

post = requests.post('http://httpbin.org/post', params=payload)
#print(post.status_code)
#print(post.text)
print(post.json())

put = requests.put('http://httpbin.org/put', params=payload)
#print(put.status_code)
#print(put.text)
print(put.json())

delete = requests.delete('http://httpbin.org/delete', params=payload)
#print(delete.status_code)
#print(delete.text)
print(delete.json())
