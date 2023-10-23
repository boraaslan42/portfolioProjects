import json
import urllib.parse
import requests

# All the raw data houses will be stored in this list as dictionary for each house
list_of_houses = []

##test link 'https://www.zillow.com/fresno-ca/?searchQueryState=%7B"pagination"%3A%7B%7D%2C"mapBounds"%3A%7B"west"%3A-133.49237243636992%2C"east"%3A-112.46454040511992%2C"south"%3A28.37382409248204%2C"north"%3A40.45682514253177%7D%2C"usersSearchTerm"%3A"undefined"%2C"customRegionId"%3A"403c964d6cX1-CR1hydev9d6b7wl_1c5d8q"%2C"mapZoom"%3A6%2C"regionSelection"%3A%5B%7B"regionId"%3A18203%2C"regionType"%3A6%7D%5D%2C"isMapVisible"%3Atrue%2C"filterState"%3A%7B"price"%3A%7B"min"%3A200000%7D%2C"fore"%3A%7B"value"%3Afalse%7D%2C"mp"%3A%7B"min"%3A1061%7D%2C"ah"%3A%7B"value"%3Atrue%7D%2C"sort"%3A%7B"value"%3A"days"%7D%2C"auc"%3A%7B"value"%3Afalse%7D%2C"nc"%3A%7B"value"%3Afalse%7D%7D%2C"isListVisible"%3Atrue%7D'


# -test-data-test-data-test-data-test-data-test-data-test-data-test-data-test-data-test-data-test-data
link = 'https://www.zillow.com/search/GetSearchPageState.htm?'
# to get params go network>select api>headers>request payload>copy then paste
# >THEN TURN THE true to True false to False...
# rest is supposed to work fine but you know
# they hate scrapers whom liberates the data
params = {
    "searchQueryState": {"pagination": {"currentPage": 1}, "mapBounds": {"west": -122.30005082666425, "east": -117.04309281885175, "south": 36.23111367681714, "north": 37.3964765262027}, "usersSearchTerm": "undefined", "customRegionId": "403c964d6cX1-CR1hydev9d6b7wl_1c5d8q", "mapZoom": 8, "isMapVisible": "true", "filterState": {"price": {"min": 200000}, "isForSaleForeclosure": {"value": "false"}, "monthlyPayment": {"min": 1061}, "isAllHomes": {"value": "true"}, "sortSelection": {"value": "days"}, "isAuction": {"value": "false"}, "isNewConstruction": {"value": "false"}}, "isListVisible": "true"}, "wants": {"cat1": ["listResults", "mapResults"], "cat2": ["total"]}, "requestId": 12
}
# -test-data-test-data-test-data-test-data-test-data-test-data-test-data-test-data-test-data-test-data



def get_houses_perPage(link, params, pageNum, list_of_houses=list_of_houses):

    params["searchQueryState"]["pagination"]["currentPage"] = pageNum

    with requests.Session() as s:
        s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        s.headers["x-requested-session"] = "BE6D8DA620E60010D84B55EB18DC9DC8"
        s.headers["cookie"] = f"JSESSIONID={s.headers['x-requested-session']}"
        data = json.dumps(
            json.loads(
                s.get(f"{link}{urllib.parse.urlencode(params)}").content),
            indent=2
        )

    jsonData = json.loads(data)

    totalPage = jsonData["cat1"]["searchList"]["totalPages"]

    # contains houses and dicts
    wanted = jsonData["cat1"]["searchResults"]["listResults"]
    list_of_houses += (wanted)
    return totalPage, wanted

def get_all_houses(link, params, list_of_houses=list_of_houses):
    totalPage = get_houses_perPage(link, params, 1)[0]
    for pageNum in range(2, totalPage+1):
        print("Scraping continues total num of houses for now is:",len(list_of_houses))
        get_houses_perPage(link, params, pageNum)
    print("Scraping ended total num of houses in search is:",len(list_of_houses))


get_all_houses(link, params)