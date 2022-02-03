
from re import L
import pytest
from playwright.sync_api import BrowserType, Browser, BrowserContext
from typing import Dict, Generator
import random 
import requests
import json 

def get_useragent(browser,os):
    
    if browser == 'chrome':
        
        ua = {'windows10': ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
                            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
                            'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'],
              'macos': ['Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'],
              'linux': ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'],
              'ios': ['Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/98.0.4758.85 Mobile/15E148 Safari/604.1', 
                      'Mozilla/5.0 (iPad; CPU OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/98.0.4758.85 Mobile/15E148 Safari/604.1', 
                      'Mozilla/5.0 (iPod; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/98.0.4758.85 Mobile/15E148 Safari/604.1'],
              'android': ['Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36',
                          'Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36',
                          'Mozilla/5.0 (Linux; Android 10; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36',
                          'Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36',
                          'Mozilla/5.0 (Linux; Android 10; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36',
                          'Mozilla/5.0 (Linux; Android 10; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36',
                          'Mozilla/5.0 (Linux; Android 10; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36',
                          'Mozilla/5.0 (Linux; Android 10; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Mobile Safari/537.36']
             }
        
        return random.choice(ua[os])
    
    if browser == 'firefox':

        ua = {'windows10': ['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0'],
              'macos': ['Mozilla/5.0 (Macintosh; Intel Mac OS X 12.2; rv:96.0) Gecko/20100101 Firefox/96.0'],
              'linux': ['Mozilla/5.0 (X11; Linux i686; rv:96.0) Gecko/20100101 Firefox/96.0',
                        'Mozilla/5.0 (Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0',
                        'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:96.0) Gecko/20100101 Firefox/96.0'],
              'ios': ['Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/96.0 Mobile/15E148 Safari/605.1.15',
                      'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/96.0 Mobile/15E148 Safari/605.1.15',
                      ''],
              'android': ['Mozilla/5.0 (Android 12; Mobile; rv:68.0) Gecko/68.0 Firefox/96.0',
                          'Mozilla/5.0 (Android 12; Mobile; LG-M255; rv:96.0) Gecko/96.0 Firefox/96.0']
             }

        return random.choice(ua[os])

    if browser == 'webkit':

        ua = {'macos': ['Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15'],
              'ios': ['Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 Safari/604.1',
                      'Mozilla/5.0 (iPad; CPU OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 Safari/604.1']
             }

        return random.choice(ua[os])



@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):

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

    devices = ['iPhone 11 Pro',
               'iPhone 12',
               'iPhone 13 Pro Max',
               'iPad Pro 11',
               'iPad (gen 7)',
               'Galaxy Note II']
    
    proxy =  random.choice(proxies)
    device = playwright.devices[random.choice(devices)]

    return {
        **browser_context_args,
        **device,
        "proxy": {"server": f"http://{proxy['ip']}:{proxy['port']}", "username": f"{proxy['username']}", "password": f"{proxy['password']}"}
    }

def test_search_for_coin(page):
    
    # Don't load images 
    page.route("**/*.svg", lambda route: route.abort()) 
    page.route("**/*.png", lambda route: route.abort()) 
    page.route("**/*.jpg", lambda route: route.abort())
    page.route("**/*.woff2", lambda route: route.abort())
    page.route("**/inpage.js", lambda route: route.abort())
    page.route("facebook.com", lambda route: route.abort())
    page.route("google.com", lambda route: route.abort())
    page.route("googletagmanager.com", lambda route: route.abort())
    page.route("jsdelivr.net", lambda route: route.abort())
    page.route("sensors.binance.cloud", lambda route: route.abort())

   
    # Goto page
    page.goto("https://coinmarketcap.com/newsletter", wait_until="domcontentloaded")

    # Check if search field has loaded, click it and enter text. 
    #assert page.inner_text('#__next > div > div.main-content > div.bywovg-0.kuGegY > div:nth-child(1) > div > div.sc-111rrsy-0.qbrWo > div:nth-child(6) > div > div.sc-266vnq-1.gffsPR') == 'Search'

    page.click("#__next > div > div.main-content > div.bywovg-0.kuGegY > div:nth-child(2) > div > nav > div > div:nth-child(2) > svg")
    page.click("[placeholder=\"What\\ are\\ you\\ looking\\ for\\?\"]")
    page.keyboard.press("M")
    page.wait_for_timeout(500)
    page.keyboard.press("A")
    page.wait_for_timeout(500)
    page.keyboard.press("N")
    page.wait_for_timeout(500)
    page.keyboard.press("A")
    page.wait_for_timeout(500)
    page.keyboard.press("Enter")
    
    
    page.wait_for_url("https://coinmarketcap.com/currencies/decentraland/", wait_until="domcontentloaded")
    
    page.evaluate(
        """
        var intervalID = setInterval(function () {
            scroll(0,1100);
        }, 200);

        """
    )
    page.click("text=👍 Good")

def test_search_for_coin1(page):
    
    # Don't load images 
    page.route("**/*.svg", lambda route: route.abort()) 
    page.route("**/*.png", lambda route: route.abort()) 
    page.route("**/*.jpg", lambda route: route.abort())
    page.route("**/*.woff2", lambda route: route.abort())
    page.route("**/inpage.js", lambda route: route.abort())
    page.route("facebook.com", lambda route: route.abort())
    page.route("google.com", lambda route: route.abort())
    page.route("googletagmanager.com", lambda route: route.abort())
    page.route("jsdelivr.net", lambda route: route.abort())
    page.route("sensors.binance.cloud", lambda route: route.abort())

   
    # Goto page
    page.goto("https://coinmarketcap.com/newsletter", wait_until="domcontentloaded")

    # Check if search field has loaded, click it and enter text. 
    #assert page.inner_text('#__next > div > div.main-content > div.bywovg-0.kuGegY > div:nth-child(1) > div > div.sc-111rrsy-0.qbrWo > div:nth-child(6) > div > div.sc-266vnq-1.gffsPR') == 'Search'

    page.click("#__next > div > div.main-content > div.bywovg-0.kuGegY > div:nth-child(2) > div > nav > div > div:nth-child(2) > svg")
    page.click("[placeholder=\"What\\ are\\ you\\ looking\\ for\\?\"]")
    page.keyboard.press("M")
    page.wait_for_timeout(500)
    page.keyboard.press("A")
    page.wait_for_timeout(500)
    page.keyboard.press("N")
    page.wait_for_timeout(500)
    page.keyboard.press("A")
    page.wait_for_timeout(500)
    page.keyboard.press("Enter")
    
    
    page.wait_for_url("https://coinmarketcap.com/currencies/decentraland/", wait_until="domcontentloaded")
    
    page.evaluate(
        """
        var intervalID = setInterval(function () {
            scroll(0,1250);
        }, 200);

        """
    )
    page.click("text=👍 Good")

def test_search_for_coin2(page):
    
    # Don't load images 
    page.route("**/*.svg", lambda route: route.abort()) 
    page.route("**/*.png", lambda route: route.abort()) 
    page.route("**/*.jpg", lambda route: route.abort())
    page.route("**/*.woff2", lambda route: route.abort())
    page.route("**/inpage.js", lambda route: route.abort())
    page.route("facebook.com", lambda route: route.abort())
    page.route("google.com", lambda route: route.abort())
    page.route("googletagmanager.com", lambda route: route.abort())
    page.route("jsdelivr.net", lambda route: route.abort())
    page.route("sensors.binance.cloud", lambda route: route.abort())

   
    # Goto page
    page.goto("https://coinmarketcap.com/newsletter", wait_until="domcontentloaded")

    # Check if search field has loaded, click it and enter text. 
    #assert page.inner_text('#__next > div > div.main-content > div.bywovg-0.kuGegY > div:nth-child(1) > div > div.sc-111rrsy-0.qbrWo > div:nth-child(6) > div > div.sc-266vnq-1.gffsPR') == 'Search'

    page.click("#__next > div > div.main-content > div.bywovg-0.kuGegY > div:nth-child(2) > div > nav > div > div:nth-child(2) > svg")
    page.click("[placeholder=\"What\\ are\\ you\\ looking\\ for\\?\"]")
    page.keyboard.press("M")
    page.wait_for_timeout(500)
    page.keyboard.press("A")
    page.wait_for_timeout(500)
    page.keyboard.press("N")
    page.wait_for_timeout(500)
    page.keyboard.press("A")
    page.wait_for_timeout(500)
    page.keyboard.press("Enter")
    
    
    page.wait_for_url("https://coinmarketcap.com/currencies/decentraland/", wait_until="domcontentloaded")
    
    height = page.context.viewport.height

    page.evaluate(
        """
        var intervalID = setInterval(function () {
            document.querySelector("#__next > div.bywovg-1.fUzJes > div.main-content > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div.sc-16r8icm-0.jKrmxw.container > div > div.sc-16r8icm-0.sc-19zk94m-5.bsBMhQ > div > div.pqmllm-2.hLrBVF > button:nth-child(1)").scrollIntoView();
        }, 200);
        """
    )
    page.wait_for_timeout(5000)
    page.click("text=👍 Good")