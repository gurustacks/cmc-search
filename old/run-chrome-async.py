import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import stealth_sync
import random 
    
async def main():
    async with async_playwright() as p:

        proxies = []
        proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_qZ3dpkhEnz-country-AT-autoReplace-True", "password": "1cc56099-7549-4fc9-8232-ea5bb7496d74", "port": "9000"})
        proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_qZ3dpkhEnz-country-DK-autoReplace-True", "password": "1cc56099-7549-4fc9-8232-ea5bb7496d74", "port": "9000"})
        proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_qZ3dpkhEnz-country-BE-autoReplace-True", "password": "1cc56099-7549-4fc9-8232-ea5bb7496d74", "port": "9000"})
        proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_qZ3dpkhEnz-country-NL-autoReplace-True", "password": "1cc56099-7549-4fc9-8232-ea5bb7496d74", "port": "9000"})
        proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_qZ3dpkhEnz-country-DE-autoReplace-True", "password": "1cc56099-7549-4fc9-8232-ea5bb7496d74", "port": "9000"})
        proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_qZ3dpkhEnz-country-US-autoReplace-True", "password": "1cc56099-7549-4fc9-8232-ea5bb7496d74", "port": "9000"})
        proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_qZ3dpkhEnz-country-CA-autoReplace-True", "password": "1cc56099-7549-4fc9-8232-ea5bb7496d74", "port": "9000"})

        proxy = random.choice(proxies)
        print(proxy)
        browser = await p.chromium.launch(headless=False, proxy={"server": f"http://{proxy['ip']}:{proxy['port']}", "username": f"{proxy['username']}", "password": f"{proxy['password']}"})
        page = await browser.new_page()
        #await stealth_sync(page)
        await page.route("**/*.svg", lambda route: route.abort()) 
        await page.route("**/*.png", lambda route: route.abort()) 
        await page.route("**/*.jpg", lambda route: route.abort())
        await page.route("**/*.woff2", lambda route: route.abort())
        await page.route("**/inpage.js", lambda route: route.abort())

        await page.goto("https://coinmarketcap.com/newsletter/")
        
        await page.click("text=Search")
        # Fill [placeholder="What\ are\ you\ looking\ for\?"]
        await page.fill("[placeholder=\"What\\ are\\ you\\ looking\\ for\\?\"]", "MANA\n")
        # Click text=Decentraland
        # with page.expect_navigation(url="https://coinmarketcap.com/currencies/decentraland/"):
        #with page.expect_navigation():
        await page.click("text=Decentraland")
        # assert page.url == "https://coinmarketcap.com/currencies/decentraland/"
        await page.mouse.wheel(0,1000)
        # Click text=👍 Good
        await page.click("text=👍 Good")
        # Click text=×
        await page.click("text=×")
        # ---------------------
        await browser.close()    
        print("Completed job..")



asyncio.run(main())