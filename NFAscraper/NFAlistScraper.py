import os
import pandas as pd
import json
import requests

## Written by Bora Aslan 24.08.2023 ##
## To reach me: https://www.linkedin.com/in/boraaslan42/ ##
## How to run: Create a folder/directory for NFA_list - Bora Aslan.py ##
## Put the script in the folder/directory ##
## Run the script from cmd, powershell or IDE ##
## The script will create .json files for each letter ##
## Then it will create .xlsx files for each letter ##
## It is pretty normal for script to run for long times! ##
## Code makes all alphabet search ##


def get_amount_of_letter_firm(letter):

    import requests

    url = "https://www.nfa.futures.org/BasicNet/basic-api/DataHandlerSearch.ashx"

    payload = f'{{"id":1,"method":"getFirmSearchResults","params":["{letter}",{{"pageIndex":0,"pageSize":1,"totalPages":0,"totalCount":0,"sort":[{{"active":true,"column":"FIRM_NAME","direction":"asc","ctrl":"sort_firm_name"}}],"filters":{{"memStatus":"","regTypes":"","regActions":""}},"filterOptions":{{"memStatus":null,"regTypes":null,"regActions":null}}}}]}}'

    
    headers = {
    'Accept': '*/*',
    'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    'Cookie': '_gid=GA1.2.1212311205.1692805935; ASPSESSIONIDCGRDTBAA=LGOPIBIDCHIDOBGFJHBJFLBB; _ga=GA1.2.1077463657.1692805935; _ga_F4CP43X86F=GS1.1.1692862244.1.1.1692862500.60.0.0; MY_WEB_SESSION=7ce2a3d9603532deb03c42ec1ef7e3894c0926ea4a0fece9723863fa88d7bffe569edabb; _gat_UA-60683221-1=1; MY_WEB_SESSION=7ce2a3d9603532deb03c42ec1ef7e3894c0926ea4a0fece9723863fa88d7bffe569edabb',
    'Origin': 'https://www.nfa.futures.org',
    'Referer': 'https://www.nfa.futures.org/BasicNet/basic-search-results.aspx?rnd=4198.642395707837',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'X-JSON-RPC': 'getFirmSearchResults',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.request("POST", url, headers=headers, data=payload)


        
    
    data=response.json()
    letterFirmAmount=data["result"]["result"]["result"]["options"]["totalCount"]



    return letterFirmAmount
def get_letter_firmsJson(letter,letterFirmAmount):
    import requests

    url = "https://www.nfa.futures.org/BasicNet/basic-api/DataHandlerSearch.ashx"

    payload = f'{{"id":1,"method":"getFirmSearchResults","params":["{letter}",{{"pageIndex":0,"pageSize":{letterFirmAmount},"totalPages":0,"totalCount":0,"sort":[{{"active":true,"column":"FIRM_NAME","direction":"asc","ctrl":"sort_firm_name"}}],"filters":{{"memStatus":"","regTypes":"","regActions":""}},"filterOptions":{{"memStatus":null,"regTypes":null,"regActions":null}}}}]}}'
    headers = {
    'Accept': '*/*',
    'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    'Cookie': '_gid=GA1.2.1212311205.1692805935; ASPSESSIONIDCGRDTBAA=LGOPIBIDCHIDOBGFJHBJFLBB; _ga=GA1.2.1077463657.1692805935; _ga_F4CP43X86F=GS1.1.1692862244.1.1.1692862500.60.0.0; MY_WEB_SESSION=7ce2a3d9603532deb03c42ec1ef7e3894c0926ea4a0fece9723863fa88d7bffe569edabb; _gat_UA-60683221-1=1; MY_WEB_SESSION=7ce2a3d9603532deb03c42ec1ef7e3894c0926ea4a0fece9723863fa88d7bffe569edabb',
    'Origin': 'https://www.nfa.futures.org',
    'Referer': 'https://www.nfa.futures.org/BasicNet/basic-search-results.aspx?rnd=4198.642395707837',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'X-JSON-RPC': 'getFirmSearchResults',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()
def alphabet_jsons_collector(letter):
    print('Collection of the JSON data of letter "{}" has been started.'.format(letter))
    letterFirmAmount=get_amount_of_letter_firm(letter)

    data=get_letter_firmsJson(letter,letterFirmAmount)
    
    file_path = f"{letter}.json"
    # Open the file in write mode and save the JSON data
    with open(file_path, "w") as json_file:
        json.dump(data, json_file)

    print('JSON data of letter "{}" has been saved to'.format(letter), file_path)
def process_letter_json(letter):
    file_path = f'{letter}.json'

    with open(file_path, 'r',encoding="utf8") as json_file:
        data = json.load(json_file)

    firms=data["result"]["result"]["result"]["rows"]

    firm_list=[]
    length=len(firms)


    for index,firm in enumerate(firms):
        try:
            if firm["PROCESSED_MEMBERSHIP_STATUS"] == "NFA Member Approved" or firm["CURRENT_MEMBERSHIP_STATUS"] == "Pending NFA Member":
                if 'Commodity Trading Advisor' in firm['CURRENT_REG_TYPES']:
                        FIRM_NAME =firm["FIRM_NAME"]
                        NAME=get_phoneNname(firm['ENTITY_ID_decrypted'])[0]
                        PHONE_NUM=get_phoneNname(firm['ENTITY_ID_decrypted'])[1]
                        firm_list.append([FIRM_NAME,NAME,PHONE_NUM])
                        print(FIRM_NAME,NAME,PHONE_NUM,index,"/",length)
        except:
            continue
    return firm_list
def get_phoneNname(nfaid):
    purl = "https://www.nfa.futures.org/BasicNet/basic-api/DataHandler.ashx"

    phonepayload = f"{{\"id\":4,\"method\":\"getVitals\",\"params\":[\"{nfaid}\",\"address\"]}}"

    phoneheaders = {
    'Accept': '*/*',
    'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    'Origin': 'https://www.nfa.futures.org',
    'Referer': 'https://www.nfa.futures.org/BasicNet/basic-profile.aspx?nfaid=MAMjWCuuFSc%3D',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'X-JSON-RPC': 'getVitals',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
    }

    phoneresponse = requests.request("POST", purl, headers=phoneheaders, data=phonepayload)


    url = "https://www.nfa.futures.org/BasicNet/basic-api/DataHandler.ashx"

    payload = "{{\"id\":18,\"method\":\"getPrincipals\",\"params\":[\"{}\"]}}".format(nfaid)

    headers = {
    'Accept': '*/*',
    'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    'Origin': 'https://www.nfa.futures.org',
    'Referer': 'https://www.nfa.futures.org/BasicNet/basic-profile.aspx?nfaid=MAMjWCuuFSc%3D',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'X-JSON-RPC': 'getPrincipals',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    name=(response.json()["result"]["result"][0]["NAME"])
    phoneNum=phoneresponse.json()["result"]["result"][0]["PHONE_NUM"]
    return name,phoneNum                    
def save_toExcel(letter,firm_list):
    df = pd.DataFrame(firm_list, columns=['Company', 'Name', 'Contact'])

    excel_file_path = f'{letter}.xlsx'

    df.to_excel(excel_file_path, index=False, engine='openpyxl')

    print(f"DataFrame of letter {letter} has been saved to Excel successfully.")

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def alphabet_search():
    print("Alphabet search has been started.")
    for letter in alphabet:
        try:
            alphabet_jsons_collector(letter)
        except:
            print("Error occured while collecting JSON data of letter {}".format(letter))


    files = os.listdir()

    json_files = [file for file in files if file.endswith(".json")]

    for file in json_files:
        if file.endswith(".json"):
            letter=file.split(".")[0]
            print("Processing data of", file,)
            data=process_letter_json(letter)
            save_toExcel(letter,data)
        

def specific_letter_search(letter):
        print("Specific search has been started.")
        try:
            alphabet_jsons_collector(letter)
        except:
            print("Error occured while collecting JSON data of letter {}".format(letter))

        print(f"Processing specific data of {letter}.json")
        data=process_letter_json(letter)
        save_toExcel(letter,data)
        return

## example of specific letter search just remove the ## from the line below and run the script ##
## specific_letter_search("m")

alphabet_search()