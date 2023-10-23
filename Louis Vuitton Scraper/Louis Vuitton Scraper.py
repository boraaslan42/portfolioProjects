import json
import time
import html
from bs4 import BeautifulSoup
import requests

pagination = 1
url = f"https://api.louisvuitton.com/eco-eu/search-merch-eapi/v1/eng-e1/plp/products/tfr7qdp?page={pagination}"

headers = {
    #to be filled
}

response = requests.get(url, headers=headers)

print(response.status_code)



lanCodeDict = {'Italian': 'ita-it', 'Japanese': 'jpn-jp', 'French': 'fra-fr', 'English': 'eng-e1',
               'Portuguese': 'por-br', 'German': 'deu-de', 'Arabic': 'ara-ae', 'Spanish': 'esp-es', 'Chinese': 'zhs-cn'}
nvprod3 = "nvprod4790010v"


def parseString(input_string):
    soup = BeautifulSoup(input_string, 'html.parser')
    cleaned_text = soup.get_text()
    cleaned_text = html.unescape(cleaned_text)
    cleaned_text = ' '.join(cleaned_text.split())
    return cleaned_text

def getProductDetails(nvprod, lanCode):
    genericurl = f"https://api.louisvuitton.com/eco-eu/catalog-lvcom/v1/{lanCode}/product/{nvprod}"
    headers = {
        #to be filled
    }
    response = requests.get(genericurl, headers=headers)
    json_data = json.loads(response.text)
    try:
        dimensionProperties = json_data["model"][0]
    except:
        print(json_data["errors"][0]["message"])
        return
    try:
        description = json_data["model"][0]["disambiguatingDescription"]
    except:
        description = json_data["errors"][0]["message"]
    print("Description: "+parseString(description))
    print("Width:", dimensionProperties["width"]["value"], dimensionProperties["width"]["unitText"], "Height:", dimensionProperties["height"]
          ["value"], dimensionProperties["height"]["unitText"], "Depth:", dimensionProperties["depth"]["value"], dimensionProperties["depth"]["unitText"])
    print("Other Details:")
    for prop in json_data["model"][0]["additionalProperty"]:
        if prop["name"] == "detailedDescription":
            soup = BeautifulSoup(prop["value"], "html.parser")
            for li in soup.find_all("li"):
                print(li.text)
            try:
                print("Last Detail:", soup.find("p").text)
            except:
                pass
    return


json_data = json.loads(response.text)
products = json_data["hits"]
productAmount = len(json_data["hits"])

for product in products:
    productCode = product["url"].split("-")[-1].split("/")[0]
    print("Scraping: "+productCode)
    for lanKey in lanCodeDict:
        lanCode = lanCodeDict[lanKey]
        print(lanKey)
        getProductDetails(productCode, lanCodeDict[lanKey])
        time.sleep(0.51)
        print("----------------------------------------------------")
    print("***********************************************************************************")
# code that saves product details one by one to excel NOT all of them at ONCE