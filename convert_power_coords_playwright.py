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
            await page.fill('input[name="source"]', code)
            await page.click('input[value="轉換"]')
            await page.wait_for_timeout(1500)  # 等轉換結果出現

            lat = await page.input_value('input[name="dest_lat"]')
            lon = await page.input_value('input[name="dest_lon"]')
            print(f"{code} → 緯度: {lat}, 經度: {lon}")

        await browser.close()

asyncio.run(convert_coords())
