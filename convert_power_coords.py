from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv

power_coords = [
    "G6898DA25",
    "G6898DA16",
    "G6898DA34"
]

# 🧩 指定 options
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.binary_location = "/usr/bin/chromium-browser"

# 🧩 使用已安裝的 chromium-chromedriver
service = Service("/usr/lib/chromium-browser/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

results = []

for coord in power_coords:
    driver.get("https://www.sunriver.com.tw/taiwanmap/grid_taipower_convert.php")
    time.sleep(1)

    input_box = driver.find_element(By.NAME, "source")
    input_box.clear()
    input_box.send_keys(coord)

    convert_button = driver.find_element(By.XPATH, '//input[@type="submit" and @value="轉換"]')
    convert_button.click()
    time.sleep(2)

    try:
        lat = driver.find_element(By.NAME, "dest_lat").get_attribute("value")
        lon = driver.find_element(By.NAME, "dest_lon").get_attribute("value")
        print(f"{coord} → 緯度: {lat}, 經度: {lon}")
        results.append([coord, lat, lon])
    except Exception as e:
        print(f"{coord} → 查詢失敗：{e}")
        results.append([coord, "錯誤", "錯誤"])

driver.quit()

with open("電力座標轉換結果.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["電力座標", "緯度(WGS84)", "經度(WGS84)"])
    writer.writerows(results)
