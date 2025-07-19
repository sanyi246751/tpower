from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# 設定 Chrome 不開啟視窗（可改成True開視窗方便debug）
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

try:
    # 1. 開啟頁面
    driver.get("https://linspace.somee.com/TPCToMap/?Branch=Miaoli")

    time.sleep(2)  # 等待網頁載入

    # 2. 找到輸入框，輸入桿號
    input_box = driver.find_element(By.ID, "txtInput")
    input_box.clear()
    input_box.send_keys("環保38")

    # 3. 找到按鈕並點擊
    btn = driver.find_element(By.ID, "btnLocate")
    btn.click()

    time.sleep(3)  # 等待查詢結果出現

    # 4. 找到經緯度文字
    # 經緯度出現在 <h1> 裡面，class="DUwDvf lfPIob"
    h1_elem = driver.find_element(By.CSS_SELECTOR, "h1.DUwDvf.lfPIob")
    coord_text = h1_elem.text.strip()

    print("抓到的經緯度座標：", coord_text)
    
    # 如果需要轉成十進位數字，也可以用下面的方式：
    # ex: 24°22'50.9"N 120°44'02.8"E
    import re

    def dms_to_decimal(dms_str):
        # 解析格式如 24°22'50.9"N
        parts = re.findall(r"(\d+)°(\d+)'([\d.]+)\"?([NSEW])", dms_str)
        if not parts:
            return None
        deg, minute, second, direction = parts[0]
        dec = float(deg) + float(minute)/60 + float(second)/3600
        if direction in ['S', 'W']:
            dec = -dec
        return dec

    lat_str, lon_str = coord_text.split(" ")
    lat = dms_to_decimal(lat_str)
    lon = dms_to_decimal(lon_str)

    print(f"十進位經緯度：{lat}, {lon}")

finally:
    driver.quit()
