
import pytest
from playwright.sync_api import BrowserType, Browser, BrowserContext
from typing import Dict, Generator
import random 

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):

    proxies = []
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_qZ3dpkhEnz-country-AT-autoReplace-True", "password": "1cc56099-7549-4fc9-8232-ea5bb7496d74", "port": "9000"})
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_qZ3dpkhEnz-country-DK-autoReplace-True", "password": "1cc56099-7549-4fc9-8232-ea5bb7496d74", "port": "9000"})
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_qZ3dpkhEnz-country-BE-autoReplace-True", "password": "1cc56099-7549-4fc9-8232-ea5bb7496d74", "port": "9000"})
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_qZ3dpkhEnz-country-NL-autoReplace-True", "password": "1cc56099-7549-4fc9-8232-ea5bb7496d74", "port": "9000"})
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_qZ3dpkhEnz-country-DE-autoReplace-True", "password": "1cc56099-7549-4fc9-8232-ea5bb7496d74", "port": "9000"})
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_qZ3dpkhEnz-country-US-autoReplace-True", "password": "1cc56099-7549-4fc9-8232-ea5bb7496d74", "port": "9000"})
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_qZ3dpkhEnz-country-CA-autoReplace-True", "password": "1cc56099-7549-4fc9-8232-ea5bb7496d74", "port": "9000"})
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_qZ3dpkhEnz-country-UK-autoReplace-True", "password": "1cc56099-7549-4fc9-8232-ea5bb7496d74", "port": "9000"})
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_qZ3dpkhEnz-country-SE-autoReplace-True", "password": "1cc56099-7549-4fc9-8232-ea5bb7496d74", "port": "9000"})
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_qZ3dpkhEnz-country-FR-autoReplace-True", "password": "1cc56099-7549-4fc9-8232-ea5bb7496d74", "port": "9000"})

    proxy =  random.choice(proxies)

    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        "proxy": {"server": f"http://{proxy['ip']}:{proxy['port']}", "username": f"{proxy['username']}", "password": f"{proxy['password']}"}
        
    }


def test_search_for_coin1(page):
    
    # Don't load images 
    page.route("**/*.svg", lambda route: route.abort()) 
    page.route("**/*.png", lambda route: route.abort()) 
    page.route("**/*.jpg", lambda route: route.abort())
    page.route("**/*.woff2", lambda route: route.abort())
    page.route("**/inpage.js", lambda route: route.abort())

    # Goto page
    page.goto("https://ipinfo.io/json")
    page.wait_for_timeout(10000)
    """"
    # Check if search field has loaded, click it and enter text. 
    #assert page.inner_text('#__next > div > div.main-content > div.bywovg-0.kuGegY > div:nth-child(1) > div > div.sc-111rrsy-0.qbrWo > div:nth-child(6) > div > div.sc-266vnq-1.gffsPR') == 'Search'
    page.click("text=Search")
    
    page.fill("[placeholder=\"What\\ are\\ you\\ looking\\ for\\?\"]", "MANA\n")
    
    with page.expect_navigation(url="https://coinmarketcap.com/currencies/decentraland/"):
        page.click("text=Decentraland")
        assert page.url == "https://coinmarketcap.com/currencies/decentraland/"
        page.mouse.wheel(0,1000)
        page.click("text=👍 Good")
    """

def test_search_for_coin2(page):
    
    # Don't load images 
    page.route("**/*.svg", lambda route: route.abort()) 
    page.route("**/*.png", lambda route: route.abort()) 
    page.route("**/*.jpg", lambda route: route.abort())
    page.route("**/*.woff2", lambda route: route.abort())
    page.route("**/inpage.js", lambda route: route.abort())

    # Goto page
    page.goto("https://ipinfo.io/json")
    page.wait_for_timeout(10000)
    """"
    # Check if search field has loaded, click it and enter text. 
    #assert page.inner_text('#__next > div > div.main-content > div.bywovg-0.kuGegY > div:nth-child(1) > div > div.sc-111rrsy-0.qbrWo > div:nth-child(6) > div > div.sc-266vnq-1.gffsPR') == 'Search'
    page.click("text=Search")
    
    page.fill("[placeholder=\"What\\ are\\ you\\ looking\\ for\\?\"]", "MANA\n")
    
    with page.expect_navigation(url="https://coinmarketcap.com/currencies/decentraland/"):
        page.click("text=Decentraland")
        assert page.url == "https://coinmarketcap.com/currencies/decentraland/"
        page.mouse.wheel(0,1000)
        page.click("text=👍 Good")
    """
