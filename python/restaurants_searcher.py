#restaurants_searcher.py

import json
import csv
import requests

# 初期設定
KEYID = "7223d528317cd05c5157c7e5ed75dd48"
HIT_PER_PAGE = 100
PREF = "PREF13"
FREEWORD_CONDITION = 1
FREEWORD = "少路駅"

#パラメータ設定
PARAMS = {"keyid": KEYID, "hit_per_page":HIT_PER_PAGE, "pref":PREF, "freeword_condition":FREEWORD_CONDITION, "freeword":FREEWORD}

def write_data_to_csv(params):
    restaurants = [["名称","住所","営業日","電話番号"]]
    json_res = requests.get("https://api.gnavi.co.jp/RestSearchAPI/v3/", params=params).text
    response = json.loads(json_res)
    if "error" in response:
        return print("エラーが発生しました！")
    for restaurant in response["rest"]:
        rest_info = [restaurant["name"], restaurant["address"], restaurant["opentime"], restaurant["tel"]]
        restaurants.append(rest_info)
    with open("restaurants_list.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(restaurants)
    return print(restaurants)

write_data_to_csv(PARAMS)