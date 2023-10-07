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
    
data = [{"name":31},{"name":32}]    

store_toXlsx(data,"test.xlsx")

