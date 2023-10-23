from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
url = "https://store.steampowered.com/specials"
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)
    page.wait_for_load_state("networkidle")
    page.evaluate("window.scrollTo(0,document.body.scrollHeight)")
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_selector("div[class*='salepreviewwidgets_SaleItemBrowserRow']")
    html = page.inner_html("body")
    tree = HTMLParser(html)
    print(tree)
    divs = tree.css('div[class*="salepreviewwidgets_SaleItemBrowserRow"]')
    print(len(divs))
    for div in divs:
        attrs={
            "title":div.css_first('div[class*="StoreSaleWidgetTitle"]').text(),
            "thumbnail":div.css_first('img[class*=CapsuleImage]').attributes['src'],
            "tags":[a.text() for a in div.css('div[class*="StoreSaleWidgetTags"] > a')[:5]]
            
            
            
        }
        
        #print(tags[0].attributes)
