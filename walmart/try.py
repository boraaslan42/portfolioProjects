import requests
import json


def get_Data(url):
    headers = {
    'authority': 'www.walmart.com',
    'accept': 'application/json',
    'accept-language': 'en-US',
    'content-type': 'application/json',
    'cookie': 'ak_bmsc=9431135EA355DDF6856D6D504DB6A9A9~000000000000000000000000000000~YAAQ9bCvw1RWpxuLAQAAa1gVIBV+lCUOgl1Cmamxw/1z5XIaE31c8yg7hITiQ1siszNeTw5vGk2VyTcamcRgWHB4Qm4VWP3NesOXTGDxbuWtL8OICNuiyA4ps5xwUG1d2w+gDQeCPGOs++VEnrz6z91otoSdLUKEEBFtPJPlaP4IdNCpasflgzKl0w6IC6j9T5GSPD4VtyG2Ci+O/r1Oj6NN55L/bkxJz1E1OVKucuZdh+ouC3RPy9ZwYyvgKX1HEJ76jLMBJaysYv0+JsuOFfMveOTgHpTSfWibJe6CccaQLbfVj6VTPE5QAiYasQDEfng4y873mjWb1RhHGod92vcs03ExcwQI/cqOHmAxHGL8s+avI6U0vAURQ3BCsh3y2zXaW0lr6hNpayA=; TBV=7; auth=MTAyOTYyMDE4TfUXAYchyu%2BXGjowTS5YhDG4Xr05yPvg7MNpS9QoWmxzmQLXTbB54izK8vdgsIgvh%2BHD9ayXfIgovs4RO0efq9pchgc0apDqHoRBxOyYYzV5HNE8jl%2BIHBakSt6d2xyw767wuZloTfhm7Wk2KcjygkeeSCv4Chv5IarMOQ7pqjcvPfYVIEJPWc9SC6eeDtjwMzQc4guZ8USGYy213BmKBLyo5tEJYWGIo0vfJ73rEO0UMk70P8glgOEpLOprhDfMDCcb9mgycy9jtT1uIyOBHaQJIEe%2BEPexb0r2SSuNcnu0U2EDhxHa%2BGKwC63iYPMIAfq12sXqchtbUQ1eHSDmTAU8PgWddm49Bqlz0KfjEb9WucPQJVEU1mMEsfKR5NNFJCXt4jPYxTxFwqOI5nGEf0jyrOXbKKhH072NS%2FW0j%2FU%3D; ACID=7138ae68-fc06-4c00-8953-8924f55b04e8; hasACID=true; _m=9; locDataV3=eyJpc0RlZmF1bHRlZCI6dHJ1ZSwiaXNFeHBsaWNpdCI6ZmFsc2UsImludGVudCI6IlNISVBQSU5HIiwicGlja3VwIjpbeyJidUlkIjoiMCIsIm5vZGVJZCI6IjMwODEiLCJkaXNwbGF5TmFtZSI6IlNhY3JhbWVudG8gU3VwZXJjZW50ZXIiLCJub2RlVHlwZSI6IlNUT1JFIiwiYWRkcmVzcyI6eyJwb3N0YWxDb2RlIjoiOTU4MjkiLCJhZGRyZXNzTGluZTEiOiI4OTE1IEdlcmJlciBSb2FkIiwiY2l0eSI6IlNhY3JhbWVudG8iLCJzdGF0ZSI6IkNBIiwiY291bnRyeSI6IlVTIiwicG9zdGFsQ29kZTkiOiI5NTgyOS0wMDAwIn0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjozOC40ODI2NzcsImxvbmdpdHVkZSI6LTEyMS4zNjkwMjZ9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJodWJOb2RlSWQiOiIzMDgxIiwic3RvcmVIcnMiOiIwNjowMC0yMzowMCIsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIlBJQ0tVUF9DVVJCU0lERSIsIlBJQ0tVUF9JTlNUT1JFIl0sInNlbGVjdGlvblR5cGUiOiJERUZBVUxURUQifV0sInNoaXBwaW5nQWRkcmVzcyI6eyJsYXRpdHVkZSI6MzguNDgyNjc3LCJsb25naXR1ZGUiOi0xMjEuMzY5MDI2LCJwb3N0YWxDb2RlIjoiOTU4MjkiLCJjaXR5IjoiU2FjcmFtZW50byIsInN0YXRlIjoiQ0EiLCJjb3VudHJ5Q29kZSI6IlVTIiwibG9jYXRpb25BY2N1cmFjeSI6ImxvdyIsImdpZnRBZGRyZXNzIjpmYWxzZX0sImFzc29ydG1lbnQiOnsibm9kZUlkIjoiMzA4MSIsImRpc3BsYXlOYW1lIjoiU2FjcmFtZW50byBTdXBlcmNlbnRlciIsImludGVudCI6IlBJQ0tVUCJ9LCJpbnN0b3JlIjpmYWxzZSwiZGVsaXZlcnkiOnsiYnVJZCI6IjAiLCJub2RlSWQiOiIzMDgxIiwiZGlzcGxheU5hbWUiOiJTYWNyYW1lbnRvIFN1cGVyY2VudGVyIiwibm9kZVR5cGUiOiJTVE9SRSIsImFkZHJlc3MiOnsicG9zdGFsQ29kZSI6Ijk1ODI5IiwiYWRkcmVzc0xpbmUxIjoiODkxNSBHZXJiZXIgUm9hZCIsImNpdHkiOiJTYWNyYW1lbnRvIiwic3RhdGUiOiJDQSIsImNvdW50cnkiOiJVUyIsInBvc3RhbENvZGU5IjoiOTU4MjktMDAwMCJ9LCJnZW9Qb2ludCI6eyJsYXRpdHVkZSI6MzguNDgyNjc3LCJsb25naXR1ZGUiOi0xMjEuMzY5MDI2fSwiaXNHbGFzc0VuYWJsZWQiOnRydWUsInNjaGVkdWxlZEVuYWJsZWQiOnRydWUsInVuU2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwiYWNjZXNzUG9pbnRzIjpbeyJhY2Nlc3NUeXBlIjoiREVMSVZFUllfQUREUkVTUyJ9XSwiaHViTm9kZUlkIjoiMzA4MSIsImlzRXhwcmVzc0RlbGl2ZXJ5T25seSI6ZmFsc2UsInN1cHBvcnRlZEFjY2Vzc1R5cGVzIjpbIkRFTElWRVJZX0FERFJFU1MiXSwic2VsZWN0aW9uVHlwZSI6IkRFRkFVTFRFRCJ9LCJyZWZyZXNoQXQiOjE2OTcwNTM5NTMyNzIsInZhbGlkYXRlS2V5IjoicHJvZDp2Mjo3MTM4YWU2OC1mYzA2LTRjMDAtODk1My04OTI0ZjU1YjA0ZTgifQ%3D%3D; assortmentStoreId=3081; hasLocData=1; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjp0cnVlLCJwaWNrdXAiOnsibm9kZUlkIjoiMzA4MSIsInRpbWVzdGFtcCI6MTY5NzA1MDM1MzI2OCwic2VsZWN0aW9uVHlwZSI6IkRFRkFVTFRFRCJ9LCJzaGlwcGluZ0FkZHJlc3MiOnsidGltZXN0YW1wIjoxNjk3MDUwMzUzMjY4LCJ0eXBlIjoicGFydGlhbC1sb2NhdGlvbiIsImdpZnRBZGRyZXNzIjpmYWxzZSwicG9zdGFsQ29kZSI6Ijk1ODI5IiwiY2l0eSI6IlNhY3JhbWVudG8iLCJzdGF0ZSI6IkNBIiwiZGVsaXZlcnlTdG9yZUxpc3QiOlt7Im5vZGVJZCI6IjMwODEiLCJ0eXBlIjoiREVMSVZFUlkiLCJ0aW1lc3RhbXAiOjE2OTcwNTAzNTMyNjcsInNlbGVjdGlvblR5cGUiOiJERUZBVUxURUQiLCJzZWxlY3Rpb25Tb3VyY2UiOm51bGx9XX0sInBvc3RhbENvZGUiOnsidGltZXN0YW1wIjoxNjk3MDUwMzUzMjY4LCJiYXNlIjoiOTU4MjkifSwibXAiOltdLCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6NzEzOGFlNjgtZmMwNi00YzAwLTg5NTMtODkyNGY1NWIwNGU4In0%3D; abqme=true; vtc=Xo-Eld06usPjYJkrRQvIRo; bstc=Xo-Eld06usPjYJkrRQvIRo; mobileweb=0; xpth=x-o-mart%2BB2C~x-o-mverified%2Bfalse; xpa=-oUgG|0kBe-|4358O|7ouni|7qUrE|8rnmC|Ahrqe|Au6pf|BukPC|Cvn2u|DNWch|FExf7|KvYZX|MAdCO|O5h3M|PKm8U|PLRdE|QpMSg|QvVcb|R--ax|RYq-N|THB7r|UON2y|XBDLO|a7htt|gJJ0D|hpQTO|htn72|hzfx4|i3vYq|ibyjh|iwrL4|lEUOy|lIID5|pyVOq|qK3OG|rDWW0|rOMmq|rl7pi|yXP-R; exp-ck=-oUgG10kBe-14358O17ouni17qUrE18rnmC2Ahrqe2Au6pf1BukPC1Cvn2u1DNWch1FExf71KvYZX1MAdCO1O5h3M1PKm8U5QpMSg1RYq-N1UON2y1a7htt1gJJ0D1hpQTO1hzfx41ibyjh2lEUOy1lIID51rDWW02rOMmq3yXP-R1; _pxhd=b0954addceb08226b69999377c0fd40947aa082b5fc2cee8ebd4acd52c1203c7:562f9e22-6867-11ee-b9a5-4acf01189173; xptwj=qq:c375b5b0a68536af4327:xs9OH4zuzJ0eTBpjABIc1tNJTIr7Lj7y96eNXryRPvf/ZFi29KSux6sY9I1eyr2VIAb4NAJ8QWGfIUHPOBV9l9v3WXgsp15A0Jif91Rz896Ft3G/yI1/O4vm6Uk1HaVhJ+/tmcoQcNHTWdTSdTIvxaR+KMo=; bm_mi=CE7AA237B011A7FA832DD1EFEF22BF2D~YAAQ9bCvw/BWpxuLAQAAmmAVIBUVa7thsEXukFIcpnZP3u6f6uxyBzrCKBGUkFBaIM53O8EJ69K8gLo9x9n3ksoCPKAmeY5avnO+rXwCtm6gj/gaJcowJGB9wVzrZ7tXbUPfTHr7OQTBVMHuDI7QN23aZY3Ss84HIi0c+AU7F5aR6DpyMMDTYKT8ciOoMlIMhY0w6E0xot0VUfk4/3ErgNl9V4BZGI46EBIaTuKAbwa9v9UmLxNrdLHJ9IVJpxdgFX75nQGnUKNPrYeu+dMUr0Ihhc7NzHqLA/k48SHetbyvjWGJP0QAtrJdJFT8L5Hmgyd1PA54g2D6g430AquBNc6Q~1; _astc=46d533ed2aedc9bd207529b86e441464; xptc=assortmentStoreId%2B3081; adblocked=false; _pxvid=562f9e22-6867-11ee-b9a5-4acf01189173; pxcts=58f764ef-6867-11ee-a6b8-2c857a8a4079; xpm=1%2B1697050355%2BXo-Eld06usPjYJkrRQvIRo~%2B0; xptwg=2597736273:1067EF44B29FDC0:29855EB:ADDDA87D:7BD59402:F19EBE73:; TS012768cf=012aaf475040567a6971b271e13d3d5bce287e91d8a092b8d425135e122128d838b156942efcd2c44f037377f4d8c43d46d10a5409; TS01a90220=012aaf475040567a6971b271e13d3d5bce287e91d8a092b8d425135e122128d838b156942efcd2c44f037377f4d8c43d46d10a5409; TS2a5e0c5c027=0824e48b03ab20001f5361f7895cdff6f1dc409bbf4a5549591a494b380b6cc8feff72705832237a0819ac31611130003f6be0b2d54d82a008e50df3974edf1f13270972ccac19b4bf224b46003704e4734f2a43df9fb71b1fd32eeb89e95fcc; akavpau_p2=1697051521~id=4a6a0e3fad2d1c3aa5da9c0c7bb06a17; bm_sv=4EDE3E9C361738126118F1AD6DA13CF3~YAAQ97Cvw7izVfCKAQAAJQseIBV5D6ZELdTP6ZM2mjlB97ztvbZVhfjqTH+plr5hkpNFr0F9LFhfSL7sARF/ZtHdIiG44O/OxaPA/m9K5aM6+1B4Z9F3Ma6mkuSq3CSEp/Vx4LvbJCmYYGhZbYTL7fakJnbOdkryBEAeZ2qnNuuKk58AXtiBhPOrSVSKvNM3vWDxQ73jkYkiGJxdve+d85sPeCQsiVIm4CsNdUzjuoFZkqjMkDR6aEvgQjOiJVos8KA=~1; TS01a90220=0178545c90bc165ff31b1769e2f11ca2e2ec9c347e66bfd2d4e04f4059b700e82841470d7251db55766a690930af8068593d493040; bstc=Xo-Eld06usPjYJkrRQvIRo; com.wm.reflector="reflectorid:0000000000000000000000^@lastupd:1697050982000@firstcreate:1696959207150"; exp-ck=-oUgG10kBe-14358O17ouni17qUrE18rnmC2Ahrqe2Au6pf1BukPC1Cvn2u1DNWch1FExf71KvYZX1MAdCO1O5h3M1PKm8U5QpMSg1RYq-N1UON2y1a7htt1gJJ0D1hpQTO1hzfx41ibyjh2lEUOy1lIID51rDWW02rOMmq3yXP-R1; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjp0cnVlLCJwaWNrdXAiOnsibm9kZUlkIjoiMzA4MSIsInRpbWVzdGFtcCI6MTY5Njk1OTA4MzQwMywic2VsZWN0aW9uVHlwZSI6IkxTX1NFTEVDVEVEIn0sInNoaXBwaW5nQWRkcmVzcyI6eyJ0aW1lc3RhbXAiOjE2OTY5NTkwODM0MDMsInR5cGUiOiJwYXJ0aWFsLWxvY2F0aW9uIiwiZ2lmdEFkZHJlc3MiOmZhbHNlLCJwb3N0YWxDb2RlIjoiOTU4MjkiLCJjaXR5IjoiU2FjcmFtZW50byIsInN0YXRlIjoiQ0EiLCJkZWxpdmVyeVN0b3JlTGlzdCI6W3sibm9kZUlkIjoiMzA4MSIsInR5cGUiOiJERUxJVkVSWSIsInRpbWVzdGFtcCI6MTY5Njk1OTA4MzQwMSwic2VsZWN0aW9uVHlwZSI6IkRFRkFVTFRFRCIsInNlbGVjdGlvblNvdXJjZSI6bnVsbH1dfSwicG9zdGFsQ29kZSI6eyJ0aW1lc3RhbXAiOjE2OTY5NTkwODM0MDMsImJhc2UiOiI5NTgyOSJ9LCJtcCI6W10sInZhbGlkYXRlS2V5IjoicHJvZDp2MjplYjliNGVlMS1jZjQ4LTQ1ODMtYmZmYi1iYmE2OTQ4NmMzZjQifQ%3D%3D; mobileweb=0; vtc=Xo-Eld06usPjYJkrRQvIRo; xpa=-oUgG|0kBe-|4358O|7ouni|7qUrE|8rnmC|Ahrqe|Au6pf|BukPC|Cvn2u|DNWch|FExf7|KvYZX|MAdCO|O5h3M|PKm8U|PLRdE|QpMSg|QvVcb|R--ax|RYq-N|THB7r|UON2y|XBDLO|a7htt|gJJ0D|hpQTO|htn72|hzfx4|i3vYq|ibyjh|iwrL4|lEUOy|lIID5|pyVOq|qK3OG|rDWW0|rOMmq|rl7pi|yXP-R; xpm=1%2B1697050355%2BXo-Eld06usPjYJkrRQvIRo~%2B0; xptc=assortmentStoreId%2B3081; xpth=x-o-mart%2BB2C~x-o-mverified%2Bfalse; xptwg=2840090267:2444ABB2F4066C0:5BCA080:E72B6C05:F101EC95:33E513B9:; TS012768cf=0178545c90bc165ff31b1769e2f11ca2e2ec9c347e66bfd2d4e04f4059b700e82841470d7251db55766a690930af8068593d493040; TS2a5e0c5c027=0881c5dd0aab20000000de81b68bd3e320ee897e246f18aacdd28245bc4da44ac10a7bc9710d73fc08328821aa113000d6cce653de0d2829e384e8e6f866a47743dbcfe2183fb7fffb2b67e5b677d97a085c127b5ca5304709b925d6e6e1ae74; abqme=true; akavpau_p2=1697051582~id=478e6995027f0a7ce9a1afafa007076c',
    'device_profile_ref_id': 'ss1KuIoHWAyNe_AzX3wvvkOkGPOOPcMyZ6Nf',
    'downlink': '10',
    'dpr': '1.125',
    'referer': 'https://www.walmart.com/shop/deals/clearance?catId=1072864',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Opera GX";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-e3bad2660d6e050b45b55410fedde3f0-9f04f42f80910654-00',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0',
    'wm_mp': 'true',
    'wm_page_url': 'https://www.walmart.com/shop/deals/clearance?catId=1072864',
    'wm_qos.correlation_id': 'PwqzPHfk8VrHbjdOChUeUKsgsfFWn4VBJCfc',
    'x-apollo-operation-name': 'Deals',
    'x-enable-server-timing': '1',
    'x-latency-trace': '1',
    'x-o-bu': 'WALMART-US',
    'x-o-ccm': 'server',
    'x-o-correlation-id': 'PwqzPHfk8VrHbjdOChUeUKsgsfFWn4VBJCfc',
    'x-o-gql-query': 'query Deals',
    'x-o-mart': 'B2C',
    'x-o-platform': 'rweb',
    'x-o-platform-version': 'us-web-1.103.0-87a2c16c4c5876776387451e4538a9a5efe9bc24-1010',
    'x-o-segment': 'oaoh'
    }

    response = requests.get(url, headers=headers)
    json_data=json.loads(response.text)
    #print(json_data)
    if len(json_data["data"]["search"]["searchResult"]["itemStacks"][0]["itemsV2"])==0:
        print("No more data")
        return
    else:
        return json_data

def changePageNum(pageNum,url):
    import urllib.parse

    #url = "http://stackoverflow.com/search?q=question"
    url_parts = urllib.parse.urlparse(url)
    query = dict(urllib.parse.parse_qsl(url_parts.query))
    abc=json.loads(query["variables"])
    """print(abc)
    print(type(query["variables"]))


    print(type(query))
    """
    print("Old page number is: ",abc["page"])
    abc["page"]=pageNum
    abc["mosaicPage"]=pageNum
    abc["searchParams"]["page"]=pageNum
    abc["searchParams"]["mosaicPage"]=pageNum
    #print(abc["page"],abc["mosaicPage"],abc["searchParams"]["page"],abc["searchParams"]["mosaicPage"])

    #print(query["variables"])
    #print(abc)
    query["variables"]=json.dumps(abc)
    #print(query["variables"])


    querynew = dict(urllib.parse.parse_qsl(url_parts.query))

    query["variables"]=json.dumps(abc)
    new_url = url_parts._replace(query=urllib.parse.urlencode(query)).geturl()
    #print(new_url==url)
    return new_url


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
    
import openpyxl
import pandas as pd

# Load the Excel file
def adjustColumnWidth(file_path):
    workbook = openpyxl.load_workbook(file_path)

    # Select the first sheet (you can change the sheet name if needed)
    sheet = workbook.active

    # Iterate through columns and adjust the width based on the length of the first item
    for column in sheet.columns:
        column_letter = openpyxl.utils.get_column_letter(column[0].column)  # Get the column letter
        first_cell = column[0]  # Get the first cell in the column
        if first_cell.value == "Tags":
            print("31111111111111111111111111111111")
            sheet.column_dimensions[column_letter].width = 25
        else:            
            # Set the column width based on the length of the first item
            adjusted_width = len(str(first_cell.value)) + 2  # Add a little extra space
            sheet.column_dimensions[column_letter].width = adjusted_width

    # Save the modified workbook
    workbook.save(file_path)




def main_function(filename,url):

    for i in range(1,10):
        url=changePageNum(i,url)
        responseJson=get_Data(url)
        if responseJson==None:
            break
        
        products=responseJson["data"]["search"]["searchResult"]["itemStacks"][0]["itemsV2"]
        data_dictList=[]


        for product in products:
            try:
                tags=[]
                for badge in product["badges"]["tags"]:
                    if badge["text"]=="Save with":
                        badge["text"]="Save with W+"
                    tags.append(badge["text"])
                data_dict={
                "Product Title":product["name"],
                
                "Picture":product["imageInfo"]["thumbnailUrl"],
                "Average Rating":product["averageRating"],
                "Number of Reviews":product["numberOfReviews"],
                "Tags":', '.join(tags)
                }
                try:
                    data_dict["Current Price"]=product["priceInfo"]["currentPrice"]["priceString"]
                except Exception as m:
                        print(2,m)
                data_dictList.append(data_dict)
            except Exception:
                pass
        
        store_toXlsx(data_dictList,filename)
        adjustColumnWidth(filename)


def changeUrlParameters(pageNum,catId,url):
    import urllib.parse
    url_parts = urllib.parse.urlparse(url)
    query = dict(urllib.parse.parse_qsl(url_parts.query))
    abc=json.loads(query["variables"])
    abc["page"]=pageNum
    abc["mosaicPage"]=pageNum
    abc["searchParams"]["page"]=pageNum
    abc["searchParams"]["mosaicPage"]=pageNum
    abc["catId"]=catId
    query["variables"]=json.dumps(abc)
    query["variables"]=json.dumps(abc)
    new_url = url_parts._replace(query=urllib.parse.urlencode(query)).geturl()
    return new_url


catIds={
    "Home Improvement":"1072864",
    "Beauty":"1085666",
    "Cell Phones":"1105910",
    "Household Essentials":"1115193",
    "Video Games":"2636",
    "Party & Occasions":"2637",
    "Jewelry & Watches":"3891",
    "Electronics":"3944",
    "Home":"4044",
    "Movies & TV Shows":"4096",
    "Sports & Outdoors":"4125",
    "Toys":"4171",
    "Photo Center":"4174",
    "Baby":"5426",
    "Patio & Garden":"5428",
    "Clothing, Shoes & Accessories":"5438",
    "Pets": "5440",
    "Auto & Tires":"91083",
    "Health and Medicine":"976760",
    "Shop by Seller":"3625709",
    "Arts, Crafts & Sewing":"1334134",
    "Industrial & Scientific":"6197502",
    "Character Shop":"5939293",
    "Shop by Brand":"3734780",
    "Shop by Video Game":"5324366",
    "Services":"6163033",
    "Personal Care":"1005862",
    "Office Supplies":"1229749",
    "Shop by TV Show":"5984018",
    "Collectibles":"5967908",
    "Featured Brands":"14503",
    "Shop by Movie":"5920738",
}
"""
catId = "5920738"  # Replace with the new catId value
string=f"https://www.walmart.com/orchestra/snb/graphql/Deals/7836e259269834397500dcfbdbd36bec9f2ec7dabc270bb7b4dd106ae218bead/deals?variables=%7B%22id%22%3A+%22%22%2C+%22dealsId%22%3A+%22deals%2Fclearance%22%2C+%22page%22%3A+2%2C+%22mosaicPage%22%3A+2%2C+%22prg%22%3A+%22desktop%22%2C+%22facet%22%3A+%22%22%2C+%22catId%22%3A+%225920738%22%2C+%22seoPath%22%3A+%22%2Fshop%2Fdeals%2Fclearance%3FcatId%3D{catId}%22%2C+%22ps%22%3A+40%2C+%22ptss%22%3A+%22%22%2C+%22trsp%22%3A+%22%22%2C+%22min_price%22%3A+%22%22%2C+%22max_price%22%3A+%22%22%2C+%22sort%22%3A+%22best_match%22%2C+%22beShelfId%22%3A+%22%22%2C+%22recall_set%22%3A+%22%22%2C+%22module_search%22%3A+%22%22%2C+%22storeSlotBooked%22%3A+%22%22%2C+%22additionalQueryParams%22%3A+%7B%22isMoreOptionsTileEnabled%22%3A+true%7D%2C+%22searchParams%22%3A+%7B%22id%22%3A+%22%22%2C+%22dealsId%22%3A+%22deals%2Fclearance%22%2C+%22query%22%3A+%22%22%2C+%22page%22%3A+2%2C+%22mosaicPage%22%3A+2%2C+%22prg%22%3A+%22desktop%22%2C+%22facet%22%3A+%22%22%2C+%22catId%22%3A+%22{catId}%22%2C+%22seoPath%22%3A+%22%2Fshop%2Fdeals%2Fclearance%3FcatId%3D{catId}%22%2C+%22ps%22%3A+40%2C+%22ptss%22%3A+%22%22%2C+%22trsp%22%3A+%22%22%2C+%22min_price%22%3A+%22%22%2C+%22max_price%22%3A+%22%22%2C+%22sort%22%3A+%22best_match%22%2C+%22beShelfId%22%3A+%22%22%2C+%22recall_set%22%3A+%22%22%2C+%22module_search%22%3A+%22%22%2C+%22storeSlotBooked%22%3A+%22%22%2C+%22additionalQueryParams%22%3A+%7B%22isMoreOptionsTileEnabled%22%3A+true%7D%2C+%22cat_id%22%3A+%22{catId}%22%2C+%22_be_shelf_id%22%3A+%22%22%2C+%22pageType%22%3A+%22DealsPage%22%7D%2C+%22query%22%3A+null%2C+%22pageType%22%3A+%22DealsPage%22%2C+%22fetchSkyline%22%3A+true%2C+%22enablePortableFacets%22%3A+true%2C+%22enableFacetCount%22%3A+true%2C+%22tenant%22%3A+%22WM_GLASS%22%7D"

"""
import time

for catId in catIds:
    catIdVar=catIds[catId]
    string=f"https://www.walmart.com/orchestra/snb/graphql/Deals/7836e259269834397500dcfbdbd36bec9f2ec7dabc270bb7b4dd106ae218bead/deals?variables=%7B%22id%22%3A+%22%22%2C+%22dealsId%22%3A+%22deals%2Fclearance%22%2C+%22page%22%3A+2%2C+%22mosaicPage%22%3A+2%2C+%22prg%22%3A+%22desktop%22%2C+%22facet%22%3A+%22%22%2C+%22catId%22%3A+%225920738%22%2C+%22seoPath%22%3A+%22%2Fshop%2Fdeals%2Fclearance%3FcatId%3D{catIdVar}%22%2C+%22ps%22%3A+40%2C+%22ptss%22%3A+%22%22%2C+%22trsp%22%3A+%22%22%2C+%22min_price%22%3A+%22%22%2C+%22max_price%22%3A+%22%22%2C+%22sort%22%3A+%22best_match%22%2C+%22beShelfId%22%3A+%22%22%2C+%22recall_set%22%3A+%22%22%2C+%22module_search%22%3A+%22%22%2C+%22storeSlotBooked%22%3A+%22%22%2C+%22additionalQueryParams%22%3A+%7B%22isMoreOptionsTileEnabled%22%3A+true%7D%2C+%22searchParams%22%3A+%7B%22id%22%3A+%22%22%2C+%22dealsId%22%3A+%22deals%2Fclearance%22%2C+%22query%22%3A+%22%22%2C+%22page%22%3A+2%2C+%22mosaicPage%22%3A+2%2C+%22prg%22%3A+%22desktop%22%2C+%22facet%22%3A+%22%22%2C+%22catId%22%3A+%22{catIdVar}%22%2C+%22seoPath%22%3A+%22%2Fshop%2Fdeals%2Fclearance%3FcatId%3D{catIdVar}%22%2C+%22ps%22%3A+40%2C+%22ptss%22%3A+%22%22%2C+%22trsp%22%3A+%22%22%2C+%22min_price%22%3A+%22%22%2C+%22max_price%22%3A+%22%22%2C+%22sort%22%3A+%22best_match%22%2C+%22beShelfId%22%3A+%22%22%2C+%22recall_set%22%3A+%22%22%2C+%22module_search%22%3A+%22%22%2C+%22storeSlotBooked%22%3A+%22%22%2C+%22additionalQueryParams%22%3A+%7B%22isMoreOptionsTileEnabled%22%3A+true%7D%2C+%22cat_id%22%3A+%22{catIdVar}%22%2C+%22_be_shelf_id%22%3A+%22%22%2C+%22pageType%22%3A+%22DealsPage%22%7D%2C+%22query%22%3A+null%2C+%22pageType%22%3A+%22DealsPage%22%2C+%22fetchSkyline%22%3A+true%2C+%22enablePortableFacets%22%3A+true%2C+%22enableFacetCount%22%3A+true%2C+%22tenant%22%3A+%22WM_GLASS%22%7D"
    print(catIds[catId],catId,string)
    main_function("Clearence - "+catId+" .xlsx",string)
    time.sleep(5)
#main_function("Walmart.xlsx",string)