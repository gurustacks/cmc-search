
from re import L
import pytest
from playwright.sync_api import BrowserType, Browser, BrowserContext
from typing import Dict, Generator
import random 
import requests
import json 

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):

    proxies = []
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_VNZbfxQtdH-country-AT-autoReplace-True", "password": "b4bf3a63-7ed2-4b2d-ae4d-37f42628e65b", "port": "9000"})
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_VNZbfxQtdH-country-DK-autoReplace-True", "password": "b4bf3a63-7ed2-4b2d-ae4d-37f42628e65b", "port": "9000"})
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_VNZbfxQtdH-country-BE-autoReplace-True", "password": "b4bf3a63-7ed2-4b2d-ae4d-37f42628e65b", "port": "9000"})
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_VNZbfxQtdH-country-NL-autoReplace-True", "password": "b4bf3a63-7ed2-4b2d-ae4d-37f42628e65b", "port": "9000"})
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_VNZbfxQtdH-country-DE-autoReplace-True", "password": "b4bf3a63-7ed2-4b2d-ae4d-37f42628e65b", "port": "9000"})
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_VNZbfxQtdH-country-US-autoReplace-True", "password": "b4bf3a63-7ed2-4b2d-ae4d-37f42628e65b", "port": "9000"})
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_VNZbfxQtdH-country-CA-autoReplace-True", "password": "b4bf3a63-7ed2-4b2d-ae4d-37f42628e65b", "port": "9000"})
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_VNZbfxQtdH-country-UK-autoReplace-True", "password": "b4bf3a63-7ed2-4b2d-ae4d-37f42628e65b", "port": "9000"})
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_VNZbfxQtdH-country-SE-autoReplace-True", "password": "b4bf3a63-7ed2-4b2d-ae4d-37f42628e65b", "port": "9000"})
    proxies.append({"ip": "rotating-residential.geonode.com", "username": "geonode_VNZbfxQtdH-country-FR-autoReplace-True", "password": "b4bf3a63-7ed2-4b2d-ae4d-37f42628e65b", "port": "9000"})

    proxy =  random.choice(proxies)

    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        "proxy": {"server": f"http://{proxy['ip']}:{proxy['port']}", "username": f"{proxy['username']}", "password": f"{proxy['password']}"}
        
    }


def get_useragent(browser):
    
    if browser == 'chrome':
        
        ua = {'windows10': '',
              'windows11': '',
              'macos': '',
              'linux': '',
              'ios': '',
              'android': []}
    
    if browser == 'firfox':
        pass

    if browser == 'webkit':
        pass



def test_search_for_coin1(page):
    
    # Don't load images 
    page.route("**/*.svg", lambda route: route.abort()) 
    page.route("**/*.png", lambda route: route.abort()) 
    page.route("**/*.jpg", lambda route: route.abort())
    page.route("**/*.woff2", lambda route: route.abort())
    page.route("**/inpage.js", lambda route: route.abort())

    # Goto page
    page.goto("https://coinmarketcap.com/newsletter")
    page.wait_for_timeout(5000)
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
