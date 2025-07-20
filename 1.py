from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# 設定 Chrome 開啟視窗
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # 視窗最大化
# chrome_options.add_argument("--headless")  # 不要啟用 headless，就會開啟視窗

# 啟動 Chrome 瀏覽器
driver = webdriver.Chrome(options=chrome_options)

try:
    # 開啟網頁
    driver.get("https://linspace.somee.com/TPCToMap/?Branch=Miaoli")
    time.sleep(2)  # 等待頁面載入

    # 輸入桿號
    input_box = driver.find_element(By.ID, "txtInput")
    input_box.clear()
    input_box.send_keys("環保38")

    # 點擊查詢按鈕
    locate_btn = driver.find_element(By.ID, "btnLocate")
    locate_btn.click()

    time.sleep(3)  # 等待查詢結果顯示

    # 抓取經緯度
    lat_text = driver.find_element(By.ID, "lblLat").text.strip()
    lng_text = driver.find_element(By.ID, "lblLng").text.strip()

    print("抓到的經緯度：", lat_text, lng_text)

    # 轉換為 float
    lat = float(lat_text)
    lon = float(lng_text)
    print(f"十進位經緯度：{lat}, {lon}")

finally:
    driver.quit()
