import requests
from bs4 import BeautifulSoup
import csv

power_coords = [
    "G6898DA25",
    "G6898DA16",
    "G6898DA34"
]

url = "https://www.sunriver.com.tw/taiwanmap/grid_taipower_convert.php"

results = []

for coord in power_coords:
    payload = {
        "source": coord,
        "method": "轉換"
    }
    response = requests.post(url, data=payload)
    soup = BeautifulSoup(response.text, "html.parser")

    try:
        lat = soup.find("input", {"name": "dest_lat"})["value"]
        lon = soup.find("input", {"name": "dest_lon"})["value"]
        print(f"{coord} → 緯度: {lat}, 經度: {lon}")
        results.append([coord, lat, lon])
    except Exception as e:
        print(f"{coord} → 查詢失敗：{e}")
        results.append([coord, "錯誤", "錯誤"])

with open("電力座標轉換結果.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["電力座標", "緯度(WGS84)", "經度(WGS84)"])
    writer.writerows(results)
