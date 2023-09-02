import requests
import json
import urllib
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
    json["data"]["property"]["zpid"]
    listingInfo=json["data"]["property"]["attributionInfo"]
    address=json["data"]["property"]["address"]

    print(listingInfo["agentName"],listingInfo["agentLicenseNumber"],listingInfo["brokerPhoneNumber"],"\n"+listingInfo["brokerName"]+"Address:",address["streetAddress"],address["city"],address["state"],address["zipcode"]+"\n")
    
    return




def get_houses_perPage(link, params, pageNum):

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
        get_Details(house["zpid"])
    
    return totalPage

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

for page in range(1, get_totalPage(link, params)+1):
    print(f"Page {page}")
    get_houses_perPage(link, params, page)

#sometime I need to make this code to save itself to a excel file
#other than that It looks completish to me





