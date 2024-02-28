import requests
import json
import urllib
import pandas as pd
import pprint

link = 'https://www.zillow.com/search/GetSearchPageState.htm?'
# to get params go network>select api>headers>request payload>copy then paste
# >THEN TURN THE true to True false to False...
# rest is supposed to work fine but you know
# they hate scrapers whom liberates the data
params = {
    "wants": {"cat1": ["listResults"], "cat2": ["total"]}, 
    "requestId": 5,
    
    "searchQueryState" : {"pagination": {"currentPage": 1},"usersSearchTerm":"Dallas TX","mapBounds":{"west":-97.43455125097657,"east":-96.12031174902344,"south":32.431040510618146,"north":33.20313651601504},"regionSelection":[{"regionId":38128,"regionType":6}],"isMapVisible":"false","filterState":{"sortSelection":{"value":"globalrelevanceex"}},"isListVisible":"true"}
    
}





#first works
def get_totalPage(link, params):
    with requests.Session() as s:
        s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        s.headers["x-requested-session"] = "BE6D8DA620E60010D84B55EB18DC9DC8"
        s.headers["cookie"] = f"JSESSIONID={s.headers['x-requested-session']}"
    response = s.get(f"{link}{urllib.parse.urlencode(params)}")

    # Print the URL used for the request

    # Process the response data
    data = json.dumps(json.loads(response.content), indent=2)
    jsonData = json.loads(data)
    totalPage = jsonData["cat1"]["searchList"]["totalPages"]
    return totalPage

#second
def get_houses_perPage(link, params, pageNum):
    tmppageList=[]
    params["searchQueryState"]["pagination"]["currentPage"] = pageNum
    with requests.Session() as s:
        s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        s.headers["x-requested-session"] = "BE6D8DA620E60010D84B55EB18DC9DC8"
        s.headers["cookie"] = f"JSESSIONID={s.headers['x-requested-session']}"
    response = s.get(f"{link}{urllib.parse.urlencode(params)}")

    # Print the URL used for the request

    # Process the response data
    data = json.dumps(json.loads(response.content), indent=2)
    jsonData = json.loads(data)
    totalPage = jsonData["cat1"]["searchList"]["totalPages"]
    
    for house in jsonData["cat1"]["searchResults"]["listResults"]:
        tmppageList.append(get_Details(house["zpid"]))
    
    return totalPage

#third
import time
def get_Details(zpid):
    url = f"https://www.zillow.com/graphql/?extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2239561ee3168d472db98de0c5da7f57fd29fb76ed7840e064da6347f007d58f90%22%7D%7D&variables=%7B%22zpid%22%3A{zpid}%2C%22contactFormRenderParameter%22%3A%7B%22zpid%22%3A{zpid}%2C%22platform%22%3A%22desktop%22%2C%22isDoubleScroll%22%3Atrue%7D%2C%22skipCFRD%22%3Afalse%7D"

    payload = {}
    headers = {
        'authority': 'www.zillow.com',
        'accept': '*/*',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'client-id': 'for-sale-sub-app-browser-client',
        'content-type': 'application/json',
        'cookie': 'x-amz-continuous-deployment-state=AYABeMel6F34shE2U+uoJxVKYJcAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADHIdAf7ZNMOMZspzhAAwaPKe1Y0NsBOVEtgJJOK+Mn3knMRYPruXU6rkggkRBx+oSSVllPRf++vdWWg%2FSFFPAgAAAAAMAAQAAAAAAAAAAAAAAAAAAFhkTvmBZkLp01e%2FXlJJKcn%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAzht9umOLxb19t+0NJhSuU7jsXlj51Q3o4XPw8F; zguid=24|%242ee18300-f1c2-4c4c-894d-e95cdb5a8765; zgsession=1|34c3097e-3313-40f4-bc8b-dda201d247e0; zjs_anonymous_id=%222ee18300-f1c2-4c4c-894d-e95cdb5a8765%22; zjs_user_id=null; zg_anonymous_id=%22fba31dc9-7da4-465a-87f0-e352d42726c6%22; _gcl_au=1.1.1962137471.1691074681; DoubleClickSession=true; pxcts=47bbb743-39c1-11ee-a406-4c704d515a67; _pxvid=47bba73a-39c1-11ee-a406-69b061c9f9e6; JSESSIONID=81E99BD7B574C62C2B6996CAFF097408; x-amz-continuous-deployment-state=AYABeOobNKWMlqXk6Opv4KqHZ00APgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADIPw8Tz1c%2FJkcGJ0sQAw+rocAg2V+6AzJbuvD%2Fa4s+Ylx4br+E+wY2L6P6cJzA68%2Fqwb7RVmdfTZaPwT20EtAgAAAAAMAAQAAAAAAAAAAAAAAAAAANqit%2FMngxR65bjOjBYJVm%2F%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAx+hQx+vBn9U086grypTwjpTYN7VgMM3GdrUppTTwjpTYN7VgMM3GdrUppTTwjpTYN7VgMM3GdrUppTTwjpTYN7VgMM3GdrUppTTwjpTYN7VgMM3GdrUppT; search=6|1695876639229%7Crect%3D32.80386902766574%252C-96.68895721435547%252C32.70728894920813%252C-96.85323715209961%26rid%3D38128%26disp%3Dmap%26mdm%3Dauto%26sort%3Dpriorityscore%26listPriceActive%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%263dhome%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0938128%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Atrue%7D%09%09%09%09%09; AWSALB=UT3+qcYR3tHuczo/TbzN8YUy1B0/uBnd1W1eCwJmlP4fdIlrjUnSL0VikXGyr5hCjVRJPoZVqpN1joR4OVqQxhClYX9Jfm9NllqrJ5hEwtA5Zm73ARi0S8rV4i+E; AWSALBCORS=UT3+qcYR3tHuczo/TbzN8YUy1B0/uBnd1W1eCwJmlP4fdIlrjUnSL0VikXGyr5hCjVRJPoZVqpN1joR4OVqQxhClYX9Jfm9NllqrJ5hEwtA5Zm73ARi0S8rV4i+E; x-amz-continuous-deployment-state=AYABeIs8bDpDqQvTOLxmullpMEoAPgACAAFEAB1kM2Jsa2Q0azB3azlvai5jbG91ZGZyb250Lm5ldAABRwAVRzA3MjU1NjcyMVRZRFY4RDcyVlpWAAEAAkNEABpDb29raWUAAACAAAAADLqrfBR3ecBLDhYnbgAwZtZr8viUp3066btA1CybuVxFoUj3kYCq9JKc46gmzh47FTKYM4PIfZ5Vep1OqhhkAgAAAAAMAAQAAAAAAAAAAAAAAAAAANLcxYezdf26FjHJLrj9XDH%2F%2F%2F%2F%2FAAAAAQAAAAAAAAAAAAAAAQAAAAyIYroULD24T6PCx5cudKnJavjLoGK4W1ukGYks; AWSALB=CmB/8DLiDb1ycFVjeKynVX6F8ahPkMrM+ZR3RoL8wCsSAh1Xp7ELPH/319qgZl8Y6wzpbYkwg3cRX0ab6OvPb1Lew9o179ZvkT51W3UGGIqDdVAIJFOMMVCD3b9r; AWSALBCORS=CmB/8DLiDb1ycFVjeKynVX6F8ahPkMrM+ZR3RoL8wCsSAh1Xp7ELPH/319qgZl8Y6wzpbYkwg3cRX0ab6OvPb1Lew9o179ZvkT51W3UGGIqDdVAIJFOMMVCD3b9r',
        'referer': f'https://www.zillow.com/homedetails/4410-Baldwin-St-Dallas-TX-75210/{zpid}_zpid/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Opera GX";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0',
        }

    response = requests.request("GET", url, headers=headers, data=payload)

    json=response.json()
    try:
        print(zpid,json)
        listingInfo=json["data"]["property"]["attributionInfo"]
        del listingInfo['providerLogo']
        del listingInfo['trueStatus']
        time.sleep(1)
        return listingInfo
    except:
        print("fucking error for "+zpid)
        return
        



def store_toXlsx(dictionaryList,fileName):
    try:
        df_existing = pd.read_excel(fileName)
        print(fileName+" exists")
    except:
        print("File does not exist creating file: "+fileName)
        df_existing=None
    df_new = pd.DataFrame(dictionaryList)
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    with pd.ExcelWriter(fileName, engine='openpyxl') as writer:
        df_combined.to_excel(writer, index=False, sheet_name='Sheet')
    print("Data is added to", fileName)
    

import requests
import pprint

import json
import urllib
import pandas as pd
import pprint
import time

link = 'https://www.zillow.com/search/GetSearchPageState.htm?'
# to get params go network>select api>headers>request payload>copy then paste
# >THEN TURN THE true to True false to False...
# rest is supposed to work fine but you know
# they hate scrapers whom liberates the data
params = {
    "wants": {"cat1": ["listResults"], "cat2": ["total"]}, 
    "requestId": 5,
    
    "searchQueryState" : {"pagination": {"currentPage": 1},"usersSearchTerm":"Dallas TX","mapBounds":{"west":-97.43455125097657,"east":-96.12031174902344,"south":32.431040510618146,"north":33.20313651601504},"regionSelection":[{"regionId":38128,"regionType":6}],"isMapVisible":"false","filterState":{"sortSelection":{"value":"globalrelevanceex"}},"isListVisible":"true"}
    
}



def house_formatter(house):
    
    keyValues=[
    "addressStreet",
    "availabilityDate",
    "badgeInfo",
    'has3DModel',
    'hasAdditionalAttributions',
    "hasImage",
    'hasOpenHouse',
    'hasVideo',
    "unformattedPrice",
    'isFeaturedListing',
    'isHomeRec',
    'isSaved',
    'isShowcaseListing',
    'isUndisclosedAddress',
    'isUserClaimingOwner',
    'isUserConfirmedClaim',
    "countryCurrency"
    ]
    for keyValue in keyValues:
        try:
            del house[keyValue]
        except:
            pass


    try:
        house["area"]=str(house["area"])+" sqft"
    except:
        pass
    
    
    keysList=[
        "rentZestimate",
        "country",
        "taxAssessedValue",
        "daysOnZillow",
        "lotAreaUnit",
        "lotAreaValue"
    ]
    for key in keysList:
        try:
            house[key]=house["hdpData"]["homeInfo"][key]
        except:
            pass
    
    
    try:
        del house["hdpData"]#has a dict in it which has a lot data I picked important ones and deleted it
    except:
        pass
    
    
    #pprint.pprint(house)
    print(1,house)
    return house

#second
def getInfo_fromGeneralPage(link, params, pageNum):
    tmppageList=[]
    url = "https://www.zillow.com/async-create-search-page-state"

    payload = json.dumps({
    "searchQueryState": {
        "pagination": {
        "currentPage": 1
        },
        "isMapVisible": False,
        "mapBounds": {
        "west": -74.047237,
        "east": -73.910408,
        "south": 40.683935,
        "north": 40.877483
        },
        "usersSearchTerm": "Manhattan, New York, NY",
        "regionSelection": [
        {
            "regionId": 12530,
            "regionType": 17
        }
        ],
        "filterState": {
        "sortSelection": {
            "value": "days"
        },
        "isAllHomes": {
            "value": True
        }
        },
        "isListVisible": True
    },
    "wants": {
        "cat1": [
        "listResults"
        ],
        "cat2": [
        "total"
        ]
    },
    "requestId": 2,
    "isDebugRequest": False
    })
    headers = {
    'authority': 'www.zillow.com',
    'accept': '*/*',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'cookie': 'zguid=24|%242ee18300-f1c2-4c4c-894d-e95cdb5a8765; zjs_anonymous_id=%222ee18300-f1c2-4c4c-894d-e95cdb5a8765%22; zjs_user_id=null; zg_anonymous_id=%22fba31dc9-7da4-465a-87f0-e352d42726c6%22; _gcl_au=1.1.1962137471.1691074681; _pxvid=47bba73a-39c1-11ee-a406-69b061c9f9e6; zgsession=1|0cb6249a-6466-435e-b58d-774cd119cce2; DoubleClickSession=true; JSESSIONID=E5BFD6F1B5639A68480FD5ADD7FD51CF; AWSALB=QsZMTsyAnJWstI2zj95pO2lYw+KjMuVMQEI1EMdSF+j+Zzz+vspuz7UAnVs9Zm+cMGj5eWpHhm59npnzK6t4QhA/jB/eQpwD+tIlG79Wsg8Nk88/2kciPJTlK6/b; AWSALBCORS=QsZMTsyAnJWstI2zj95pO2lYw+KjMuVMQEI1EMdSF+j+Zzz+vspuz7UAnVs9Zm+cMGj5eWpHhm59npnzK6t4QhA/jB/eQpwD+tIlG79Wsg8Nk88/2kciPJTlK6/b; search=6|1700939183013%7Caddress%3DelementSelector.css.map%26rb%3DManhattan%252C-New-York%252C-NY%26rect%3D40.877483%252C-73.910408%252C40.683935%252C-74.047237%26disp%3Dmap%26mdm%3Dauto%26sort%3Ddays%26listPriceActive%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%263dhome%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0912530%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Atrue%7D%09%09%09%09%09; search=6|1700939295633%7Crect%3D40.877483%2C-73.910408%2C40.683935%2C-74.047237%26rid%3D12530%26disp%3Dmap%26mdm%3Dauto%26p%3D2%26sort%3Ddays%26z%3D1%26listPriceActive%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26commuteMode%3Ddriving%26commuteTimeOfDay%3Dnow%09%0912530%09%7B%22isList%22%3Atrue%2C%22isMap%22%3Afalse%7D%09%09%09%09%09; zguid=24|%24c485302e-8272-42fb-a3c7-e75fa41c1930',
    'origin': 'https://www.zillow.com',
    'referer': 'https://www.zillow.com/manhattan-new-york-ny/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22isMapVisible%22%3Afalse%2C%22mapBounds%22%3A%7B%22west%22%3A-74.047237%2C%22east%22%3A-73.910408%2C%22south%22%3A40.683935%2C%22north%22%3A40.877483%7D%2C%22usersSearchTerm%22%3A%22Manhattan%2C%20New%20York%2C%20NY%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12530%2C%22regionType%22%3A17%7D%5D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22days%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Opera GX";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0'
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    print(response.text)
    # Print the URL used for the request

    # Process the response data
    data = json.dumps(json.loads(response.content), indent=2)
    jsonData = json.loads(data)
    totalPage = jsonData["cat1"]["searchList"]["totalPages"]
    
    for house in jsonData["cat1"]["searchResults"]["listResults"][:30]:
        try:
            tmppageList.append(house_formatter(house))
            time.sleep(1)
        except:
            tmppageList.append(house_formatter(house))
        
            
    
    return [totalPage,tmppageList]

import pandas as pd

def store_toXlsx(dictionaryList,fileName):
    try:
        df_existing = pd.read_excel(fileName)
        print(fileName+" exists")
    except:
        print("File does not exist creating file: "+fileName)
        df_existing=None
    df_new = pd.DataFrame(dictionaryList)
    df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    with pd.ExcelWriter(fileName, engine='openpyxl') as writer:
        df_combined.to_excel(writer, index=False, sheet_name='Sheet')
    print("Data is added to", fileName)
    





print(31)


store_toXlsx(getInfo_fromGeneralPage(link, params, 1)[1],"ZillowExampleOutput3.xlsx")
