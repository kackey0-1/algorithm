import json
import csv
import requests

KEYID = "***"
COUNT = 100
PREF = "Z011"
FREEWORD = "渋谷駅"
FORMAT = "json"

PARAMS = {
    "key": KEYID,
    "COUNT": COUNT,
    "large_area": PREF,
    "keyword": FREEWORD,
    "format": FORMAT
}


def write_data_to_csv(params):
    restaurants = []
    json_res = requests.get("http://webservice.recruit.co.jp/hotpepper/gourmet/v1/", params=params).text
    response = json.loads(json_res)
    if "error" in response["results"]:
        print(response)
        return print("エラーが発生しました")
    for restaurant in response["results"]:
        restaurant_name = restaurant["name"]
        restaurant.append(restaurant_name)

    with open("restaurants_list.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(restaurants)
        return print(restaurants)

if __name__ == '__main__':
    write_data_to_csv(PARAMS)

