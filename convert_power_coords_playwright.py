import asyncio
from playwright.async_api import async_playwright

power_codes = [
    "G6898DA25",
    "G6898DA16",
    "G6898DA34"
]

async def convert_coords():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.sunriver.com.tw/taiwanmap/grid_taipower_convert.php")

        for code in power_codes:
            # 清除並輸入電力座標
            await page.fill("#source", code)
            # 點擊轉換按鈕
            await page.click("input[value='轉換']")

            # 等待轉換結果出現
            await page.wait_for_timeout(1000)  # 等一秒確保結果出現

            # 擷取轉換後經緯度
            result = await page.input_value("#dest")
            print(f"{code} → {result}")

        await browser.close()

asyncio.run(convert_coords())
