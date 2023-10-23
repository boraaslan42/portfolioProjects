import requests
from bs4 import BeautifulSoup
import pandas as pd

# Written By Bora Aslan

file_path = 'rera.xlsx'

try:
    primeDf = pd.read_excel(file_path)
    print("File found, continuing")
except Exception as e:
    print("No such file as", file_path,"creating new file")
    primeDf = pd.DataFrame()



def find_unsavedProjects():
    projectList=[]
    url = "http://rera.wb.gov.in/district_project.php?dcode=0"
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'PHPSESSID=2rtual9m4mqum0mh40eulev5sb',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }
    print("Project data is requested from website")
    response = requests.request("GET", url, headers=headers)
    if response.status_code!=200:
        print("ERROR OCCURED")
        return
    else:
        print("Project data is recieved continuing")

    soup=BeautifulSoup(response.text,'html.parser')

    projects=soup.find("table",id="projectDataTable").find("tbody").find_all("tr")
    print("Total project amount in website:",len(projects))
    print("Saved project amount in database:",len(primeDf))
    
    try:
        primeDf["project_id"].values
    except:
        for project in projects:
            "http://rera.wb.gov.in/project_details.php?procode=14424000000007"
            link="http://rera.wb.gov.in/"+project.find_all("td")[2].a["href"]
            registrationDate=project.find_all("td")[-1].text
            projectID=project.find_all("td")[1].text
            projectList.append([link,registrationDate,projectID])
    else:
        for project in projects:
            link="http://rera.wb.gov.in/"+project.find_all("td")[2].a["href"]
            registrationDate=project.find_all("td")[-1].text
            projectID=project.find_all("td")[1].text

            if projectID not in primeDf["project_id"].values:
                projectList.append([link,registrationDate,projectID])

            

    print("Unsaved project amount in website:",len(projectList))
    return projectList


def create_dict_for_project(listt):
    print("Sending request to",listt[0])

    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'PHPSESSID=f36r9t3i88e4a1uaumj8u179tm',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", listt[0], headers=headers)
    soup=BeautifulSoup(response.text,'html.parser')
    p_tag = soup.find_all('p')
    div_elements = soup.find(
        "div", class_="col-sm-3 col-md-6 col-lg-4").p.find_all('div', class_='lead')
    texts = [div.get_text(strip=True) for div in div_elements]

    try:
        consultantString = ""
        table=soup.find_all("table", id="agentDataTable")[1].find("tbody")
        consultants=table.find_all("tr")

        for consultant in consultants:
            consultantString+=consultant.find_all("td")[1].text.strip()+" - "+consultant.find_all("td")[-1].text.strip()+" / "
    except:
        consultantString = None
    
    project_dict = {
        "project_name": soup.h2.text,
        "project_id": listt[2],
        "project_type": p_tag[1].b.text.strip(),
        "project_status":  soup.find("ul", class_="outerrera").li.text.split("-")[1].strip(),
        "location": ' '.join(soup.find("h5", style="text-transform: capitalize;").stripped_strings),
        "consultants": consultantString[:-2],
        "promoter_details": soup.find("span", class_="text-primary").text+" "+' '.join(texts),
        "mechanical_parking": p_tag[6].b.text,
        "covered_car_parking": p_tag[5].b.text,
        "basement_parking ": p_tag[4].b.text,
        "registration_date": listt[1],#?
        "completion_date": soup.find("ul", class_="outerrera").find_all("li")[2].text.split(" ")[-1],
        "email_id": None,  
        "website": None, 
        "land_area": p_tag[1].b.text.strip(), 
        "number of apartmens":None
    }
    if p_tag[2].b:
        project_dict["website"] = p_tag[2].b.text
    try:
        if soup.find_all("div",style="float:left;",class_="col-md-3")[3].find_all("span")[-1].text.strip():
            project_dict["number of apartmens"] = soup.find_all("div",style="float:left;",class_="col-md-3")[3].find_all("span")[-1].text.strip()
    except:
        pass


    try:
        for info in soup.find_all("table", id="agentDataTable")[2].find("tbody").tr.find_all("td"):
            if "@" in info.text:
                project_dict["email_id"] = info.text
    except:
        pass



    print("Completed ")
    return project_dict

for index,link in enumerate(find_unsavedProjects()[:30]):
    print("Index:",index,end=" ")
    try:
        tempDf=pd.DataFrame([create_dict_for_project(link)])

        primeDf=pd.concat([primeDf,tempDf])
    except:
        print("Error occured in index:",index,"continuing")
        continue


primeDf.to_excel(file_path, index=False, header=True)
