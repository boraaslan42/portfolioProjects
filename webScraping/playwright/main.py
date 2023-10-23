from selectolax.parser import HTMLParser
from playwright.sync_api import sync_playwright

def extracthtml(url):
    url='https://www.usaspending.gov/agency/department-of-defense?fy=2023'
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        page=browser.new_page()
        page.goto(url)
        page.wait_for_load_state("networkidle",timeout=60000)
        page.wait_for_selector("div.visualization-section__data",timeout=60000)
        return page.inner_html("body")

    pass
def extractbudget(html):
    tree=HTMLParser(html)
    budget_div=tree.css_first("div.visualization-section__data")
    return budget_div.text()
    pass
print(extractbudget(extracthtml('https://www.usaspending.gov/agency/department-of-defense?fy=2023')))