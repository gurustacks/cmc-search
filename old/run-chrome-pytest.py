
import pytest


def test_example_is_working(page):
    
    # Don't load images 
    page.route("**/*.svg", lambda route: route.abort()) 
    page.route("**/*.png", lambda route: route.abort()) 
    page.route("**/*.jpg", lambda route: route.abort())
    page.route("**/*.woff2", lambda route: route.abort())
    page.route("**/inpage.js", lambda route: route.abort())

    # Goto page
    page.goto("https://coinmarketcap.com/newsletter/")

    # Check if search field has loaded, click it and enter text. 
    $assert page.inner_text('#__next > div > div.main-content > div.bywovg-0.kuGegY > div:nth-child(1) > div > div.sc-111rrsy-0.qbrWo > div:nth-child(6) > div > div.sc-266vnq-1.gffsPR') == 'Search'
    page.click("text=Search")
    page.click("text=Search")
    
    page.fill("[placeholder=\"What\\ are\\ you\\ looking\\ for\\?\"]", "MANA\n")
    
    with page.expect_navigation(url="https://coinmarketcap.com/currencies/decentraland/"):
        page.click("text=Decentraland")
        assert page.url == "https://coinmarketcap.com/currencies/decentraland/"
        page.mouse.wheel(0,1000)
        page.click("text=👍 Good")