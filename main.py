from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType

from selenium_stealth import stealth
import time
import requests
from fake_useragent import UserAgent
from sys import platform
import multiprocessing

def get_proxy_server():
    url = "https://gimmeproxy.com/api/getProxy?protocol=sock4,socks5"
    response = requests.get(url)
    data = {
        "protocol": response.json()["protocol"],
        "proxy": response.json()["curl"],
    }    
    return data

def get_useragent():
    ua = UserAgent()
    useragent = ua.random
    return useragent


def start_session(a):
    """
    try:
        proxy_server = get_proxy_server()
        print(f"Proxy server: {proxy_server['proxy']}")
    except Exception as e:
        print("Error getting proxy server")
    """

    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    
    options.add_argument("--headless")
    
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    """
    prox = Proxy()
    prox.proxy_type = ProxyType.MANUAL
    prox.http_proxy = "lum-customer-c_b3d82549-zone-zone1:sjvnvvecnjol@zproxy.lum-superproxy.io:22225"
    #prox.socks_proxy = proxy_server['proxy']
    #if proxy_server['protocol'] == 'socks4':
    #    prox.socks_version = 4
    #elif proxy_server['protocol'] == 'socks5':
    #    prox.socks_version = 5     
    prox.ssl_proxy = "lum-customer-c_b3d82549-zone-zone1:sjvnvvecnjol@zproxy.lum-superproxy.io:22225"

    capabilities = webdriver.DesiredCapabilities.CHROME
    prox.add_to_capabilities(capabilities)
    """

    if platform == "linux" or platform == "linux2":
        ser = Service("./chromdriver_linux")
        driver = webdriver.Chrome(options=options, service=ser)
    elif platform == "darwin":          
        ser = Service("./chromedriver_mac")
        driver = webdriver.Chrome(options=options, service=ser)
    elif platform == "win32":             
        print("Windows.. not supported yet")
    
    try:
        useragent = get_useragent()
        print(f"Useragent: {useragent}")
    except Exception as e:
        print(f"Failed getting useragent with errror: {e}")

    try:    
        stealth(driver,
                user_agent=f"{useragent}",
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )

        url = "https://coinmarketcap.com/"
        
        print(f"Starting session with useragent: {useragent}")    
        driver.set_page_load_timeout(10)
        driver.get(url)
    except Exception as e:
        print(f"Failed starting session with error: {e}")
        driver.quit()
    
    try:
        search_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#__next > div > div.main-content > div.bywovg-0.kuGegY > div:nth-child(1) > div > div.sc-111rrsy-0.qbrWo > div:nth-child(6) > div > div.sc-266vnq-1.gffsPR")))
        search_element.click()
        search_field = driver.switch_to.active_element
        search_field.click()
        search_field.send_keys("M")
        time.sleep(1)
        search_field.send_keys("A")
        time.sleep(1)
        search_field.send_keys("N")
        time.sleep(1)
        search_field.send_keys("A")
        time.sleep(1)
        search_field.click()
        driver.switch_to.active_element.send_keys(Keys.ENTER)
        time.sleep(1)
        driver.quit()
    except Exception as e:
        print(f"Failed searching with error: {e}")
        driver.quit()

if __name__ == "__main__":
    
    while True:
        pool = multiprocessing.Pool()
        pool = multiprocessing.Pool(processes=5)
        inputs = [
            "A","B","C","D","E"
        ]
        outputs = pool.map(start_session, inputs)


