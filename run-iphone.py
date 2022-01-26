from playwright.sync_api import Playwright, sync_playwright
from playwright_stealth import stealth_sync

import random 

def get_proxy():

    proxies = []
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_qZ3dpkhEnz-country-AT-autoReplace-True", "password": "1cc56099-7549-4fc9-8232-ea5bb7496d74", "port": "9000"})
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_qZ3dpkhEnz-country-DK-autoReplace-True", "password": "1cc56099-7549-4fc9-8232-ea5bb7496d74", "port": "9000"})
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_qZ3dpkhEnz-country-BE-autoReplace-True", "password": "1cc56099-7549-4fc9-8232-ea5bb7496d74", "port": "9000"})
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_qZ3dpkhEnz-country-NL-autoReplace-True", "password": "1cc56099-7549-4fc9-8232-ea5bb7496d74", "port": "9000"})
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_qZ3dpkhEnz-country-DE-autoReplace-True", "password": "1cc56099-7549-4fc9-8232-ea5bb7496d74", "port": "9000"})
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_qZ3dpkhEnz-country-US-autoReplace-True", "password": "1cc56099-7549-4fc9-8232-ea5bb7496d74", "port": "9000"})
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_qZ3dpkhEnz-country-CA-autoReplace-True", "password": "1cc56099-7549-4fc9-8232-ea5bb7496d74", "port": "9000"})


    return random.choice(proxies)
    

def run(playwright: Playwright) -> None:
    
    try:
        proxy = get_proxy()
        proxy_test = {"server": f"http://{proxy['ip']}:{proxy['port']}", "username": f"{proxy['username']}", "password": f"{proxy['password']}"}
        print(proxy_test)
        
        webkit = playwright.webkit
        iphone = playwright.devices["iPhone 12"]
        browser = webkit.launch(headless=False, proxy={"server": f"http://{proxy['ip']}:{proxy['port']}", "username": f"{proxy['username']}", "password": f"{proxy['password']}"})
        context = browser.new_context(**iphone)
        page = context.new_page()

        stealth_sync(page)
        # Go to https://coinmarketcap.com/
        page.route("**/*.svg", lambda route: route.abort()) 
        page.route("**/*.png", lambda route: route.abort()) 
        page.route("**/*.jpg", lambda route: route.abort())
        page.route("**/*.woff2", lambda route: route.abort())
        #page.route("**/inpage.js", lambda route: route.abort())
        
        entry_pages = ["https://coinmarketcap.com/newsletter/","https://coinmarketcap.com/newsletter/"]
        
        chosen_page = random.choice(entry_pages)
        print(chosen_page)
        page.goto(chosen_page, timeout=50000)
        page.click("#__next > div > div.main-content > div.bywovg-0.kuGegY > div:nth-child(2) > div > nav > div > div:nth-child(2) > svg") 
        # Click text=Search
        #page.click("#__next > div > div.main-content > div.bywovg-0.kuGegY > div:nth-child(1) > div > div.sc-111rrsy-0.qbrWo > div:nth-child(6) > div > div.sc-266vnq-1.gffsPR")
        #page.click("text=Search")
        # Fill [placeholder="What\ are\ you\ looking\ for\?"]
        page.fill("[placeholder=\"What\\ are\\ you\\ looking\\ for\\?\"]", "MANA\n")
        # Click text=Decentraland
        # with page.expect_navigation(url="https://coinmarketcap.com/currencies/decentraland/"):
        #with page.expect_navigation():
        page.click("text=Decentraland")
        # assert page.url == "https://coinmarketcap.com/currencies/decentraland/"
      
        page.evaluate(
            """
            var intervalID = setInterval(function () {
                scroll(0,4000);
            }, 200);

            """
        )
      
        # Click text=👍 Good
        page.click("text=👍 Good")
        # Click text=×
        page.click("text=×")
        # ---------------------
        context.close()
        browser.close()
        print("Completed job..")
    except Exception as e:
        print("Failed completing job..")
        context.close()
        browser.close()

with sync_playwright() as playwright:
    while True:
        run(playwright)
        run(playwright)
        run(playwright)
        run(playwright)
        
        